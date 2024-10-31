# Домашнее задание к 1 занятию:
# Запустить приложение из первого занятия локально.
# Создать свой репозиторий и написать в нем несколько автотестов для приложения с lesson1

# import json
# import allure
# import requests
# from allure_commons.types import AttachmentType
# from lesson1.api_tests.services.config import settings
# from curlify2 import Curlify  # Curlify2 работает и с httpx и с requests.
# from loguru import logger
# from requests import Response
# from lesson1.api_tests.utils.api_response import APIResponse
#
#
# class APIClient:
#     @staticmethod
#     def response_logging(response: Response):
#         logger.info("Запрос на ручку: " + str(response.request.url))
#         if response.request.body:
#             if isinstance(response.request.body, bytes):
#                 logger.debug("Тело запроса: " + response.request.body.decode("utf-8"))
#             else:
#                 logger.debug("Тело запроса: " + response.request.body)
#         logger.debug("Заголовки запроса: " + str(response.request.headers))
#         logger.info("Код ответа: " + str(response.status_code))
#         logger.debug("Тело ответа: " + response.text)
#         logger.debug("Curl: " + Curlify(response.request, compressed=True).to_curl())
#
#     @staticmethod
#     def send_request(response: Response):
#         if response.request.headers:
#             allure.attach(
#                 body=str(response.request.headers),
#                 name="Заголовки запроса",
#                 attachment_type=AttachmentType.TEXT,
#             )
#
#         if response.request.body:
#             content_str = response.request.body.decode("utf-8")
#             json_content = json.dumps(
#                 json.loads(content_str), indent=4, ensure_ascii=False
#             )
#             allure.attach(
#                 body=json_content,
#                 name="Тело запроса",
#                 attachment_type=AttachmentType.JSON,
#                 extension="json",
#             )
#
#     @staticmethod
#     def get_response(response: Response):
#         allure.attach(
#             body=str(response.status_code),
#             name="Код ответа",
#             attachment_type=AttachmentType.TEXT,
#         )
#
#         if response.text:
#             try:
#                 json_response = response.json()
#                 allure.attach(
#                     body=json.dumps(json_response, indent=4, ensure_ascii=False),
#                     name="Тело ответа",
#                     attachment_type=AttachmentType.JSON,
#                     extension="json",
#                 )
#             except ValueError:
#                 allure.attach(
#                     body=response.text,
#                     name="Тело ответа",
#                     attachment_type=AttachmentType.TEXT,
#                 )
#
#     @staticmethod
#     def useful_info(response: Response):
#         allure.attach(
#             body=Curlify(response.request, compressed=True).to_curl(),
#             name="Curl запроса",
#             attachment_type=AttachmentType.TEXT,
#         )
#
#
#     def make_request(
#         self,
#         handle: str,
#         method: str,
#         json=None,
#         data=None,
#         params=None,
#         headers=None,
#         attach=True,
#         cookies=None,
#     ):
#         response = requests.request(
#             method,
#             url=settings.base_url + handle,
#             json=json,
#             data=data,
#             params=params,
#             headers=headers,
#             cookies=cookies,
#         )
#
#         self.response_logging(response)
#
#         if attach:
#             with allure.step(
#                 f"Отправляем {response.request.method} запрос на ручку: {response.request.url}"
#             ):
#                 self.send_request(response)
#                 self.get_response(response)
#                 self.useful_info(response)
#
#         return APIResponse(response)
#
#
# client = APIClient()
#
# create_case_dict = {
#     "id": 0,
#     "name": "Тестовое задание",
#     "description": "Тестовое задание",
#     "priority": "высокий",
#     "steps": ["шаг 1", "шаг 2", "шаг 3"],
#     "expected_result": "Задание выполнено",
# }
#
# def test_create_case():
#     response = client.make_request(
#         handle="/testcases",
#         method="POST",
#         json=create_case_dict
#     )
#     response.status_code_should_be_eq(200)
#     response.json_should_contains({"id": 1})
#     response.value_with_key("id").should_be_eq(1)
#
#
# def test_create_case_empty_data():
#     response = client.make_request(
#         handle="/testcases",
#         method="POST",
#         json={}
#     )
#     response.status_code_should_be_eq(422)
#
#
# def test_create_case_missed_priority_data():
#     response = client.make_request(
#         handle="/testcases",
#         method="POST",
#         json={"id": 0,
#               "name": "string",
#               "description": "string",
#               "steps": [
#                   "string"
#               ],
#               "expected_result": "string"}
#     )
#     response.status_code_should_be_eq(422)
#
#
# def test_get_read_root():
#     response = client.make_request(
#         handle="/",
#         method="GET"
#     )
#     response.status_code_should_be_eq(200)
#     response.json_should_be_eq({"Hello": "World"})
#
#
# def test_get_testcases():
#     response = client.make_request(
#         handle="/testcases",
#         method="GET",
#     )
#     response.status_code_should_be_eq(200)
import json
import allure
import requests
from allure_commons.types import AttachmentType
from lesson1.api_tests.services.config import settings
from curlify2 import Curlify  # Curlify2 работает и с httpx и с requests.
from loguru import logger
from requests import Response
from lesson1.api_tests.utils.api_response import APIResponse


class APIClient:

    @staticmethod
    def response_logging(response: Response):
        """Логирует детали ответа."""
        logger.info("Запрос на ручку: " + str(response.request.url))
        if response.request.body:
            body_content = response.request.body.decode("utf-8") if isinstance(response.request.body,
                                                                               bytes) else response.request.body
            logger.debug("Тело запроса: " + body_content)
        logger.debug("Заголовки запроса: " + str(response.request.headers))
        logger.info("Код ответа: " + str(response.status_code))
        logger.debug("Тело ответа: " + response.text)
        logger.debug("Curl: " + Curlify(response.request, compressed=True).to_curl())

    @staticmethod
    def send_request(response: Response):
        """Логирует заголовки и тело запроса."""
        if response.request.headers:
            allure.attach(
                body=str(response.request.headers),
                name="Заголовки запроса",
                attachment_type=AttachmentType.TEXT,
            )

        if response.request.body:
            content_str = response.request.body.decode("utf-8")
            json_content = json.dumps(json.loads(content_str), indent=4, ensure_ascii=False)
            allure.attach(
                body=json_content,
                name="Тело запроса",
                attachment_type=AttachmentType.JSON,
                extension="json",
            )

    @staticmethod
    def get_response(response: Response):
        """Логирует код и тело ответа."""
        allure.attach(
            body=str(response.status_code),
            name="Код ответа",
            attachment_type=AttachmentType.TEXT,
        )

        if response.text:
            try:
                json_response = response.json()
                allure.attach(
                    body=json.dumps(json_response, indent=4, ensure_ascii=False),
                    name="Тело ответа",
                    attachment_type=AttachmentType.JSON,
                    extension="json",
                )
            except ValueError:
                allure.attach(
                    body=response.text,
                    name="Тело ответа",
                    attachment_type=AttachmentType.TEXT,
                )

    @staticmethod
    def useful_info(response: Response):
        """Логирует Curl-запрос."""
        allure.attach(
            body=Curlify(response.request, compressed=True).to_curl(),
            name="Curl запроса",
            attachment_type=AttachmentType.TEXT,
        )

    def make_request(
            self,
            handle: str,
            method: str,
            json=None,
            data=None,
            params=None,
            headers=None,
            attach=True,
            cookies=None,
    ):
        """Отправляет запрос к API и обрабатывает ответ."""
        response = requests.request(
            method,
            url=settings.base_url + handle,
            json=json,
            data=data,
            params=params,
            headers=headers,
            cookies=cookies,
        )

        self.response_logging(response)

        if attach:
            with allure.step(f"Отправляем {response.request.method} запрос на ручку: {response.request.url}"):
                self.send_request(response)
                self.get_response(response)
                self.useful_info(response)

        return APIResponse(response)


# Инициализация клиента
client = APIClient()

create_case_dict = {
    "id": 0,
    "name": "Тестовое задание",
    "description": "Тестовое задание",
    "priority": "высокий",
    "steps": ["шаг 1", "шаг 2", "шаг 3"],
    "expected_result": "Задание выполнено",
}


# Тесты
def test_create_case():
    response = client.make_request(
        handle="/testcases",
        method="POST",
        json=create_case_dict
    )
    response.status_code_should_be_eq(200)
    response.json_should_contains({"id": 0})
    response.value_with_key("id").should_be_eq(0)


def test_create_case_empty_data():
    response = client.make_request(
        handle="/testcases",
        method="POST",
        json={}
    )
    response.status_code_should_be_eq(422)


def test_create_case_missed_priority_data():
    response = client.make_request(
        handle="/testcases",
        method="POST",
        json={
            "id": 0,
            "name": "string",
            "description": "string",
            "steps": ["string"],
            "expected_result": "string"
        }
    )
    response.status_code_should_be_eq(422)


def test_get_read_root():
    response = client.make_request(
        handle="/",
        method="GET"
    )
    response.status_code_should_be_eq(200)
    response.json_should_be_eq({"Hello": "World"})


def test_get_testcases():
    response = client.make_request(
        handle="/testcases",
        method="GET",
    )
    response.status_code_should_be_eq(200)

