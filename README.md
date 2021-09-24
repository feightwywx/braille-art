# braille-art

一个便利的盲文字符画生成工具

## 安装

请先确保安装好Python环境，本程序在以下环境经过测试：

- Windows 10, CPython 3.9.7 (amd64)

- macOS 11.6, CPython 3.9.7 (amd64)

- Ubuntu 20.04 LTS, CPython 3.8.10 (amd64, WSL2)

之后，利用pip进行安装：

```sh
pip3 install braille-art
```

## 用法

```sh
brailleart <你的图片路径>
```

另外，提供了以下可选开关：

- `-w`/`--width`, `-h`/`--height`: 控制图片的长/宽，如果只给其中一个值，则等比例缩放

- `-o`/`--output`: 输出盲文字符画到指定文件

- `-s`/`--threshold`: 可以指定进行二值化时使用的阈值

当然也可以在python中引用：

```python
import brailleart as ba

ba.convert(your_path, optional_width, optional_height, optional_threshold)
```

## 感谢

感谢[这篇文章](https://www.luogu.com.cn/blog/hejy/canvas)给出的盲文字符表和权值表。
