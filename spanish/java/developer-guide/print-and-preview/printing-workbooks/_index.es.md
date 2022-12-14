---
title: Impresión de libros de trabajo
type: docs
weight: 20
url: /es/java/printing-workbooks/
description: Cómo imprimir hojas de trabajo y libros de trabajo usando Java. Este artículo proporciona el código Java para imprimir hojas de trabajo y libros de trabajo usando Aspose.Cells for Java API.
keywords: printing workbooks, printing worksheets, printing workbook sheets, printing a workbook, printing workbook java, printing worksheets java, printing excel workbook java, print excel worksheet java, print workbook, print worksheet
---
{{% alert color="primary" %}}

Este documento está diseñado para proporcionar a los desarrolladores una comprensión (de manera compacta) sobre cómo imprimir hojas de cálculo.

{{% /alert %}}

## Escenario de uso

Después de que termine de crear su hoja de cálculo, probablemente querrá imprimir una copia impresa de la hoja para su necesidad. Cuando está imprimiendo, MS Excel asume que desea imprimir el área completa de la hoja de trabajo a menos que especifique su selección. La siguiente captura de pantalla muestra el cuadro de diálogo para imprimir el libro de trabajo con Excel.

![todo:imagen_alternativa_texto](printing-workbooks_1.png)

**Figura:** Imprimir cuadro de diálogo

## Impresión de libros de trabajo usando Aspose.Cells

 Aspose.Cells for Java proporciona un[**aImpresora**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String) ) método de la[**HojaRenderizar**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) clase. Al usar el[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)), puede proporcionar el nombre de la impresora y el nombre del trabajo de impresión.

## Código de muestra

### Imprimir hoja de trabajo seleccionada

El siguiente fragmento de código demuestra el uso de la[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)) para imprimir la hoja de trabajo seleccionada.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### Imprimir todo el libro de trabajo

 También puede utilizar el[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String) ) para imprimir todo el libro de trabajo. El siguiente fragmento de código demuestra el uso de la[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String)) para imprimir todo el libro de trabajo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## Artículos relacionados

- [Especifique el nombre del trabajo o del documento al imprimir con Aspose.Cells](/cells/es/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
