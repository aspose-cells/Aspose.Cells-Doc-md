---
title: Ajustar automáticamente columnas y filas al cargar HTML en el libro de trabajo con Golang vía C++
linktitle: Ajustar automáticamente columnas y filas al cargar HTML en el libro de trabajo
type: docs
weight: 120
url: /es/go-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Aprenda cómo ajustar automáticamente columnas y filas al cargar HTML en un libro de trabajo usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Puedes ajustar automáticamente columnas y filas al cargar tu archivo HTML dentro del objeto Workbook. Por favor, establece la propiedad [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) en **true** para este propósito.

## **Ajustar automáticamente columnas y filas al cargar HTML en el libro de trabajo**

El siguiente código de muestra primero carga el HTML de muestra en el Libro de trabajo sin ninguna opción de carga y lo guarda en formato XLSX. Luego carga nuevamente el HTML de muestra en el Libro de trabajo pero esta vez, carga el HTML después de establecer la propiedad [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) a **true** y lo guarda en formato XLSX. Por favor, descarga ambos los archivos de excel de salida es decir. [Archivo de Excel de Salida Sin AjusteAutomáticoColsYFilas](outputWithout_AutoFitColsAndRows.xlsx) y [Archivo de Excel de Salida Con AjusteAutomáticoColsYFilas](outputWith_AutoFitColsAndRows.xlsx). La siguiente captura de pantalla muestra el efecto de la propiedad [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) en ambos archivos de excel de salida.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutofitColumnsAndRowsWhileLoadingHtmlInWorkbook.go" >}}
