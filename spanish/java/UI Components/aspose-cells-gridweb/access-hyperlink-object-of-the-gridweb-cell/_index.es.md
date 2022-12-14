---
title: Acceder al objeto Hipervínculo de GridWeb Cell
type: docs
weight: 60
url: /es/java/access-hyperlink-object-of-the-gridweb-cell/
---
## **Posibles escenarios de uso**
Puede verificar si la celda contiene un hipervínculo o no utilizando los siguientes dos métodos. Estos métodos devolverán un valor nulo si la celda no contiene un hipervínculo y, si contiene un hipervínculo, devolverá el objeto GridHyperlink.

- GridHyperlinkCollection.getHyperlink (celda GridCell)
- GridHyperlinkCollection.getHyperlink(int fila,int columna)
## **Abrir hipervínculo en una ventana nueva o existente**
 Si su archivo de Excel contiene un hipervínculo que se vincula a alguna URL como<http://wwww.aspose.com/> y lo carga en GridWeb, los hipervínculos se representarán con el atributo de destino establecido en_ vacío. Significa que cuando haga clic en el hipervínculo en una celda de GridWeb, se abrirá en una nueva ventana en lugar de la ventana existente. Además, si desea abrir el hipervínculo en la ventana existente, configure GridHyperlink.Target en_uno mismo.
## **Acceder al objeto Hipervínculo de GridWeb Cell**
El siguiente código de ejemplo tiene acceso al hipervínculo de la celda A1. Si la celda A1 contiene un hipervínculo, devolverá el objeto GridHyperlink; de lo contrario, devolverá un valor nulo.
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}
