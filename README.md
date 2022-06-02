# AStarAlgorithm

## To do

1. Obter o estado objetivo e guardar para comparação[v];
2. Em Nó, adicionar função para expandir nó "expandir", calcular h, incrementar g(g do pai mais + 1, quando o pai for diferente de null), movimentar(chamar as funções andar_cima, andar_baixo, andar_esquerda e andar_direita) e adicionar os nos expandidos na borda[v];
3. Em Nó, adicionar função "mostrar_resultado" para mostrar ações até chegar no resultado[v];
4. Em Border, criar função para adicionar nós "adicionar_no", não inserir nós repetidos, ou seja, os nós que estão no atributo "explorados"[v];
5. Em Border, criar função "adicionar_no_explorado" para adicionar o nós a lista "explorados"[v];
6. Em Border, criar função "obter_no_resultado" que retorna o primeiro nó em que a matrix é igual ao estado objetivo[v];
7. Em Border, criar função "tem_no_resultado" para verificar se algum nó na borda tem a matriz igual ao estado objetivo e retornar um valor boleano[v];
8. Em Border, criar função "obter_primeiro_no" para remover e retornar o primeiro nó(folha)[v];
9. Em Border, criar atributo "qtd" para retornar a quantidade de nós expandios[v];
10. Na main, seguir o seguinte raciocínio[v]:
     
     ```py
    no_raiz = Node()#no raiz
    no_raiz.expandir(Border)#estado inicial da borda
    result = None
    while(result is None and Border.qtd < 9!/2):        
       if(Border.tem_no_resultado() == true):
          result = Border.obter_no_resultado()
       else:
         primeiro_no = Border.obter_primeiro_no()
         primeiro_no.expandir(Border)

     if(result is None):
       print("sem resultado")
     else:
       result.mostrar_resultado()
```
     
