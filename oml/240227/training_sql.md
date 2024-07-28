[training_sql.ipynb](https://github.com/Suyeon-j/study_oml/blob/main/240227/training_sql.ipynb)

```
속성: label, path, split, is_query, is_gallery // 모두 NOT NULL 
입력: 사진 // 한 명당 3장씩 파일 이름을 영어로 설정해둘 것 ex) 홍길동01.jpg (X) => Hong01.jpg (O)
```

> 수정할 내용
```
1. RuntimeError: stack expects each tensor to be equal size, but got [3, 647, 647] at entry 0 and [3, 651, 1179] at entry 1 문제 해결
2. 한 사람당 여러 장이 들어와도 프로그램이 문제 없이 수행되도록 수정할 것
```
