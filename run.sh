( 
    python -m venv venv && 
    venv/Scripts/activate && 
    dao/dataset.py && 
    !unzip -q data.zip &&
    !rm -rf data.zip &&
    src/Regression.py &&
    src/2ndOrder.py &&
    src/3rdOrder.py && 
    src/4thOrder.py 
)