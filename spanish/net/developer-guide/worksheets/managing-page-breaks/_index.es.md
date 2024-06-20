---
title: Gestionar Saltos de Página
type: docs
weight: 30
url: /es/net/managing-page-breaks/
description: Este artículo proporciona un código de ejemplo y explica cómo agregar saltos de página, borrar saltos de página o eliminar saltos de página específicos en hojas de cálculo de Excel de forma programática utilizando la API de C# o la Biblioteca .NET.
keywords: saltos de página c#, saltos de página en excel c#, borrar salto de página c#, eliminar salto de página específico c#
---

{{% alert color="primary" %}}

Según la definición, un salto de página es un lugar en un flujo de texto donde una página termina y comienza la siguiente. Microsoft Excel permite a los usuarios agregar saltos de página en cualquier celda seleccionada de una hoja de cálculo.

La ubicación de la celda donde se agrega el salto de página, la página termina y el resto de los datos después del salto de página se imprime en la siguiente página al imprimir. En pocas palabras, los saltos de página dividen su hoja de cálculo en múltiples páginas de acuerdo con sus especificaciones. También puedes agregar saltos de página a tus hojas de trabajo en tiempo de ejecución utilizando Aspose.Cells. Aspose.Cells permite a los desarrolladores agregar dos tipos de saltos de página:

- Salto de página horizontal
- Salto de página vertical

En el resto de la discusión, describiremos cómo puedes agregar saltos de página horizontales o verticales en tus hojas de cálculo usando Aspose.Cells.

{{% /alert %}}

## **Saltos de página**

Aspose.Cells proporciona una clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos utilizados para gestionar una hoja de cálculo.

Para agregar los saltos de página, utiliza las propiedades [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) y [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) de la clase,.

Las propiedades [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) y [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks) son colecciones que pueden contener varios saltos de página. Cada colección contiene varios métodos para gestionar saltos de página horizontales y verticales.

### **Añadir Saltos de Página**

Para agregar un salto de página en una hoja de cálculo, inserta saltos de página verticales y horizontales en la celda especificada llamando a los métodos [**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) y [**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index) de la clase. Cada método **Agregar** toma el nombre de la celda donde se debe agregar el salto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

En la vista preliminar de saltos de página o en la vista preliminar de impresión, puedes ver cómo funcionan los saltos de página.

{{% /alert %}}

### **Borrar Todos los Saltos de Página**

Para borrar todos los saltos de página en una hoja de cálculo, llama a los métodos [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) y [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) de las colecciones [**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **Eliminación de un salto de página específico**

Para eliminar un salto de página específico, llame a los métodos [**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) y [**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat). Cada método **RemoveAt** toma el índice del salto de página que se va a eliminar.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **Importante saber**

Cuando se establecen las propiedades **FitToPages** (es decir, [**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) y [**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) en la configuración de la página, la configuración de saltos de página se ve afectada, por lo que si imprime la hoja de cálculo, la configuración de saltos de página no se tiene en cuenta aunque esté configurada.
