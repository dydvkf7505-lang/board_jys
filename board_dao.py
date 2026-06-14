import pymysql

class BoardDAO:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'board_user'
        self.password = 'board1234'
        self.database = 'board_db'

    def get_connection(self):
        return pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
            charset = 'utf8mb4' #
        )
    
    def select_all(self):
        conn = self.get_connection()
        cursor = conn.cursor()      # cursor => sql 실행 도구이다. 즉 DB와 대화하는 인터페이스

        # DB에 보냄
        sql = """    
        select *
        from board
        order by id desc
        """

        cursor.execute(sql)    # sql 실행
        result = cursor.fetchall()    # 결과 가져오기, 모든 행을 튜플 리스트로 가져온다.
        cursor.close()     # DB 연결 후 반드시 닫아야 한다 -> 메모리,성능에 문제 방지
        conn.close()

        return result
    
# # 전체 흐름
# 1. DB 연결
# 2. 커서 생성
# 3. SQL 실행
# 4. 결과 가져오기
# 5. 자원 해제
    
    # 데이터 삽입문 INSERT
    def insert(self, title, content,writer):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # DB에 보냄
        sql = """
        INSERT INTO board (title, content, writer)
        VALUES (%s, %s, %s)
        """

        try:
            # 3. SQL 실행 (매개변수로 받은 값을 %s 자리에 쏙 넣어줍니다)
            cursor.execute(sql, (title, content, writer))
            
            # 💡 중요: INSERT, UPDATE, DELETE 후에는 반드시 commit을 해야 DB에 실제 반영됩니다!
            conn.commit()    # DB에 실제로 저장 확정
            print("DB에 데이터가 성공적으로 저장되었습니다.")
            
            # 에러 발생 시 원래대로 되돌림 (롤백)
        except Exception as e:
            
            conn.rollback()
            print(f"데이터 저장 중 에러가 발생했습니다: {e}")
            
        finally:
            # 4. 자원 닫기
            cursor.close()
            conn.close()

# 흐름 요약
# 1. 연결
# 2. SQL 실행
# 3. commit → 저장 완료
# 4. 실패 시 rollback
# 5. 종료

        # 특정 글을 조회한다. SELECR ONE
    def select_one(self, board_id):
        conn = self.get_connection()
        cursor = conn.cursor()

        # 특정 id의 글만 조회하는 SQL문
        sql = """
        SELECT id, title, content, writer
        FROM board
        WHERE id = %s
        """

        cursor.execute(sql, (board_id,))  #(board_id,) ← 튜플 (쉼표 중요!)
        # 하나의 행만 가져올 때는 fetchall 대신 fetchone을 씁니다.
        result = cursor.fetchone() # 한 개만 가져온다.
        
        cursor.close()
        conn.close()

        return result
    
        # 삭제 하기 DELETE
    def delete(self, board_id):
        conn = self.get_connection()
        cursor = conn.cursor()

        # 특정 id를 가진 데이터를 삭제하는 SQL문
        sql = """
        DELETE FROM board 
        WHERE id = %s
        """

        try:
            cursor.execute(sql, (board_id,))   # sql 실행 (execute)
            conn.commit()    # 저장 확정
            print("DB에서 데이터가 성공적으로 삭제되었습니다.")
        except Exception as e:
            conn.rollback()  # 저장 취소
            print(f"데이터 삭제 중 에러가 발생했습니다: {e}")
        finally:
            cursor.close()
            conn.close()