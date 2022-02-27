import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    test case to test the behavior of the News class
    '''

    def setUp(self):
        '''
        method to run before each test case
        '''
        self.new_news = News('Milica', 'Meghan Markle news latest – Prince Harry & Duchess pick up prestigious award as Duke acknowledges people o... - The US Sun', "Inside Harry and Meghan's business empire- Meghan and Harry’s net worth explained",'https://www.the-sun.com/lifestyle/4759440/meghan-markle-prince-harry-latest-news/', 'https://www.the-sun.com/wp-content/uploads/sites/6/2022/02/Meghan-3.png?strip=all&quality=100&w=1200&h=800&crop=1', '2022-02-27T10:40:00Z', "Harry's diet Stanton has analysed the Royal family's preferred food choices, on behalf of UK coffee retailer Coffee Friend… [+1166 chars]" )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__=='__main__':
    unittest.main()





#asda
