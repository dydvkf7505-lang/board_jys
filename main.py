from board_dao import *

board_dao = BoardDAO()

# 커넥션 테스트
# board_dao.get_connection()

while True:

    print('='*40)
    print("1.목록 2.등록 3.내용 4.삭제 0.종료")
    print('='*40)
    menu = input('선택 > ')

    if menu == "0":
        break

    elif menu == '1':
        boards = board_dao.select_all()

        print('\n📋 게시글 목록')
        print('='*50)

        for board in boards:
            print(f"번호 : {board[0]}")
            print(f"제목 : {board[1]}")
            print(f"내용 : {board[2]}")
            print(f"작성자 : {board[3]}")
            print('-'*50)

    elif menu == '2':
        title = input("제목 입력 >")
        content = input("내용 입력 >")
        writer = input("작성자 입력 >")

        board_dao.insert(title,content,writer)
        print("글이 정상적으로 등록되었습니다.")

    elif menu == '3':
        print('\n--- 🔍 글 상세보기 ---')
        board_id = input("조회할 글 번호 입력 > ")
        
        # DAO를 통해 해당 번호의 글을 가져옵니다.
        board = board_dao.select_one(board_id)
        
        if board: # 데이터가 존재하는 경우
            print('-'*40)
            print(f"📌 번호 : {board[0]}")
            print(f"📌 제목 : {board[1]}")
            print(f"📌 작성자: {board[3]}")
            print('-'*40)
            print(f"📝 내용 :\n{board[2]}")
            print('-'*40)
        else: # 해당 번호의 글이 없는 경우
            print("❌ 존재하지 않는 글 번호입니다.")

    
    elif menu == '4':
        print('\n--- 🗑️ 글 삭제하기 ---')
        board_id = input("삭제할 글 번호 입력 > ")
        
        # [선택사항] 삭제하기 전 진짜 삭제할 건지 한번 물어보는 절차를 넣으면 좋습니다.
        confirm = input(f"정말 {board_id}번 글을 삭제하시겠습니까? (y/n) > ")
        
        if confirm.lower() == 'y':
            # BoardDAO의 delete 함수 호출!
            board_dao.delete(board_id)

            print("💡 글이 정상적으로 삭제되었습니다.")
        else:
            print("❌ 삭제가 취소되었습니다.")

        

print('게시판 종료')



