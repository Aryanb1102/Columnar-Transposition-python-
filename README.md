**Columnar Transposition Cipher Encryption and Decryption**
This is a Python program that performs encryption and decryption using the columnar transposition cipher. The key can be chosen randomly or provided by the user.

**Cryptography Class Assignment**

CS Department, Ashoka University

Professor Debayan Gupta

**Description**
The columnar transposition cipher is a simple encryption technique that rearranges the plaintext letters based on a keyword. The plaintext is written row-wise into a grid of fixed dimensions, and the ciphertext is obtained by reading the letters column-wise in a specific order determined by the key.

This program allows users to:

Encrypt a plaintext message using a key.
Decrypt a ciphertext message using the same key.
How to Run the Program
Ensure you have Python installed (version 3.x).

Save the script provided into a file named columnar_transposition.py.

Run the script from the command line:

bash
Copy code
python columnar_transposition.py
Follow the prompts to input the key and plaintext or ciphertext.

Sample Run
plaintext
Copy code
Do you want to input the key? (y/n): y
Enter the key: CRYPTOGRAPHY
Enter the plaintext: people say nothing is impossible but i do nothing every day

Encrypted Ciphertext:
ypdrphitysitvosndesuepgennooyeibhamielibgonlitsoa

Decrypted Plaintext:
PEOPLESAYNOTHINGISIMPOSSIBLEBUTIDONOTHINGEVERYDAY

**Mathematics Behind the Cipher**
Encryption Process
Key Preparation:

The key is a word or phrase (e.g., "CRYPTOGRAPHY").
Assign a numerical value to each letter based on its position in the alphabet and its occurrence in the key.
Grid Construction:

Remove spaces from the plaintext.
Calculate the number of rows needed: ceil(len(plaintext) / len(key)).
Write the plaintext into a grid row-wise.
Columnar Rearrangement:

Rearrange the columns based on the numerical order of the key letters.
Read off the ciphertext by concatenating the letters column-wise in this order.
Decryption Process
Key Preparation:

Use the same numerical assignments as in encryption.
Grid Reconstruction:

Calculate the number of rows and columns.
Determine the number of filled cells in each column.
Fill the grid column-wise with the ciphertext letters according to the key's numerical order.
Plaintext Retrieval:

Read the plaintext row-wise from the reconstructed grid.
Example
For the key "CRYPTOGRAPHY" and plaintext "PEOPLE SAY NOTHING IS IMPOSSIBLE BUT I DO NOTHING EVERY DAY":

Assign Numerical Order to Key Letters:

Letter	Position
A	1
C	2
G	3
H	4
O	5
P	6
P	7
R	8
R	9
T	10
Y	11
Y	12
Construct Grid and Encrypt:

Grid Filled Row-wise:

C	R	Y	P	T	O	G	R	A	P	H	Y
P	E	O	P	L	E	S	A	Y	N	O	T
H	I	N	G	I	S	I	M	P	O	S	S
I	B	L	E	B	U	T	I	D	O	N	O
T	H	I	N	G	E	V	E	R	Y	D	A
Ciphertext: Read columns in the order determined by the key.

Notes
Case Sensitivity: The program converts all inputs to uppercase for consistency.
Spaces: Spaces are removed from the plaintext during encryption.
Duplicate Letters in Key: The program handles duplicate letters by considering their positions.
Conclusion
This program demonstrates the implementation of the columnar transposition cipher in Python. It showcases how classical encryption techniques can be programmed and the importance of key management in cryptography.

