import setuptools

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="braille-art",
    version="0.0.3",
    author=".direwolf",
    author_email="kururinmiracle@outlook.com",
    description="Braille art generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/feightwywx/braille-art",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    entry_points={"console_scripts": [
        "brailleart = brailleart:main"
        ]
    },
    install_requires=[
        'numpy>=1.21.2',
        'opencv-python>=4.5.3.56'
    ]
)
