import io
import os, sys
import unittest

from ribbon.elements import (Root, Ribbon, Group, Tabs, ContextualTabs, Tab,
    ButtonRegular, Separator)

class Test_BuildRibbon(unittest.TestCase):
    outfile = None
    outfile_path = ''
    ribbon = None

    @classmethod
    def setUpClass(cls):
        cls.outfile = io.StringIO()
        cls.ribbon = Ribbon()

    def test_001_add_content_to_ribbon(self):
        self.ribbon.create_tab(id='mytab')
        charttab = Tab(id='charttab')
        self.ribbon.add_tab(charttab, tab_type='chart')
        self.ribbon.create_tab(id='another chart tab', tab_type='chart')
    
    def test_002_general_test(self):
        r = Ribbon()
        r.create_tab(id='MyTab', label='My Tab', insertAfterMso='TabView', keytip='T')
        r.create_tab(label='My Chart Tab', tab_type='chart') # generated id is 'MyChartTab'

        # the following line references an inexistent group, which is inferred
        # and automatically created in the MyTab tab for simplicity 
        r.create_button(label='Foo button', group='My Group', group_kwargs={'label': 'My Group'}, tab='MyTab')
        r.create_button(label='Bar button', group='My Group', tab='MyTab', level=1)
        r.create_separator(group='My Group', tab='My Tab', level=2)
        r.create_button(label='Bar button', group='My Group', tab='MyTab')
        r.create_button(label='Chart button', group='Chart Group', tab='MyChartTab', tab_type='chart')
        r.build_ribbon(outfile=self.outfile)

    def _test_100_build_ribbon(self):
        self.ribbon.build_ribbon(outfile=self.outfile)

    @classmethod
    def tearDownClass(cls):
        cls.outfile.seek(0)
        for l in cls.outfile.readlines():
            sys.stdout.write(l)
        sys.stdout.write('')
        print('\n')
        cls.outfile.close()

if __name__ == '__main___':
    unittest.main()

