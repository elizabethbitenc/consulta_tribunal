# Descrição do projeto
 
 O objetivo do projeto é buscar informações de um determinado processo no site do tribunal e retornar alguns dados. A linguagem usada no projeto é Python e também foi utilizado o Docker. O projeto não possui testes pois infelizmente não consegui fazer. 

 ## Como instalar e executar

```
$- git clone 
$- docker compose -f "docker-compose.yml" up  --build 
```

## Como usar 
- Acessar http://localhost:5000/buscar-processo/tribunal/numero_processo

Exemplos de numeros de processos para TJAL: '0710802-55.2018.8.02.0001', '070704866.2022.8.02.0001'
Exemplos de numeros de processos para TJCE: '0070337-91.2008.8.06.0001', '0149943-95.2013.8.06.0001'