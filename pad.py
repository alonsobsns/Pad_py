#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import showinfo

import tkinter as tk
import os
import subprocess

class appmint:
 def __init__(self):
  
  # Cria janela principal
  self.janela_principal = Tk()

  # titulo e tamanho janela principal
  self.janela_principal.title('Padronização de SO - CBMPR')
  self.janela_principal.geometry("550x250")
  
  # Cria dois frames
  self.frame_up = Frame(self.janela_principal)
  self.frame_bot = Frame(self.janela_principal)
  
  # Objetos IntVar dos botões
  self.checkvar1 = IntVar()
  self.checkvar2 = IntVar()
  self.checkvar3 = IntVar()
  self.checkvar4 = IntVar()
  self.checkvar5 = IntVar()
  self.checkvar6 = IntVar()
  
  # Setando valor 0 para aparecem desmarcados
  self.checkvar1.set(0)
  self.checkvar2.set(0)
  self.checkvar3.set(0)
  self.checkvar4.set(0)
  self.checkvar5.set(0)
  self.checkvar6.set(0)
  
  # Criando os check buttons e o label
  self.label = Label(self.frame_up, text='Sistema de automatização de tarefas, selecione as opções que deseja executar: ')
  self.checkbutton1 = Checkbutton(self.frame_up, text='Atualizar Computador', \
       variable = self.checkvar1)
  self.checkbutton2 = Checkbutton(self.frame_up, text='Sincronizar Status de Rede', \
       variable = self.checkvar2)
  self.checkbutton3 = Checkbutton(self.frame_up, text='Sincronizar Data', \
       variable = self.checkvar3)
  self.checkbutton4 = Checkbutton(self.frame_up, text='Instalar Modulo Bancos', \
       variable = self.checkvar4)
  self.checkbutton5 = Checkbutton(self.frame_up, text='Instalar Cliente LDAP', \
       variable = self.checkvar5)
  self.checkbutton6 = Checkbutton(self.frame_up, text='Alterar senha VNC', \
       variable = self.checkvar6)
  
  # Empacotando o label e os check buttons
  self.label.pack(anchor = 'w')
  self.checkbutton1.pack(anchor = 'w')
  self.checkbutton2.pack(anchor = 'w')
  self.checkbutton3.pack(anchor = 'w')
  self.checkbutton4.pack(anchor = 'w')
  self.checkbutton5.pack(anchor = 'w')
  self.checkbutton6.pack(anchor = 'w')
  
  # Criando os botões
  self.botao = Button(self.frame_bot, text='Executar',command=self.exibe)
  self.botao_sair = Button(self.frame_bot, text='Sair',command=self.janela_principal.quit)
            
  # Empacotando os botões
  self.botao.pack(side='left')
  self.botao_sair.pack(side='left')
  
  # Empacotando os frames na janela principal
  self.frame_up.pack()
  self.frame_bot.pack()

  #progressbar
  #self.progressbar = ttk.Progressbar(mode="indeterminate")
  #self.progressbar.place(x=100, y=300, width=400)
  
  #self.progressbar.pack ()


  # Rodando
  mainloop()
  
 def exibe(self):
   self.texto = 'Modulo(s) Atualizados! \n'
   if self.checkvar1.get() == 1:
    #self.texto += 'Sistema Atualizado\n'
    subprocess.run(["./scripts/atualizar.sh"], shell=True)
   if self.checkvar2.get() == 1:
    subprocess.run(["./scripts/conky.sh"], shell=True)
   if self.checkvar3.get() == 1:
    subprocess.run(["./scripts/data.sh"], shell=True)
   if self.checkvar4.get() == 1:
    subprocess.run(["./scripts/bancos.sh"], shell=True)
   if self.checkvar5.get() == 1:
    subprocess.run(["./scripts/cliente_ldap.sh"], shell=True)
   if self.checkvar6.get() == 1:
    subprocess.call('x11vnc --storepasswd /etc/x11vnc/vncpwd', shell=True)

   messagebox.showinfo('Padronização de SO - CBMPR', self.texto)

gui = appmint()
