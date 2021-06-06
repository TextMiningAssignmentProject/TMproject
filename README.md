# TMproject

텍스트마이닝 프로젝트

주제 : 실시간 카테고리 분류

프로젝트 이름 : 너의 주제를 알라

설명 : 현재 작성하는 글이 어떤 주제를 띄고 있는지 실시간으로 확인 시켜줍니다. 해당 프로젝트는 교내에서 기말고사 대체 프로젝트이며, 좋은 성능은 기대하지마세요.

### Requirement Software

1. Python 3.7
2. konlpy
3. bs4
4. etc..

Run as administartor

```
conda create --name tmclass-3 python=3.7
conda activate tmclass-3
conda install -c conda-forge jpype1=1.1.2 ipykernel
pip install konlpy requests bs4 sklearn flask
```

#### How to use it? ( 사용 방법 )

###### service.py 실행

```
py service.py
```

#### Author

- Yonghoon Jung, @dydgns2017
- Ikjun Jin, @ikju1117
- Hyosun Yang, @didgytjs

#### Reference

- H 교수님 자료
- 블로그 포스트의 자동 분류 시스템, 제 25회 한글 및 한국어 정보처리 학술대회 논문집 (2013년)
