// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.
// Usage: put the value of m1 and m2 in RAM[0] and RAM[1] respectively

// Put your code here.

// Pseudo code:

// int m1, m2;
// int n=m2;
// sum=0;
// while (n>0){
//    sum+=m1;
//    n--;
// }
// return sum;

@R2  // sum variable
M=0  // multiplication using repeated addition, hence we take M=0, initialised to 0

@R1
D=M
@n
M=D

(ADD_LOOP)
    @n //extracting the value for comparison
    D=M
    @END // jump to end if n = 0
    D;JEQ

    @R0
    D=M //m1

    @R2
    M=D+M //sum+=m1

    @n
    M=M-1 //n--

    @ADD_LOOP // unconditional jump to the start of the program
    0;JMP //unconditional jump to the end when the above condition becomes false

(END) //program termination with infinite loop
    @END
    0; JMP     