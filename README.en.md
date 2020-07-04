# Greek Alphabet Header

> README in other language  :  [한국어](README.md)

## Abstract

> Greek AlphaBet Header for Lazy C++ User

I made this header for one who use Greek Alphabets for scientific and mathematical reasons.

But if you are really lazy, you just don't download this, and type "us" for micro seconds".

Well, it's true that this header is purely for self-satisfaction, and inefficent to use.

***

## What's inside?

> You only needs  [GreakAlphabet.h](GreakAlphabet.h)  file

There is cosnt std::string type variables inside Greek namespace

    namespace Greek
    {
        //A 
        const std::string Alpha("\u0391"); 
        //B 
        const std::string Beta("\u0392"); 
        ......

The Capital letters are starts with a Capital letter like :

    Greek::Alpha.

The small letters are starts with a small letter like : 

    Greek::alpha.


## Tips

1. Use in VSCode Terminal
   
   To print out Unicode letters on VSCode's Terminal. You first need to call a fucntion below, because of the buffer issue.  :

    bool Greek::UseUnicodeInVSCode()

    You only need to call it once, before print through cout

2. Use in CMD
    
    You need to type "chcp 65001" on CMD to use unicode


