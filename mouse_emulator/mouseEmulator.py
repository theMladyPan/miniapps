#Boa:Frame:Main

import wx, keymouse
from threading import Thread
from time import sleep

def create(parent):
    return Main(parent)

[wxID_MAIN, wxID_MAINBUTTON, 
] = [wx.NewId() for _init_ctrls in range(2)]

class Main(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MAIN, name=u'Main', parent=prnt,
              pos=wx.Point(512, 373), size=wx.Size(225, 83),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Pohyb mysou')
        self.SetClientSize(wx.Size(209, 45))
        self.SetToolTipString(u'Hlavne Okno')
        self.SetIcon(wx.Icon(u'ico.ico',
              wx.BITMAP_TYPE_ICO))

        self.button = wx.Button(id=wxID_MAINBUTTON,
              label=u'Begin mouse movement', name=u'button', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(209, 45), style=0)
        self.button.SetToolTipString(u'Zacni/prestan hybat mysou')
        self.button.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'MS Shell Dlg 2'))
        self.button.Bind(wx.EVT_BUTTON, self.OnButton, id=wxID_MAINBUTTON)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.mouse=keymouse.Keymouse()
        self.hyb=False
        
    def beginMovement(self):
        while(self.hyb):
            (x,y)=self.mouse.getMouse()
            x=x+10
            self.mouse.moveMouse(x,y)
            sleep(0.1)
            (x,y)=self.mouse.getMouse()
            x=x-10
            self.mouse.moveMouse(x,y)
            sleep(0.1)
            
    def OnButton(self, event):
        if self.hyb:
            self.hyb=False
            self.button.SetLabel("Begin mouse movement")
        else:
            self.hyb=True
            Thread(target=self.beginMovement, args=()).start()
            self.button.SetLabel("Stop mouse movement")
            


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
