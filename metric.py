
def dcg_score(y_true, y_score, k=10):
    order = np.argsort(y_score)[::-1]
    y_true = np.take(y_true, order[:k])
    gains = 2 ** y_true - 1
    discounts = np.log2(np.arange(len(y_true)) + 2)
    return np.sum(gains / discounts)


def ndcg_score(y_true, y_score, k=10):
    best = dcg_score(y_true, y_true, k)
    actual = dcg_score(y_true, y_score, k)
    return actual / best


def mrr_score(y_true, y_score):
    order = np.argsort(y_score)[::-1]
    y_true = np.take(y_true, order)
    rr_score = y_true / (np.arange(len(y_true)) + 1)
    return np.sum(rr_score) / np.sum(y_true)


def auc(label,score):
    label=np.array(label)
    score=np.array(score)
    false_score = score[label==0]
    positive_score = score[label==1]
    num_positive = (label==1).sum()
    num_negative = (label==0).sum()
    positive_score = positive_score.reshape((num_positive,1))
    positive_score = np.repeat(positive_score,num_negative,axis=1)
    false_score = false_score.reshape((1,num_negative))
    false_score = np.repeat(false_score,num_positive,axis=0)
    return 1-((positive_score<false_score).mean()+0.5*(positive_score==false_score).mean())
