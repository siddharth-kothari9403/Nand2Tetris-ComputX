// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// Pseudo code:

// color = white ;   (0)
// while (true){ //keep listening to keyboard input forever  

//    if (key pressed, i.e. the keyboard register has a non zero value){
//       color = black; (-1)
//    }else{
//       color= white; (0)
//    }

//    address = screen;  //address is a pointer variable 

//    while (address in limits of screen, i.e. address < 24576){
//        mem[address] = color;
//        address++; 
//    }
// }


@color
M=0 //setting initial value of color variable to zero

(INFINITE_LOOP)
    @KBD 
    D=M //extracting value to check later
    @BLACK  //jump to this location if key presses, i.e. keyboard register has a non zero value
    D;JNE

    @color
    M=0
    @PROGRESS
    0;JMP  // unconditional jump to progress label

    (BLACK)
        @color
        M=-1
    
    (PROGRESS)
        @SCREEN
        D=A   
        @address
        M=D   //to assign address = starting address of screen  

        //address is now a pointer variable

        (INNER_LOOP)
            @address
            D=M  //obtaining value of address
            @24576
            D=D-A // address - 24576
            @END_INNER 
            D;JGE // if address >= 24576, i.e. address - 24576 >= 0 , then jump to END_INNER

            @color
            D=M // extracting value of color
            @address
            A=M // address is a pointer variable, get the address it points to
            M=D // making *(address) = color

            @address
            M=M+1 //incrementing address
            @INNER_LOOP
            0;JMP //jumping back to start of inner loop. unconditional jump
        
(END_INNER)
    @INFINITE_LOOP //going back to start of program, unconditional jmup
    0;JMP
