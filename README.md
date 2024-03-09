# Automatização de Envio de E-mails para Notas Fiscais com Erros

Este script em Python tem como objetivo automatizar o envio de e-mails para notificar sobre erros em notas fiscais. Ele lê uma planilha contendo informações sobre as notas fiscais com problemas, como o motivo do erro, e envia e-mails personalizados para os destinatários específicos, solicitando a validação e correção dos problemas.

## Funcionalidades Principais

- **Leitura e Tratamento da Planilha:** O script lê uma planilha contendo informações sobre as notas fiscais com erros e realiza tratamentos necessários nos dados para prepará-los para o envio de e-mails.

- **Envio de E-mails Personalizados:** Para cada linha da planilha, o script dispara um e-mail personalizado, informando sobre o erro na nota fiscal e solicitando a validação e correção.

## Passo a Passo do Projeto

1. **Leitura da Planilha:** O script lê a planilha contendo informações sobre as notas fiscais com erros.

2. **Tratamento dos Dados:** Realiza tratamentos necessários nos dados, como remoção de colunas desnecessárias.

3. **Envio de E-mails:** Para cada linha da planilha, o script envia um e-mail personalizado aos destinatários especificados, informando sobre o erro na nota fiscal e solicitando a validação e correção.

## Tecnologias Utilizadas

- **Python:** Utilizado para desenvolver o script de automação do envio de e-mails.
- **pandas:** Biblioteca utilizada para manipulação e análise de dados, especialmente para trabalhar com a planilha.
- **smtplib:** Módulo utilizado para enviar e-mails através do protocolo SMTP.
- **email.message:** Módulo utilizado para construir e manipular mensagens de e-mail.

## Autor

- **Nome:** Lucas Degrande
- **Contato:** lucasdegrande15@gmail.com
