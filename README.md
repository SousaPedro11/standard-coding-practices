# Standard-Coding-Practices

O objetivo deste repositório é documentar as **melhores práticas de codificação** a serem seguidas no projeto. Tudo
baseado em princípios de codigicação amplamente difundidos.

## Tabela de Conteúdos

- [Standard-Coding-Practices](#standard-coding-practices)
  - [Tabela de Conteúdos](#tabela-de-conteúdos)
  - [Princípios](#princípios)
    - [Clean Code](#clean-code)
    - [SOLID](#solid)
    - [Design Pattern](#design-pattern)
      - [Formato](#formato)
      - [Classificação](#classificação)
    - [DRY](#dry)
    - [KISS](#kiss)
  - [Análise de Qualidade de Código](#análise-de-qualidade-de-código)
  - [Contribuição](#contribuição)

## Princípios

### Clean Code

_"Mesmo um código ruim pode funcionar. Mas se ele não for limpo, pode acabar com uma empresa de desenvolvimento.
Perdem-se, a cada ano, horas incontáveis e recursos importantes devido a um código mal escrito." - Robert C. "Tio Bob"
Martin_

Repositório com resumo e algumas implementações referentes ao Clean Code em Python:
[clean-code-python](https://github.com/zedr/clean-code-python)

### SOLID

SOLID é um acrônimo para 5 princípios que têm a finalidade de melhorar o design e arquitetura do código, reduzindo
complexidade e riscos de falhas. Torna o código mais legível, flexível e gerenciável.

O 5 princípios são:

- **S** - Single Responsability
- **O** - Open Closed
- **L** - Liskov Substitution
- **I** - Interface Segregation
- **D** - Dependency Inversion

Repositório com resumo e algumas implementações em Python: [solid](https://github.com/SousaPedro11/solid/)

### Design Pattern

Design Pattern surgiu a partir da análise de problemas por programadores experientes que perceberam que os mesmos
problemas começaram aparecer várias vezes e a solução para aqueles problemas eram sempre as mesmas, decidiram catalogar
tais padrões. Em meados da década de 90, quatro pessoas escreveram um livro
**_"Design Patterns: Elements of Reusable Object-Oriented Software"_** iniciando os Design Patterns que se tornou
referência neste assunto. As quatro pessoas conhecidas como Gang Of Four (GOF) são: Erich Gamma, Richard Helm, Ralph
Johnson e John Vlissides.

Nesse livro foram apresentados 23 padrões de projetos e com o passar do tempo surgiram outros aumentando o número de
padrões para a casa dos 3 dígitos, ainda assim os 23 iniciais são os mais conhecidos e utilizados.

Como são soluções típicas para padrões recorrentes em projetos de desenvolvimento de software, cada padrão é como uma
planta de uma casa para o seu código, um molde para a solução. Cada padrão pode ser e adaptado ao código, pois é um
conceito geral para resolver um problema em particular.

Com o Design Pattern você terá vários benefícios dentre eles são: código mais enxuto, limpo, organizado, aumentar a
qualidade e diminuir a complexidade do seu código.

#### Formato

Os padrões GoF possuem o seguinte formato:

- **Nome**: Identificação do padrão
- **Objetivo/Intenção**
- **Motivação**: cenário mostrando o problema e a necessidade
- **Aplicabilidade**: como identificar as situações nas quais o padrão é aplicável
- **Estrutura**: representação gráfica em diagrama de classes (UML)
- **Consequências**: vantagens e desvantagens
- **Implementações**: detalhes a serem analisados referentes a especificidade de cada linguagem
- **Usos conhecidos**
- **Padrões relacionados**

#### Classificação

Os padrões de projeto podem ser classificados de acordo com seu propósito ou intenção:

- **Padrões Criacionais**: Fornecem mecanismos para criação de objetos que aumentam a flexibilidade e reutilização do
  código.

  - **Abstract Factory**: permite que um cliente crie famílias de objetos sem especificar suas classes concretas.
  - **Builder**: encapsula a construção de um produto e permite que ele seja construído em etapas.
  - **Factory Method**: as subclasses decidem quais classes concretas serão criadas, permitindo alterar os tipos dos
    objetos.
  - **Prototype**: permite copiar objetos existentes sem fazer o código ficar dependente de suas classes.
  - **Singleton**: assegura que tenha apenas uma instância de uma determinada classe no projeto todo, enquanto provê um
    ponto de acesso global para essa instância.

- **Padrões Estruturais**: Explicam como montar objetos e classes em estruturas maiores mas ainda mantendo essas estruturas
  flexíveis e eficientes.

  - **Adapter**: permite que objetos com interfaces incompatíveis colaborem entre si.
  - **Bridge**: permite que divida uma classe grande ou conjunto de classes ligadas em duas hierarquias separadas -
    abstração e implementação - que podem ser desenvolvidas de forma independente.
  - **Composite**: permite a composição de objetos em estruturas de árvores e tratar essas estruturas como se fossem
    objetos individuais.
  - **Decorator**: acopla novos comportamentos para os objetos ao colocá-los dentro de envelopes que contém os
    comportamentos.
  - **Facade**: fornece uma interface simplificada para uma biblioteca, um framework ou conjunto complexo de classes.
  - **Flyweight**: uma instância de classes pode ser utilizada para fornecer muitas instâncias virtuais a fim de aumentar
    a quantidade de objetos na RAM disponível.
  - **Proxy**: envelopa um substitudo de um objeto para controlar o acesso ao objeto original.

- **Padrões Comportamentais**: voltados aos algoritmos e designação de responsabilidades entre objetos
  - **Chain of Responsability**: permite dar a mais de um objeto a oportunidade de processar uma solicitação.
  - **Command**: encapsula a solicitação como um objeto.
  - **Interpreter**: permite construir um intérprete para uma linguagem.
  - **Iterator**: permite percorrer elementos de uma coleção sem expor as representações dele.
  - **Mediator**: centraliza as operações complexas de comunicação e controle entre objetos a partir de um objeto
    mediador.
  - **Memento**: permite que salve e restaure o estado anterior de um objeto sem revelar os detalhes da implementação.
  - **Observer**: notifica múltiplos objetos sobre eventos que ocorram com o objeto observado.
  - **State**: permite que um objeto altere seu comportamento quando seu estado interno muda.
  - **Strategy**: permite definir uma família de algoritmos (comportamentos), em classes separadas, e faz os objetos deles
    intercambiáveis.
  - **Template Method**: as subclasses definem como implementar um comportamento sem modificar sua estrutura.
  - **Visitor**: permite acrescentar novos recursos a um composto de objetos e o encapsulamento não é importante.

Repositório com implementação em Python: [design-patterns-python](https://github.com/kelvins/design-patterns-python)

### DRY

### KISS

## Análise de Qualidade de Código

É um conjunto de técnicas que objetiva melhorar o desempenho, organização, legibilidade e segurança do projeto.

A documentação pode ser encontrada em: [Análise de Qualidade](./QA/)

## Contribuição

Esta documentação se dá por meio de exemplos de codificação simples que implementam provas de conceito. Ao implementar
novas classes no sistema este repositório deve sempre ser consultado e

1. As melhores práticas devem ser seguidas.

2. Caso você discorde ou tenha **sugestões de melhorias**, implemente e convide a equipe para conversar/demonstrar. A
   deliberação será sempre por consenso, com decisões democráticas.

3. Se você está implementando algo diferente, que não existe exemplo disponível, é oportunidade para trocar ideia com a
   equipe e **definir um novo padrão** de forma democrática, documentar aqui e depois seguir com a sua implementação, a
   partir desta chancela da equipe.
