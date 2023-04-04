## RSA Algorithm

RSA is an asymmetric cryptographic algorithm used to encrypt and decrypt data securely. This repository contains the implementation of RSA algorithm in Python and a command-line interface (CLI) for encrypting and decrypting messages.
```
Usage:
  rsa_cli keypair <key_size> <public_key_file> <private_key_file>
  rsa_cli encrypt <public_key_file> <message_file> <output_file>
  rsa_cli decrypt <private_key_file> <ciphertext_file> <output_file>

Commands:
  keypair       Generate public and private keys
  encrypt       Encrypt a message using public
  decrypt       Decrypt a ciphertext using a private key.

```

To encrypt a message using a public key, run:
```
python rsa_cli.py keypair --key-size 512 data/public_key.txt data/private_key.txt
python rsa_cli.py encrypt data/public_key.txt data/input.txt data/output.bin
```
To decrypt a message using a previously generated private key:
```
python rsa_cli.py decrypt data/private_key.txt data/output.bin data/output.txt
```