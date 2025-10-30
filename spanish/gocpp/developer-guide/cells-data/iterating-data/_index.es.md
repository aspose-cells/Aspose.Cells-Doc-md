---
title: Cómo y Dónde Usar Enumeradores con Golang vía C++
linktitle: Iterar datos
type: docs
weight: 55
url: /es/go-cpp/how-and-where-to-use-enumerators/
description: Aprende cómo Cómo y Dónde Usar Enumeradores mediante la API Aspose.Cells for C++.
keywords: Cómo usar Enumeradores, Enumerador de celdas, Enumerador de filas, Enumerador de columnas
---

{{% alert color="primary" %}}

Un enumerador es un objeto que proporciona la capacidad de recorrer un contenedor o colección. Los enumeradores se pueden usar para leer los datos de la colección, pero no pueden usarse para modificar la colección subyacente, mientras que IEnumerable es una interfaz que define un método GetEnumerator que devuelve una interfaz IEnumerator, lo cual permite acceso solo de lectura a una colección.

Las API de Aspose.Cells proporcionan una serie de enumeradores, sin embargo, este artículo discute principalmente los tres tipos que se enumeran a continuación.

1. Enumerador de celdas
1. Enumerador de filas
1. Enumerador de columnas

{{% /alert %}}

## **Cómo usar Enumeradores**

### **Enumerador de celdas**

Hay diversas formas de acceder al enumerador de celdas, y se puede utilizar cualquiera de estos métodos según los requisitos de la aplicación. Aquí están los métodos que devuelven el enumerador de celdas.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/range/getenumerator/)

Todos los métodos mencionados anteriormente devuelven el enumerador que permite recorrer la colección de celdas que han sido inicializadas.

{{% alert color="primary" %}}

Mientras se recorren las celdas, la colección no debe modificarse (operaciones que causarán una nueva celda que se instancie o celda existente que se elimine). De lo contrario, es posible que el enumerador no pueda recorrer todas las celdas correctamente (algunos elementos pueden ser recorridos repetidamente o ignorados).

{{% /alert %}}

El siguiente ejemplo de código demuestra la implementación de la interfaz IEnumerator para una colección de celdas.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData.go" >}}
### **Enumerador de filas**

El enumerador de filas se puede acceder al usar el método [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/rowcollection/getenumerator/). El siguiente ejemplo de código demuestra la implementación de la interfaz IEnumerator para [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-1.go" >}}
### **Obtener Columnas**

Las Columnas se pueden acceder al usar el método [**ColumnCollection.Get**](https://reference.aspose.com/cells/go-cpp/columncollection/get/). El siguiente ejemplo de código demuestra la implementación del método Get para [**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-2.go" >}}
## **Dónde usar Enumeradores**

Para discutir las ventajas de usar enumeradores, tomemos un ejemplo en tiempo real.

Escenario

Un requisito de la aplicación es recorrer todas las celdas en un [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) dado para leer sus valores. Podrían implementarse varias formas de lograr esto. Se muestran algunas a continuación.

### **Usando Rango de Visualización**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-3.go" >}}
### **Usando MaxDataRow y MaxDataColumn**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-4.go" >}}
Como puedes observar, ambos enfoques mencionados anteriormente utilizan más o menos una lógica similar; es decir, recorrer todas las celdas en la colección para leer los valores de las celdas. Esto podría ser problemático por varias razones, como se discute a continuación.

1. Las APIs como [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/cells/getmaxrow/), [**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/), [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/), [**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) y [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) requieren tiempo adicional para recopilar las estadísticas correspondientes. En caso de que la matriz de datos (filas x columnas) sea grande, usar estas APIs podría afectar el rendimiento.
1. En la mayoría de los casos, no todas las celdas en un rango dado están instanciadas. En tales situaciones, verificar cada celda en la matriz no es tan eficiente en comparación con verificar solo las celdas inicializadas.
1. Acceder a una celda en un bucle como Cells fila, columna hará que se instancien todos los objetos de celda en un rango, lo que eventualmente podría causar OutOfMemoryException.

## **Conclusión**

Con base en los hechos mencionados anteriormente, los siguientes son los posibles escenarios en los que se deben usar los enumeradores.

1. Se requiere acceso de solo lectura a la colección de celdas, es decir; el requisito es solo inspeccionar las celdas.
1. Se deben recorrer un gran número de celdas.
1. Solo se deben recorrer celdas/filas/columnas inicializadas.
