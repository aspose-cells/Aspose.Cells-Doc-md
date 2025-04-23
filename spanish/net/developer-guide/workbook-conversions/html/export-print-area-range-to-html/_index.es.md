---
title: Exportar rango de área de impresión a HTML
type: docs
weight: 60
url: /es/net/export-print-area-range-to/
---

## **Escenarios de uso posibles**

Este es un escenario común donde necesitamos exportar solo el área de impresión, es decir, el rango seleccionado de celdas en lugar de toda la hoja a HTML. Esta funcionalidad ya está disponible para la representación de PDF, sin embargo, ahora puede realizar esta tarea también para HTML. Primero configure el área de impresión en el objeto de configuración de página de la hoja de cálculo. Más adelante, utilice la bandera [**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) para exportar solo el rango seleccionado.

## Código de Muestra

El siguiente código de muestra carga un libro de trabajo y luego exporta el área de impresión al HTML. Puede descargar el archivo de muestra para probar esta característica desde el siguiente enlace:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
