from typing import Any
import time
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class ThrottleMiddleware(MiddlewareMixin):
    # Определите лимит времени (в секундах) между запросами
    TIME_LIMIT = 5  # 5 секунд

    # Хранилище для хранения времени последнего запроса по IP
    ip_request_times = {}

    def process_request(self, request):
        ip = self.get_client_ip(request)
        current_time = time.time()

        # Получаем время последнего запроса
        last_request_time = self.ip_request_times.get(ip)

        if last_request_time:
            elapsed_time = current_time - last_request_time
            
            # Если прошло меньше времени, чем лимит, возвращаем ошибку
            if elapsed_time < self.TIME_LIMIT:
                return JsonResponse(
                    {"error": "Слишком много запросов. Пожалуйста, попробуйте позже."},
                    status=429
                )
        # Обновляем время последнего запроса
        self.ip_request_times[ip] = current_time

    def get_client_ip(self, request):
        """ Получает IP адрес клиента из запроса """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip