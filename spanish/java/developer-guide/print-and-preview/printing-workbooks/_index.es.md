---
title: Impresión de libros de trabajo
type: docs
weight: 20
url: /es/java/printing-workbooks/
description: Cómo imprimir hojas de trabajo y libros de trabajo usando Java. Este artículo proporciona el código Java para imprimir hojas de trabajo y libros de trabajo utilizando la API Aspose.Cells for Java.
keywords: impresión de libros de trabajo, impresión de hojas de trabajo, impresión de hojas de libros de trabajo, impresión de un libro de trabajo, impresión de libro de trabajo en Java, impresión de hojas de trabajo en Java, impresión de libro de trabajo de Excel en Java, imprimir hoja de Excel en Java, imprimir libro de trabajo, imprimir hoja de trabajo
---

{{% alert color="primary" %}}

Este documento está diseñado para brindar a los desarrolladores una comprensión (de manera compacta) de cómo imprimir hojas de cálculo.

{{% /alert %}}

## Escenario de uso

Después de terminar de crear su hoja de cálculo, probablemente querrá imprimir una copia impresa de la hoja para sus necesidades. Al imprimir, MS Excel asume que desea imprimir toda el área de la hoja de trabajo a menos que especifique su selección. La siguiente captura de pantalla muestra el cuadro de diálogo para imprimir un libro de trabajo con Excel.

![todo:image_alt_text](printing-workbooks_1.png)

**Figura:** Cuadro de diálogo de impresión

## Impresión de libros de trabajo usando Aspose.Cells

Aspose.Cells for Java proporciona un método [**toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)) de la clase [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender). Al utilizar el método [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)), puede proporcionar el nombre de la impresora, así como el nombre del trabajo de impresión.

## Código de Muestra

### Imprimir hoja de trabajo seleccionada

El siguiente fragmento de código demuestra el uso del método [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)) para imprimir su hoja de trabajo seleccionada.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### Imprimir todo el libro de trabajo

También puede usar el método [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String)) para imprimir el libro de trabajo completo. El siguiente fragmento de código demuestra el uso del método [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String)) para imprimir el libro de trabajo completo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## Artículos relacionados

- [Especificar nombre de trabajo o documento al imprimir con Aspose.Cells](/cells/es/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
