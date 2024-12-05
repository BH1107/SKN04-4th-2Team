const chatBox = document.getElementById("chatBox");
const progressBar = document.getElementById("progressBar");
let isProcessing = false;

// 사용자 메시지 전송 함수
async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const chatBox = document.getElementById('chatBox');
    const progressBar = document.getElementById('progressBar');
    
    if (!userInput.value.trim() || isProcessing) return;
    
    isProcessing = true;
    
    // 사용자 메시지 추가
    const userMessage = document.createElement('div');
    userMessage.className = 'message user';
    userMessage.innerHTML = `<div class="bubble">${userInput.value}</div>`;
    chatBox.appendChild(userMessage);
    
    // 진행 상태 바 표시
    progressBar.style.display = 'block';
    let progress = 0;
    const progressInterval = setInterval(() => {
        if (progress < 90) {  // 90%까지만 자동으로 증가
            progress += 5;
            progressBar.style.width = `${progress}%`;
        }
    }, 100);

    try {
        // API 호출 또는 응답 처리 로직
        const response = await fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                message: userInput.value
            })
        });
        const data = await response.json();
        const botResponse = data.response;
        
        // 챗봇 응답 메시지 추가
        const botMessage = document.createElement('div');
        botMessage.className = 'message assistant';
        botMessage.innerHTML = `<div class="bubble">${botResponse}</div>`;
        chatBox.appendChild(botMessage);
        
        // 진행 완료
        progress = 100;
        progressBar.style.width = '100%';
        
        // 0.5초 후 진행 상태 바 리셋
        setTimeout(() => {
            progressBar.style.width = '0';
            progressBar.style.display = 'none';
        }, 500);
        
    } catch (error) {
        console.error('Error:', error);
        // 에러 메시지 표시
        const errorMessage = document.createElement('div');
        errorMessage.className = 'message assistant';
        errorMessage.innerHTML = `<div class="bubble">죄송합니다. 오류가 발생했습니다.</div>`;
        chatBox.appendChild(errorMessage);
    } finally {
        clearInterval(progressInterval);
        isProcessing = false;
        userInput.value = '';
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

// Enter 키 이벤트 처리
document.getElementById('userInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// API 호출을 시뮬레이션하는 함수
function mockApiCall(message) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(`"${message}"에 대한 응답입니다.`);
        }, 2000);  // 2초 후 응답
    });
}

// 초기 상태 설정
document.addEventListener('DOMContentLoaded', function() {
    const progressBar = document.getElementById('progressBar');
    progressBar.style.width = '0';
    progressBar.style.display = 'none';
});