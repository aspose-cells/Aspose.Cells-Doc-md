---
title: Buscar datos
type: docs
weight: 50
url: /es/net/find-or-search-data/
description: Aprenda cómo encontrar o buscar celdas en una hoja de cálculo que contenga datos especificados a través de la API Aspose.Cells for .NET.
keywords: Encontrar datos, buscar datos, encontrar celdas que contengan fórmulas, buscar celdas que contengan fórmulas, encontrar datos o fórmulas usando FindOptions, buscar datos o fórmulas usando FindOptions, encontrar o buscar celdas que contengan un valor o número especificado, encontrar o buscar celdas que contengan datos especificados
---

{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios encontrar celdas en una hoja de cálculo que contienen datos especificados.

{{% /alert %}}

## **Encontrar celdas que contienen datos especificados**

### **Usar Microsoft Excel**

Microsoft Excel permite a los usuarios encontrar celdas en una hoja de cálculo que contienen datos especificados. Si seleccionas **Editar** en el menú **Buscar** de Microsoft Excel, verás un cuadro de diálogo en el que podrás especificar el valor de búsqueda.

Aquí, estamos buscando el valor "Naranjas". Aspose.Cells también permite a los desarrolladores encontrar celdas en la hoja de cálculo que contienen valores especificados.

### **Usar Aspose.Cells**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) que representa todas las celdas en la hoja de cálculo. La colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) proporciona varios métodos para encontrar celdas en una hoja de cálculo que contienen datos especificados por el usuario. Algunos de estos métodos se discuten a continuación con más detalle.

{{% alert color="primary" %}}

Todos los métodos de búsqueda devuelven las referencias de las celdas que contienen los datos especificados.

{{% /alert %}}

## **Buscar celdas que contienen una fórmula**

Los desarrolladores pueden encontrar una fórmula especificada en la hoja de cálculo llamando al método [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Típicamente, el método [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) acepta tres parámetros:

- **Objeto:** El objeto que se va a buscar. El tipo debe ser int, double, DateTime, string, bool.
- **Celda anterior:** Celda anterior con el mismo objeto. Este parámetro puede establecerse en nulo si se busca desde el principio.
- Opciones de búsqueda: Opciones para encontrar el objeto requerido.

Los ejemplos a continuación utilizan datos de hoja de cálculo para practicar los métodos de búsqueda:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **Encontrar datos o fórmulas utilizando FindOptions**

Es posible encontrar valores especificados utilizando el método [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) con varios [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions). Típicamente, el método [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) acepta los siguientes parámetros:

- **Valor de búsqueda**, los datos o valores a buscar.
- **Celda anterior**, la última celda que contenía el mismo valor. Este parámetro puede establecerse en nulo al buscar desde el principio.
- **Opciones de búsqueda**, las opciones de búsqueda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **Encontrar celdas que contengan un valor de cadena o número especificado**

Es posible encontrar valores de cadena especificados llamando al mismo método [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) encontrado en la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) con varios [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

Especifique las propiedades [**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) y [**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype). El siguiente ejemplo de código ilustra cómo utilizar estas propiedades para encontrar celdas con varios números de cadenas al **principio** o al **centro** o al **final** de la cadena de la celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **Temas avanzados**
- [Encontrar celdas con estilo específico](/cells/es/net/find-cells-with-specific-style/)
- [Encontrar si el valor de la celda comienza con una comilla simple](/cells/es/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Buscar Datos usando Valores Originales](/cells/es/net/search-data-using-original-values/)
{{< app/cells/assistant language="csharp" >}}
