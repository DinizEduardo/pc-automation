# day-to-day

## Descrição

Este script automatizado tem a finalidade de registrar os programas que estão abertos em seu computador a cada minuto e salvar esses dados em um arquivo Excel para fins de monitoramento e análise.

## Funcionalidades

- **Leitura Periódica**: O script lê a cada minuto qual aplicativo está com foco no momento e salva essas informações no excel.

- **Registro em Excel**: Script responsavel por compilar as informações do dia anterior e começar a salvar o dia atual. 

## Configurando

Para fazer com que o script seja rodado assim que o computador ligar basta executar o script `configurar.bat`. Esse script irá fazer a seguinte configuração:
1. Irá criar um atalho para o script de leitura periodica
2. Colocará o atalho do arquivo dentro da pasta de startup do windows

Com isso você já conseguirá gerar informações constantes sobre o seu uso do computador.

## Estrutura do Arquivo Excel

O arquivo Excel gerado terá a seguinte estrutura:

| Timestamp           | Programa em Execução |
|---------------------|----------------------|
| 2023-09-11 12:00:00 | Google Chrome        |
| 2023-09-11 12:01:00 | Visual Studio Code   |
| 2023-09-11 12:02:00 | Spotify              |

## Analise de dados

A analise de dados poderá ser feita de diversas formas, mas inicialmente iremos compilar todos os dias os 10 programas mais usados no determinado dia

## Contribuições

Se você deseja melhorar este script ou adicionar recursos adicionais, sinta-se à vontade para abrir um pull request. Contribuições são bem-vindas!

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE). Sinta-se à vontade para usá-lo e modificá-lo de acordo com suas necessidades.

## Contato

Se você tiver alguma pergunta ou precisar de assistência com o script, não hesite em entrar em contato em `eduardo.diniz987@gmail.com`.
