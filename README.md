# shila_mecro

![image](https://user-images.githubusercontent.com/42954693/133355203-fc6607b4-172d-4e7a-b865-fcc8b1f703e9.png)

 ## 신라호텔 (팔선) 예약 매크로
  - 별실 (셀비아 룸) 예약 가능
  - 날짜 선택 가능
 
 ## 시작하기
  ```
  Run Python File in Terminal
  ```
 
 ## 애플리케이션 빌드 및 배포 (윈도우 배포 기준)
  ```
  pyinstaller -w -F '.\shilla_mecro.py'
  ```
  
 ## 라이선스
  **MIT** 
 
 ## 사용 프레임워크
  - selenium + bs4
  - tkinter (UI)
  - PyInstaller

 ## 이슈 사항 및 불편 사항
  - 크롬 드라이버 관리가 필요 (버젼이 맞지 않으면 프로그램이 실행되지 않는 이슈 발생)
  - 크롬 드라이버 위치를 수동으로 입력해줘야함
