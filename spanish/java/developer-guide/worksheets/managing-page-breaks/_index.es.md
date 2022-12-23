---
title: Gestión de saltos de página
type: docs
weight: 30
url: /es/java/managing-page-breaks/
---
{{% alert color="primary" %}}

Un salto de página es un lugar en el texto donde termina una página y comienza la siguiente. Microsoft Excel puede agregar saltos de página en cualquier celda seleccionada en una hoja de trabajo.
La página termina en la celda donde se agrega el salto de página y todos los datos después del salto de página se imprimen en la página siguiente. En palabras simples, los saltos de página dividen las hojas de trabajo en varias páginas. También es posible agregar saltos de página a las hojas de trabajo en tiempo de ejecución usando Aspose.Cells. Aspose.Cells admite dos tipos de saltos de página:

- horizontal
- vertical.

Este artículo describe cómo agregar saltos de página horizontales o verticales en las hojas de trabajo usando Aspose.Cells.

{{% /alert %}}

## **Aspose.Cells y saltos de página**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Excel. Él[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)que permite el acceso a cada hoja de trabajo en el archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)clase que proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo. Para agregar los saltos de página, utilice el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase'[**Saltos de página horizontales**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) y[**Saltos de página verticales**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)propiedades.

 Él[**Saltos de página horizontales**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) y[**Saltos de página verticales**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)Las propiedades son, de hecho, colecciones que pueden contener varios saltos de página. Cada colección contiene varios métodos para administrar los saltos de página horizontales y verticales. A continuación se explica cómo se utilizan estos métodos.

## **Adición de saltos de página**

 Para agregar un salto de página en una hoja de trabajo, inserte saltos de página verticales y horizontales en la celda especificada llamando al[**Saltos de página horizontales**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) y[**Saltos de página verticales**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) colecciones'**Agregar** métodos. Cada**Agregar**El método toma el nombre de la celda donde se agregará el salto de página.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

En los modos de vista previa de salto de página o vista previa de impresión, puede ver cómo funcionan estos saltos de página.

{{% /alert %}}

## **Borrar todos los saltos de página**

 Para borrar todos los saltos de página en una hoja de cálculo, llame al[**HorizontalPageBreakCollectionHorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) y[**VerticalPageBreakCollectionVerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) colecciones'**Claro**métodos.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **Eliminación de un salto de página específico**

 Para eliminar un salto de página específico en la hoja de trabajo, llame al[**HorizontalPageBreakCollectionHorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) y[**VerticalPageBreakCollectionVerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) colecciones'**eliminar en** métodos. Cada**eliminar en**El método tomará el índice del salto de página para ser eliminado.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**Importante saber** : cuando configura las propiedades de ajuste a la página (es decir,[**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) y[**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)) en la configuración de configuración de página, la configuración de salto de página se ve afectada, por lo que, si imprime la hoja de trabajo, la configuración de salto de página no se tiene en cuenta, aunque todavía existe en el archivo.

{{% /alert %}}
