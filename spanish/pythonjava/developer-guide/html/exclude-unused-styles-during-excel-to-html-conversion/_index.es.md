---
title: Excluir Estilos No Utilizados durante la conversión de Excel a HTML
type: docs
weight: 30
url: /es/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Excluir estilos no utilizados durante la conversión de Excel a HTML**
Los archivos de Microsoft Excel pueden contener muchos estilos no utilizados. Cuando estos archivos se exportan al formato HTML, los estilos no utilizados también se exportan. Esto resulta en un mayor tamaño del HTML de salida. Aspose.Cells para Python via Java admite excluir estos estilos durante la conversión del archivo de Excel a HTML. Para esto, la API proporciona la propiedad [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles). Establecer el valor de la propiedad [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) en **True** excluira todos los estilos no utilizados del HTML de salida.

La siguiente captura de pantalla muestra los estilos no utilizados en el archivo HTML que serán eliminados al establecer el valor de la propiedad [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) en **True**.

![todo:image_alt_text](HtmlSaveOptions-Exclude-Unused-Styles.png)

El siguiente código de ejemplo demuestra la eliminación de estilos no utilizados durante la conversión de Excel a HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
