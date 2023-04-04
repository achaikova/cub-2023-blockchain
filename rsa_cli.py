import argparse
from rsa import RSA
import pickle


def generate_keypair(args: argparse.Namespace):
    rsa = RSA(args.key_size)
    public_key, private_key = rsa.get_public_key(), rsa.get_private_key()
    with open(args.public_key_file, "wb") as f:
        pickle.dump(public_key, f)
    with open(args.private_key_file, "wb") as f:
        pickle.dump(private_key, f)
    print("Generated public and private keys")


def encrypt(args: argparse.Namespace):
    rsa = RSA()
    with open(args.public_key_file, "rb") as f:
        public_key = pickle.load(f)
    with open(args.input_file, "r") as f:
        message = f.read()
    crypto = rsa.encrypt(message, public_key)
    private_key = rsa.get_private_key()
    with open(args.output_file, "wb") as f:
        pickle.dump(crypto, f)
    print(f"Encrypted message written to {args.output_file}")


def decrypt(args: argparse.Namespace):
    rsa = RSA()
    with open(args.private_key_file, "rb") as f:
        private_key = pickle.load(f)
    with open(args.input_file, "rb") as f:
        crypto = pickle.load(f)
    message = rsa.decrypt(crypto, private_key)
    with open(args.output_file, "w") as f:
        f.write(message)
    print(f"Decrypted message written to {args.output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RSA CLI")
    subparsers = parser.add_subparsers()

    keypair_parser = subparsers.add_parser("keypair", help="Generate an RSA keypair")
    keypair_parser.add_argument("--key-size", type=int, default=512,
                                help="The size of the keypair in bits (default: 512)")
    keypair_parser.add_argument("public_key_file",
                                help="The file to write the public key to")
    keypair_parser.add_argument("private_key_file",
                                help="The file to write the private key to")
    keypair_parser.set_defaults(func=generate_keypair)

    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt a message with RSA")
    encrypt_parser.add_argument("public_key_file",
                                help="The file to write the public key to")
    encrypt_parser.add_argument("input_file",
                                help="The file containing the plaintext message to encrypt")
    encrypt_parser.add_argument("output_file",
                                help="The file to write the encrypted ciphertext to")
    encrypt_parser.set_defaults(func=encrypt)

    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt a crypto text with RSA")
    decrypt_parser.add_argument("private_key_file",
                                help="The file containing the private key")
    decrypt_parser.add_argument("input_file",
                                help="The file containing the crypto text to decrypt")
    decrypt_parser.add_argument("output_file", help="The file to write the decrypted message to")
    decrypt_parser.set_defaults(func=decrypt)

    args = parser.parse_args()
    args.func(args)
