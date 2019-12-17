from ribbon import customUI14base as base

class Root(base.CT_CustomUI):

    def __init__(self, onLoad=None, loadImage=None, commands=None, ribbon=None,
        backstage=None, contextMenus=None, **kwargs):
        super(Root, self).__init__(onLoad, loadImage, commands, ribbon,
            backstage, contextMenus, **kwargs)
        self.ns_prefix_ = ""
    
    def export(self, *args, **kwargs):
        kwargs.update({
            'namespacedef_': 'xmlns="http://schemas.microsoft.com/office/2009/07/customui"',
            'name_': 'customUI',
        })
        super(Root, self).export(*args, **kwargs)

class Ribbon(base.CT_Ribbon):
    def __init__(self, startFromScratch=None, qat=None, tabs=None, contextualTabs=None,
        **kwargs):
        super(Ribbon, self).__init__(startFromScratch, qat, tabs, contextualTabs,
            **kwargs)

class Groups(base.CT_SimpleGroups):
    """Specifies a collection of simple groups"""
    def __init__(self, group=None, taskGroup=None, **kwargs):
        super(Groups, self).__init__(group, taskGroup,  **kwargs)

class Group(base.CT_Group):
    """Specifies a single group"""
    def __init__(self, autoScale=None, centerVertically=None, id=None, idQ=None, tag=None,
        idMso=None, label=None, getLabel=None, image=None, imageMso=None, getImage=None,
        insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None,
        screentip=None, getScreentip=None, supertip=None, getSupertip=None, visible=None,
        getVisible=None, keytip=None, getKeytip=None, control=None, labelControl=None,
        button=None, toggleButton=None, checkBox=None, editBox=None, comboBox=None,
        dropDown=None, gallery=None, menu=None, dynamicMenu=None, splitButton=None,
        box=None, buttonGroup=None, separator=None, dialogBoxLauncher=None, **kwargs):
        super(Group, self).__init__(autoScale, centerVertically, id, idQ, tag,
            idMso, label, getLabel, image, imageMso, getImage, insertAfterMso,
            insertBeforeMso, insertAfterQ, insertBeforeQ, screentip, getScreentip,
            supertip, getSupertip, visible, getVisible, keytip, getKeytip, control,
            labelControl, button, toggleButton, checkBox, editBox, comboBox, dropDown,
            gallery, menu, dynamicMenu, splitButton, box, buttonGroup, separator,
            dialogBoxLauncher,  **kwargs)

class Tabs(base.CT_Tabs):
    """Specifies a collection of regular tabs"""
    def __init__(self, tab=None, **kwargs):
        super(Tabs, self).__init__(tab,  **kwargs)

class ContextualTabs(base.CT_ContextualTabs):
    """Specifies a collection of contextual tabs such as Chart tabs"""
    def __init__(self, tabSet=None, **kwargs):
        super(ContextualTabs, self).__init__(tabSet,  **kwargs)

class Tab(base.CT_Tab):
    """Specifies a single tab"""
    def __init__(self, id=None, idQ=None, tag=None, idMso=None, label=None,
        getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None,
        insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None,
        group=None, **kwargs):
        super(Tab, self).__init__(id, idQ, tag, idMso, label, getLabel,
            insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible,
            getVisible, keytip, getKeytip, group,  **kwargs)

class ButtonRegular(base.CT_ButtonRegular):
    template_callback = """
    Sub call{fun}(control as IRibbonControl)
        Call {fun}
    End Sub
    """

    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, 
        getScreentip=None, supertip=None, getSupertip=None, enabled=None,
        getEnabled=None, label=None, getLabel=None, insertAfterMso=None, 
        insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None,
        getVisible=None, keytip=None, getKeytip=None, showLabel=None,
        getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None,
        tag=None, idMso=None, onAction=None, description=None, getDescription=None,
        extensiontype_=None, **kwargs):
        super(ButtonRegular, self).__init__(image, imageMso, getImage, screentip,
            getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel,
            insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible,
            getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage,
            getShowImage, id, idQ, tag, idMso, onAction, description, getDescription,
            extensiontype_,  **kwargs)


class Separator(base.CT_Separator):
    """Specifies a ribbon separator"""
    def __init__(self, id=None, idQ=None, tag=None, visible=None, getVisible=None,
        insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None,
        **kwargs):
        super(Separator, self).__init__(id, idQ, tag, visible, getVisible, insertAfterMso,
            insertBeforeMso, insertAfterQ, insertBeforeQ,  **kwargs)