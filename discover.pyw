#Boa:Frame:Frame1

import wx, os, subprocess, sys, webbrowser

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1COUNTDOWN, wxID_FRAME1DISCOVER, 
 wxID_FRAME1ENTRY_SUBNET, wxID_FRAME1GAUGE, wxID_FRAME1LIST_NODES, 
 wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='discover', parent=prnt,
              pos=wx.Point(220, 267), size=wx.Size(425, 376),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Discoverpy')
        self.SetClientSize(wx.Size(409, 337))

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Subnet matrice', name='staticBox1', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(392, 100), style=0)

        self.entry_subnet = wx.TextCtrl(id=wxID_FRAME1ENTRY_SUBNET,
              name=u'entry_subnet', parent=self, pos=wx.Point(16, 32),
              size=wx.Size(216, 32), style=0, value=u'192.168.0.x')

        self.gauge = wx.Gauge(id=wxID_FRAME1GAUGE, name=u'gauge', parent=self,
              pos=wx.Point(16, 72), range=255, size=wx.Size(216, 24),
              style=wx.GA_HORIZONTAL)

        self.discover = wx.Button(id=wxID_FRAME1DISCOVER, label=u'Discover!',
              name=u'discover', parent=self, pos=wx.Point(240, 32),
              size=wx.Size(152, 32), style=0)
        self.discover.Bind(wx.EVT_BUTTON, self.OnDiscoverButton,
              id=wxID_FRAME1DISCOVER)

        self.list_nodes = wx.ListBox(choices=[], id=wxID_FRAME1LIST_NODES,
              name=u'list_nodes', parent=self, pos=wx.Point(16, 136),
              size=wx.Size(376, 184), style=0)
        self.list_nodes.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnList_nodesListboxDclick, id=wxID_FRAME1LIST_NODES)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Nodes discovered', name='staticBox2', parent=self,
              pos=wx.Point(8, 112), size=wx.Size(392, 216), style=0)

        self.countdown = wx.StaticText(id=wxID_FRAME1COUNTDOWN,
              label=u'Approx. time: NaN', name=u'countdown', parent=self,
              pos=wx.Point(240, 72), size=wx.Size(135, 21), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.ShowFullScreen(False) 

    def OnDiscoverButton(self, event):
        self.discover.Disable()
        self.entry_subnet.Disable()
        for i in range(len(self.list_nodes.GetItems())):
            self.list_nodes.Delete(i)
        prefix=self.entry_subnet.GetValue().replace("x","")
        wx.Yield()
        with open(os.devnull, 'wb') as devnull:
            for i in range(1,255):
                try:
                    self.entry_subnet.SetValue("%s%d"%(prefix,i))
                    if os.name=="nt":
                        subprocess.check_call(['ping','/n','1','/w','50','%s%d'%(prefix,i)], stdout=devnull, stderr=subprocess.STDOUT, shell=True)
                    elif os.name=="posix":
                        subprocess.check_call(['ping -c1 -w1 %s%d'%(prefix,i)], stdout=devnull, stderr=subprocess.STDOUT, shell=True)
                    else:
                         pass
                    self.list_nodes.Insert("%s%d"%(prefix,i), len(self.list_nodes.GetItems()))

                except subprocess.CalledProcessError:
                    pass
                self.gauge.SetValue(i)
                self.countdown.Label="Approx. time: %02d:%02d"%((254-i)/60, (254-i)%60)
                wx.Yield()
        
        self.entry_subnet.SetValue("%sx"%prefix)
        self.discover.Enable()
        self.entry_subnet.Enable()

    def OnList_nodesListboxDclick(self, event):
        webbrowser.open('http://'+self.list_nodes.GetItems()[self.list_nodes.GetSelection()], new=1, autoraise=True)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
