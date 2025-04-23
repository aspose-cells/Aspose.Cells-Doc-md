---
title: Cómo y dónde utilizar los enumeradores
linktitle: Iterar datos
type: docs
weight: 55
url: /es/net/how-and-where-to-use-enumerators/
description: Aprenda cómo y dónde utilizar los enumeradores a través de la API Aspose.Cells for .NET.
keywords: Cómo usar Enumeradores, Enumerador de celdas, Enumerador de filas, Enumerador de columnas
---

{{% alert color="primary" %}}

Un enumerador es un objeto que proporciona la capacidad de recorrer un contenedor o una colección. Los enumeradores se pueden usar para leer los datos en la colección, pero no se pueden usar para modificar la colección subyacente, mientras que IEnumerable es una interfaz que define un método GetEnumerator que devuelve una interfaz IEnumerator, esto, a su vez, permite el acceso de solo lectura a una colección.

Las API de Aspose.Cells proporcionan una serie de enumeradores, sin embargo, este artículo discute principalmente los tres tipos que se enumeran a continuación.

1. Enumerador de celdas
1. Enumerador de filas
1. Enumerador de columnas

{{% /alert %}}

## **Cómo usar Enumeradores**

### **Enumerador de celdas**

Hay diversas formas de acceder al enumerador de celdas, y se puede utilizar cualquiera de estos métodos según los requisitos de la aplicación. Aquí están los métodos que devuelven el enumerador de celdas.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Todos los métodos mencionados anteriormente devuelven el enumerador que permite recorrer la colección de celdas que han sido inicializadas.

{{% alert color="primary" %}}

Mientras se recorren las celdas, la colección no debe modificarse (operaciones que causarán una nueva celda que se instancie o celda existente que se elimine). De lo contrario, es posible que el enumerador no pueda recorrer todas las celdas correctamente (algunos elementos pueden ser recorridos repetidamente o ignorados).

{{% /alert %}}

El siguiente ejemplo de código demuestra la implementación de la interfaz IEnumerator para una colección de celdas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **Enumerador de filas**

El Enumerador de filas se puede acceder mientras se usa el método [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator). El siguiente ejemplo de código demuestra la implementación de la interfaz IEnumerator para [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **Enumerador de columnas**

El Enumerador de columnas se puede acceder mientras se usa el método [**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection). El siguiente ejemplo de código demuestra la implementación de la interfaz IEnumerator para [**ColumnCollection**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **Dónde usar Enumeradores**

Para discutir las ventajas de usar enumeradores, tomemos un ejemplo en tiempo real.

Escenario

Un requisito de la aplicación es recorrer todas las celdas en un [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) dado para leer sus valores. Podría haber varias formas de implementar este objetivo. Se demuestran algunas a continuación.

### **Usando Rango de Visualización**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **Usando MaxDataRow y MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Como puedes observar, ambos enfoques mencionados anteriormente utilizan más o menos una lógica similar; es decir, recorrer todas las celdas en la colección para leer los valores de las celdas. Esto podría ser problemático por varias razones, como se discute a continuación.

1. Las API como [**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) y [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) requieren tiempo adicional para recopilar las estadísticas correspondientes. En caso de que la matriz de datos (filas x columnas) sea grande, el uso de estas API podría imponer una penalización en el rendimiento.
1. En la mayoría de los casos, no todas las celdas en un rango dado están instanciadas. En tales situaciones, verificar cada celda en la matriz no es tan eficiente en comparación con verificar solo las celdas inicializadas.
1. Acceder a una celda en un bucle como Cells fila, columna hará que se instancien todos los objetos de celda en un rango, lo que eventualmente podría causar OutOfMemoryException.

## **Conclusión**

Con base en los hechos mencionados anteriormente, los siguientes son los posibles escenarios en los que se deben usar los enumeradores.

1. Se requiere acceso de solo lectura a la colección de celdas, es decir; el requisito es solo inspeccionar las celdas.
1. Se deben recorrer un gran número de celdas.
1. Solo se deben recorrer celdas/filas/columnas inicializadas.
{{< app/cells/assistant language="csharp" >}}
