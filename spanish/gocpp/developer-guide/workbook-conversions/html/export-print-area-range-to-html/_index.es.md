---
title: Exportar rango de área de impresión a HTML con Golang a través de C++
linktitle: Exportar rango de área de impresión a HTML
type: docs
weight: 60
url: /es/go-cpp/export-print-area-range-to/
description: Aprenda cómo exportar el rango del área de impresión a HTML usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Este es un escenario común donde necesitamos exportar solo el área de impresión, es decir, un rango seleccionado de celdas, en lugar de toda la hoja a HTML. Esta función ya está disponible para renderizado en PDF; sin embargo, ahora también puede realizar esta tarea en HTML. Primero, configure el área de impresión en el objeto de configuración de página de la hoja. Luego, use la bandera [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportprintareaonly/) para exportar solo el rango seleccionado.

## **Código de muestra**

El siguiente código de ejemplo carga un libro y luego exporta el área de impresión a HTML. El archivo de prueba para esta función se puede descargar desde el siguiente enlace:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportPrintAreaRangeToHtml.go" >}}
