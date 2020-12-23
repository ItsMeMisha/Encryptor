import sys
import argparse
import pickle

import ceasarCoder
import vigenereCoder


def parseArgs():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='modeName')

    parserEncode = subparsers.add_parser('encode')
    parserEncode.add_argument(
        '--cipher', choices=['ceasar', 'vigenere'], required=True)
    parserEncode.add_argument('--key', required=True)
    parserEncode.add_argument('--input-file', type=str, dest='input')
    parserEncode.add_argument('--output-file', type=str, dest='output')

    parserDecode = subparsers.add_parser('decode')
    parserDecode.add_argument(
        '--cipher', choices=['ceasar', 'vigenere'], required=True)
    parserDecode.add_argument('--key', required=True)
    parserDecode.add_argument('--input-file', type=str, dest='input')
    parserDecode.add_argument('--output-file', type=str, dest='output')

    parserTrain = subparsers.add_parser('train')
    parserTrain.add_argument('--model-file', type=str,
                             required=True, dest='model')
    parserTrain.add_argument('--text-file', type=str, dest='input')

    parserHack = subparsers.add_parser('hack')
    parserHack.add_argument('--model-file', type=str,
                            required=True, dest='model')
    parserHack.add_argument('--input-file', type=str, dest='input')
    parserHack.add_argument('--output-file', type=str, dest='output')

    return parser.parse_args()


args = parseArgs()
coder = ceasarCoder.CeasarCoder
key = None
if args.modeName == 'encode' or args.modeName == 'decode':
    if args.cipher == 'vigenere':
        coder = vigenereCoder.VigenereCoder
        key = args.key
    else:
        key = int(args.key)

text = ''
if not (args.input is None):
    with open(args.input, 'r') as inputFile:
        text = inputFile.read()
else:
    text = input()

output = None
if args.modeName == 'encode':
    output = coder.encode(text, key)

elif args.modeName == 'decode':
    output = coder.decode(text, key)

model = None
if args.modeName == 'hack':
    with open(args.model, 'rb') as modelFile:
        model = pickle.load(modelFile)
    output = coder.hack(text, model)

if not (output is None):
    if not (args.output is None):
        with open(args.output, 'w') as outputFile:
            outputFile.write(output)
    else:
        print(output)

if args.modeName == 'train':
    model = coder.train(text)
    with open(args.model, 'wb') as modelFile:
        pickle.dump(model, modelFile)
