# braille-art

一个便利的盲文字符画生成工具

## 安装

```sh
pip install braille-art
```

## 用法

```sh
brailleart <你的图片路径>
```

另外，提供了以下开关：

- `-w`/`--width`, `-h`/`--height`: 控制图片的长/宽，如果只给其中一个值，则等比例缩放

- `-o`/`--output`: 输出盲文字符画到指定文件

当然也可以在python中引用：

```python
import brailleart as ba

ba.convert(your_path, optional_width, optional_height)
```

## 感谢

感谢[这篇文章](https://www.luogu.com.cn/blog/hejy/canvas)给出的盲文字符表和权值表。
