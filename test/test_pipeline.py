import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from day3_pipeline.dataloader import load_data

def test_load_data():
    data = load_data()
    assert data is not None
    assert hasattr(data, 'data')
    assert hasattr(data, 'target')
    assert len(data.data) > 0
    assert len(data.target) > 0