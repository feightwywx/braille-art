from .converter import convert
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="your image path (to be converted)")
    parser.add_argument("-w", "--width",
    help="resize your image to this width (proportionally, if you don't assign height at the same time)",
    type=int)
    parser.add_argument("-t", "--height",
    help="resize your image to this height (proportionally, if you don't assign width at the same time)",
    type=int)
    parser.add_argument("-o", "--output",
    help="output your braille art to this file if you want")

    args = parser.parse_args()
    result = convert(args.path, args.width, args.height)
    print(result)
    if args.output:
        with open(args.output, mode='w') as f:
            f.write(result)
            print(''.join(['Braille art saved: ', args.output]))
    
        