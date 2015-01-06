import test_setup
import test_fixtures

import json

from bookmark import Bookmark as B

class TestBookmark(object):

    def test_klass_create_bookmark(self):
        fixture_klass = test_fixtures.BookmarkFixture
        f = fixture_klass()

        #bookmark = B.create(**f.data)
        #for attribute in B.required_attrs: 
            #assert getattr(bookmark, attribute) == f.data[attribute]



