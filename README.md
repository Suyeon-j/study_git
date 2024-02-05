# study_oml
> [OML](https://open-metric-learning.readthedocs.io/en/latest/index.html)


> [OML example_training](https://colab.research.google.com/drive/1kntDAIdIZ9L40jcndguLAb-XqmCFOgS5?usp=sharing)
>> Training
```
ViTExtractor("vits16_dino", arch="vits16", normalise_features=False).train()
```
ViTExtractor(weights(사전 훈련된 가중치 지정 매개변수), arch(모델 아키텍처 선택), normalise_features(특성 정규화 여부)): Visual Transformer 아키텍처를 따르는 추출기의 기본 클래스
```
TripletLossWithMiner(margin=0.1, miner=AllTripletsMiner(), need_logs=True)
```
TripletLossWithMiner(margin(triplet loss의 마진 설정), miner(triplet을 생성하는데 사용되는 miner를 지정하는 함수), need_logs(로그 기록 여부)): Miner and TripletLoss 조합

AllTripletsMiner():모든 가능한 트리플릿을 생성하는 miner를 사용하여 triplet을 구성
```
BalanceSampler(train_dataset.get_labels(), n_labels=2, n_instances=2)
```
BalanceSampler(labels(레이블 이), n_labels(배치 레이블 수), n_instances(배치 레이블 인스턴스 수)): n_instances x n_labels 배치 구성

![image](https://github.com/Suyeon-j/study_oml/assets/66247203/a44f12de-a80d-4051-936b-65b661a0d1ac)

양/음 거리, 활성 삼중항 


>> Validation


>> Training + Validation [Lightning and logging]
Open In Colab

>> Using a trained model for retrieval
Open In Colab
