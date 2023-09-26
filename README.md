# ASCII-Fence-Cypher
Self-created encryption method by altering ASCII code to synthesize two codes to store the original code.

It will accept any letter that ASCII code digits is 2.

NO limitation on the length of the code.

Create a 4 by n matrix, each row contains 2 digits of the code.
If the length of the code is odd then the remainder will be created to store the last digit of the code.

The ASCII code of the remainder will be separated and added to the final cypher and key after altering the column and row of the Matrix.
Cypher and key will have the same length.

For the Decryption, test if the length of the cypher is odd or even in order to decrypt the remainder.
The position of the ASCII code of the original code will follow the pattern depending on the number of rows of the matrix that was first synthesized.
Then acquire and decrypt each ASCII code and put them together. The remainder wil be added to the final result.

# USE
Import the file and use encrypt() and decrypt() to make up ur code. 

Two int codes are required for decrypt.
The code for encrypt must be str and dont accept alphabet letter like d, use capital D instead.
encrypt() will return two int codes
