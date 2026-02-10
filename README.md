# Agenda em Python

Este projeto foi elaborado para permitir o aprendizado de conceitos como o padrão de projeto MVC (Model-View-Controller), framework Flask e seus componentes, variáveis de ambiente, paradigma de programação orientado a objetos e reforço de fundamentos da linguagem de programação Python.

Para implementar este projeto localmente, siga os seguintes passos:

1. Faça um fork deste repositório, clicando no botão `Fork`;

1. Clone este repositório localmente:

    ~~~bash
    git clone <url_repositorio>
    ~~~

3. Abra o projeto utilizando seu IDE de preferência;

4. Crie, preferencialmente, um ambiente virtual utilizando uma versão do Python > 3.12.10:

    ~~~bash
    python -m venv .venv
    ~~~

5. Ative seu ambiente virtual:

    No bash:

    ~~~bash
    source .venv/Scripts/activate
    ~~~

    No PowerShell:
    
    ~~~powershell
    .\.venv\Scripts\Activate.ps1
    ~~~

6. Instale todas as dependências constantes no arquivo `requirements.txt`:

    ~~~python
    pip install -r requirements.txt
    ~~~

7. Copie o arquivo `.env.example`, cole na raiz do projeto e renomeie a cópia para `.env`;

8. Edite o arquivo `.env` para definir o caminho do seu banco de dados na constante `DATABASE`. Exemplo:

    ~~~env
    DATABASE='./data/meubanco.db'
    ~~~

9. Rode a aplicação no Python utilizando o comando:

    ~~~bash
    flask run
    ~~~