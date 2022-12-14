---
title: Exportar rango de área de impresión a HTML
type: docs
weight: 60
url: /es/java/export-print-area-range-to-html/
---
## Posibles escenarios de uso

Este es un escenario muy común en el que necesitamos exportar solo el área de impresión, es decir, el rango de celdas seleccionado en lugar de la hoja completa a HTML. Esta función ya está disponible para la representación de PDF; sin embargo, ahora también puede realizar esta tarea para HTML. Primero, configure el área de impresión en el objeto de configuración de página de la hoja de trabajo. uso posterior[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly)propiedad para exportar solo el rango seleccionado.

## Java código para exportar el rango del área de impresión a HTML

El siguiente código de muestra carga un libro de trabajo y luego exporta el área de impresión al HTML. El archivo de muestra para probar esta función se puede descargar desde el siguiente enlace:

[muestraInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

