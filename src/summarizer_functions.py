import requests
from io import BytesIO
from PyPDF2 import PdfReader
from openai import OpenAI

class Article:
    '''
    Representaion of a research article.
    '''
    def __init__(self, url):
        '''
        Creates an article object from the given URL.
        
        Args:
            url (str): URL of the research article PDF.
        '''
        self.url = url
        response = requests.get(self.url)
        if response.status_code == 200:
            pdf_bytes = BytesIO(response.content)
            reader = PdfReader(pdf_bytes)
            
            text = ''
            for page in reader.pages:
                text += page.extract_text()
                
            self.text = text
            self.title = reader.metadata.get('/Title', 'No title found')
        else:
            print(f'Failed to fetch PDF. Error code: {response.status_code}')
            self.text = 'No text found'
            self.title = 'No title found'
            
            
def create_user_prompt(article):
    '''
    Generates user prompt based on the article.
    
    Args:
        article (Article): Research article object.
        
    Returns:
        str: User prompt.
    '''
    user_pompt = f'You are looking at a research article titled {article.title}.\n Based on the body of this article, please summarize this whole article. \
                The body of the article is as follows.'
    user_pompt += article.text
    return user_pompt


def create_messages(article):
    '''
    Generates messages for summarization based on the article.
    
    Args:
        article (Article): Research article object.
        
    Returns:
        list: List of messages.
    '''
    system_prompt = 'You are an AI assistant that analyses the contents of research articles and generate summary of whole article in 250 words or less. \
                    Ignore text that does not belong to the article, like headers or navigation related text. Respond in markdown format.'
    return [
        {'role': 'systen', 'content': system_prompt},
        {'role': 'user', 'content': create_user_prompt(article)}
    ]
    
    
def summarize(url, model = 'llama3.2', api_base_url = 'http://localhost:11434/v1', api_key = 'ollama'):
    '''
    Summarizes the research article from the given URL.
    
    Args:
        url (str): URL of the research article PDF.
        model (str): OpenAI model to use for summarization.
        api_base_url (str): Base URL of the OpenAI API.
        api_key (str): OpenAI API key.
        
    Returns:
        str: Summary of the research article.
    '''
    openai = OpenAI(base_url = api_base_url, api_key = api_key)
    article = Article(url)
    response = openai.chat.completions.create(
        model = model,
        messages = create_messages(article)
    )
    return response.choices[0].message.content