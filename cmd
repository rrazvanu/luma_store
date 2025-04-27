pip install -U selenium
pip install behave  / py -m pip install behave
pip install behave-html-formatter
pip install html-pretty
pip install webdriver_manager/ pip install webdriver-manager
pip install packaging

run tests:
Normal run with html report:
behave -f html -o behave-report.html --tags=smoke

Normal run without html report:
behave --tags=file

New report type:
python -X utf8 -m behave -f html-pretty -o behave-report.html --tags=smoke

behave -f html-pretty -o behave-report.html --tags=login
behave -f html-pretty -o behave-report.html --tags=login --reruns=1

$ pip install allure-behave
$ behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features
$ allure serve %allure_result_folder%

Re-run if any tests fail:
pytest --reruns 1 --html=report.html --self-contained-html

idei:
import logging
def catch_exceptions(step_func):
    def wrapper(*args, **kwargs):
        try:
            return step_func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Caught exception: {e}")

    return wrapper

@catch_exceptions

Selector cu eliminarea spatiilor libere:
//td[normalize-space(text())="text"]