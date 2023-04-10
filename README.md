# Django REST Framework

### Poetry

```shell
# 패키지 추가 (dev는 -D 옵션)
$ poetry add {패키지}

# 정의된 패키지 설치
$ poetry install

# 설치된 패키지 삭제
$ poetry remove {패키지}

# 패키지 동기화
$ poetry install --sync
$ poetry install --without dev --sync
$ poetry install --with docs --sync
$ poetry install --only dev
```

### Seed

```shell
# 프로그램
$ python manage.py seed_programs --number={개수}

# 호스트
$ python manage.py seed_hosts --number={개수}
```