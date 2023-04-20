
Laboratório de LFI (Local File Inclusion)
# Escopo e objetivo

O objetivo deste código em PHP é permitir a inclusão de conteúdo de outros arquivos PHP no arquivo atual através do comando include() e explorar a vulnerabilidade conhecida como inclusão de arquivos locais (LFI). Com o LFI, um invasor pode manipular a entrada do usuário para incluir arquivos no servidor, executando código malicioso e comprometendo a segurança do sistema.

## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/robertocoliver/LFI
```

Entre no diretório do projeto

```bash
  cd LFI
```

mova o arquivo para pasta raiz do apache

```bash
  cp index.php /var/www/html/
```

Inicie o servidor

```bash
  systemctl start apache2  
```
## Desativar diretivas no arquivo de configuração PHP

Abrindo arquivo de configuração 
```bash
  nano /etc/php/8.2/cli/php.ini  
```
![App Screenshot](https://user-images.githubusercontent.com/102238044/233325316-9ee3d9c0-4f21-4d7c-8797-6279a2c827d2.jpg))

## Alerta
Essas diretivas permitem que o PHP abra URLs como se fossem arquivos locais, o que pode ser perigoso se um invasor passar uma URL maliciosa como entrada, levando a uma vulnerabilidade de inclusão de arquivos remotos (RFI) e inclusão de arquivo local (LFI). É altamente recomendado desativar essas diretivas em ambientes de produção para reduzir o risco de vulnerabilidades de segurança. 


Reiniciar o servidor e aplicar modificações 
```bash
  systemctl restart apache2  
```
