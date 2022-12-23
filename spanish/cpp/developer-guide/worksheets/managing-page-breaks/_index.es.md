---
title: Gestión de saltos de página
type: docs
weight: 30
url: /es/cpp/managing-page-breaks/
---
{{% alert color="primary" %}} 

Según la definición, un salto de página es un lugar en un flujo de texto donde termina una página y comienza la siguiente. Microsoft Excel permite a los usuarios agregar saltos de página en cualquier celda seleccionada de una hoja de cálculo.

La ubicación de la celda donde se agrega el salto de página, la página finaliza y el resto de los datos después del salto de página se imprimen en la página siguiente durante la impresión. En palabras simples, los saltos de página dividen su hoja de trabajo en varias páginas según sus especificaciones. También puede agregar saltos de página a sus hojas de trabajo en tiempo de ejecución usando Aspose.Cells. Aspose.Cells permite a los desarrolladores agregar dos tipos de saltos de página:

- Salto de página horizontal
- Salto de página vertical

En el resto de la discusión, describiremos cómo puede agregar saltos de página horizontales o verticales en sus hojas de trabajo usando Aspose.Cells.

{{% /alert %}} 
## **Saltos de página**
 Aspose.Cells proporciona una clase[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) que representa un archivo de Excel. Él[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)colección que permite el acceso a cada hoja de trabajo en el archivo de Excel.

 Una hoja de trabajo está representada por el[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase. Él[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)La clase proporciona una amplia gama de métodos utilizados para administrar una hoja de cálculo. Para agregar los saltos de página, utilice el[Agregar saltos de página](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5f8dd5624b81e0ee2e7455f2b83380f6) metodo de la[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)clase.
### **Adición de saltos de página**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks.cpp" >}}
