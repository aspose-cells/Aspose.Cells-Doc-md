---
title: Cómo y dónde usar iteradores
linktitle: iterar datos
type: docs
weight: 640
url: /es/java/how-and-where-to-use-iterators/
---
{{% alert color="primary" %}} 

Un objeto de una interfaz de iterador se puede utilizar para recorrer todos los elementos de una colección. Los iteradores se pueden usar para inspeccionar los datos en una colección, pero no se pueden usar para modificar la colección subyacente. En general, para usar un iterador para recorrer el contenido de una colección, se deben seguir los siguientes pasos:

1. Obtenga un iterador al inicio de la colección llamando al método iterador de la colección.
1. Configure un bucle que haga una llamada al método hasNext. Haga que el bucle se repita siempre que el método hasNext devuelva verdadero.
1. Dentro del bucle, obtenga cada elemento llamando al siguiente método.

Las API Aspose.Cells proporcionan un montón de iteradores, sin embargo, este artículo analiza principalmente los tres tipos que se enumeran a continuación.

1. Cells iterador
1. Iterador de filas
1. Iterador de columnas

{{% /alert %}} 
## **Cómo usar iteradores**
### **Cells iterador**
Hay varias formas de acceder al iterador de celdas, y uno puede usar cualquiera de estos métodos según los requisitos de la aplicación. Estos son los métodos que devuelven el iterador de las celdas.

1. Cells.iterator
1. Fila.iterador
1. Rango.iterador

Todos los métodos mencionados anteriormente devuelven el iterador que permite recorrer la colección de celdas que se han inicializado.

{{% alert color="primary" %}} 

Al atravesar las celdas, la colección no debe modificarse (operaciones que harán que se cree una instancia de un nuevo Cell o que se elimine un Cell existente). De lo contrario, es posible que el iterador no pueda recorrer todas las celdas correctamente (algunos elementos pueden recorrerse repetidamente u omitirse).

{{% /alert %}} 

El siguiente ejemplo de código demuestra la implementación de la clase Iterator para una colección de celdas.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **Iterador de filas**
Se puede acceder al iterador de filas mientras se usa el método RowCollection.iterator. El siguiente ejemplo de código muestra la implementación de la clase Iterator for RowCollection.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **Iterador de columnas**
Se puede acceder al iterador de columnas mientras se usa el método ColumnCollection.iterator. El siguiente ejemplo de código muestra la implementación de la clase Iterator for ColumnCollection.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **Dónde usar iteradores**
Para discutir las ventajas de usar iteradores, tomemos un ejemplo en tiempo real.
##### **Guión**
Un requisito de la aplicación es recorrer todas las celdas de una hoja de trabajo determinada para leer sus valores. Podría haber varias formas de implementar este objetivo. Algunos se muestran a continuación.
###### **Uso del rango de visualización**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **Uso de MaxDataRow y MaxDataColumn**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





Como puede observar, los dos enfoques mencionados anteriormente utilizan una lógica más o menos similar, es decir; recorra todas las celdas de la colección para leer los valores de las celdas. Esto podría ser problemático por varias razones, como se analiza a continuación.

1. Las API como MaxRow, MaxDataRow, MaxColumn, MaxDataColumn y MaxDisplayRange requieren más tiempo para recopilar las estadísticas correspondientes. En caso de que la matriz de datos (filas x columnas) sea grande, el uso de estas API podría penalizar el rendimiento.
1. En la mayoría de los casos, no se instancian todas las celdas en un rango dado. En tales situaciones, verificar cada celda de la matriz no es tan eficiente en comparación con verificar solo las celdas inicializadas.
1. Acceder a una celda en un bucle como Cells.get(rowIndex, columnIndex) hará que se creen instancias de todos los objetos de celda en un rango, lo que eventualmente puede causar OutOfMemoryError.
##### **Conclusión**
Con base en los hechos mencionados anteriormente, a continuación se muestran los posibles escenarios en los que se deben usar los iteradores.

1. Se requiere acceso de solo lectura de la colección de celdas, es decir; El requisito es solo inspeccionar las celdas.
1. Se va a atravesar un gran número de celdas.
1. Solo se deben recorrer las celdas/filas/columnas inicializadas.
