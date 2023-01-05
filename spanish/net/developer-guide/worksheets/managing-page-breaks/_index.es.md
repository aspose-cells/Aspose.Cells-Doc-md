---
title: Gestión de saltos de página
type: docs
weight: 30
url: /es/net/managing-page-breaks/
---
{{% alert color="primary" %}}

Según la definición, un salto de página es un lugar en un flujo de texto donde termina una página y comienza la siguiente. Microsoft Excel permite a los usuarios agregar saltos de página en cualquier celda seleccionada de una hoja de cálculo.

La ubicación de la celda donde se agrega el salto de página, la página finaliza y el resto de los datos después del salto de página se imprimen en la página siguiente durante la impresión. En palabras simples, los saltos de página dividen su hoja de trabajo en varias páginas según sus especificaciones. También puede agregar saltos de página a sus hojas de trabajo en tiempo de ejecución usando Aspose.Cells. Aspose.Cells permite a los desarrolladores agregar dos tipos de saltos de página:

- Salto de página horizontal
- Salto de página vertical

En el resto de la discusión, describiremos cómo puede agregar saltos de página horizontales o verticales en sus hojas de trabajo usando Aspose.Cells.

{{% /alert %}}

## **Saltos de página**

Aspose.Cells proporciona un[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase que representa un archivo de Excel. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite el acceso a cada hoja de trabajo en el archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)La clase proporciona una amplia gama de propiedades y métodos utilizados para administrar una hoja de trabajo.

 Para agregar los saltos de página, utilice el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase'[**Saltos de página horizontales**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) y[**Saltos de página verticales**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)propiedades.

 Él[**Saltos de página horizontales**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) y[**Saltos de página verticales**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)Las propiedades son colecciones que pueden contener varios saltos de página. Cada colección contiene varios métodos para administrar los saltos de página horizontales y verticales.

### **Adición de saltos de página**

 Para agregar un salto de página en una hoja de trabajo, inserte saltos de página verticales y horizontales en la celda especificada llamando al[**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) y[**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index) métodos. Cada**Agregar** El método toma el nombre de la celda donde se debe agregar el salto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

En los modos de vista previa de salto de página o vista previa de impresión, puede ver cómo funcionan estos saltos de página.

{{% /alert %}}

### **Borrar todos los saltos de página**

 Para borrar todos los saltos de página en una hoja de cálculo, llame al[**HorizontalPageBreakCollectionHorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) y[**VerticalPageBreakCollectionVerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) colecciones'[**Claro()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear)métodos.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **Eliminación de un salto de página específico**

 Para eliminar un salto de página específico, llame al[**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) y[**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat) métodos. Cada**Eliminar en**El método toma el índice del salto de página que se va a eliminar.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **Importante saber**

 cuando configuras**Ajustar a las páginas** propiedades (es decir[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) y[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) en la configuración de configuración de página, la configuración de salto de página se ve afectada, por lo que, si imprime la hoja de trabajo, la configuración de salto de página no se tiene en cuenta, aunque todavía está configurada.
