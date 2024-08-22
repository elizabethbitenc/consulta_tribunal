# Descrição do projeto
 
 O objetivo do projeto é buscar informações de um determinado processo no site do tribunal e retornar alguns dados. A linguagem usada no projeto é Python e também foi utilizado o Docker. O projeto não possui testes pois infelizmente não consegui fazer. Os frameworks usados no projeto foram o Flask e o Scrapy. 

 ## Como instalar e executar

```
$- git clone git@github.com:elizabethbitenc/consulta_tribunal.git
$- docker compose -f "docker-compose.yml" up  --build 
```

## Como usar 
- Acessar para rodar o crawler http://localhost:5000/rodar-crawler/tribunal/numero_processo
- Acessar para ver o resultado http://localhost:5000/buscar-processo/tribunal/numero_processo

Exemplos de numeros de processos para TJAL: '0710802-55.2018.8.02.0001', '070704866.2022.8.02.0001'

Exemplos de numeros de processos para TJCE: '0000267-50.2016.8.06.0201', '0070337-91.2008.8.06.0001', '0149943-95.2013.8.06.0001'