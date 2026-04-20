# HealthTrack - Portal Hospitalar de Monitoramento (Trabalho de Programação para Web)

Sistema web desenvolvido como trabalho prático da disciplina de Programação Web, utilizando Django 6 com autenticação via JWT e banco de dados SQLite.

---

## Alunos

* Diogo Marassi: 2220354
* Lucas Lopes: 2220647

---

## Organizacao do Readme

- [Escopo do Projeto](#escopo-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Rodar o Projeto](#como-rodar-o-projeto)
- [Manual do Usuário](#manual-do-usuário)
- [O que Funcionou e o que Não Funcionou](#o-que-funcionou-e-o-que-não-funcionou)

---

## Escopo do Projeto

O HealthTrack é um portal hospitalar voltado ao controle e monitoramento de três tipos de itens do ambiente clínico:

- **Equipamentos médicos** - Dispositivos com número de série, fabricante, tipo e status operacional (Ativo, Em Manutenção, Inativo).
- **Medicamentos** - itens de estoque com princípio ativo, dosagem, quantidade, unidade de medida e validade. Na prática é onde registram os remédios.
- **Suprimentos** - Materiais de apoio como EPIs, descartáveis e utensílios, com controle de quantidade, unidade e validade opcional. Por exemplo, luvas cirúrgicas, gazes, etc...

Além do controle de itens, o sistema tambem tem gerenciamento de usuários, separando dois perfis de acesso: **Médico** (somente leitura) e **Engenheiro/Administrador** (acesso completo).

Usamos JWT para autenticação e as páginas são feitas inteiramente em html e css (sem javasctipt).

---

## Como Rodar o Projeto localmente

* Primeiro crie o arquivo .env e adicione nele ALLOWED_HOSTS=localhost
```bash
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

Acesse em: `http://localhost:8000`

## Como acessar na nuvem

* Basta entrar no link abaixo:
https://diogomarassi.pythonanywhere.com/

* Depois disso, pode seguir as instruções para o usuário  abaixo

### Contas de exemplo

| Usuário | Senha | Perfil |
|---|---|---|
| admin | admin123 | Engenheiro (Superuser) |
| medico_teste | teste123 | Médico |

### Usuários

* O usuário do tipo "medico" não é capaz de editar nenhum equipamento e nem ter um controle de usuários. Isso é tarefa do "administrador/engenheiro". O segundo tipo é capaz de aditar os supreimentos do hospital e gerenciar usuários, criar novos médicos e novos admins.

* Na página inicial de login, é possivel que qualquer pessoa crie um usuário do tipo 'médico'. Porém, o usuário do tipo 'admin/engenheiro' só poderá ser criado por outro 'admin/engenheiro', por dentro do sistema, na interface de 'gerenciamento de usuarios'.

---

## Manual do Usuário

### Entrando no sistema

Ao abrir o site, você vai cair na tela de login. Digite seu usuário e senha e clique em **Acessar Sistema**.

Tente: usuario: admin e senha: Admin12345 ou usuario: medico e senha: Medico12345

Se você ainda não tem uma conta de médico, clique em **Criar conta** na tela de login e criar uma conta de 'médico'. Poderá fazer isso por dentro da conta do admin/engenheiro também.

---

### Página de Monitoramento (Dispositivos)

Essa é a página principal do sistema. Ela aparece logo após o login e mostra três seções:

- **Equipamentos** — aparelhos médicos cadastrados no sistema.
- **Medicamentos** — itens do estoque de medicamentos.
- **Suprimentos** — materiais de apoio como luvas, seringas e EPIs.

No topo da página há quatro botões com os filtros para exibição. Clicando em um deles, apenas aquela seção é exibida.

Cada item é exibido como um card com as informações principais. Usuários com perfil Médico só visualizam os itens. Usuários com perfil Engenheiro veem, além disso, os botões de Editar e Excluir em cada card, e os botões de adição no topo.

---

### Adicionando itens (apenas Engenheiro/Admin)

No topo da página de monitoramento, há três botões:

- **+ Equipamento** — abre o formulário para cadastrar um novo equipamento médico.
- **+ Medicamento** — abre o formulário de medicamento. 
- **+ Suprimento** — abre o formulário de suprimento. 

Cada um tem o próprio Forms com suas informações específicas daquela entidade. Após preencher e salvar, o sistema volta automaticamente para a página de monitoramento.

---

### Editando e excluindo itens (apenas Engenheiro/Admin)

Em cada card, os botões Editar e Excluir ficam visíveis para engenheiros. Ao clicar em Excluir, o sistema pede uma confirmação antes de apagar o item permanentemente.

---

### Gerenciamento de Usuários (apenas Engenheiro/Admin)

Na barra de navegação superior, o link "Usuários" aparece somente para engenheiros. Ao clicar, você acessa o painel de usuários, que exibe uma tabela com todos os cadastrados no sistema.

Nesse painel é possível:

- **Editar** qualquer conta : alterar nome, e-mail, usuário e perfil de acesso.
- **Excluir** qualquer conta, exceto a sua própria obviamente.
- **Criar um novo usuário** clicando em "+ Novo Usuário" : nesse formulário é possível escolher qualquer perfil, incluindo Engenheiro.

---

### Saindo do sistema

Clique no botão 'Desconectar' no canto superior direito. Isso apaga os cookies de autenticação e encerra a sessão.

---

## O que Funcionou e o que Não Funcionou

### O que funcionou

- **Controle de acesso por perfil** — médicos não conseguem acessar rotas restritas a engenheiros, nem veem os botões de ação. A proteção existe tanto no backend (via mixin) quanto no frontend (via template). Dessa forma, cada usuário tem uma tela diferente,
- **CRUD completo de Equipamentos** — criação, edição, exclusão e listagem funcionando.
- **CRUD completo de Medicamentos** — criação, edição, exclusão e listagem funcionando, com campos específicos como dosagem, unidade e validade.
- **CRUD completo de Suprimentos** — mesma estrutura, com validade opcional.- **Usuarios** - O controle de usuários funcionou perfeitamente, bem como o CRUD de usuários e a adição de um novo usuário.
- **JWT auth** - A autenticação foi corretamente implementada no sistema, o id do usuario salvo nos cookies (via access_token) de forma q é possivel acessar informações como "Nome" e exibir no cabeçalho o nome do usuário.
- **Login** - Testado e funcionando corretamente
- **Cadastro** - Testado e funcionando corretamente
- **Filtro da pagina inicial** - É possível filtrar cada tipo de 'entidade' na página inicial
- **Separação do cadastro público e do cadastro administrativo** — o formulário público (`/registrar/`) cria apenas contas de Médico. O formulário do painel admin permite criar qualquer perfil.
- **Controle de usuários** - Tem uma página funcional apenas para admins na qual é possivel administrar e visualizar todos os usuários da plataforma. Nele, tem um CRUD completo e funcional. Podemos editar, adicionar, remover e ver usuários pelo admin.

### O que não funcionou 

- **refresh token jwt** - Tudo da autenticação funciona perfeitamente, mas não salvamos o "refresh_token" pelo fato de não precisarmos de um tempo de acesso maior do que 8 horas. Ou seja, depois de 8 horas o token expira e o usuário tem que logar de novo. Isso não impacta na usabilidade, mas estamos registrando.

### O que não funcionou (não foi implementado)

- **Controle de estoque com histórico** - O que não estava no escopo do trabalho mas seria fundamental, é implementar um registro de movimentações (entradas e saídas) de itens do estoque. Para o escopo, apenas podemos editar manualmente a quantidade, o que não é tão prático.
- **Esqueci a senha** - A lógica de recuperação de senha por email não foi implementada. Tentamos usar o RESEND mas tivemos problemas e acabamos voltando atrás para não atrasar o deploy que também estava dificil e não sabiamos se podia atrasar a entrega.


