from app.parameters import selectors
from app.utils import get_item

class Opinion():
    def __init__(self, opinion_id="", author="", recommendation=None, stars=0, content="", useful=0, useless=0, published = None, purchased=None, pros=[], cons=[]):
        self.opinion_id = opinion_id
        self.author = author
        self.recommendation = recommendation
        self.stars = stars 
        self.content = content 
        self.useful = useful 
        self.useless = useless 
        self.published = published
        self.purchased = purchased
        self.pros = pros 
        self.cons = cons
        

    def extract_opinions(self, opinion):
        for key, value in selectors.items():
            setattr(self, key, get_item(opinion, *value))
        self.opinion_id = opinion["data-entry-id"]
        return self    
        
    def __str__(self) -> str:
        text = f"""Opinion ID:     {self.opinion_id}
        Author:         {self.author}
        Recommendation: {self.recommendation}
        Stars:          {self.stars} 
        Content:        {self.content} 
        Useful:         {self.useful} 
        Useless:        {self.useless} 
        Published:      {self.published}
        Purchased:      {self.purchased}
        Pros:           {self.pros} 
        Cons:           {self.cons}"""   
        return text

    def __repr__(self) -> str:
        return f"Opinion({self.opinion_id},{self.author},{self.recommendation},{self.stars},{self.content},{self.useful},{self.useless},{self.published},{self.purchased},{self.pros},{self.cons})"    

    def to_dict(self) -> dict:
        toDict = {
            "opinion_id": self.opinion_id,
            "author": self.author,
            "recommendation": self.recommendation,
            "stars": self.stars, 
            "content": self.content, 
            "useful": self.useful, 
            "useless": self.useless,
            "published": self.published,
            "purchased": self.purchased,
            "pros": self.pros, 
            "cons": self.cons,
        }
        return toDict