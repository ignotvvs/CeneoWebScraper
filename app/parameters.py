selectors = {
    "author": ["span.user-post__author-name"],
    "recommendation": ["span.user-post__author-recomendation > em"],
    "stars": ["span.user-post__score-count"],
    "content": ["div.user-post__text"],
    "useful": ["button.vote-yes > span"],
    "useless": ["button.vote-no > span"],
    "published": ["span.user-post__published > time:nth-child(1)", "datetime"],
    "purchased": ["span.user-post__published > time:nth-child(2)", "datetime"],
    "pros": ["div.review-feature > div.review-feature__section > div.review-feature__item--positive", None, True],
    "cons": ["div.review-feature > div.review-feature__section > div.review-feature__item--negative", None, True]
}