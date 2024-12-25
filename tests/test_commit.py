import subprocess
from commitmaker.commit import realizar_commit

def test_realizar_commit(mocker):
    mocker.patch("subprocess.run")
    realizar_commit()
    subprocess.run.assert_called()
