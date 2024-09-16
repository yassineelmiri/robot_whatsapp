@echo off
setlocal

echo Checking if virtual environment exists...

if not exist ".venv\Scripts\activate" (
    echo Virtual environment not found. Creating a new one...
    py -m venv .venv

    if ERRORLEVEL 1 (
        echo `py -m venv .venv` failed. Trying with `python`...
        python -m venv .venv

        if ERRORLEVEL 1 (
            echo `python -m venv .venv` also failed. Exiting with error level %ERRORLEVEL%.
            exit /b %ERRORLEVEL%
        )
    ) else (
        echo Virtual environment created successfully using `py`.
    )
) else (
    echo Virtual environment already exists.
)

echo Activating the virtual environment...
call .venv\Scripts\activate

echo Updating pip...
python.exe -m pip install --upgrade pip

echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

echo Deactivating the virtual environment...
deactivate

echo generating file bat to run main.py try to run it using py main.py or python main.py
(
echo @echo off
echo py main.py

echo if ERRORLEVEL 1 (
echo     echo `py main.py` failed. Trying with `python`...
echo     python main.py

echo     if ERRORLEVEL 1 (
echo         echo `python main.py` also failed. Exiting with error level %ERRORLEVEL%.
echo         exit /b %ERRORLEVEL%
echo     ) else (
echo         echo Script completed successfully using `python`.
echo     )
echo ) else (
echo     echo Script completed successfully using `py`.
echo )
) > run.bat

echo Script completed.
endlocal
