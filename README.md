# 그리스 알파벳 헤더

> README in other language  :  [English](README.en.md)

## 개요

> 게으른 사람들을 위한 그리스 알파벳 C++ 헤더!

과학 또는 수학에 관련되서 각종 그리스문자를 출력할 필요가 있는 분들을 위해 만들었습니다.

근데 생각해보니까 진짜 게으른 사람들이며 이 헤더를 다운 받는 것는 것도 귀찮을 텐데...

네, 결국 순전히 자기만족을위해 만든 겁니다

* * *

## 내용

> [GreekAlphabet.h](GreekAlphabet.h) 만 사용하면 됩니다!

나머지는 파일 만드는데 사용한 텍스트와 코드입니다.

네임 스페이스 Greek 안에 그리스 대소문자
    cosnt std::string
변수가 들어있습니다.

    namespace Greek
    {
        //A 
        const std::string Alpha("\u0391"); 
        //B 
        const std::string Beta("\u0392"); 
        ......


대문자는 Greek::Alpha 와 같이 대문자로 시작하고, 소문자는 Greek::alpha 와 같이 소문자로 시작합니다.

헤더파일은 utf-8로 인코딩 되어 있고, 주석으로 해당하는 그리스문자를 달아놨으니, VSCode, VS 등에서 해당 문자를 미리 볼 수 있습니다.



* * * 

## 팁


1. cmd에서 사용 시
  
    커맨드라인을 열자마자 chcp 65001을 치면 유니코드를 쓸 수 있는 커맨드 창이 나옵니다.

    이후 정상적으로 cout을 통해 쓸 수 있습니다.(wcout없어도 됩니다?)

    아니면 경로가 "C:\Windows\System32\cmd.exe /K chcp 65001"인 바로가기를 만들어 사용하세요
     *** 

2. 윈도우 터미널 사용 시
   
   윈도우 터미널을 통해 cmd를 사용한다면, 1번과 같이 터미널 경로가 "C:\Windows\System32\cmd.exe /K chcp 65001"인 프로필을 만들어 쓰시면 됩니다.
   ***

3. 파일 쓰기
   
    별다른 처리 없이도 std::ofstream 으로 쓸 수 있습니다.

    ***


4. 비주얼 스튜디오 코드에서 사용 시
    ctrl + p에서 검색하여 settings.json파일을 열고

    "terminal.integrated.shellArgs.windows": ["/K", "chcp 65001"]
    
    을 추가해 줍니다.

    이후 cout으로 그리스 문자를 출력하기 전에 Greek::UseUnicodeInVSCode() 
    함수를 사용해 주세요.

    ***