from django.shortcuts import render
from django.http import JsonResponse
import json

def chat_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            
            # 여기에 챗봇 로직을 구현할 수 있습니다
            response_message = "죄송합니다. 아직 응답을 생성할 수 없습니다."
            
            return JsonResponse({'response': response_message})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
            
    return render(request, 'laptops/main.html')
