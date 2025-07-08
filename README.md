# Padrões de Projeto -  Prática 1

**Disciplina:** Qualidade de Software  
**Professor:** Anderson Gonçalves Uchôa  
---

## Projeto: Sistema de Gerenciamento de Pedidos em uma Cafeteria Digital

---

## Objetivo da Atividade

O objetivo desta atividade é aplicar três padrões de projeto fundamentais no desenvolvimento orientado a objetos. Os padrões utilizados são:

- **Factory Method**
- **Strategy**
- **Observer**

A proposta visa:

- Compreender quando e como aplicar padrões para resolver problemas recorrentes de projeto;
- Melhorar a flexibilidade e a manutenibilidade do código por meio de boas abstrações e desacoplamento entre componentes;
- Praticar a modelagem e implementação orientada a objetos em Python, respeitando princípios como SRP e OCP (Princípios SOLID).

---

## Contexto do Problema

Você foi contratado para desenvolver um sistema de pedidos online para uma cafeteria artesanal, que está modernizando seu atendimento. A cafeteria oferece diversos produtos (cafés, chás, doces) com possibilidade de personalização (adicionais, tamanhos, embalagens ecológicas).
O gerente deseja um sistema modular, que permita:
- Cadastrar e preparar diferentes tipos de bebidas;
- Oferecer diferentes estratégias de desconto (ex: fidelidade, horário promocional);
- Enviar notificações automatizadas (para cozinha, cliente, e histórico do pedido).
Como o cardápio muda com frequência, e novas promoções são lançadas a cada semana, o sistema deve ser flexível e fácil de manter.
