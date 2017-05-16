#-*- coding:utf-8 -*-
#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1SLIDER1, wxID_FRAME1STATICBOX1, 
] = [wx.NewId() for _init_ctrls in range(3)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(340, 187), size=wx.Size(671, 66),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Backlit')
        self.SetClientSize(wx.Size(671, 66))

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Podsvietenie: 100%', name='staticBox1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(672, 64), style=0)
        self.staticBox1.SetMinSize(wx.Size(200, 10))
        self.staticBox1.SetToolTipString(u'')

        self.slider1 = wx.Slider(id=wxID_FRAME1SLIDER1, maxValue=100,
              minValue=1, name='slider1', parent=self, pos=wx.Point(8, 24),
              size=wx.Size(648, 24), style=wx.SL_HORIZONTAL, value=100)
        self.slider1.SetLabel(u'')
        self.slider1.Bind(wx.EVT_COMMAND_SCROLL_THUMBTRACK,
              self.OnSlider1CommandScrollThumbtrack, id=wxID_FRAME1SLIDER1)
        self.slider1.Bind(wx.EVT_SCROLL, self.OnSlider1CommandScrollThumbtrack)

    def __init__(self, parent):
        self._init_ctrls(parent)
        with open("/sys/class/backlight/intel_backlight/max_brightness","r") as subor:
            self.max_bright=int(subor.read())
        with open("/sys/class/backlight/intel_backlight/brightness","r") as subor:
            hodnota=int(subor.read())
            self.slider1.SetValue(int((hodnota*(100**2/self.max_bright))**0.5))
            self.staticBox1.SetLabel("Podsvietenie: %s%%"%(hodnota*100/self.max_bright))

    def OnSlider1CommandScrollThumbtrack(self, event):
        hodnota = str(int((self.slider1.GetValue()**2) / (100**2/self.max_bright)))
        if int(hodnota) > self.max_bright:
            hodnota=str(self.max_bright)
        self.staticBox1.SetLabel("Podsvietenie: %s%%"%(int(hodnota)*100/self.max_bright))
        with open("/sys/class/backlight/intel_backlight/brightness","w") as subor:
            subor.write(hodnota)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
