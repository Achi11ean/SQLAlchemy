class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise TypeError("Title Must be of type str")
        if not (5 <= len(title) <= 50):
            raise ValueError("Must be between 5 - 50 characters")
        self.author = author
        self.magazine = magazine
        self._title = title
        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)
    @property
    def title(self):
        return self._title
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) == 0: 
            raise ValueError("Must be more than 0 characters long")
        self._name = name
        self._articles = [] 
    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise TypeError("must be of type str")
        if not (2 <= len(value) <= 16):
            raise ValueError("must be between 2-16 characters")
        self._name = value
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be of type str")
        if len(value) == 0:
            raise ValueError("Category Must be longer than 0 characters")
        self._category = value
    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:        
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = [article.author for article in self._articles]
        author_counts = {author: authors.count(author) for author in set(authors)}
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        # return list(set(article.author for article in self._articles))

        if not contributing_authors:
            return None
        return contributing_authors