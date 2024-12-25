import os
from commitmaker.readme_updater import atualizar_readme

def test_atualizar_readme(mocker):
    mocker.patch("commitmaker.readme_updater.obter_frase_meme", return_value="Test meme")
    readme_path = os.path.join(os.path.dirname(__file__), "../README.md")
    
    with open(readme_path, "r") as f:
        lines_before = f.readlines()
    
    atualizar_readme()
    
    with open(readme_path, "r") as f:
        lines_after = f.readlines()
    
    assert len(lines_after) > len(lines_before)
    assert "Test meme" in lines_after[-1]
