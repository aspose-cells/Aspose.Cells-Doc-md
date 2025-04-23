---
title: Cómo y dónde usar iteradores
linktitle: Iterar datos
type: docs
weight: 640
url: /es/java/how-and-where-to-use-iterators/
---

{{% alert color="primary" %}} 

Un objeto de una interfaz de iterador se puede utilizar para recorrer todos los elementos de una colección. Los iteradores se pueden utilizar para inspeccionar los datos en una colección, pero no se pueden utilizar para modificar la colección subyacente. En general, para usar un iterador para recorrer el contenido de una colección, se deben seguir los siguientes pasos:

1. Obtener un iterador al comienzo de la colección llamando al método iterador de la colección.
2. Configurar un bucle que haga una llamada al método hasNext. Hacer que el bucle itere siempre que el método hasNext devuelva true.
3. Dentro del bucle, obtener cada elemento llamando al método next.

Aspose.Cells APIs proporciona una variedad de iteradores, sin embargo, este artículo principalmente discute los tres tipos enumerados a continuación.

1. Iterador de Celdas
1. Iterador de Filas
1. Iterador de Columnas

{{% /alert %}} 
## **Cómo usar Iteradores**
### **Iterador de Celdas**
Existen varias formas de acceder al iterador de celdas, y se puede usar cualquiera de estos métodos según los requisitos de la aplicación. Aquí están los métodos que devuelven el iterador de celdas.

1. Cells.iterator
1. Row.iterator
1. Range.iterator

Todos los métodos mencionados anteriormente devuelven el iterador que permite recorrer la colección de celdas que han sido inicializadas.

{{% alert color="primary" %}} 

Durante el recorrido de las celdas, la colección no debe ser modificada (operaciones que provocarán que se instancie una nueva Celda o que se elimine una Celda existente). De lo contrario, el iterador puede no ser capaz de recorrer todas las celdas correctamente (algunos elementos pueden ser recorridos repetidamente o saltados).

{{% /alert %}} 

El siguiente ejemplo de código demuestra la implementación de la clase Iterator para una colección de celdas.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **Iterador de Filas**
El Iterador de Filas se puede acceder al usar el método RowCollection.iterator. El siguiente ejemplo de código demuestra la implementación del Iterador para la clase RowCollection.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **Iterador de Columnas**
El Iterador de Columnas se puede acceder al usar el método ColumnCollection.iterator. El siguiente ejemplo de código demuestra la implementación del Iterador para la clase ColumnCollection.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **Dónde usar Iteradores**
Para discutir las ventajas de usar iteradores, veamos un ejemplo en tiempo real.
##### **Escenario**
Un requisito de la aplicación es recorrer todas las celdas en una Hoja de Cálculo dada para leer sus valores. Podrían haber varias formas de implementar este objetivo. Algunas se muestran a continuación.
###### **Usando Rango de Visualización**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **Usando MaxDataRow y MaxDataColumn**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





Como puedes observar, ambos enfoques mencionados anteriormente utilizan una lógica más o menos similar, es decir; recorrer todas las celdas en la colección para leer los valores de las celdas. Esto podría ser problemático por varias razones, como se discute a continuación.

1. Las APIs como MaxRow, MaxDataRow, MaxColumn, MaxDataColumn y MaxDisplayRange requieren tiempo adicional para recopilar las estadísticas correspondientes. En caso de que la matriz de datos (filas x columnas) sea grande, usar estas APIs podría imponer una penalización en el rendimiento.
1. En la mayoría de los casos, no todas las celdas en un rango dado están instanciadas. En tales situaciones, verificar cada celda en la matriz no es tan eficiente en comparación con verificar solo las celdas inicializadas.
1. Acceder a una celda en un bucle como Cells.get(filaIndice, columnaIndice) hará que se instancien todos los objetos de celda en un rango, lo que eventualmente puede causar un OutOfMemoryError.
##### **Conclusión**
Basándose en los hechos mencionados anteriormente, a continuación se presentan los posibles escenarios donde deberían usarse los iteradores.

1. Se requiere acceso de solo lectura a la colección de celdas, es decir; la necesidad es solo inspeccionar las celdas.
1. Se deben recorrer un gran número de celdas.
1. Se deben recorrer solo celdas/filas/columnas inicializadas.
{{< app/cells/assistant language="java" >}}
