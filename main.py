import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
from spacy.util import filter_spans

import json

f = open("annotations_0.json")
annotations = json.load(f) # Load the annotations as array

training_data = {
    'classes': ['NAME', 'MAIL', 'PHONE', 'LINK', 'DEGREE', 'UNIV', 'SKILL'],
    'annotations': annotations
}

# load blank spacy model
nlp = spacy.blank("en")
doc_bin = DocBin()

# add training data to docbin
for training_example  in tqdm(training_data['annotations']): 
    text = training_example['text']
    labels = training_example['entities']
    doc = nlp.make_doc(text) 
    ents = []
    for start, end, label in labels:
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is not None:
            ents.append(span)
    filtered_ents = filter_spans(ents)
    doc.ents = filtered_ents 
    doc_bin.add(doc)

# save the docbin object
doc_bin.to_disk("training_data.spacy")
