import sys, argparse
import meme

def main():
    parser = argparse.ArgumentParser(description='Python CLI Meme Generator')

    parser.add_argument('-i', '--input', required=True, type=str, help='Input file to generate meme from.')
    parser.add_argument('-o', '--output', required=True, type=str, help='Output file name to generate meme.')
    parser.add_argument('-t', '--type', required=True, type=int, help='Type of meme. (1 - 3)')
    parser.add_argument('-s', '--string', required=True, type=str, nargs='+', help='Text/String to add to the meme.')
    parser.add_argument('-f', '--font', type=str, help='Choose the font you want to use for the meme.')

    args = parser.parse_args()
    meme.gen_meme(args.input, args.output, args.type, args.string, args.font)

if __name__ == '__main__':
    if not sys.argv[1:]:
        print('[Usage]: python {} -h (--help)'.format(sys.argv[0]))
    main()