import unittest
import os, sys

from ribbon.elements import Root, Ribbon, Groups, Group, Tabs, ContextualTabs, Tab

class Test_BuildRibbonManually(unittest.TestCase):
    outfile = None
    outfile_path = ''

    group_one = None
    groups = None
    tab_one = None
    tabs = None
    ribbon = None
    root = None
    
    @classmethod
    def setUpClass(cls):
        cls.outfile_path = 'tests/build_ribbon/ribbon.xml'
        cls.outfile = open(cls.outfile_path, 'w')
        cls.group_one = Group(id='GroupOne')
        cls.tab_one = Tab(id='TabOne')
        cls.ribbon = Ribbon()
        cls.tabs = Tabs()
        cls.tabs.add_tab(cls.tab_one)
        cls.groups = []
        cls.groups.append(cls.group_one)
        cls.root = Root()

    def test_create_group(self):
        self.assertEqual(self.group_one.id, 'GroupOne')

    def test_create_tab(self):
        self.assertEqual(self.tab_one.id, 'TabOne')

    def test_add_tab_to_group(self):
        self.tab_one.group = self.groups
        self.assertEqual(self.tab_one.group, self.groups)

    def test_create_ribbon(self):
        self.ribbon.tabs = self.tabs

    def test_export_ribbon(self):
        self.root.ribbon = self.ribbon
        self.root.export(outfile=self.outfile, level=0, name_='customUI')

    @classmethod
    def tearDownClass(cls):
        cls.outfile.close()
        print('\n')
        with open(cls.outfile_path, 'r') as f:
            for l in f.readlines():
                sys.stdout.write(l)

        try:
            # os.unlink(cls.outfile_path)
            pass
        except:
            pass

if __name__ == '__main___':
    unittest.main()

