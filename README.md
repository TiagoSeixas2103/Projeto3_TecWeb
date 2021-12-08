# Projeto3_TecWeb
<li>Ana Carolina Souza <br>
<li> Tiago Seixas <br>

Checklist:
<li> Semana 1 - Preparar base django do projeto, fazer o projeto usar docker como database <br>
<li> Semana 2 - Criar funcionalidades, criar páginas das funcionalidades <br>
<li> Semana 3 - Dar deploy do projeto finalizado <br>
  
Link do deploy: https://rocky-depths-50359.herokuapp.com/

# Arquitetura da aplicação:

Nós fizemos uma aplicação para que lojas consigam acompanhar o seu desempenho mensal, assim como o desempenho de seus funcionários e o quão bem os seus produtos têm se saído.

<li>Página Inicial - Na página inicial, o/a gerente da loja deve colocar o nome dos funcionários, o produto vendido pelo funcinário e a quantidade desse produto que o funcionário conseguiu vender por mês. Caso o produto desejado não esista no banco de dados, quando for adicionar produto, o usuário serálevado para uma página onde poderá preencher as informações do produto em questão. Abaixo do formulário aparecerá cartões com os nomes dos funcionários, as informações do produto vendido, e a quantidade do produto vendido pelo funcionário. No topo de todas as páginas terá o logo da nossa aplicação, o seu nome e botões que levam para as outras páginas. ATENÇÃO: É esperado que hajam cartões com funcionários repetidos, pois os cartões se referem apenas ao desempenho do funcionário na venda de um único produto.<br>

![Página Inicial](https://github.com/TiagoSeixas2103/Projeto3_TecWeb/blob/main/readmeImg/PaginaAppPaginaInicial.png?raw=true)

<li>Adicionando o produto - Formulário para o preenchimento dos dados do produto, onde o/a gerente deve colocar o nome do produto, o seu preço de venda, e o custo desse produto para a loja.<br>

![Adiciona Produto](https://github.com/TiagoSeixas2103/Projeto3_TecWeb/blob/main/readmeImg/PaginaAppAdicionaProduto.png?raw=true)

<li>Produtos - Na página dos produtos, estão exibidos os dados fornecidos sobre o produto pelo formulário.<br>

![Produtos](https://github.com/TiagoSeixas2103/Projeto3_TecWeb/blob/main/readmeImg/PaginaAppProduto.png?raw=true)

<li>Lucro Mensal - Na página de lucro mensal, está exibido o lucro mensal calculado usando o preço de venda e o custo de todos os produtos da loja.<br>

![Lucro Mensal](https://github.com/TiagoSeixas2103/Projeto3_TecWeb/blob/main/readmeImg/PaginaAppLucroMensal.png?raw=true)

<li>Funcionários - Na página dos funcionários, está exibida a receita de cada funcionário, levando em consideração todos os produtos por eles vendidos.<br>

![Receita Funcionários](https://github.com/TiagoSeixas2103/Projeto3_TecWeb/blob/main/readmeImg/PaginaAppReceitaFuncionario.png?raw=true)

<li>Lucro dos Produtos - Na página de lucro dos produtos, está exibido o lucro gerado por cada produto.<br>

![Lucro Produto](https://github.com/TiagoSeixas2103/Projeto3_TecWeb/blob/main/readmeImg/PaginaAppLucroProduto.png?raw=true)

<li>KPI - Na página de KPI, estão exibidos os 'key performance indicators', ou seja, os indicadores de performance que nós consideramos como sendo chave para o usuário, de acordo com os dados fornecidos.<br>

![KPI](https://github.com/TiagoSeixas2103/Projeto3_TecWeb/blob/main/readmeImg/PaginaAppKPI.png?raw=true)

