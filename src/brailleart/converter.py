import cv2


def array_to_braille(array) -> str:
    magic_table = (
    "⠀", "⠁", "⠂", "⠃", "⠄", "⠅", "⠆", "⠇", "⠈", "⠉", "⠊", "⠋", "⠌", "⠍", "⠎", "⠏",
    "⠐", "⠑", "⠒", "⠓", "⠔", "⠕", "⠖", "⠗", "⠘", "⠙", "⠚", "⠛", "⠜", "⠝", "⠞", "⠟",
    "⠠", "⠡", "⠢", "⠣", "⠤", "⠥", "⠦", "⠧", "⠨", "⠩", "⠪", "⠫", "⠬", "⠭", "⠮", "⠯",
    "⠰", "⠱", "⠲", "⠳", "⠴", "⠵", "⠶", "⠷", "⠸", "⠹", "⠺", "⠻", "⠼", "⠽", "⠾", "⠿",

    "⡀", "⡁", "⡂", "⡃", "⡄", "⡅", "⡆", "⡇", "⡈", "⡉", "⡊", "⡋", "⡌", "⡍", "⡎", "⡏",
    "⡐", "⡑", "⡒", "⡓", "⡔", "⡕", "⡖", "⡗", "⡘", "⡙", "⡚", "⡛", "⡜", "⡝", "⡞", "⡟",
    "⡠", "⡡", "⡢", "⡣", "⡤", "⡥", "⡦", "⡧", "⡨", "⡩", "⡪", "⡫", "⡬", "⡭", "⡮", "⡯",
    "⡰", "⡱", "⡲", "⡳", "⡴", "⡵", "⡶", "⡷", "⡸", "⡹", "⡺", "⡻", "⡼", "⡽", "⡾", "⡿",

    "⢀", "⢁", "⢂", "⢃", "⢄", "⢅", "⢆", "⢇", "⢈", "⢉", "⢊", "⢋", "⢌", "⢍", "⢎", "⢏",
    "⢐", "⢑", "⢒", "⢓", "⢔", "⢕", "⢖", "⢗", "⢘", "⢙", "⢚", "⢛", "⢜", "⢝", "⢞", "⢟",
    "⢠", "⢡", "⢢", "⢣", "⢤", "⢥", "⢦", "⢧", "⢨", "⢩", "⢪", "⢫", "⢬", "⢭", "⢮", "⢯",
    "⢰", "⢱", "⢲", "⢳", "⢴", "⢵", "⢶", "⢷", "⢸", "⢹", "⢺", "⢻", "⢼", "⢽", "⢾", "⢿",

    "⣀", "⣁", "⣂", "⣃", "⣄", "⣅", "⣆", "⣇", "⣈", "⣉", "⣊", "⣋", "⣌", "⣍", "⣎", "⣏",
    "⣐", "⣑", "⣒", "⣓", "⣔", "⣕", "⣖", "⣗", "⣘", "⣙", "⣚", "⣛", "⣜", "⣝", "⣞", "⣟",
    "⣠", "⣡", "⣢", "⣣", "⣤", "⣥", "⣦", "⣧", "⣨", "⣩", "⣪", "⣫", "⣬", "⣭", "⣮", "⣯",
    "⣰", "⣱", "⣲", "⣳", "⣴", "⣵", "⣶", "⣷", "⣸", "⣹", "⣺", "⣻", "⣼", "⣽", "⣾", "⣿"
    )

    weight_table = (1, 2, 4, 8, 16, 32, 64, 128)

    flatten = array.T.flatten()
    char_id = 0
    for i in range(len(flatten)):
        char_id += flatten[i] * weight_table[i]
    return magic_table[char_id]


def init_img(img, width: int = None, height: int = None, threshold: int = None):
    img_shape = img.shape
    # 如果指定了width，等比例调整尺寸
    if width is not None and height is not None:
        img = cv2.resize(img, (width, height))
    elif width is not None:
        img = cv2.resize(img, (width, int(img_shape[1] * (width / img_shape[0]))))
    elif height is not None:
        img = cv2.resize(img, (int(img_shape[0] * (height / img_shape[1])), height))
    # 如果不是灰度图，转灰度
    if len(img_shape) > 2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 大律法二值化
    if threshold is None:
        ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        print('OTSU estimated threshold: {}'.format(ret))
    else:
        ret, img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    # 补边
    img_width = img.shape[0]
    img_height = img.shape[1]
    img = cv2.copyMakeBorder(img, 0, img_height % 4, 0, img_width % 2, cv2.BORDER_CONSTANT, value=255)
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j] == 0:
                img[i][j] = 1
            elif img[i][j] == 255:
                img[i][j] = 0
    return img


def convert(path: str, width: int = None, height: int = None, threshold: int = None):
    img = cv2.imread(path)
    img = init_img(img, width if width else None, height if width else None, threshold)

    # 切分图像数组
    row_per_canvas = len(img) // 4
    char_per_row = len(img[0]) // 2
    chars = []
    for i in range(0, row_per_canvas):
        for j in range(0, char_per_row):
            chars.append(img[i * 4:(i + 1) * 4, j * 2:(j + 1) * 2])

    result = ''
    count = 0
    for each in chars:
        result += array_to_braille(each)
        count += 1
        if count == char_per_row:
            count = 0
            result += '\n'
    return result
    