class BookBuilder:
    def __init__(self):
        self.book = {
            "title": "Default Title",
            "author": "Default Author",
            "description": "Default Description",
            "year_published": 2000
        }

    def with_title(self, title):
        self.book["title"] = title
        return self

    def with_author(self, author):
        self.book["author"] = author
        return self

    def with_description(self, description):
        self.book["description"] = description
        return self

    def with_year_published(self, year):
        self.book["year_published"] = year
        return self

    def build(self):
        return self.book
