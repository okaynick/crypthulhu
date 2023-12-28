# Crypthulhu 1.0
Crypthulhu is a file encryption tool that uses the bitwise Xor operator.

## Usage
```python3 crypthulhu.py file_a file_b file_c```

Assume file_b is longer (in bytes) than file_a. Crypthulhu creates an encrypted version of file_a as file_c, with file_b serving as the key.

The process can be reversed: 
```python3 crypthulhu.py file_c file_b file_d```

file_d is then the decrypted file_c and should be identical to file_a.
