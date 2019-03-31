# -*- coding: utf-8 -*-
import unittest
import textwrap
from delete_last_comma import core

class CoreTestSuite(unittest.TestCase):
    """Core.py test cases."""

    def test_delete_last_comma(self):
        """ケツカンマ削除"""
        including_last_comma = textwrap.dedent(
            """
            {
                "hoge" : ["hoge1", "hoge2", "hoge3", ],
                "bar" : 1,
                "foo" : "foo1",
            }
            """)
        excluding_last_comma = textwrap.dedent(
            """
            {
                "hoge" : ["hoge1", "hoge2", "hoge3" ],
                "bar" : 1,
                "foo" : "foo1"
            }
            """)
        deleted_comma = core.delete_last_comma(including_last_comma)
        self.assertEqual(deleted_comma, excluding_last_comma)

if __name__ == '__main__':
    unittest.main()