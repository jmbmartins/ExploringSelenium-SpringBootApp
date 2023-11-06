## Explorar o Selenium na aplicação do "Hotel para Animais" 

## Relatório -  OverLeaf

https://www.overleaf.com/2471912627fhdbwsbqtqxq#7f702a

### Principais Cenários de Teste 
- Criação, atualização e exclusão de clientes.
- Registro de animais, incluindo associação com clientes.
- Gerenciamento de quartos.
- Criação e gerenciamento de reservas.
- Associação de tipos de alimentação aos animais.
- Geração de estatísticas e relatórios.
  
## Teste de Perfil de Usuário (João) ✅
- Automatize o teste de seleção de perfil de usuário. Certifique-se de que os perfis de "Hotel Administrator" e "Customer" funcionem corretamente.

## Teste de Gerenciamento de Clientes (João)
- Automatizar testes para:
  - Registo de um cliente. ✅ 
  - Inserir dados pessoais de um cliente. **Failed (UserID and Client_Id)**
  - Atualização de detalhes de um cliente. ✅
  - Exclusão de clientes. ✅ **Failed (UserID and Client_Id)**

## Teste de Gerenciamento de Animais (Vasco)
- Automatize testes para:
  - Registro de animais com detalhes como nome, espécie, idade e raça.✅
  - Atualização de dados.✅
  - Exclusão de animais.✅

## Teste de Gerenciamento de Quartos (Rui)
- Automatize testes para:
  - Registro de informações de quartos.
  - Verificação da disponibilidade de quartos.
  - Atualização de detalhes de quartos.

## Teste de Reservas de Alojamento (João)
- Automatize testes para:
  - Criação de reservas para animais. ✅
  - Eliminar determinada reserva. ✅
  - **Negative Test Cases**: Verificação de casos particulares (Marcar para uma data que já passou, a data de check-out é anterior à de check-in). ✅

## Teste de Alimentação  (Vasco)
- Automatize testes para:
  - Associação de tipos de alimentação a animais.✅
  - Criação de reservas com base no tipo de alimentação desejado.✅

## Teste de Estatísticas e Relatórios (Rui)
- Automatize testes para gerar estatísticas e relatórios com base nas operações realizadas na aplicação.

## Estrutura do Relatório


### Introdução
- Introduzir o tema do trabalho e explicar a importância da Qualidade de Software na indústria de desenvolvimento de software.
- Apresentar o objetivo do trabalho, que é explorar a ferramenta Selenium na aplicação SpringBootApp Hotel para animais.


### Ferramenta Selenium
- Introdução detalhada à ferramenta Selenium. Explicar o que é, a sua importância na automação de testes e as suas principais características.
- Descrever os conceitos-chave relacionados à automação de testes, como seletores, testes de caixa preta, e estratégias de automação.


### Aplicação SpringBootApp Hotel para Animais
- Apresentar a aplicação SpringBootApp Hotel para animais. Explicar o seu propósito, as funcionalidades e o público-alvo.
- Descrever os principais desafios ou áreas críticas de qualidade que podem ser melhorados com automação de testes.


###  Cenários de Teste e a sua Implementação com Selenium
- Detalhar o processo de implementação dos cenários de teste com o Selenium.
- Fornecer código de exemplo, scripts ou pseudocódigos para demonstrar como os testes foram automatizados.


### Resultados e Evidências
- Apresentar os resultados dos testes realizados com o Selenium, incluindo capturas de tela ou registros de testes bem-sucedidos e falhas.
- Discutir os benefícios e desafios encontrados durante a implementação dos testes automatizados.


### Discussão e Conclusão
- Analisar os resultados à luz dos conceitos das aulas T03 a T07.
- Concluir sobre a eficácia da automação de testes usando o Selenium na melhoria da qualidade de software da aplicação SpringBootApp Hotel para animais.
