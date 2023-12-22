---
title: Cómo y dónde utilizar los enumeradores
linktitle: Iterar datos
type: docs
weight: 55
url: /es/net/how-and-where-to-use-enumerators/
description: Aprenda cómo y dónde utilizar los enumeradores a través del Aspose.Cells for .NET API.
keywords: How to use Enumerators, Cells Enumerator, Rows Enumerator, Columns Enumerator
---
{{% alert color="primary" %}}

Un enumerador es un objeto que brinda la capacidad de atravesar un contenedor o una colección. Los enumeradores se pueden usar para leer los datos de la colección, pero no se pueden usar para modificar la colección subyacente, mientras que IEnumerable es una interfaz que define un método GetEnumerator que devuelve una interfaz IEnumerator, esto, a su vez, permite acceso de solo lectura a Una colección.

Las API Aspose.Cells proporcionan varios enumeradores; sin embargo, este artículo analiza principalmente los tres tipos que se enumeran a continuación.

1. Cells Enumerador
1. Enumerador de filas
1. Enumerador de columnas

{{% /alert %}}

##  **Cómo utilizar enumeradores**

###  **Cells Enumerador**

Hay varias formas de acceder al enumerador Cells y se puede utilizar cualquiera de estos métodos según los requisitos de la aplicación. Estos son los métodos que devuelven el enumerador de celdas.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Fila.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Rango.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Todos los métodos mencionados anteriormente devuelven el enumerador que permite recorrer la colección de celdas que se han inicializado.

{{% alert color="primary" %}}

Mientras atraviesa las celdas, la colección no debe modificarse (operaciones que provocarán la creación de una instancia de un nuevo Cell o la eliminación de un Cell existente). De lo contrario, es posible que el enumerador no pueda recorrer todas las celdas correctamente (algunos elementos pueden atravesarse repetidamente u omitirse).

{{% /alert %}}

El siguiente ejemplo de código demuestra la implementación de la interfaz IEnumerator para una colección Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

###  **Enumerador de filas**

 Se puede acceder al enumerador de filas mientras se utiliza el[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) método. El siguiente ejemplo de código demuestra la implementación de la interfaz IEnumerator para[**Colección de filas**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

###  **Enumerador de columnas**

 Se puede acceder al enumerador de columnas mientras se utiliza el[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) método. El siguiente ejemplo de código demuestra la implementación de la interfaz IEnumerator para[**Colección de columnas**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

##  **Dónde utilizar enumeradores**

Para analizar las ventajas de utilizar enumeradores, tomemos un ejemplo en tiempo real.

**Guión**

 Un requisito de la aplicación es atravesar todas las celdas en un determinado[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)para leer sus valores. Podría haber varias formas de implementar este objetivo. Algunos se demuestran a continuación.

###  **Usando el rango de visualización**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

###  **Usando MaxDataRow y MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Como puede observar, ambos enfoques mencionados anteriormente utilizan una lógica más o menos similar, es decir; recorra todas las celdas de la colección para leer los valores de las celdas. Esto podría resultar problemático por varias razones, como se analiza a continuación.

1.  API como[**fila máxima**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**Fila de datos máx.**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**Columna máxima**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**Columna de datos máx.**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**Rango máximo de visualización**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)requieren más tiempo para recopilar las estadísticas correspondientes. En caso de que la matriz de datos (filas x columnas) sea grande, el uso de estas API podría imponer una penalización en el rendimiento.
1. En la mayoría de los casos, no se crean instancias de todas las celdas de un rango determinado. En tales situaciones, verificar cada celda de la matriz no es tan eficiente en comparación con verificar solo las celdas inicializadas.
1. Acceder a una celda en un bucle como Cells fila, columna hará que se creen instancias de todos los objetos de celda en un rango, lo que eventualmente puede causar OutOfMemoryException.

##  **Conclusión**

Con base en los hechos mencionados anteriormente, los siguientes son los posibles escenarios en los que se deben utilizar enumeradores.

1. Se requiere acceso de sólo lectura a la colección de células, es decir; el requisito es inspeccionar únicamente las celdas.
1. Se debe atravesar un gran número de celdas.
1. Sólo se recorrerán las celdas/filas/columnas inicializadas.
