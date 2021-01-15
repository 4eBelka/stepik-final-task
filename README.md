# stepik-final-task
Финальное задание по курсу https://stepik.org/course/575/syllabus

**Команды для запуска:**
pytest -v --tb=line --language=en -m need_review test_product_page.py

pytest -v --tb=line --language=ru -m need_review test_product_page.py - выбор языка ru
pytest -v --tb=line --language=en --browser_name=firefox -m need_review test_product_page.py - запуск через Мозилу
pytest -rx -v --tb=line -m need_review test_product_page.py - запуск с сообщениями xfail

pytest -v --tb=line test_main_page.py - запуск test_main_page.py

**Дополнительно:**
add_product_to_basket и add_product_to_basket_promo сделаны специально, чтобы при вызове не писать по 4 строки (5)

В solve_quiz_and_get_code специально добавлена пауза, чтобы отрабатывали тесты в мозиле, иначе они падуют.

Файлы .gitignore, pytest.ini добавлены специально.
.gitignore - нужен для скрытия файлов и папок от системы контроля версий
pytest.ini - для зарегистрации меток

Все тесты проверены перед публикацией. Проблем с выполнением не возникло.