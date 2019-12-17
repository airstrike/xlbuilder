import customUI14base

class Ribbon(supermod.CT_Ribbon):
    def __init__(self, startFromScratch=None, qat=None, tabs=None, contextualTabs=None,
        **kwargs_):
        super(Ribbon, self).__init__(startFromScratch, qat, tabs, contextualTabs,
            **kwargs_)

class Group(customUI14base.CT_Group):
    def __init__(self, autoScale=None, centerVertically=None, id=None, idQ=None, tag=None,
        idMso=None, label=None, getLabel=None, image=None, imageMso=None, getImage=None,
        insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None,
        screentip=None, getScreentip=None, supertip=None, getSupertip=None, visible=None,
        getVisible=None, keytip=None, getKeytip=None, control=None, labelControl=None,
        button=None, toggleButton=None, checkBox=None, editBox=None, comboBox=None,
        dropDown=None, gallery=None, menu=None, dynamicMenu=None, splitButton=None,
        box=None, buttonGroup=None, separator=None, dialogBoxLauncher=None, **kwargs_):
        super(Group, self).__init__(autoScale, centerVertically, id, idQ, tag,
            idMso, label, getLabel, image, imageMso, getImage, insertAfterMso,
            insertBeforeMso, insertAfterQ, insertBeforeQ, screentip, getScreentip,
            supertip, getSupertip, visible, getVisible, keytip, getKeytip, control,
            labelControl, button, toggleButton, checkBox, editBox, comboBox, dropDown,
            gallery, menu, dynamicMenu, splitButton, box, buttonGroup, separator,
            dialogBoxLauncher, **kwargs_)

class Tab(customUI14base.CT_Tab):
    def __init__(self, id=None, idQ=None, tag=None, idMso=None, label=None,
        getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None,
        insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None,
        group=None, **kwargs_):
        super(Tab, self).__init__(id, idQ, tag, idMso, label, getLabel,
            insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible,
            getVisible, keytip, getKeytip, group, **kwargs_)

class ButtonRegular(customUI14base.CT_ButtonRegular):
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
        extensiontype_=None, **kwargs_):
        super(ButtonRegular, self).__init__(image, imageMso, getImage, screentip,
            getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel,
            insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible,
            getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage,
            getShowImage, id, idQ, tag, idMso, onAction, description, getDescription,
            extensiontype_, **kwargs_)
