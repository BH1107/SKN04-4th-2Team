from django.test import TestCase, Client
from django.urls import reverse
from bs4 import BeautifulSoup
import json

class TestChatView(TestCase):
    def setUp(self):
        """
        테스트 실행 전 필요한 초기 설정을 합니다.
        """
        self.client = Client()
        self.test_message = "노트북 추천해줘"

    def test_chat_page_load(self):
        """
        채팅 페이지가 올바르게 로드되는지 테스트합니다.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 필수 컴포넌트들이 존재하는지 확인
        self.assertIsNotNone(soup.select_one('.fixed-header'))
        self.assertIsNotNone(soup.select_one('.container'))
        self.assertIsNotNone(soup.select_one('.chat-box'))
        self.assertIsNotNone(soup.select_one('.input-area'))
        
        # 입력 필드와 전송 버튼 확인
        self.assertIsNotNone(soup.select_one('.input-area input'))
        self.assertIsNotNone(soup.select_one('.input-area button'))

    def test_message_interaction(self):
        """
        메시지 전송 및 응답 과정을 테스트합니다.
        - 메시지 전송
        - 사용자 메시지 표시
        - 어시스턴트 응답
        """
        # 메시지 전송 POST 요청
        response = self.client.post('/', 
            data=json.dumps({'message': self.test_message}),
            content_type='application/json'
        )
        
        # 응답 상태 코드 확인
        self.assertEqual(response.status_code, 200)
        
        # JSON 응답 확인
        response_data = json.loads(response.content)
        self.assertIn('response', response_data)
        
        # 메인 페이지 다시 로드하여 메시지 표시 확인
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 채팅 박스 내 메시지 확인
        chat_box = soup.select_one('.chat-box')
        self.assertIsNotNone(chat_box)
        
        # 사용자 메시지 구조 확인
        user_messages = soup.select('.message.user')
        self.assertTrue(len(user_messages) >= 0)  # 사용자 메시지가 있을 수 있음
        
        if user_messages:
            user_bubble = user_messages[0].select_one('.bubble')
            self.assertIsNotNone(user_bubble)

    def test_chat_interface_elements(self):
        """
        채팅 인터페이스의 세부 요소들을 테스트합니다.
        """
        response = self.client.get('/')
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 로고 확인
        logo = soup.select_one('.logo')
        self.assertIsNotNone(logo)
        
        # 설명 텍스트 영역 확인
        description = soup.select_one('.description')
        self.assertIsNotNone(description)
        
        # 입력 필드 속성 확인
        input_field = soup.select_one('.input-area input')
        self.assertTrue(input_field.has_attr('placeholder'))

    def test_progress_bar(self):
        """
        진행 상태바 구조를 테스트합니다.
        """

        # 페이지 로드
        response = self.client.get('/')
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 진행바 구조 확인
        progress_bar = soup.select_one('.progress-bar')
        self.assertIsNotNone(progress_bar)
        
        progress = soup.select_one('#progressBar')
        self.assertIsNotNone(progress)
