**Prática 5: Configuração de Serviços no SystemD e Controle de Versão com Git**

**Discentes:** Bruno Henrique Corrêa Bega - 14651994 & Miguel Eduardo Bressan - 14670582

**Disciplina:** SEL0337 - Projetos em Sistemas Embarcados

## Resumo do Projeto

Nesta prática, explorou-se o processo de inicialização (boot) do sistema operacional Linux embarcado na Raspberry Pi. O objetivo principal foi configurar o SystemD, o sistema de inicialização padrão do Raspbian, para gerenciar serviços personalizados.

Foram desenvolvidos scripts e criados "Unit Files" (arquivos `.service`). Esses arquivos de configuração permitiram que os programas fossem executados automaticamente assim que a placa é ligada, sem necessidade de intervenção manual ou login de usuário, utilizando o comando `systemctl` para iniciar, parar, habilitar e verificar o status desses serviços em tempo real.

Além da configuração do sistema, todo o desenvolvimento foi documentado e versionado utilizando o Git, por meio do controle de versão local e sincronização com este repositório remoto no GitHub, garantindo a integridade e o histórico das alterações do código.

## Demonstração Prática

Abaixo estão as evidências do funcionamento do projeto, incluindo a montagem física e a verificação do serviço rodando no terminal.

### 1. Montagem Prática
As fotos abaixo mostram o circuito da Raspberry Pi como também a print do terminal mostrando o comando `systemctl status` com o serviço ativo

![LED apagado quando o botão não é pressionado](https://drive.google.com/file/d/198mRkwrKa7omcWd5HLA5S1I4NTKZncu4/view?usp=sharing)

![LED acesso quando o botão é pressionado](https://drive.google.com/file/d/1c89IJZIwcXH2dzwY6cIb1dtip6BU3dhU/view?usp=sharing)

![LED acendendo com o controle PWM](https://drive.google.com/file/d/1T-2nU46veEExWUUtDy7DycGkTj3UlXbd/view?usp=sharing)
![LED apagando com o controle PWM](https://drive.google.com/file/d/1Sv0fdYbAk7HqcBIs3dtqpefdF9JGOoHd/view?usp=sharing)


