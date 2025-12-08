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


<img src="https://github.com/Bruno1880/Pratica_5/blob/master/botao_led_apagado.jpg" alt="LED apagado quando o botão não é pressionado">

<img src="https://github.com/Bruno1880/Pratica_5/blob/master/botao_led_acesso.jpg" alt="LED acesso quando o botão é pressionado">

<img src="https://github.com/Bruno1880/Pratica_5/blob/master/controle_pwm_apagado.jpg" alt="LED apagando com o controle PWM">

<img src="https://github.com/Bruno1880/Pratica_5/blob/master/pwm_controle_acesso.jpg" alt="LED acendendo com o controle PWM">





