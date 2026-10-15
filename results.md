| name | model_type | hidden_size | learning_rate | optimizer | epochs | best_accuracy | training_time_sec | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cnn_baseline | cnn | 128 | 0.001 | adam | 5 | 0.9902 | 104.56 | 换成 CNN，准确率应该更高 |
| fc_deep_256 | fc_deep | 256 | 0.001 | adam | 5 | 0.9798 | 35.11 | 两层隐藏层的全连接 |
| fc_hidden_256 | fc | 256 | 0.001 | adam | 5 | 0.9792 | 35.97 | 隐藏层从 128 改到 256 |
| baseline_fc_128_adam_0.001 | fc | 128 | 0.001 | adam | 5 | 0.9751 | 29.46 | 基线：全连接 + 128 隐藏层 + Adam |
| fc_hidden_64 | fc | 64 | 0.001 | adam | 5 | 0.9709 | 42.17 | 隐藏层从 128 改到 64 |
| fc_lr_0.01 | fc | 128 | 0.01 | adam | 5 | 0.9674 | 39.13 | 学习率 0.001 -> 0.01 |
| fc_lr_0.0001 | fc | 128 | 0.0001 | adam | 5 | 0.9324 | 33.5 | 学习率 0.001 -> 0.0001 |
| fc_sgd | fc | 128 | 0.01 | sgd | 5 | 0.9132 | 26.01 | Adam 换成 SGD（学习率调大） |