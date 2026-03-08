#자동화테스트코드(ct)
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200 # 서버가 200(정상)을 반환하는지 테스트!
    assert response.json() == {"message": "Hello Mobis! CI/CD/CT Pipeline is working!"}