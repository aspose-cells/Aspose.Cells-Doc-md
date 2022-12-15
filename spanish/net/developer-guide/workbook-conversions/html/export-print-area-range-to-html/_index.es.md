---
title: Exportar rango de área de impresión a HTML
type: docs
weight: 60
url: /es/net/export-print-area-range-to/
---
## **Posibles escenarios de uso**

 Este es un escenario común en el que necesitamos exportar solo el área de impresión, es decir, el rango de celdas seleccionado en lugar de la hoja completa a HTML. Esta función ya está disponible para la representación de PDF; sin embargo, ahora también puede realizar esta tarea para HTML. Primero configure el área de impresión en el objeto de configuración de página de la hoja de trabajo. Posteriormente, utiliza[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) marca para exportar solo el rango seleccionado.

## Código de muestra

El siguiente código de muestra carga un libro de trabajo y luego exporta el área de impresión al HTML. El archivo de muestra para probar esta función se puede descargar desde el siguiente enlace:

[muestraInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
