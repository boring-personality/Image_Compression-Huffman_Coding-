# Image_Compression-Huffman_Coding-
### Huffman Coding
Huffman coding is a lossless data compression algorithm. In this algorithm, a variable-length code is assigned to input different characters. The code length is related to how frequently characters are used. Most frequent characters have the smallest codes and longer codes for least frequent characters.

In case of images, histogram of the image is identified and base on the frequency of the pixel values the coding is done.

### Input image
![Screenshot](lena1.png)

### Output
#### Code For each pixel
- 77.0 00000
- 101.0 000010
- 130.0 0000110
- 190.0 00001110
- 194.0 00001111
- 93.0 000100
- 8.0 000101
- 4.0 00011
- 81.0 00100
- 69.0 00101
- 73.0 00110
- 215.0 00111000
- 210.0 00111001
- 170.0 0011101
- 125.0 001111
- 89.0 010000
- 20.0 010001
- 113.0 01001
- 121.0 01010
- 40.0 010110
- 16.0 010111
- 182.0 0110000
- 198.0 01100010
- 206.0 01100011
- 24.0 011001
- 12.0 011010
- 178.0 0110110
- 154.0 0110111
- 0.0 01110
- 36.0 011110
- 138.0 011111
- 186.0 1000000
- 158.0 1000001
- 32.0 100001
- 28.0 100010
- 146.0 1000110
- 162.0 1000111
- 109.0 10010
- 174.0 1001100
- 150.0 1001101
- 166.0 1001110
- 202.0 10011110
- 219.0 100111110
- 223.0 1001111110
- 227.0 10011111110
- 231.0 100111111110
- 251.0 100111111111000
- 235.0 100111111111001
- 243.0 10011111111101
- 255.0 100111111111100
- 247.0 100111111111101
- 239.0 10011111111111
- 61.0 10100
- 97.0 10101
- 65.0 10110
- 57.0 10111
- 142.0 110000
- 134.0 110001
- 85.0 11001
- 105.0 11010
- 49.0 11011
- 53.0 11100
- 45.0 11101
- 117.0 1111

#### Size of image after huffman coding
- Average length of code is  **5.5290984375 bits**.
- Size of the image is  **625.0 Kb**.
- Size after compression is  **431.9608154296875 Kb**.
- Compression Ratio is  **1.4468904994965555**.
