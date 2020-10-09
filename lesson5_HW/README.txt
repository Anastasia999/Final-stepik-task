Папка с отчетами расположена в папке Stepik_lessons.

Тест должен запускаться с параметром language следующей командой:
pytest --browser=chrome --language=en-gb --alluredir=/путь/к/вашей/директории/allure_report test_make_report.py
Далее нужно собрать отчет командой:
allure serve /путь/к/вашей/директории/allure_report
