import whisper, argparse, json

def main():
    parser = argparse.ArgumentParser(description='Transcribe audio file')
    parser.add_argument('-m', '--model', help='Model to use', default='base')
    parser.add_argument('-i', '--input', help='Input audio file', required=True)
    parser.add_argument('-o', '--output', help='Output text file', required=True)
    args = parser.parse_args()

    model = whisper.load_model(args.model)
    result = model.transcribe(args.input)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
