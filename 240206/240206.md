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
```
torch.utils.data.DataLoader(train_dataset, batch_sampler=sampler)
```
torch.utils.data.DataLoader(): 데이터를 로드하고 배치를 만들어주는 유틸리티 클래스

![image](https://github.com/Suyeon-j/study_oml/assets/66247203/a44f12de-a80d-4051-936b-65b661a0d1ac)
print(criterion.last_logs): 양/음 거리, 활성 삼중항 


>> Validation
```
DatasetQueryGallery(df_val, dataset_root=dataset_root)
```
DatasetQueryGallery(): 검증 단계에서 데이터 세트로 사용하기 위해 쿼리/갤러리 분할 정보를 넘겨줘야함 
+) 유효성 검사 프로세스를 수행할 때 데이터셋이 분할 정보를 포함하고 있지않다면 is_query와 is_gallery가 모두 True여야 함
```
calculator = EmbeddingMetrics(extra_keys=["paths",]).setup(num_samples=len(val_dataset))
```
EmbeddingMetrics(extra_keys(배치에서 몇가지 정보를 추가 정보를 축적하는 키)): 매 배치마다 모델이 생성한 배치와 임베딩에서 얻은 정보를 에포크 단위로 축적

calculator.setup(num_samples=len(val_dataset)): self.update_data() 첫 호출 전에 호출해야 함
```
calculator.update_data(batch)
```
calculator.update_data(batch): 나중에 메트릭을 계산하기 위해 데이터를 전달하는 것
```
calculator.compute_metrics()
calculator.metrics  # metrics
calculator.metrics_unreduced  # metrics without averaging over queries(쿼리에 대한 평균을 사용하지 않은 것)
```
calculator.compute_metrics(): 포멧 형식
```
{
    "self.overall_categories_key": {"metric1": ..., "metric2": ...},
    "category1": {"metric1": ..., "metric2": ...},
    "category2": {"metric1": ..., "metric2": ...}
}
```
![image](https://github.com/Suyeon-j/study_oml/assets/66247203/ae918bcd-17fc-4500-8ad2-f6af96cbad90)
- cmc: 쿼리까지의 거리로 정렬된 상위 k 갤러리 인스턴스에 이 쿼리와 관련된 인스턴스가 하나 이상 있는 경우 1, 그렇지 않은 경우 0 (cmc@k: 각 쿼리에 대해 계산된 결과 평균)
- map: 평균 정밀도를 계산하는 함수(map@k: recall의 함수로 간주되는 정밀도의 평균 값)
- pcf: 주성분 분석을 사용해 임베딩의 주성분 비율을 추정(metric은 데이터의 필요한 분산을 설명하는데 필요한 성분의 비율로 정의)
- precision: 정밀도(precision@k: 쿼리에서 갤러리까지의 거리로 정렬된 상위 k개 인스턴스 중 관련 갤러리 인스턴스의 일부)
![image](https://github.com/Suyeon-j/study_oml/assets/66247203/df591ad5-baaf-4511-aa88-cdb8bce01cb6)
시각화
Draw predictions for predefined queries: 미리 정의된 쿼리에 대한 예측
Draw the queries worst by map@5: map@5로 최악의 쿼리 그리기

>> Training + Validation [Lightning and logging]
```
plt.ioff()
```
plt.ioff(): 대화 모드 비활성화 -> 그래프가 자동으로 보이지 않음
```
MetricValCallback(metric=EmbeddingMetrics(extra_keys=["paths",]), log_images=True);
```
MetricValCallback(metric):검증단계에서 metric을 계산하고 로그에 기록하는 역할

Tensorboard, Neptune, Weights and Biases: 로그 기록

```
ExtractorModule(model, criterion, optimizer)
```
ExtractorModule(model, criterion, optimizer): 라이트닝 모델 훈련시키기 위한 기본 모듈
```
pl.Trainer(max_epochs=3, callbacks=[metric_callback], num_sanity_val_steps=0, logger=logger)
```
pl.Trainer(): 모델의 학습을 담당하는 클래스

>> Using a trained model for retrieval
```
pairwise_dist(x1=features_queries, x2=features_galleries)
```
pairwise_dist(x1=features_queries, x2=features_galleries): 두 텐서 간 거리를 계산하는 함수
