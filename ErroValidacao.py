#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
import email.message
import pandas as pd

def enviar_email(Nota, Motivo, EmailDestinatarios):  
    corpo_email = """
    <p>Olá</p>
    <p>Fiscal,</p>
    <p>Por favor, podem validar o erro da nota fiscal?</p>
    """

    msg = email.message.Message()
    msg['Subject'] = f"NF {Nota} {Motivo}"
    msg['From'] = 'lucas.degrande@bmchyundai.com.br'
    Destinatarios = EmailDestinatarios.split(',')
    msg['To'] = ', '.join(Destinatarios)
    password = 'wssbhscozclgrphe' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login com as credenciais s.login e enviar os emails com s.sendmail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], Destinatarios, msg.as_string().encode('utf-8'))
    print(f'E-mails enviados para: {Destinatarios}')
    print('Email enviado')
    
planilha = pd.read_excel('EnviarEmailErro.xlsx')
planilha = planilha.drop(columns='Formula')

print(planilha)

for CadaLinha, row in planilha.iterrows():
    Nota = row['NF']
    Motivo = row['MOTIVO']
    EmailDestinatarios = row['EmailDestinatarios']

    enviar_email(Nota, Motivo, EmailDestinatarios)

# In[ ]:




