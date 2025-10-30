---
title: Gestionar Saltos de Página
type: docs
weight: 30
url: /es/cpp/managing-page-breaks/
---

{{% alert color="primary" %}} 

Según la definición, un salto de página es un lugar en un flujo de texto donde una página termina y comienza la siguiente. Microsoft Excel permite a los usuarios agregar saltos de página en cualquier celda seleccionada de una hoja de cálculo.

La ubicación de la celda donde se agrega el salto de página, la página termina y todos los datos restantes después del salto de página se imprimen en la siguiente página al imprimir. En palabras simples, los saltos de página dividen tu hoja de cálculo en varias páginas según tus especificaciones. También puedes agregar saltos de página a tus hojas de cálculo en tiempo de ejecución utilizando Aspose.Cells. Aspose.Cells permite a los desarrolladores agregar dos tipos de saltos de página:

- Salto de página horizontal
- Salto de página vertical

En el resto de la discusión, describiremos cómo puedes agregar saltos de página horizontales o verticales en tus hojas de cálculo usando Aspose.Cells.

{{% /alert %}} 
## **Saltos de página**
Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) que representa un archivo de Excel. La clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) contiene una colección [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una amplia gama de métodos utilizados para gestionar una hoja de cálculo. Para agregar los saltos de página, utiliza el método [AddPageBreaks](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks) de la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).
### **Añadir Saltos de Página**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
