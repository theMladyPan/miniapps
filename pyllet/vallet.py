# -*- coding: cp1250 -*-
from usering import Usering, User
import pickle, os, time

clear = lambda: os.system('cls')
koniec = lambda: raw_input("koniec...")

class Penaznik:
  def __init__(self):
    self.savings=0
    self.common=0
    self.money=0
    self.bank=0
    self.history=[]
    self.args={'x':u'In�...'}

  def change_funds(self, scmb, value, koment):
    string=time.strftime('%X %x')+ u"\nupraven� prostriedky: "+str(value)+u"eur"
    if "s" in scmb:
      self.savings+=value
      string+=u"\nako u�etren� peniaze"
    if "c" in scmb:
      self.common+=value
      string+=u"\nako be�n� peniaze"
    if "m" in scmb:
      self.money+=value
      string+=u" v hotovosti."
    if "b" in scmb:
      self.bank+=value
      string+=u" na ��te."
    string+=u"\n��el: "+koment+u"\n--------------------------------------------------\n"
    self.history.append(string)

  def get_savings(self):
    return self.savings

  def get_common(self):
    return self.common

  def get_money(self):
    return self.money

  def get_bank(self):
    return self.bank

  def get_history(self):
    return self.history

  def get_args(self):
    return self.args

  def choose_arg(self):
    print u"Vyberte koment�r: "
    for i in self.args.keys():
      print i, ' - ', self.args.get(i)
    koment=""
    while koment not in self.args.keys():
      koment=raw_input(" > ")
      if koment not in self.args.keys():
        print u'Koment�r nen�jden�'
      elif koment == 'x':
        return raw_input('Zadaj komentar: ')
    return self.args.get(koment)

  def dump(self):
    pickle.dump(self,file("wallet.rdf","w"))

  def load(self):
    return pickle.load(file("wallet.rdf","r"))

  def skratky(self):
    string= u"Definovan� skratky:\n-----------------------\n"
    for skratka in penaznik.args.keys():
      string+= skratka+ " - "+ self.args.get(skratka)+'\n'
    return string +'-----------------------'

if __name__ == "__main__":
  try:
    penaznik=Penaznik().load()
  except:
    penaznik=Penaznik()

  usering=Usering()
  if usering.userCount()>0:
    print u"Pros�m prihl�ste sa."
    a=0
    while not a:
      a=usering.login(raw_input("Zadaj meno: "), raw_input("Zadaj heslo: "))
      clear()
      if a==0:
        print u"Zadan� zl� heslo, sk�ste znova"
      if a==-1:
        print u"Meno nenajden�, sk�ste znova"
        a=0

  else:
    print u"�iadny pou��vate�, pros�m zaregistrujte sa."
    while not usering.addUser(raw_input("Zadaj meno: "), raw_input("Zadaj heslo: ")):
      clear()
      print u"U��vate� existuje, sk�ste znova"
    clear()
    print u"Pros�m prihl�ste sa."
    a=0
    while not a:
      a=usering.login(raw_input("Zadaj meno: "), raw_input("Zadaj heslo: "))
      clear()
      if a==0:
        print u"Zadan� zl� heslo, sk�ste znova"
      if a==-1:
        print u"Meno nenajden�, sk�ste znova"
        a=0
  usering.dump()
  prikaz=1
  while prikaz!="x":
    clear()
    print u"""Zoznam pr�kazov
-----------------------
Nov� pohyby          n
Prostriedky          p
Skratky              s
Hist�ria pohybov     h
Opusti� program      x
-----------------------"""
    prikaz=raw_input(" > ")
    clear()
    if prikaz=="s":
      print u"""Zoznam pr�kazov:
-----------------------
Nov� skratka         +
Odobra� skratku      -
Prezrie� skratky     s
-----------------------"""
      prikaz=raw_input(" > ")
      clear()
      print penaznik.skratky()
      if prikaz=="+":
        skratka=raw_input("Pridaj skratku: ")
        popis=  raw_input("Pridaj popis:   ")
        penaznik.args[skratka]=popis
        print u"Skratka ",skratka, "pridana"
        koniec()
        clear()

      if prikaz=="-":
        skratka=raw_input("Zadaj skratku k odobratu: ")
        try:
          print penaznik.args.pop(skratka), u'bola odstr�nen�'
        except:
          print 'Skratka ', skratka, u' nen�jden�'
        koniec()
        clear()

      if prikaz=="s":
        koniec()
        clear()
      else: clear()

    if prikaz=="h":
      filter=raw_input('Pouzi filter (enter pre vsetko): ')
      print ""
      for polozka in penaznik.get_history():
        if filter in polozka: print polozka
      koniec()
      clear()

    if prikaz=="p":
      print u"Dostupn� prostriedky:"
      print u"-----------------------"
      print u"U�etren� | ",penaznik.get_savings()
      print u"Be�n�    | ",penaznik.get_common()
      print u"-----------------------"
      print u"��ty     | ",penaznik.get_bank()
      print u"Hotovos� | ",penaznik.get_money()
      print u"-----------------------"
      print u"Spolu    | ",penaznik.get_money()+penaznik.get_bank()
      print u"-----------------------"
      koniec()
      clear()

    if prikaz=="n":
      print u"""Zoznam pr�kazov
-----------------------
Prida� prostriedky   +
Odobra� prostriedky  -
Presun�� prostriedky =
-----------------------"""
      prikaz=raw_input(" > ")
      clear()

      if prikaz=="=":
        print u"""Zobra� z:
Be�n� peniaze: c
�spory       : s"""
        skade=raw_input(u" > ")
        clear()
        print u"""Zobra� z:
Hotovos�: m
��et    : b"""
        skade+=raw_input(u" > ")
        clear()

        print u"""Prida� kam:
Be�n� peniaze: c
�spory       : s"""
        kam=raw_input(u" > ")
        clear()
        print u"""Prida� kam:
Hotovos�: m
��et    : b"""
        kam+=raw_input(u" > ")
        clear()

        kolko=raw_input("Hodnota: ")
        penaznik.change_funds(skade, -float(kolko), "presun")
        penaznik.change_funds(kam, float(kolko), "presun")

      if prikaz=="+":
        print u"""Prida� prostriedky:
Be�n� peniaze: c
�spory       : s"""
        scmb=raw_input(u" > ")
        clear()
        print u"""Prida� prostriedky:
Hotovos�: m
��et    : b"""
        scmb+=raw_input(u" > ")
        clear()
        penaznik.change_funds(scmb, float(raw_input(u"Hodnota: ")), penaznik.choose_arg())
        clear()

      if prikaz=="-":
        print u"""Prida� prostriedky:
Be�n� peniaze: c
�spory       : s"""
        scmb=raw_input(u" > ")
        clear()
        print u"""Prida� prostriedky:
Hotovos�: m
��et    : b"""
        scmb+=raw_input(u" > ")
        clear()
        penaznik.change_funds(scmb, -1*float(raw_input(u"Hodnota: ")), penaznik.choose_arg())
        clear()

    penaznik.dump()