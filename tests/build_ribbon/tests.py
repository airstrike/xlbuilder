import unittest
import os, sys

from ribbon.elements import (Root, Ribbon, Group, Tabs, ContextualTabs, Tab,
    ButtonRegular, Separator)

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
        cls.group_one = Group(id='productivityGroup', label='Productivity')
        cls.tab_one = Tab(id='TerraTab', label='Terra', insertAfterMso='TabView', keytip='/')
        cls.ribbon = Ribbon()
        cls.tabs = Tabs()
        cls.tabs.add_tab(cls.tab_one)
        cls.groups = []
        cls.groups.append(cls.group_one)
        cls.root = Root()
        cls.button_one = None

    def test_001_create_group(self):
        self.assertEqual(self.group_one.id, 'productivityGroup')

    def test_002_create_tab(self):
        self.assertEqual(self.tab_one.id, 'TerraTab')

    def test_003_assign_tab_to_group(self):
        self.tab_one.group = self.groups
        self.assertEqual(self.tab_one.group, self.groups)

    def test_004_add_buttons_to_group(self):
        button_one = ButtonRegular(id='btnCircSwitch', label='Circularity', size='large',
            onAction='callCircSwitch', imageMso='ReviewPreviousComment', keytip='C')
        self.group_one.add_control(button_one)

    def test_005_add_separator_to_group(self):
        s = Separator()
        self.group_one.add_control(s)
        button_one = ButtonRegular(id='btnCircSwitch', label='Circularity', size='large',
            onAction='callCircSwitch', imageMso='ReviewPreviousComment', keytip='C')
        self.group_one.add_control(button_one)

    def test_090_create_ribbon(self):
        self.ribbon.tabs = self.tabs

    def test_091_export_ribbon(self):
        self.root.ribbon = self.ribbon
        self.root.export(outfile=self.outfile, level=0, name_='customUI')

    @classmethod
    def tearDownClass(cls):
        cls.outfile.close()
        print('\n')
        with open(cls.outfile_path, 'r') as f:
            for l in f.readlines():
                sys.stdout.write(l)
            sys.stdout.write('')
        try:
            os.unlink(cls.outfile_path)
            pass
        except:
            pass

if __name__ == '__main___':
    unittest.main()

