from typing import List

class CountVectorizer:

    def __init__(self, lowercase=True):
        self.lowercase = lowercase
        self._vocabulary = []

    def fit_transform(self, corpus : List[str]) -> List[List[int]]:
        """
        Fit transform method

        input
        -----
        corpus of texts

        return
        ------
        feature vectors, 1 if word in the text, o.w. 0
        """
        corpus_cp = self._preprocess_text(corpus)
        vocab = self.get_feature_names()

        feature_vects = []
        for text in corpus_cp:
            feature_vects.append([1 if word in text else 0 for word in vocab])
        return feature_vects

    def get_feature_names(self) -> List[str]:
        return self._vocabulary

    def _feature_names(self, corpus : List[str]):
        """
        Extract features from the corpus of texts

        input
        -----
        corpus of texts

        return
        ------
        feature names assigned to _vocabulary attribute
        """
        
        # convert to one string of words
        words = ' '.join(corpus).split(' ')

        text_vocab = set(words)
        for word in words:
            if word in text_vocab:
                self._vocabulary.append(word)
                text_vocab.remove(word)

    def _preprocess_text(self, corpus : List[str]) -> List[str]:
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
        remove_punc = lambda s : s.translate(
            str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
        
        if self.lowercase:
            corpus_cp = list(map(lambda s: remove_punc(s.lower()), corpus_cp))
        else:
            corpus_cp = list(map(lambda s: remove_punc(s), corpus_cp))
        
        # extract feature names
        self._feature_names(corpus_cp)
        
        return corpus_cp
