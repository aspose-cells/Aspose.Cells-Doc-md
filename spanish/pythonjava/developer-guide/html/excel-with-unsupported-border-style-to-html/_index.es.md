---
title: Excel con estilo de borde no compatible con HTML
type: docs
weight: 80
url: /es/python-java/excel-with-unsupported-border-style-to/
---
## **Excel con estilo de borde no compatible con HTML**
Microsoft Excel admite algún tipo de bordes discontinuos que no son compatibles con los navegadores web. Cuando dichos archivos se convierten a HTML usando Aspose.Cells, esos bordes se eliminan. Sin embargo, Aspose.Cells para Python a través de Java admite la visualización de bordes similares con[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)propiedad. Puede establecer el valor de[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) propiedad a**Verdadero**para exportar bordes no admitidos.

El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](sampleExportSimilarBorderStyle.xlsx)que contiene algunos bordes no admitidos, como se muestra en la siguiente captura de pantalla. La captura de pantalla ilustra aún más el efecto de[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)propiedad dentro de la[HTML de salida](outputExportSimilarBorderStyle.zip).

![todo:imagen_alternativa_texto](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
