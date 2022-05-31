# AStarAlgorithm

## To do

1. Obter o estado objetivo e guardar para comparação;
2. Em Nó, adicionar função para criar nó "cria_no", calcular h, incrementar g(g do pai mais + 1, quando o pai for diferente de null), movimentar(chamar as funções andar_cima, andar_baixo, andar_esquerda e andar_direita);
3. Em Border, criar função para adicionar nós "adicionar_no", não inserir nós repetidos, ou seja, os nós que estão no atributo "explorados";
4. Em Border, criar função "adicionar_no_explorado" para adicionar o nós a lista "explorados";
5. Em Border, criar função "obter_no_resultado" que retorna o primeiro nó em que a matrix é igual ao estado objetivo;
6. Em Border, criar função "tem_no_resultado" para verificar se algum nó na borda tem a matriz igual ao estado objetivo e retornar um valor boleano;
7. Em Nó, adicionar função "mostrar_resultado" para mostrar ações até chegar no resultado;

8. Na main, seguir o seguinte raciocínio(validar):
     
     ```py
     result = null
     do:         
       
       novo_no = Node.cria_no()
       Border.adicionar_no(novo_no)
       
       if(Border.tem_no_resultado() == true):
          result = Border.obter_no_resultado()
       else:
          Border.adicionar_no_explorado(novo_no)

     while(result is null and borda.size <= 9!) 

     if(result is null):
       print("sem resultado")
     else:
       result.mostrar_resultado()
```
     
