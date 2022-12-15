---
title: Cómo y dónde usar enumeradores
linktitle: iterar datos
type: docs
weight: 55
url: /es/net/how-and-where-to-use-enumerators/
---
{{% alert color="primary" %}}

Un enumerador es un objeto que proporciona la capacidad de recorrer un contenedor o una colección. Los enumeradores se pueden usar para leer los datos en la colección, pero no se pueden usar para modificar la colección subyacente, mientras que IEnumerable es una interfaz que define un método GetEnumerator que devuelve una interfaz IEnumerator, esto, a su vez, permite el acceso de solo lectura a Una colección.

Las API Aspose.Cells proporcionan una serie de enumeradores; sin embargo, este artículo analiza principalmente los tres tipos que se enumeran a continuación.

1. Cells enumerador
1. Enumerador de filas
1. Enumerador de columnas

{{% /alert %}}

## **Cómo usar enumeradores**

### **Cells enumerador**

Hay varias formas de acceder al Enumerador Cells, y uno puede usar cualquiera de estos métodos según los requisitos de la aplicación. Estos son los métodos que devuelven el enumerador de celdas.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Fila.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Todos los métodos mencionados anteriormente devuelven el enumerador que permite recorrer la colección de celdas que se han inicializado.

{{% alert color="primary" %}}

Al atravesar las celdas, la colección no debe modificarse (operaciones que harán que se cree una instancia de un nuevo Cell o que se elimine un Cell existente). De lo contrario, es posible que el enumerador no pueda recorrer todas las celdas correctamente (algunos elementos pueden recorrerse repetidamente u omitirse).

{{% /alert %}}

El siguiente ejemplo de código muestra la implementación de la interfaz IEnumerator para una colección Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **Enumerador de filas**

 Se puede acceder al enumerador de filas mientras se usa el[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) método. El siguiente ejemplo de código demuestra la implementación de la interfaz IEnumerator para[**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **Enumerador de columnas**

 Se puede acceder al enumerador de columnas mientras se usa el[**ColumnCollection.GetEnumeratorColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) método. El siguiente ejemplo de código demuestra la implementación de la interfaz IEnumerator para[**ColumnCollection**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **Dónde usar enumeradores**

Para discutir las ventajas de usar enumeradores, tomemos un ejemplo en tiempo real.

**Guión**

 Un requisito de la aplicación es recorrer todas las celdas en un determinado[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)para leer sus valores. Podría haber varias formas de implementar este objetivo. Algunos se muestran a continuación.

### **Uso del rango de visualización**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **Uso de MaxDataRow y MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Como puede observar, los dos enfoques mencionados anteriormente utilizan una lógica más o menos similar, es decir; recorra todas las celdas de la colección para leer los valores de las celdas. Esto podría ser problemático por varias razones, como se analiza a continuación.

1.  API como[**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**MaxColumna**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)requieren tiempo adicional para recopilar las estadísticas correspondientes. En caso de que la matriz de datos (filas x columnas) sea grande, el uso de estas API podría imponer una penalización en el rendimiento.
1. En la mayoría de los casos, no se instancian todas las celdas en un rango dado. En tales situaciones, verificar cada celda de la matriz no es tan eficiente en comparación con verificar solo las celdas inicializadas.
1. Acceder a una celda en un bucle como Cells fila, columna hará que se creen instancias de todos los objetos de celda en un rango, lo que eventualmente puede causar OutOfMemoryException.

## **Conclusión**

Sobre la base de los hechos mencionados anteriormente, los siguientes son los posibles escenarios en los que se deben utilizar enumeradores.

1. Se requiere acceso de solo lectura de la colección de celdas, es decir; el requisito es solo inspeccionar las celdas.
1. Se va a atravesar un gran número de celdas.
1. Solo se recorrerán las celdas/filas/columnas inicializadas.
