---
title: Ajustar automáticamente columnas y filas al cargar HTML en el libro de trabajo
type: docs
weight: 120
url: /es/python-net/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Este tema le muestra cómo ajustar automáticamente columnas y filas al cargar HTML en el libro de trabajo utilizando Aspose.Cells para Python via NET.
keywords: Ajustar automáticamente columnas y filas al cargar HTML en el libro de trabajo, ajustar automáticamente columnas y filas para cargar HTML.
---

## **Escenarios de uso posibles**

Puedes ajustar automáticamente columnas y filas al cargar tu archivo HTML dentro del objeto Workbook. Por favor, establece la propiedad [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) en **true** para este propósito.

## **Ajustar automáticamente columnas y filas al cargar HTML en el libro de trabajo**

El siguiente código de muestra primero carga el HTML de muestra en el Libro de trabajo sin ninguna opción de carga y lo guarda en formato XLSX. Luego carga nuevamente el HTML de muestra en el Libro de trabajo pero esta vez, carga el HTML después de establecer la propiedad [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) a **true** y lo guarda en formato XLSX. Por favor, descarga ambos los archivos de excel de salida es decir. [Archivo de Excel de Salida Sin AjusteAutomáticoColsYFilas](outputWithout_AutoFitColsAndRows.xlsx) y [Archivo de Excel de Salida Con AjusteAutomáticoColsYFilas](outputWith_AutoFitColsAndRows.xlsx). La siguiente captura de pantalla muestra el efecto de la propiedad [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) en ambos archivos de excel de salida.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
