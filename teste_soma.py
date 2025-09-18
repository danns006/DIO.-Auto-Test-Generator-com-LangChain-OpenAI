import pytest
from soma import soma

def test_soma_sucesso():
    assert soma(2, 3) == 5

def test_soma_falha():
    with pytest.raises(TypeError):
        soma(2, "a")
