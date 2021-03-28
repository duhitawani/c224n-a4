#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch.nn as nn

class ModelEmbeddings(nn.Module): 
    """
    Class that converts input words to their embeddings.
    """
    def __init__(self, embed_size, vocab):
        """
        Init the Embedding layers.

        @param embed_size (int): Embedding size (dimensionality)
        @param vocab (Vocab): Vocabulary object containing src and tgt languages
                              See vocab.py for documentation.
        """
        super(ModelEmbeddings, self).__init__()
        self.embed_size = embed_size

        # default values
        self.source = None
        self.target = None

        src_pad_token_idx = vocab.src['<pad>']
        tgt_pad_token_idx = vocab.tgt['<pad>']

        
        self.source = nn.Embedding(num_embeddings=len(vocab.src),embedding_dim=self.embed_size,padding_idx=src_pad_token_idx) 
        self.target = nn.Embedding(num_embeddings=len(vocab.tgt),embedding_dim=self.embed_size,padding_idx=tgt_pad_token_idx)
        
        self.source = nn.Embedding(num_embeddings=len(vocab.src),embedding_dim=self.embed_size,padding_idx=src_pad_token_idx) 
        self.target = nn.Embedding(num_embeddings=len(vocab.tgt),embedding_dim=self.embed_size,padding_idx=tgt_pad_token_idx)


