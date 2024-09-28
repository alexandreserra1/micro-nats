# Projeto de Comunicação entre Microserviços com NATS e Docker

Este projeto demonstra a comunicação entre microserviços utilizando o sistema de mensagens NATS. A aplicação é composta por vários serviços que interagem entre si para gerar números, verificar se são primos ou palíndromos e, em seguida, enviar esses números para um cliente que os exibe.

## **Índice**

- [Visão Geral](#visão-geral)
- [Arquitetura](#arquitetura)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Executar](#como-executar)
- [Serviços](#serviços)
  - [service1_generator](#service1_generator)
  - [service2_prime_checker](#service2_prime_checker)
  - [service3_palindrome_checker](#service3_palindrome_checker)
  - [client_service](#client_service)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## **Visão Geral**

O objetivo principal deste projeto é demonstrar como microserviços podem se comunicar eficientemente usando o NATS como sistema de mensagens. A aplicação consiste em:

- **Gerador de Números**: Gera números aleatórios e os publica em um assunto NATS.
- **Verificador de Primos**: Recebe números, verifica se são primos e publica os números primos em outro assunto.
- **Verificador de Palíndromos**: Recebe números, verifica se são palíndromos e publica os números palíndromos em outro assunto.
- **Cliente**: Inscrito nos assuntos de números primos e palíndromos, exibe os números recebidos.


## **Pré-requisitos**

- **Docker** instalado na máquina.
- **Docker Compose** para orquestração dos contêineres.
- **Git** para clonar o repositório (opcional).

