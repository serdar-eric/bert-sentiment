import transformers


MAX_LEN = 512
TRAIN_BATCH_SIZE = 2
VALID_BATCH_SIZE = 2
EPOCHS = 10
BERT_PATH = "bert-base-uncased" #"../input/bert_base_uncased/"
MODEL_PATH = "model.bin"
TRAINING_FILE = "../input/imdb.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(
    "bert-base-uncased",
    do_lower_case=True
)
