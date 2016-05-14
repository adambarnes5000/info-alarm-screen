import feedparser


def get_news():
    data = feedparser.parse("http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk")
    return map(convert_entry, data.entries[:5])


def convert_entry(entry):
    return {'title': entry.title, 'detail': entry.description, 'linkUrl': entry.link}


if __name__ == "__main__":
    print get_news()
