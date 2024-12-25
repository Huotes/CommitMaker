from commitmaker.api_client import obter_frase_meme

def test_obter_frase_meme(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"joke": "Test joke"}
    mocker.patch("requests.get", return_value=mock_response)
    
    joke = obter_frase_meme()
    assert joke == "Test joke"
