<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Página Vulnerável</title>
  </head>
  <body>
    <h1>Bem-vindo à Página Vulnerável!</h1>
    <?php
      // Recebe um parâmetro 'page' do usuário e inclui o arquivo com base nesse parâmetro
      $page = $_GET['page'];
      include($page . '.php');
    ?>
  </body>
</html>
