---
title: Buscar datos
type: docs
weight: 50
url: /es/python-net/find-or-search-data/
description: Aprende cómo encontrar o buscar celdas en una hoja de cálculo que contienen datos específicos a través de la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Python para Excel, Buscar datos en Python, Buscar datos en Python, Buscar celdas que contienen una fórmula en Python, Buscar celdas que contienen una fórmula en Python, Buscar datos o fórmulas en Python utilizando FindOptions, Buscar datos o fórmulas en Python utilizando FindOptions, Buscar o buscar celdas que contienen un valor de cadena o número especificado en Python, Buscar o buscar celdas contiene datos especificados en Python
---

{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios encontrar celdas en una hoja de cálculo que contienen datos especificados.

{{% /alert %}}

## **Encontrar celdas que contienen datos especificados**

### **Usar Microsoft Excel**

Microsoft Excel permite a los usuarios encontrar celdas en una hoja de cálculo que contienen datos especificados. Si seleccionas **Editar** en el menú **Buscar** de Microsoft Excel, verás un cuadro de diálogo en el que podrás especificar el valor de búsqueda.

Aquí, estamos buscando el valor "Naranjas". Aspose.Cells también permite a los desarrolladores encontrar celdas en la hoja de cálculo que contienen valores especificados.

### **Usar Aspose.Cells**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) que representa todas las celdas en la hoja de cálculo. La colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) proporciona varios métodos para encontrar celdas en una hoja de cálculo que contienen datos especificados por el usuario. Algunos de estos métodos se discuten a continuación con más detalle.

{{% alert color="primary" %}}

Todos los métodos de búsqueda devuelven las referencias de las celdas que contienen los datos especificados.

{{% /alert %}}

## **Buscar celdas que contienen una fórmula**

Los desarrolladores pueden encontrar una fórmula especificada en la hoja de cálculo llamando al método [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) de la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Típicamente, el método [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) acepta tres parámetros:

- **qué:** El objeto que se busca. El tipo debe ser int, double, DateTime, string, bool.
- **celda_anterior:** Celda anterior con el mismo objeto. Este parámetro puede establecerse como nulo si se busca desde el inicio.
- **opciones_búsqueda:** Opciones para encontrar el objeto requerido.

Los ejemplos a continuación utilizan datos de hoja de cálculo para practicar los métodos de búsqueda:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingFormula-1.py" >}}

## **Encontrar datos o fórmulas utilizando FindOptions**

Es posible encontrar valores especificados utilizando el método [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) de la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) con varios [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions). Típicamente, el método [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) acepta los siguientes parámetros:

- **qué:**, los datos o el valor a buscar.
- **celda_anterior**, la última celda que contenía el mismo valor. Este parámetro puede establecerse como nulo al buscar desde el inicio.
- **opciones_busqueda**, las opciones de búsqueda.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingDataOrFormulasUsingFindOptions-1.py" >}}

## **Encontrar celdas que contengan un valor de cadena o número especificado**

Es posible encontrar valores de cadena especificados llamando al mismo método [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) encontrado en la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) con varios [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions).

Especifique las propiedades [**FindOptions.look_in_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_in_type/) y [**FindOptions.look_at_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_at_type/). El siguiente ejemplo de código ilustra cómo utilizar estas propiedades para encontrar celdas con varios números de cadenas al **principio** o al **centro** o al **final** de la cadena de la celda.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingStringValueOrNumber-1.py" >}}

## **Temas avanzados**
- [Encontrar celdas con estilo específico](/cells/es/python-net/find-cells-with-specific-style/)
- [Encontrar si el valor de la celda comienza con una comilla simple](/cells/es/python-net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Buscar Datos usando Valores Originales](/cells/es/python-net/search-data-using-original-values/)
{{< app/cells/assistant language="python-net" >}}
