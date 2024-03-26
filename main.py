import os
import warnings
from typing import Dict

from openfabric_pysdk.utility import SchemaUtil

from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import Ray, State
from openfabric_pysdk.loader import ConfigClass

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "allenai/scibert_scivocab_uncased"
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

############################################################
# Use SciBERT Pre-trained Model
############################################################
def generate_answer(text):
    question, context = text.split(' ||| ')
    
    answer = nlp({
        'question': question,
        'context': context
    })['answer']
    
    return answer

############################################################
# Callback function called on update config
############################################################
def config(configuration: Dict[str, ConfigClass], state: State):
    # TODO Add code here
    pass

############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:
    output = []
    for text in request.text:
        response = generate_answer(text)
        output.append(response)

    return SchemaUtil.create(SimpleText(), dict(text=output))
