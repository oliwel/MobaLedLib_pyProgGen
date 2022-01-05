# -*- coding: utf-8 -*-
#
#         Write header
#
# * Version: 1.21
# * Author: Harold Linke
# * Date: January 1st, 2020
# * Copyright: Harold Linke 2020
# *
# *
# * MobaLedCheckColors on Github: https://github.com/haroldlinke/MobaLedCheckColors
# *
# *
# * History of Change
# * V1.00 10.03.2020 - Harold Linke - first release
# *  
# * https://github.com/Hardi-St/MobaLedLib
# *
# * MobaLedCheckColors is free software: you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation, either version 3 of the License, or
# * (at your option) any later version.
# *
# * MobaLedCheckColors is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program.  if not, see <http://www.gnu.org/licenses/>.
# *
# *
# ***************************************************************************

from vb2py.vbfunctions import *
from vb2py.vbdebug import *

import mlpyproggen.M06_Write_Header as M06
import mlpyproggen.M03_Dialog as M03

def Arduino_Button_Click():
    #---------------------------------
    __Button_Pressed_Proc()
    M06.Create_HeaderFile()

def ClearSheet_Button_Click():
    #------------------------------------
    __Button_Pressed_Proc()
    ClearSheet()

def Dialog_Button_Click():
    #-------------------------------
    __Button_Pressed_Proc()
    M03.Dialog_Guided_Input()

def Help_Button_Click():
    #------------------------------
    __Button_Pressed_Proc()
    Show_Help()

def __Button_Pressed_Proc():
    #--------------------------------
    #Selection.Select()
    #Application.EnableEvents = True
    #__Correct_Buttonsizes()
    pass

def __Name_with_LF():
    Hide_Button.Caption = 'Aus- oder' + vbLf + 'Einblenden'

def __Correct_Create_Buttonsize(obj):
    #-----------------------------------------
    obj.Height = 160
    obj.Width = 100
    obj.Height = 76
    obj.Width = 60

def __Correct_Buttonsizes():
    OldScreenupdating = Boolean()
    #------------------------
    # There is a bug in excel which changes the size of the buttons
    # if the resolution of the display is changed. This happens
    # fore instance if the computer is connected to a beamer.
    # To prevent this the buttons are resized with this function.
    OldScreenupdating = Application.ScreenUpdating
    Application.ScreenUpdating = False
    __Correct_Create_Buttonsize(Arduino_Button)
    __Correct_Create_Buttonsize(Dialog_Button)
    __Correct_Create_Buttonsize(Insert_Button)
    __Correct_Create_Buttonsize(Del_Button)
    __Correct_Create_Buttonsize(Move_Button)
    __Correct_Create_Buttonsize(Copy_Button)
    __Correct_Create_Buttonsize(Hide_Button)
    __Correct_Create_Buttonsize(UnHideAll_Button)
    __Correct_Create_Buttonsize(ClearSheet_Button)
    __Correct_Create_Buttonsize(Options_Button)
    __Correct_Create_Buttonsize(Help_Button)
    Application.ScreenUpdating = OldScreenupdating

def EnableDisableAllButtons(Enab):
    #------------------------------------------------------
    Arduino_Button.Enabled = Enab
    Dialog_Button.Enabled = Enab
    Insert_Button.Enabled = Enab
    Del_Button.Enabled = Enab
    Move_Button.Enabled = Enab
    Copy_Button.Enabled = Enab
    Hide_Button.Enabled = Enab
    UnHideAll_Button.Enabled = Enab
    ClearSheet_Button.Enabled = Enab
    Options_Button.Enabled = Enab

def __EnableAllButtons():
    #-----------------------------
    # Could be called manually after a crash
    EnableDisableAllButtons(True)

def Hide_Button_Click():
    #------------------------------
    __Button_Pressed_Proc()
    Proc_Hide_Unhide()

def Insert_Button_Click():
    __Button_Pressed_Proc()
    Proc_Insert_Line()

def Del_Button_Click():
    #-----------------------------
    __Button_Pressed_Proc()
    Proc_Del_Row()

def Move_Button_Click():
    #------------------------------
    __Button_Pressed_Proc()
    Proc_Move_Row()

def Copy_Button_Click():
    #------------------------------
    __Button_Pressed_Proc()
    Proc_Copy_Row()

def Options_Button_Click():
    #----------------------------------
    __Button_Pressed_Proc()
    Option_Dialog()

def UnHideAll_Button_Click():
    #-----------------------------------
    __Button_Pressed_Proc()
    Proc_UnHide_All()

# VB2PY (UntranslatedCode) Argument Passing Semantics / Decorators not supported: Target - ByVal 
def __Worksheet_Change(Target):
    #--------------------------------------------------------
    # This function is called if the worksheet is changed.
    # It performs several checks after a user input depending form the column of the changed cell:
    Global_Worksheet_Change(Target)

# VB2PY (UntranslatedCode) Argument Passing Semantics / Decorators not supported: Target - ByVal 
def __Worksheet_SelectionChange(Target):
    #-----------------------------------------------------------------
    # Is called by event if the worksheet selection has changed
    Global_Worksheet_SelectionChange(Target)

def __Worksheet_Activate():
    #-------------------------------
    Global_Worksheet_Activate()

def __Worksheet_Calculate():
    #--------------------------------
    # This proc is also called if an other workbook (from a mail/internet) is opened    24.02.20:
    if DEBUG_CHANGEEVENT:
        Debug.Print('Worksheet_Calculate() in sheet \'DCC\' called')
    if ActiveSheet is None:
        return
    if Cells.Parent.Name == ActiveSheet.Name:
        Global_Worksheet_Calculate()

# VB2PY (UntranslatedCode) Option Explicit
