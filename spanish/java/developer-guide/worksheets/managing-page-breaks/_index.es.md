---
title: Gestionar Saltos de Página
type: docs
weight: 30
url: /es/java/managing-page-breaks/
---

{{% alert color="primary" %}}

Un salto de página es un lugar en el texto donde termina una página y comienza la siguiente. Microsoft Excel puede agregar saltos de página en cualquier celda seleccionada en una hoja de cálculo.
La página termina en la celda donde se agrega el salto de página y todos los datos después del salto de página se imprimen en la siguiente página. En pocas palabras, los saltos de página dividen las hojas de cálculo en varias páginas. También es posible agregar saltos de página a las hojas de cálculo en tiempo de ejecución utilizando Aspose.Cells. Aspose.Cells admite dos tipos de saltos de página:

- horizontal
- vertical.

Este artículo describe cómo agregar saltos de página horizontales o verticales en hojas de cálculo utilizando Aspose.Cells.

{{% /alert %}}

## **Aspose.Cells y Saltos de Página**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) que proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para agregar los saltos de página, utilice la propiedad [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) y [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks) de la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Las propiedades [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) y [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks) son de hecho colecciones que pueden contener varios saltos de página. Cada colección contiene varios métodos para gestionar saltos de página horizontales y verticales. Cómo se utilizan estos métodos se discute a continuación.

## **Añadir Saltos de Página**

Para agregar un salto de página en una hoja de cálculo, inserta saltos de página verticales y horizontales en la celda especificada llamando a los métodos **Agregar** de las colecciones [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) y [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection). Cada método **Agregar** toma el nombre de la celda donde se agregará el salto de página.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

En la vista preliminar de saltos de página o en la vista preliminar de impresión, puedes ver cómo funcionan los saltos de página.

{{% /alert %}}

## **Borrar Todos los Saltos de Página**

Para borrar todos los saltos de página en una hoja de cálculo, llama a los métodos **Borrar** de las colecciones [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) y [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **Eliminación de un salto de página específico**

Para eliminar un salto de página específico en la hoja de cálculo, llama a los métodos **removeAt** de las colecciones [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) y [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection). Cada método **removeAt** tomará el índice del salto de página que se va a eliminar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**Importante saber**: Cuando configures las propiedades de ajuste a página (es decir, [**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) y [**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide-) en la configuración del diseño de página), se afectarán las configuraciones de salto de página, de modo que, si imprimes la hoja, no se considerarán las configuraciones, aunque todavía existan en el archivo.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
