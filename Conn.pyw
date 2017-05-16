#Boa:Frame:Frame1

import wx, sys
import wx.richtext
import urllib

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1EXIT_BTN, wxID_FRAME1GAUGE, wxID_FRAME1HELP_BTN, 
 wxID_FRAME1LOAD_BTN, wxID_FRAME1NAZOV_SUBORU, wxID_FRAME1RICHTEXTCTRL1, 
 wxID_FRAME1RICHTEXTCTRL2, wxID_FRAME1SAVE_BTN, wxID_FRAME1SAV_OUT_BTN, 
 wxID_FRAME1SUBMIT_BTN, 
] = [wx.NewId() for _init_ctrls in range(11)]

class PopupWindow1(wx.PopupWindow):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.PopupWindow.__init__(self, flags=wx.SIMPLE_BORDER, parent=prnt)
        self.SetSize(wx.Size(234, 328))
        self.Move(wx.Point(413, 294))

        self.textbox = wx.StaticText(id=wxID_POPUPWINDOW1TEXTBOX,
              label='Welcome to Remote python server 0.0.1\n\nServer runs on Python 2.7 with limmited access to resources.\n\nUse with response.\n\nFor shortcuts use Control key plus keys listed below\n\nH - Hint\nQ - Quit\nS - Save\nO - Open\nDelete - Delete all content\nReturn - Submit program\n\nEnjoy!',
              name='textbox', parent=self, pos=wx.Point(0, 0), size=wx.Size(218,
              289), style=0)
        self.textbox.SetToolTipString('Info')
        self.textbox.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Consolas'))

    def __init__(self, parent):
        self._init_ctrls(parent)

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(341, 54), size=wx.Size(927, 667),
              style=wx.DEFAULT_FRAME_STYLE,
              title='Remote python server terminal')
        self.SetClientSize(wx.Size(911, 628))

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL1,
              parent=self, pos=wx.Point(0, 0), size=wx.Size(912, 288),
              style=wx.richtext.RE_MULTILINE, value='\n')
        self.richTextCtrl1.SetLabel('text')
        self.richTextCtrl1.SetToolTipString('Write down few python lines to send to remote server')
        self.richTextCtrl1.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Consolas'))
        self.richTextCtrl1.Bind(wx.EVT_CHAR, self.on_char)

        self.richTextCtrl2 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL2,
              parent=self, pos=wx.Point(-8, 312), size=wx.Size(920, 316),
              style=wx.richtext.RE_MULTILINE, value='')
        self.richTextCtrl2.SetLabel('text')
        self.richTextCtrl2.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Consolas'))
        self.richTextCtrl2.SetToolTipString('Output from remote machine')

        self.submit_btn = wx.Button(id=wxID_FRAME1SUBMIT_BTN, label='Submit',
              name='submit_btn', parent=self, pos=wx.Point(0, 288),
              size=wx.Size(64, 24), style=0)
        self.submit_btn.SetToolTipString('Submit program to server')
        self.submit_btn.Bind(wx.EVT_BUTTON, self.submit,
              id=wxID_FRAME1SUBMIT_BTN)

        self.save_btn = wx.Button(id=wxID_FRAME1SAVE_BTN, label='Save',
              name='save_btn', parent=self, pos=wx.Point(64, 288),
              size=wx.Size(64, 24), style=0)
        self.save_btn.SetToolTipString('Save to specified file')
        self.save_btn.Bind(wx.EVT_BUTTON, self.save_file,
              id=wxID_FRAME1SAVE_BTN)

        self.load_btn = wx.Button(id=wxID_FRAME1LOAD_BTN, label='Load',
              name='load_btn', parent=self, pos=wx.Point(128, 288),
              size=wx.Size(64, 24), style=0)
        self.load_btn.SetToolTipString('Load from specified file')
        self.load_btn.Bind(wx.EVT_BUTTON, self.load_file,
              id=wxID_FRAME1LOAD_BTN)

        self.sav_out_btn = wx.Button(id=wxID_FRAME1SAV_OUT_BTN,
              label='Save Output', name='sav_out_btn', parent=self,
              pos=wx.Point(192, 288), size=wx.Size(80, 24), style=0)
        self.sav_out_btn.SetToolTipString('Save output to specified file')
        self.sav_out_btn.Bind(wx.EVT_BUTTON, self.save_out,
              id=wxID_FRAME1SAV_OUT_BTN)

        self.nazov_suboru = wx.TextCtrl(id=wxID_FRAME1NAZOV_SUBORU,
              name='nazov_suboru', parent=self, pos=wx.Point(400, 288),
              size=wx.Size(312, 24), style=0, value='file.py')
        self.nazov_suboru.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Consolas'))
        self.nazov_suboru.SetToolTipString('Name of working file')

        self.gauge = wx.Gauge(id=wxID_FRAME1GAUGE, name='gauge', parent=self,
              pos=wx.Point(712, 288), range=100, size=wx.Size(200, 24),
              style=wx.GA_HORIZONTAL)
        self.gauge.SetToolTipString('Progress gauge')

        self.exit_btn = wx.Button(id=wxID_FRAME1EXIT_BTN, label='Exit',
              name='exit_btn', parent=self, pos=wx.Point(272, 288),
              size=wx.Size(64, 24), style=0)
        self.exit_btn.SetToolTipString('Exit terminal')
        self.exit_btn.Bind(wx.EVT_BUTTON, self.on_exit, id=wxID_FRAME1EXIT_BTN)

        self.help_btn = wx.Button(id=wxID_FRAME1HELP_BTN, label='Help',
              name='help_btn', parent=self, pos=wx.Point(336, 288),
              size=wx.Size(64, 24), style=0)
        self.help_btn.SetToolTipString('Show help')
        self.help_btn.Bind(wx.EVT_BUTTON, self.help, id=wxID_FRAME1HELP_BTN)
        self.help_btn.Bind(wx.EVT_CHAR, self.help_btn_key)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def empty(self):
        self.gauge.SetValue(10)
    def full(self):
        self.gauge.SetValue(100)

    def submit(self, event=None):
        self.empty()
        try:
            data=self.richTextCtrl1.GetValue().replace('\n',';').replace('\t','    ')
            conn = urllib.urlopen("http://server-pyloger.rhcloud.com/run?%s" % data)
            self.richTextCtrl2.SetValue(conn.read())
        except:
            self.richTextCtrl2.SetValue(str(sys.exc_info()[:]))
        self.full()
        
    def save_file(self, event=None):
        self.empty()
        try:
            subor=file(self.nazov_suboru.GetValue(),"w")
            subor.write(self.richTextCtrl1.GetValue())
            subor.close()
        except:
            self.richTextCtrl2.SetValue(str(sys.exc_info()[:]))
        self.full()

    def load_file(self, event=None):
        self.empty()
        try:
            subor=file(self.nazov_suboru.GetValue(),"r")
            self.richTextCtrl1.SetValue(subor.read())
            subor.close()
        except:
            self.richTextCtrl2.SetValue(str(sys.exc_info()[:]))
        self.full()

    def save_out(self, event):
        self.empty()
        try:
            subor=file(self.nazov_suboru.GetValue(),"w")
            subor.write(self.richTextCtrl2.GetValue())
            subor.close()
        except:
            self.richTextCtrl2.SetValue(str(sys.exc_info()[:]))
        self.full()

    def on_exit(self, event=None):
        exit(0)

    def on_char(self, event):
        if event.ControlDown():
            if event.GetKeyCode() == 10:
                self.submit()
            elif event.GetKeyCode() == 19:
                self.save_file()
            elif event.GetKeyCode() == 15:
                self.load_file()
            elif event.GetKeyCode() == 12:
                self.nazov_suboru.SetFocus()
            elif event.GetKeyCode() == 127:
                self.richTextCtrl1.SetValue("")
            elif event.GetKeyCode() == 17:
                self.on_exit()
            elif event.GetKeyCode() == 8:
                self.help()
            else:
                print event.GetKeyCode()
        else:
            event.Skip()
        self.richTextCtrl1.SetFocus()

    def help_btn_key(self, event):
        self.on_char(event)
        
    def help(self, event=None):
        self.richTextCtrl1.SetValue("""
Welcome user of python remote server!
Please use with responsibility, server has limited resources.

To use shortcuts, press down Control Key together with following keys:
    S - Save
    O - Open
    H - Help
    Q - Quit
    Delete - Delete board
    Return - Submit script
    
Server does not remember, so you have to send all classes and
functions in one file. Write down "help" and submit. Enjoy !
""")
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
