#!/usr/bin/env python

#
# Generated Tue Dec 17 16:17:48 2019 by generateDS.py version 2.35.7.
# Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)]
#
# Command line options:
#   ('-f', '')
#   ('-o', 'customUI14base.py')
#   ('-s', 'customUI14subs.py')
#   ('--super', 'customUI14base')
#   ('--root-element', 'CT_CustomUI|customUI')
#
# Command line arguments:
#   customUI14.xsd
#
# Command line:
#   C:\virtual\terra\Scripts\generateDS.py -f -o "customUI14base.py" -s "customUI14subs.py" --super="customUI14base" --root-element="CT_CustomUI|customUI" customUI14.xsd
#
# Current working directory (os.getcwd()):
#   ribbon
#

import os
import sys
from lxml import etree as etree_

import customUI14base as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Globals
#

ExternalEncoding = ''
SaveElementTreeNode = True

#
# Data representation classes
#


class CT_CommandSub(supermod.CT_Command):
    def __init__(self, onAction=None, enabled=None, getEnabled=None, idMso=None, **kwargs_):
        super(CT_CommandSub, self).__init__(onAction, enabled, getEnabled, idMso,  **kwargs_)
supermod.CT_Command.subclass = CT_CommandSub
# end class CT_CommandSub


class CT_ControlBaseSub(supermod.CT_ControlBase):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, extensiontype_=None, **kwargs_):
        super(CT_ControlBaseSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, extensiontype_,  **kwargs_)
supermod.CT_ControlBase.subclass = CT_ControlBaseSub
# end class CT_ControlBaseSub


class CT_ControlSub(supermod.CT_Control):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, extensiontype_=None, **kwargs_):
        super(CT_ControlSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, extensiontype_,  **kwargs_)
supermod.CT_Control.subclass = CT_ControlSub
# end class CT_ControlSub


class CT_ControlCloneRegularSub(supermod.CT_ControlCloneRegular):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, **kwargs_):
        super(CT_ControlCloneRegularSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso,  **kwargs_)
supermod.CT_ControlCloneRegular.subclass = CT_ControlCloneRegularSub
# end class CT_ControlCloneRegularSub


class CT_ControlCloneQatSub(supermod.CT_ControlCloneQat):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, idMso=None, description=None, getDescription=None, size=None, getSize=None, **kwargs_):
        super(CT_ControlCloneQatSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, idMso, description, getDescription, size, getSize,  **kwargs_)
supermod.CT_ControlCloneQat.subclass = CT_ControlCloneQatSub
# end class CT_ControlCloneQatSub


class CT_LabelControlSub(supermod.CT_LabelControl):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, **kwargs_):
        super(CT_LabelControlSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso,  **kwargs_)
supermod.CT_LabelControl.subclass = CT_LabelControlSub
# end class CT_LabelControlSub


class CT_ButtonRegularSub(supermod.CT_ButtonRegular):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, onAction=None, description=None, getDescription=None, extensiontype_=None, **kwargs_):
        super(CT_ButtonRegularSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, onAction, description, getDescription, extensiontype_,  **kwargs_)
supermod.CT_ButtonRegular.subclass = CT_ButtonRegularSub
# end class CT_ButtonRegularSub


class CT_ButtonSub(supermod.CT_Button):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, onAction=None, description=None, getDescription=None, size=None, getSize=None, **kwargs_):
        super(CT_ButtonSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, onAction, description, getDescription, size, getSize,  **kwargs_)
supermod.CT_Button.subclass = CT_ButtonSub
# end class CT_ButtonSub


class CT_VisibleButtonSub(supermod.CT_VisibleButton):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, onAction=None, description=None, getDescription=None, **kwargs_):
        super(CT_VisibleButtonSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, onAction, description, getDescription,  **kwargs_)
supermod.CT_VisibleButton.subclass = CT_VisibleButtonSub
# end class CT_VisibleButtonSub


class CT_ToggleButtonRegularSub(supermod.CT_ToggleButtonRegular):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, onAction=None, description=None, getDescription=None, getPressed=None, extensiontype_=None, **kwargs_):
        super(CT_ToggleButtonRegularSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, onAction, description, getDescription, getPressed, extensiontype_,  **kwargs_)
supermod.CT_ToggleButtonRegular.subclass = CT_ToggleButtonRegularSub
# end class CT_ToggleButtonRegularSub


class CT_ToggleButtonSub(supermod.CT_ToggleButton):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, onAction=None, description=None, getDescription=None, getPressed=None, size=None, getSize=None, **kwargs_):
        super(CT_ToggleButtonSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, onAction, description, getDescription, getPressed, size, getSize,  **kwargs_)
supermod.CT_ToggleButton.subclass = CT_ToggleButtonSub
# end class CT_ToggleButtonSub


class CT_VisibleToggleButtonSub(supermod.CT_VisibleToggleButton):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, onAction=None, description=None, getDescription=None, getPressed=None, **kwargs_):
        super(CT_VisibleToggleButtonSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, onAction, description, getDescription, getPressed,  **kwargs_)
supermod.CT_VisibleToggleButton.subclass = CT_VisibleToggleButtonSub
# end class CT_VisibleToggleButtonSub


class CT_CheckBoxSub(supermod.CT_CheckBox):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, onAction=None, description=None, getDescription=None, getPressed=None, **kwargs_):
        super(CT_CheckBoxSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, onAction, description, getDescription, getPressed,  **kwargs_)
supermod.CT_CheckBox.subclass = CT_CheckBoxSub
# end class CT_CheckBoxSub


class CT_EditBoxSub(supermod.CT_EditBox):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, maxLength=None, getText=None, onChange=None, sizeString=None, extensiontype_=None, **kwargs_):
        super(CT_EditBoxSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, maxLength, getText, onChange, sizeString, extensiontype_,  **kwargs_)
supermod.CT_EditBox.subclass = CT_EditBoxSub
# end class CT_EditBoxSub


class CT_ItemSub(supermod.CT_Item):
    def __init__(self, id=None, label=None, image=None, imageMso=None, screentip=None, supertip=None, **kwargs_):
        super(CT_ItemSub, self).__init__(id, label, image, imageMso, screentip, supertip,  **kwargs_)
supermod.CT_Item.subclass = CT_ItemSub
# end class CT_ItemSub


class CT_ComboBoxSub(supermod.CT_ComboBox):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, maxLength=None, getText=None, onChange=None, sizeString=None, showItemImage=None, getItemCount=None, getItemLabel=None, getItemScreentip=None, getItemSupertip=None, getItemImage=None, getItemID=None, invalidateContentOnDrop=None, item=None, **kwargs_):
        super(CT_ComboBoxSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, maxLength, getText, onChange, sizeString, showItemImage, getItemCount, getItemLabel, getItemScreentip, getItemSupertip, getItemImage, getItemID, invalidateContentOnDrop, item,  **kwargs_)
supermod.CT_ComboBox.subclass = CT_ComboBoxSub
# end class CT_ComboBoxSub


class CT_DropDownRegularSub(supermod.CT_DropDownRegular):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, getSelectedItemID=None, getSelectedItemIndex=None, showItemLabel=None, onAction=None, showItemImage=None, getItemCount=None, getItemLabel=None, getItemScreentip=None, getItemSupertip=None, getItemImage=None, getItemID=None, sizeString=None, item=None, button=None, extensiontype_=None, **kwargs_):
        super(CT_DropDownRegularSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, getSelectedItemID, getSelectedItemIndex, showItemLabel, onAction, showItemImage, getItemCount, getItemLabel, getItemScreentip, getItemSupertip, getItemImage, getItemID, sizeString, item, button, extensiontype_,  **kwargs_)
supermod.CT_DropDownRegular.subclass = CT_DropDownRegularSub
# end class CT_DropDownRegularSub


class CT_GalleryRegularSub(supermod.CT_GalleryRegular):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, getSelectedItemID=None, getSelectedItemIndex=None, showItemLabel=None, onAction=None, showItemImage=None, getItemCount=None, getItemLabel=None, getItemScreentip=None, getItemSupertip=None, getItemImage=None, getItemID=None, sizeString=None, item=None, button=None, columns=None, rows=None, itemWidth=None, itemHeight=None, getItemWidth=None, getItemHeight=None, showInRibbon=None, description=None, getDescription=None, invalidateContentOnDrop=None, extensiontype_=None, **kwargs_):
        super(CT_GalleryRegularSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, getSelectedItemID, getSelectedItemIndex, showItemLabel, onAction, showItemImage, getItemCount, getItemLabel, getItemScreentip, getItemSupertip, getItemImage, getItemID, sizeString, item, button, columns, rows, itemWidth, itemHeight, getItemWidth, getItemHeight, showInRibbon, description, getDescription, invalidateContentOnDrop, extensiontype_,  **kwargs_)
supermod.CT_GalleryRegular.subclass = CT_GalleryRegularSub
# end class CT_GalleryRegularSub


class CT_GallerySub(supermod.CT_Gallery):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, getSelectedItemID=None, getSelectedItemIndex=None, showItemLabel=None, onAction=None, showItemImage=None, getItemCount=None, getItemLabel=None, getItemScreentip=None, getItemSupertip=None, getItemImage=None, getItemID=None, sizeString=None, item=None, button=None, columns=None, rows=None, itemWidth=None, itemHeight=None, getItemWidth=None, getItemHeight=None, showInRibbon=None, description=None, getDescription=None, invalidateContentOnDrop=None, size=None, getSize=None, **kwargs_):
        super(CT_GallerySub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, getSelectedItemID, getSelectedItemIndex, showItemLabel, onAction, showItemImage, getItemCount, getItemLabel, getItemScreentip, getItemSupertip, getItemImage, getItemID, sizeString, item, button, columns, rows, itemWidth, itemHeight, getItemWidth, getItemHeight, showInRibbon, description, getDescription, invalidateContentOnDrop, size, getSize,  **kwargs_)
supermod.CT_Gallery.subclass = CT_GallerySub
# end class CT_GallerySub


class CT_MenuRegularSub(supermod.CT_MenuRegular):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, itemSize=None, description=None, getDescription=None, id=None, idQ=None, tag=None, idMso=None, control=None, button=None, checkBox=None, gallery=None, toggleButton=None, menuSeparator=None, splitButton=None, menu=None, dynamicMenu=None, extensiontype_=None, **kwargs_):
        super(CT_MenuRegularSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, itemSize, description, getDescription, id, idQ, tag, idMso, control, button, checkBox, gallery, toggleButton, menuSeparator, splitButton, menu, dynamicMenu, extensiontype_,  **kwargs_)
supermod.CT_MenuRegular.subclass = CT_MenuRegularSub
# end class CT_MenuRegularSub


class CT_DynamicMenuRegularSub(supermod.CT_DynamicMenuRegular):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, description=None, getDescription=None, id=None, idQ=None, tag=None, idMso=None, getContent=None, invalidateContentOnDrop=None, extensiontype_=None, **kwargs_):
        super(CT_DynamicMenuRegularSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, description, getDescription, id, idQ, tag, idMso, getContent, invalidateContentOnDrop, extensiontype_,  **kwargs_)
supermod.CT_DynamicMenuRegular.subclass = CT_DynamicMenuRegularSub
# end class CT_DynamicMenuRegularSub


class CT_MenuWithTitleSub(supermod.CT_MenuWithTitle):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, itemSize=None, id=None, idQ=None, tag=None, idMso=None, title=None, getTitle=None, control=None, button=None, checkBox=None, gallery=None, toggleButton=None, menuSeparator=None, splitButton=None, menu=None, dynamicMenu=None, **kwargs_):
        super(CT_MenuWithTitleSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, itemSize, id, idQ, tag, idMso, title, getTitle, control, button, checkBox, gallery, toggleButton, menuSeparator, splitButton, menu, dynamicMenu,  **kwargs_)
supermod.CT_MenuWithTitle.subclass = CT_MenuWithTitleSub
# end class CT_MenuWithTitleSub


class CT_MenuSub(supermod.CT_Menu):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, itemSize=None, description=None, getDescription=None, id=None, idQ=None, tag=None, idMso=None, control=None, button=None, checkBox=None, gallery=None, toggleButton=None, menuSeparator=None, splitButton=None, menu=None, dynamicMenu=None, size=None, getSize=None, **kwargs_):
        super(CT_MenuSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, itemSize, description, getDescription, id, idQ, tag, idMso, control, button, checkBox, gallery, toggleButton, menuSeparator, splitButton, menu, dynamicMenu, size, getSize,  **kwargs_)
supermod.CT_Menu.subclass = CT_MenuSub
# end class CT_MenuSub


class CT_DynamicMenuSub(supermod.CT_DynamicMenu):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, description=None, getDescription=None, id=None, idQ=None, tag=None, idMso=None, getContent=None, invalidateContentOnDrop=None, size=None, getSize=None, **kwargs_):
        super(CT_DynamicMenuSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, description, getDescription, id, idQ, tag, idMso, getContent, invalidateContentOnDrop, size, getSize,  **kwargs_)
supermod.CT_DynamicMenu.subclass = CT_DynamicMenuSub
# end class CT_DynamicMenuSub


class CT_SplitButtonBaseSub(supermod.CT_SplitButtonBase):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, **kwargs_):
        super(CT_SplitButtonBaseSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso,  **kwargs_)
supermod.CT_SplitButtonBase.subclass = CT_SplitButtonBaseSub
# end class CT_SplitButtonBaseSub


class CT_SplitButtonRestrictedSub(supermod.CT_SplitButtonRestricted):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, extensiontype_=None, **kwargs_):
        super(CT_SplitButtonRestrictedSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, extensiontype_,  **kwargs_)
supermod.CT_SplitButtonRestricted.subclass = CT_SplitButtonRestrictedSub
# end class CT_SplitButtonRestrictedSub


class CT_SplitButtonRegularSub(supermod.CT_SplitButtonRegular):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, button=None, toggleButton=None, menu=None, extensiontype_=None, **kwargs_):
        super(CT_SplitButtonRegularSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, button, toggleButton, menu, extensiontype_,  **kwargs_)
supermod.CT_SplitButtonRegular.subclass = CT_SplitButtonRegularSub
# end class CT_SplitButtonRegularSub


class CT_SplitButtonWithTitleSub(supermod.CT_SplitButtonWithTitle):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, button=None, toggleButton=None, menu=None, **kwargs_):
        super(CT_SplitButtonWithTitleSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, button, toggleButton, menu,  **kwargs_)
supermod.CT_SplitButtonWithTitle.subclass = CT_SplitButtonWithTitleSub
# end class CT_SplitButtonWithTitleSub


class CT_SplitButtonSub(supermod.CT_SplitButton):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, button=None, toggleButton=None, menu=None, size=None, getSize=None, **kwargs_):
        super(CT_SplitButtonSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, button, toggleButton, menu, size, getSize,  **kwargs_)
supermod.CT_SplitButton.subclass = CT_SplitButtonSub
# end class CT_SplitButtonSub


class CT_DialogLauncherSub(supermod.CT_DialogLauncher):
    def __init__(self, button=None, **kwargs_):
        super(CT_DialogLauncherSub, self).__init__(button,  **kwargs_)
supermod.CT_DialogLauncher.subclass = CT_DialogLauncherSub
# end class CT_DialogLauncherSub


class CT_BoxSub(supermod.CT_Box):
    def __init__(self, boxStyle=None, id=None, idQ=None, tag=None, visible=None, getVisible=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, control=None, labelControl=None, button=None, toggleButton=None, checkBox=None, editBox=None, comboBox=None, dropDown=None, gallery=None, menu=None, dynamicMenu=None, splitButton=None, box=None, buttonGroup=None, **kwargs_):
        super(CT_BoxSub, self).__init__(boxStyle, id, idQ, tag, visible, getVisible, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, control, labelControl, button, toggleButton, checkBox, editBox, comboBox, dropDown, gallery, menu, dynamicMenu, splitButton, box, buttonGroup,  **kwargs_)
supermod.CT_Box.subclass = CT_BoxSub
# end class CT_BoxSub


class CT_SeparatorSub(supermod.CT_Separator):
    def __init__(self, id=None, idQ=None, tag=None, visible=None, getVisible=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, **kwargs_):
        super(CT_SeparatorSub, self).__init__(id, idQ, tag, visible, getVisible, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ,  **kwargs_)
supermod.CT_Separator.subclass = CT_SeparatorSub
# end class CT_SeparatorSub


class CT_MenuSeparatorSub(supermod.CT_MenuSeparator):
    def __init__(self, id=None, idQ=None, tag=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, title=None, getTitle=None, **kwargs_):
        super(CT_MenuSeparatorSub, self).__init__(id, idQ, tag, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, title, getTitle,  **kwargs_)
supermod.CT_MenuSeparator.subclass = CT_MenuSeparatorSub
# end class CT_MenuSeparatorSub


class CT_MenuSeparatorNoTitleSub(supermod.CT_MenuSeparatorNoTitle):
    def __init__(self, id=None, idQ=None, tag=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, **kwargs_):
        super(CT_MenuSeparatorNoTitleSub, self).__init__(id, idQ, tag, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ,  **kwargs_)
supermod.CT_MenuSeparatorNoTitle.subclass = CT_MenuSeparatorNoTitleSub
# end class CT_MenuSeparatorNoTitleSub


class CT_ButtonGroupSub(supermod.CT_ButtonGroup):
    def __init__(self, id=None, idQ=None, tag=None, visible=None, getVisible=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, control=None, button=None, toggleButton=None, gallery=None, menu=None, dynamicMenu=None, splitButton=None, separator=None, **kwargs_):
        super(CT_ButtonGroupSub, self).__init__(id, idQ, tag, visible, getVisible, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, control, button, toggleButton, gallery, menu, dynamicMenu, splitButton, separator,  **kwargs_)
supermod.CT_ButtonGroup.subclass = CT_ButtonGroupSub
# end class CT_ButtonGroupSub


class CT_GroupSub(supermod.CT_Group):
    def __init__(self, autoScale=None, centerVertically=None, id=None, idQ=None, tag=None, idMso=None, label=None, getLabel=None, image=None, imageMso=None, getImage=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, visible=None, getVisible=None, keytip=None, getKeytip=None, control=None, labelControl=None, button=None, toggleButton=None, checkBox=None, editBox=None, comboBox=None, dropDown=None, gallery=None, menu=None, dynamicMenu=None, splitButton=None, box=None, buttonGroup=None, separator=None, dialogBoxLauncher=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(CT_GroupSub, self).__init__(autoScale, centerVertically, id, idQ, tag, idMso, label, getLabel, image, imageMso, getImage, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, screentip, getScreentip, supertip, getSupertip, visible, getVisible, keytip, getKeytip, control, labelControl, button, toggleButton, checkBox, editBox, comboBox, dropDown, gallery, menu, dynamicMenu, splitButton, box, buttonGroup, separator, dialogBoxLauncher, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.CT_Group.subclass = CT_GroupSub
# end class CT_GroupSub


class CT_TabSub(supermod.CT_Tab):
    def __init__(self, id=None, idQ=None, tag=None, idMso=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, group=None, **kwargs_):
        super(CT_TabSub, self).__init__(id, idQ, tag, idMso, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, group,  **kwargs_)
supermod.CT_Tab.subclass = CT_TabSub
# end class CT_TabSub


class CT_QatItemsSub(supermod.CT_QatItems):
    def __init__(self, control=None, button=None, separator=None, **kwargs_):
        super(CT_QatItemsSub, self).__init__(control, button, separator,  **kwargs_)
supermod.CT_QatItems.subclass = CT_QatItemsSub
# end class CT_QatItemsSub


class CT_QatSub(supermod.CT_Qat):
    def __init__(self, sharedControls=None, documentControls=None, **kwargs_):
        super(CT_QatSub, self).__init__(sharedControls, documentControls,  **kwargs_)
supermod.CT_Qat.subclass = CT_QatSub
# end class CT_QatSub


class CT_TabsSub(supermod.CT_Tabs):
    def __init__(self, tab=None, **kwargs_):
        super(CT_TabsSub, self).__init__(tab,  **kwargs_)
supermod.CT_Tabs.subclass = CT_TabsSub
# end class CT_TabsSub


class CT_TabSetSub(supermod.CT_TabSet):
    def __init__(self, idMso=None, visible=None, getVisible=None, tab=None, **kwargs_):
        super(CT_TabSetSub, self).__init__(idMso, visible, getVisible, tab,  **kwargs_)
supermod.CT_TabSet.subclass = CT_TabSetSub
# end class CT_TabSetSub


class CT_ContextualTabsSub(supermod.CT_ContextualTabs):
    def __init__(self, tabSet=None, **kwargs_):
        super(CT_ContextualTabsSub, self).__init__(tabSet,  **kwargs_)
supermod.CT_ContextualTabs.subclass = CT_ContextualTabsSub
# end class CT_ContextualTabsSub


class CT_ContextMenuSub(supermod.CT_ContextMenu):
    def __init__(self, idMso=None, control=None, button=None, checkBox=None, gallery=None, toggleButton=None, splitButton=None, menu=None, dynamicMenu=None, menuSeparator=None, **kwargs_):
        super(CT_ContextMenuSub, self).__init__(idMso, control, button, checkBox, gallery, toggleButton, splitButton, menu, dynamicMenu, menuSeparator,  **kwargs_)
supermod.CT_ContextMenu.subclass = CT_ContextMenuSub
# end class CT_ContextMenuSub


class CT_CommandsSub(supermod.CT_Commands):
    def __init__(self, command=None, **kwargs_):
        super(CT_CommandsSub, self).__init__(command,  **kwargs_)
supermod.CT_Commands.subclass = CT_CommandsSub
# end class CT_CommandsSub


class CT_RibbonSub(supermod.CT_Ribbon):
    def __init__(self, startFromScratch=None, qat=None, tabs=None, contextualTabs=None, **kwargs_):
        super(CT_RibbonSub, self).__init__(startFromScratch, qat, tabs, contextualTabs,  **kwargs_)
supermod.CT_Ribbon.subclass = CT_RibbonSub
# end class CT_RibbonSub


class CT_ContextMenusSub(supermod.CT_ContextMenus):
    def __init__(self, contextMenu=None, **kwargs_):
        super(CT_ContextMenusSub, self).__init__(contextMenu,  **kwargs_)
supermod.CT_ContextMenus.subclass = CT_ContextMenusSub
# end class CT_ContextMenusSub


class CT_MenuRootSub(supermod.CT_MenuRoot):
    def __init__(self, itemSize=None, title=None, getTitle=None, control=None, button=None, checkBox=None, gallery=None, toggleButton=None, menuSeparator=None, splitButton=None, menu=None, dynamicMenu=None, **kwargs_):
        super(CT_MenuRootSub, self).__init__(itemSize, title, getTitle, control, button, checkBox, gallery, toggleButton, menuSeparator, splitButton, menu, dynamicMenu,  **kwargs_)
supermod.CT_MenuRoot.subclass = CT_MenuRootSub
# end class CT_MenuRootSub


class CT_BackstageButtonBaseSub(supermod.CT_BackstageButtonBase):
    def __init__(self, id=None, idQ=None, tag=None, onAction=None, isDefinitive=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, keytip=None, getKeytip=None, image=None, imageMso=None, getImage=None, extensiontype_=None, **kwargs_):
        super(CT_BackstageButtonBaseSub, self).__init__(id, idQ, tag, onAction, isDefinitive, enabled, getEnabled, label, getLabel, visible, getVisible, keytip, getKeytip, image, imageMso, getImage, extensiontype_,  **kwargs_)
supermod.CT_BackstageButtonBase.subclass = CT_BackstageButtonBaseSub
# end class CT_BackstageButtonBaseSub


class CT_BackstageRegularButtonSub(supermod.CT_BackstageRegularButton):
    def __init__(self, id=None, idQ=None, tag=None, onAction=None, isDefinitive=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, keytip=None, getKeytip=None, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, extensiontype_=None, **kwargs_):
        super(CT_BackstageRegularButtonSub, self).__init__(id, idQ, tag, onAction, isDefinitive, enabled, getEnabled, label, getLabel, visible, getVisible, keytip, getKeytip, image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, extensiontype_,  **kwargs_)
supermod.CT_BackstageRegularButton.subclass = CT_BackstageRegularButtonSub
# end class CT_BackstageRegularButtonSub


class CT_BackstageGroupButtonSub(supermod.CT_BackstageGroupButton):
    def __init__(self, id=None, idQ=None, tag=None, onAction=None, isDefinitive=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, keytip=None, getKeytip=None, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, expand=None, style=None, **kwargs_):
        super(CT_BackstageGroupButtonSub, self).__init__(id, idQ, tag, onAction, isDefinitive, enabled, getEnabled, label, getLabel, visible, getVisible, keytip, getKeytip, image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, expand, style,  **kwargs_)
supermod.CT_BackstageGroupButton.subclass = CT_BackstageGroupButtonSub
# end class CT_BackstageGroupButtonSub


class CT_BackstageMenuButtonSub(supermod.CT_BackstageMenuButton):
    def __init__(self, id=None, idQ=None, tag=None, onAction=None, isDefinitive=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, keytip=None, getKeytip=None, image=None, imageMso=None, getImage=None, description=None, getDescription=None, **kwargs_):
        super(CT_BackstageMenuButtonSub, self).__init__(id, idQ, tag, onAction, isDefinitive, enabled, getEnabled, label, getLabel, visible, getVisible, keytip, getKeytip, image, imageMso, getImage, description, getDescription,  **kwargs_)
supermod.CT_BackstageMenuButton.subclass = CT_BackstageMenuButtonSub
# end class CT_BackstageMenuButtonSub


class CT_BackstageFastCommandButtonSub(supermod.CT_BackstageFastCommandButton):
    def __init__(self, id=None, idQ=None, tag=None, onAction=None, isDefinitive=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, keytip=None, getKeytip=None, image=None, imageMso=None, getImage=None, idMso=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, **kwargs_):
        super(CT_BackstageFastCommandButtonSub, self).__init__(id, idQ, tag, onAction, isDefinitive, enabled, getEnabled, label, getLabel, visible, getVisible, keytip, getKeytip, image, imageMso, getImage, idMso, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ,  **kwargs_)
supermod.CT_BackstageFastCommandButton.subclass = CT_BackstageFastCommandButtonSub
# end class CT_BackstageFastCommandButtonSub


class CT_BackstageCheckBoxBaseSub(supermod.CT_BackstageCheckBoxBase):
    def __init__(self, id=None, idQ=None, tag=None, onAction=None, getPressed=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, keytip=None, getKeytip=None, extensiontype_=None, **kwargs_):
        super(CT_BackstageCheckBoxBaseSub, self).__init__(id, idQ, tag, onAction, getPressed, enabled, getEnabled, label, getLabel, visible, getVisible, keytip, getKeytip, extensiontype_,  **kwargs_)
supermod.CT_BackstageCheckBoxBase.subclass = CT_BackstageCheckBoxBaseSub
# end class CT_BackstageCheckBoxBaseSub


class CT_BackstageCheckBoxSub(supermod.CT_BackstageCheckBox):
    def __init__(self, id=None, idQ=None, tag=None, onAction=None, getPressed=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, keytip=None, getKeytip=None, expand=None, description=None, getDescription=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, **kwargs_):
        super(CT_BackstageCheckBoxSub, self).__init__(id, idQ, tag, onAction, getPressed, enabled, getEnabled, label, getLabel, visible, getVisible, keytip, getKeytip, expand, description, getDescription, screentip, getScreentip, supertip, getSupertip,  **kwargs_)
supermod.CT_BackstageCheckBox.subclass = CT_BackstageCheckBoxSub
# end class CT_BackstageCheckBoxSub


class CT_BackstageMenuCheckBoxSub(supermod.CT_BackstageMenuCheckBox):
    def __init__(self, id=None, idQ=None, tag=None, onAction=None, getPressed=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, keytip=None, getKeytip=None, description=None, getDescription=None, extensiontype_=None, **kwargs_):
        super(CT_BackstageMenuCheckBoxSub, self).__init__(id, idQ, tag, onAction, getPressed, enabled, getEnabled, label, getLabel, visible, getVisible, keytip, getKeytip, description, getDescription, extensiontype_,  **kwargs_)
supermod.CT_BackstageMenuCheckBox.subclass = CT_BackstageMenuCheckBoxSub
# end class CT_BackstageMenuCheckBoxSub


class CT_BackstageMenuToggleButtonSub(supermod.CT_BackstageMenuToggleButton):
    def __init__(self, id=None, idQ=None, tag=None, onAction=None, getPressed=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, keytip=None, getKeytip=None, description=None, getDescription=None, image=None, imageMso=None, getImage=None, **kwargs_):
        super(CT_BackstageMenuToggleButtonSub, self).__init__(id, idQ, tag, onAction, getPressed, enabled, getEnabled, label, getLabel, visible, getVisible, keytip, getKeytip, description, getDescription, image, imageMso, getImage,  **kwargs_)
supermod.CT_BackstageMenuToggleButton.subclass = CT_BackstageMenuToggleButtonSub
# end class CT_BackstageMenuToggleButtonSub


class CT_BackstageEditBoxSub(supermod.CT_BackstageEditBox):
    def __init__(self, getText=None, onChange=None, maxLength=None, sizeString=None, id=None, idQ=None, tag=None, alignLabel=None, expand=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, keytip=None, getKeytip=None, **kwargs_):
        super(CT_BackstageEditBoxSub, self).__init__(getText, onChange, maxLength, sizeString, id, idQ, tag, alignLabel, expand, enabled, getEnabled, label, getLabel, visible, getVisible, keytip, getKeytip,  **kwargs_)
supermod.CT_BackstageEditBox.subclass = CT_BackstageEditBoxSub
# end class CT_BackstageEditBoxSub


class CT_BackstageDropDownSub(supermod.CT_BackstageDropDown):
    def __init__(self, getSelectedItemIndex=None, sizeString=None, getItemCount=None, getItemLabel=None, getItemID=None, id=None, idQ=None, tag=None, alignLabel=None, expand=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, onAction=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, keytip=None, getKeytip=None, item=None, **kwargs_):
        super(CT_BackstageDropDownSub, self).__init__(getSelectedItemIndex, sizeString, getItemCount, getItemLabel, getItemID, id, idQ, tag, alignLabel, expand, enabled, getEnabled, label, getLabel, visible, getVisible, onAction, screentip, getScreentip, supertip, getSupertip, keytip, getKeytip, item,  **kwargs_)
supermod.CT_BackstageDropDown.subclass = CT_BackstageDropDownSub
# end class CT_BackstageDropDownSub


class CT_RadioGroupSub(supermod.CT_RadioGroup):
    def __init__(self, getSelectedItemIndex=None, getItemCount=None, getItemLabel=None, getItemID=None, id=None, idQ=None, tag=None, alignLabel=None, expand=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, onAction=None, keytip=None, getKeytip=None, radioButton=None, **kwargs_):
        super(CT_RadioGroupSub, self).__init__(getSelectedItemIndex, getItemCount, getItemLabel, getItemID, id, idQ, tag, alignLabel, expand, enabled, getEnabled, label, getLabel, visible, getVisible, onAction, keytip, getKeytip, radioButton,  **kwargs_)
supermod.CT_RadioGroup.subclass = CT_RadioGroupSub
# end class CT_RadioGroupSub


class CT_BackstageComboBoxSub(supermod.CT_BackstageComboBox):
    def __init__(self, getText=None, onChange=None, sizeString=None, getItemCount=None, getItemLabel=None, getItemID=None, id=None, idQ=None, tag=None, alignLabel=None, expand=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, keytip=None, getKeytip=None, item=None, **kwargs_):
        super(CT_BackstageComboBoxSub, self).__init__(getText, onChange, sizeString, getItemCount, getItemLabel, getItemID, id, idQ, tag, alignLabel, expand, enabled, getEnabled, label, getLabel, visible, getVisible, keytip, getKeytip, item,  **kwargs_)
supermod.CT_BackstageComboBox.subclass = CT_BackstageComboBoxSub
# end class CT_BackstageComboBoxSub


class CT_BackstageItemSub(supermod.CT_BackstageItem):
    def __init__(self, id=None, label=None, getLabel=None, **kwargs_):
        super(CT_BackstageItemSub, self).__init__(id, label, getLabel,  **kwargs_)
supermod.CT_BackstageItem.subclass = CT_BackstageItemSub
# end class CT_BackstageItemSub


class CT_HyperlinkSub(supermod.CT_Hyperlink):
    def __init__(self, target=None, getTarget=None, id=None, idQ=None, tag=None, alignLabel=None, expand=None, enabled=None, getEnabled=None, visible=None, getVisible=None, keytip=None, getKeytip=None, label=None, getLabel=None, onAction=None, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, **kwargs_):
        super(CT_HyperlinkSub, self).__init__(target, getTarget, id, idQ, tag, alignLabel, expand, enabled, getEnabled, visible, getVisible, keytip, getKeytip, label, getLabel, onAction, image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip,  **kwargs_)
supermod.CT_Hyperlink.subclass = CT_HyperlinkSub
# end class CT_HyperlinkSub


class CT_BackstageLabelControlSub(supermod.CT_BackstageLabelControl):
    def __init__(self, noWrap=None, id=None, idQ=None, tag=None, alignLabel=None, expand=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, **kwargs_):
        super(CT_BackstageLabelControlSub, self).__init__(noWrap, id, idQ, tag, alignLabel, expand, enabled, getEnabled, label, getLabel, visible, getVisible,  **kwargs_)
supermod.CT_BackstageLabelControl.subclass = CT_BackstageLabelControlSub
# end class CT_BackstageLabelControlSub


class CT_PrimaryItemSub(supermod.CT_PrimaryItem):
    def __init__(self, button=None, menu=None, **kwargs_):
        super(CT_PrimaryItemSub, self).__init__(button, menu,  **kwargs_)
supermod.CT_PrimaryItem.subclass = CT_PrimaryItemSub
# end class CT_PrimaryItemSub


class CT_BackstageMenuGroupSub(supermod.CT_BackstageMenuGroup):
    def __init__(self, itemSize=None, id=None, idQ=None, tag=None, label=None, getLabel=None, button=None, checkBox=None, menu=None, toggleButton=None, **kwargs_):
        super(CT_BackstageMenuGroupSub, self).__init__(itemSize, id, idQ, tag, label, getLabel, button, checkBox, menu, toggleButton,  **kwargs_)
supermod.CT_BackstageMenuGroup.subclass = CT_BackstageMenuGroupSub
# end class CT_BackstageMenuGroupSub


class CT_BackstageMenuBaseSub(supermod.CT_BackstageMenuBase):
    def __init__(self, id=None, idQ=None, tag=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, image=None, imageMso=None, getImage=None, keytip=None, getKeytip=None, menuGroup=None, extensiontype_=None, **kwargs_):
        super(CT_BackstageMenuBaseSub, self).__init__(id, idQ, tag, enabled, getEnabled, label, getLabel, visible, getVisible, image, imageMso, getImage, keytip, getKeytip, menuGroup, extensiontype_,  **kwargs_)
supermod.CT_BackstageMenuBase.subclass = CT_BackstageMenuBaseSub
# end class CT_BackstageMenuBaseSub


class CT_BackstagePrimaryMenuSub(supermod.CT_BackstagePrimaryMenu):
    def __init__(self, id=None, idQ=None, tag=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, image=None, imageMso=None, getImage=None, keytip=None, getKeytip=None, menuGroup=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, **kwargs_):
        super(CT_BackstagePrimaryMenuSub, self).__init__(id, idQ, tag, enabled, getEnabled, label, getLabel, visible, getVisible, image, imageMso, getImage, keytip, getKeytip, menuGroup, screentip, getScreentip, supertip, getSupertip,  **kwargs_)
supermod.CT_BackstagePrimaryMenu.subclass = CT_BackstagePrimaryMenuSub
# end class CT_BackstagePrimaryMenuSub


class CT_BackstageSubMenuSub(supermod.CT_BackstageSubMenu):
    def __init__(self, id=None, idQ=None, tag=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, image=None, imageMso=None, getImage=None, keytip=None, getKeytip=None, menuGroup=None, description=None, getDescription=None, **kwargs_):
        super(CT_BackstageSubMenuSub, self).__init__(id, idQ, tag, enabled, getEnabled, label, getLabel, visible, getVisible, image, imageMso, getImage, keytip, getKeytip, menuGroup, description, getDescription,  **kwargs_)
supermod.CT_BackstageSubMenu.subclass = CT_BackstageSubMenuSub
# end class CT_BackstageSubMenuSub


class CT_ImageControlSub(supermod.CT_ImageControl):
    def __init__(self, id=None, idQ=None, tag=None, enabled=None, getEnabled=None, visible=None, getVisible=None, image=None, imageMso=None, getImage=None, altText=None, getAltText=None, **kwargs_):
        super(CT_ImageControlSub, self).__init__(id, idQ, tag, enabled, getEnabled, visible, getVisible, image, imageMso, getImage, altText, getAltText,  **kwargs_)
supermod.CT_ImageControl.subclass = CT_ImageControlSub
# end class CT_ImageControlSub


class CT_GroupControlsSub(supermod.CT_GroupControls):
    def __init__(self, button=None, checkBox=None, editBox=None, dropDown=None, radioGroup=None, comboBox=None, hyperlink=None, labelControl=None, groupBox=None, layoutContainer=None, imageControl=None, **kwargs_):
        super(CT_GroupControlsSub, self).__init__(button, checkBox, editBox, dropDown, radioGroup, comboBox, hyperlink, labelControl, groupBox, layoutContainer, imageControl,  **kwargs_)
supermod.CT_GroupControls.subclass = CT_GroupControlsSub
# end class CT_GroupControlsSub


class CT_BackstageGroupSub(supermod.CT_BackstageGroup):
    def __init__(self, id=None, idQ=None, tag=None, idMso=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, label=None, getLabel=None, visible=None, getVisible=None, style=None, getStyle=None, helperText=None, getHelperText=None, showLabel=None, getShowLabel=None, primaryItem=None, topItems=None, bottomItems=None, **kwargs_):
        super(CT_BackstageGroupSub, self).__init__(id, idQ, tag, idMso, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, label, getLabel, visible, getVisible, style, getStyle, helperText, getHelperText, showLabel, getShowLabel, primaryItem, topItems, bottomItems,  **kwargs_)
supermod.CT_BackstageGroup.subclass = CT_BackstageGroupSub
# end class CT_BackstageGroupSub


class CT_HeaderGroupSub(supermod.CT_HeaderGroup):
    def __init__(self, id=None, idQ=None, tag=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, button=None, **kwargs_):
        super(CT_HeaderGroupSub, self).__init__(id, idQ, tag, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, button,  **kwargs_)
supermod.CT_HeaderGroup.subclass = CT_HeaderGroupSub
# end class CT_HeaderGroupSub


class CT_TaskGroupSub(supermod.CT_TaskGroup):
    def __init__(self, allowedTaskSizes=None, id=None, idQ=None, tag=None, idMso=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, label=None, getLabel=None, visible=None, getVisible=None, helperText=None, getHelperText=None, showLabel=None, getShowLabel=None, category=None, **kwargs_):
        super(CT_TaskGroupSub, self).__init__(allowedTaskSizes, id, idQ, tag, idMso, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, label, getLabel, visible, getVisible, helperText, getHelperText, showLabel, getShowLabel, category,  **kwargs_)
supermod.CT_TaskGroup.subclass = CT_TaskGroupSub
# end class CT_TaskGroupSub


class CT_TaskGroupCategorySub(supermod.CT_TaskGroupCategory):
    def __init__(self, id=None, idQ=None, tag=None, idMso=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, label=None, getLabel=None, task=None, **kwargs_):
        super(CT_TaskGroupCategorySub, self).__init__(id, idQ, tag, idMso, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, label, getLabel, task,  **kwargs_)
supermod.CT_TaskGroupCategory.subclass = CT_TaskGroupCategorySub
# end class CT_TaskGroupCategorySub


class CT_TaskGroupTaskSub(supermod.CT_TaskGroupTask):
    def __init__(self, id=None, idQ=None, tag=None, idMso=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, onAction=None, isDefinitive=None, image=None, imageMso=None, getImage=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, description=None, getDescription=None, keytip=None, getKeytip=None, **kwargs_):
        super(CT_TaskGroupTaskSub, self).__init__(id, idQ, tag, idMso, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, onAction, isDefinitive, image, imageMso, getImage, enabled, getEnabled, label, getLabel, visible, getVisible, description, getDescription, keytip, getKeytip,  **kwargs_)
supermod.CT_TaskGroupTask.subclass = CT_TaskGroupTaskSub
# end class CT_TaskGroupTaskSub


class CT_TaskFormGroupSub(supermod.CT_TaskFormGroup):
    def __init__(self, allowedTaskSizes=None, id=None, idQ=None, tag=None, idMso=None, label=None, getLabel=None, visible=None, getVisible=None, helperText=None, getHelperText=None, showLabel=None, getShowLabel=None, category=None, **kwargs_):
        super(CT_TaskFormGroupSub, self).__init__(allowedTaskSizes, id, idQ, tag, idMso, label, getLabel, visible, getVisible, helperText, getHelperText, showLabel, getShowLabel, category,  **kwargs_)
supermod.CT_TaskFormGroup.subclass = CT_TaskFormGroupSub
# end class CT_TaskFormGroupSub


class CT_TaskFormGroupCategorySub(supermod.CT_TaskFormGroupCategory):
    def __init__(self, id=None, idQ=None, tag=None, idMso=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, label=None, getLabel=None, task=None, **kwargs_):
        super(CT_TaskFormGroupCategorySub, self).__init__(id, idQ, tag, idMso, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, label, getLabel, task,  **kwargs_)
supermod.CT_TaskFormGroupCategory.subclass = CT_TaskFormGroupCategorySub
# end class CT_TaskFormGroupCategorySub


class CT_TaskFormGroupTaskSub(supermod.CT_TaskFormGroupTask):
    def __init__(self, id=None, idQ=None, tag=None, idMso=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, image=None, imageMso=None, getImage=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, description=None, getDescription=None, keytip=None, getKeytip=None, group=None, **kwargs_):
        super(CT_TaskFormGroupTaskSub, self).__init__(id, idQ, tag, idMso, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, image, imageMso, getImage, enabled, getEnabled, label, getLabel, visible, getVisible, description, getDescription, keytip, getKeytip, group,  **kwargs_)
supermod.CT_TaskFormGroupTask.subclass = CT_TaskFormGroupTaskSub
# end class CT_TaskFormGroupTaskSub


class CT_GroupBoxSub(supermod.CT_GroupBox):
    def __init__(self, id=None, idQ=None, tag=None, expand=None, label=None, getLabel=None, button=None, checkBox=None, editBox=None, dropDown=None, radioGroup=None, comboBox=None, hyperlink=None, labelControl=None, groupBox=None, layoutContainer=None, imageControl=None, **kwargs_):
        super(CT_GroupBoxSub, self).__init__(id, idQ, tag, expand, label, getLabel, button, checkBox, editBox, dropDown, radioGroup, comboBox, hyperlink, labelControl, groupBox, layoutContainer, imageControl,  **kwargs_)
supermod.CT_GroupBox.subclass = CT_GroupBoxSub
# end class CT_GroupBoxSub


class CT_LayoutContainerSub(supermod.CT_LayoutContainer):
    def __init__(self, align=None, expand=None, layoutChildren=None, id=None, idQ=None, tag=None, button=None, checkBox=None, editBox=None, dropDown=None, radioGroup=None, comboBox=None, hyperlink=None, labelControl=None, groupBox=None, layoutContainer=None, imageControl=None, **kwargs_):
        super(CT_LayoutContainerSub, self).__init__(align, expand, layoutChildren, id, idQ, tag, button, checkBox, editBox, dropDown, radioGroup, comboBox, hyperlink, labelControl, groupBox, layoutContainer, imageControl,  **kwargs_)
supermod.CT_LayoutContainer.subclass = CT_LayoutContainerSub
# end class CT_LayoutContainerSub


class CT_BackstageGroupsSub(supermod.CT_BackstageGroups):
    def __init__(self, taskFormGroup=None, group=None, taskGroup=None, **kwargs_):
        super(CT_BackstageGroupsSub, self).__init__(taskFormGroup, group, taskGroup,  **kwargs_)
supermod.CT_BackstageGroups.subclass = CT_BackstageGroupsSub
# end class CT_BackstageGroupsSub


class CT_SimpleGroupsSub(supermod.CT_SimpleGroups):
    def __init__(self, group=None, taskGroup=None, **kwargs_):
        super(CT_SimpleGroupsSub, self).__init__(group, taskGroup,  **kwargs_)
supermod.CT_SimpleGroups.subclass = CT_SimpleGroupsSub
# end class CT_SimpleGroupsSub


class CT_BackstageTabSub(supermod.CT_BackstageTab):
    def __init__(self, columnWidthPercent=None, firstColumnMinWidth=None, firstColumnMaxWidth=None, secondColumnMinWidth=None, secondColumnMaxWidth=None, id=None, idQ=None, tag=None, idMso=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, enabled=None, getEnabled=None, label=None, getLabel=None, visible=None, getVisible=None, keytip=None, getKeytip=None, title=None, getTitle=None, firstColumn=None, secondColumn=None, **kwargs_):
        super(CT_BackstageTabSub, self).__init__(columnWidthPercent, firstColumnMinWidth, firstColumnMaxWidth, secondColumnMinWidth, secondColumnMaxWidth, id, idQ, tag, idMso, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, enabled, getEnabled, label, getLabel, visible, getVisible, keytip, getKeytip, title, getTitle, firstColumn, secondColumn,  **kwargs_)
supermod.CT_BackstageTab.subclass = CT_BackstageTabSub
# end class CT_BackstageTabSub


class CT_BackstageSub(supermod.CT_Backstage):
    def __init__(self, onShow=None, onHide=None, tab=None, button=None, **kwargs_):
        super(CT_BackstageSub, self).__init__(onShow, onHide, tab, button,  **kwargs_)
supermod.CT_Backstage.subclass = CT_BackstageSub
# end class CT_BackstageSub


class CT_CustomUISub(supermod.CT_CustomUI):
    def __init__(self, onLoad=None, loadImage=None, commands=None, ribbon=None, backstage=None, contextMenus=None, **kwargs_):
        super(CT_CustomUISub, self).__init__(onLoad, loadImage, commands, ribbon, backstage, contextMenus,  **kwargs_)
supermod.CT_CustomUI.subclass = CT_CustomUISub
# end class CT_CustomUISub


class CT_ControlCloneSub(supermod.CT_ControlClone):
    def __init__(self, image=None, imageMso=None, getImage=None, screentip=None, getScreentip=None, supertip=None, getSupertip=None, enabled=None, getEnabled=None, label=None, getLabel=None, insertAfterMso=None, insertBeforeMso=None, insertAfterQ=None, insertBeforeQ=None, visible=None, getVisible=None, keytip=None, getKeytip=None, showLabel=None, getShowLabel=None, showImage=None, getShowImage=None, id=None, idQ=None, tag=None, idMso=None, onAction=None, description=None, getDescription=None, size=None, getSize=None, **kwargs_):
        super(CT_ControlCloneSub, self).__init__(image, imageMso, getImage, screentip, getScreentip, supertip, getSupertip, enabled, getEnabled, label, getLabel, insertAfterMso, insertBeforeMso, insertAfterQ, insertBeforeQ, visible, getVisible, keytip, getKeytip, showLabel, getShowLabel, showImage, getShowImage, id, idQ, tag, idMso, onAction, description, getDescription, size, getSize,  **kwargs_)
supermod.CT_ControlClone.subclass = CT_ControlCloneSub
# end class CT_ControlCloneSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'CT_CustomUI'
        rootClass = supermod.customUI
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'CT_CustomUI'
        rootClass = supermod.customUI
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'CT_CustomUI'
        rootClass = supermod.customUI
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'CT_CustomUI'
        rootClass = supermod.customUI
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from customUI14base import *\n\n')
        sys.stdout.write('import customUI14base as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
