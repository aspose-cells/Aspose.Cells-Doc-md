---
title: Excel con estilo de borde no compatible a HTML
type: docs
weight: 80
url: /es/python-java/excel-with-unsupported-border-style-to/
---

## **Excel con estilo de borde no compatible a HTML**
Microsoft Excel admite ciertos tipos de bordes discontinuos que no son compatibles con los navegadores web. Cuando dichos archivos se convierten a HTML utilizando Aspose.Cells, esos bordes se eliminan. Sin embargo, Aspose.Cells para Python via Java admite mostrar bordes similares con la propiedad [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle). Puede establecer el valor de la propiedad [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) a **Verdadero** para exportar los bordes no compatibles.

El siguiente código de ejemplo carga el [archivo de Excel de muestra](sampleExportSimilarBorderStyle.xlsx) que contiene algunos bordes no compatibles como se muestra en la siguiente captura de pantalla. La captura de pantalla ilustra aún más el efecto de la propiedad [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) dentro de [HTML de salida](outputExportSimilarBorderStyle.zip).

![todo:image_alt_text](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
