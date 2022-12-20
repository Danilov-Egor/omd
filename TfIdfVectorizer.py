import numpy as np
from typing import List

from countvectorizer import CountVectorizer


class TfidfVectorizer(CountVectorizer):

    def __init__(self, lowercase=True):
        self.lowercase = lowercase

        # cv = CountVectorizer(lowercase=lowercase)
        # self.cv_matrix = np.array(cv.fit_transform(corpus))
        # self._vocabulary = cv._vocabulary

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Fit transform method

        input
        -----
        corpus of texts

        return
        ------
        tf-idf matrix
        """
        cv = CountVectorizer(lowercase=self.lowercase)
        cv_matrix = np.array(cv.fit_transform(corpus))
        self._vocabulary = cv._vocabulary

        tf_matrix = TfidfVectorizer._tf_transform(self, cv_matrix)
        idf_matrix = TfidfVectorizer._idf_transform(self, cv_matrix)
        tf_idf_matrix = []
        for i in range(len(tf_matrix)):
            vect = []
            for j in range(len(tf_matrix[i])):
                vect.append(round(tf_matrix[i][j] * idf_matrix[j], 3))
            tf_idf_matrix.append(vect)
        return tf_idf_matrix

    def get_feature_names(self) -> List[str]:
        return list(self._vocabulary.keys())

    def _tf_transform(self, cv_matrix):
        """
        tf_transform
        """
        tf_matrix = []
        for arr in cv_matrix:
            sum_arr = sum(arr)
            tf_matrix.append([i / sum_arr for i in arr])
        return tf_matrix

    def _idf_transform(self, cv_matrix):
        """
        idf_transform
        """
        numb_of_docs = len(cv_matrix)
        idf_matrix = np.array([0] * len(self._vocabulary))
        for arr in cv_matrix:
            for j in range(len(arr)):
                if arr[j] > 0:
                    idf_matrix[j] += 1
        idf_matrix = np.log((numb_of_docs + 1) / (idf_matrix + 1)) + 1
        return idf_matrix

    def _preprocess_text(self, corpus: List[str]) -> List[str]:
        """
        processing corpus of texts, remove punctuation
        and apply lower function.

        input
        -----
        corpus of texts

        return
        ------
        copy of preprocessed texts
        """
        corpus_cp = corpus.copy()

        # remove punctuation
        remove_punc = lambda s: s.translate(
            str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))

        if self.lowercase:
            corpus_cp = list(map(lambda s: remove_punc(s.lower()), corpus_cp))
        else:
            corpus_cp = list(map(lambda s: remove_punc(s), corpus_cp))

        # extract feature names
        self._feature_names(corpus_cp)

        return corpus_cp


corpus = [
 'Crock Pot Pasta Never boil pasta again',
 'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
print(tfidf_matrix)
