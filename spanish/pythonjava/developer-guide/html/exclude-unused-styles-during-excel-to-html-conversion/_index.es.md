---
title: Excluir estilos no utilizados durante la conversión de Excel a HTML
type: docs
weight: 30
url: /es/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Excluir estilos no utilizados durante la conversión de Excel a HTML**
Microsoft Los archivos de Excel pueden contener muchos estilos sin usar. Cuando estos archivos se exportan al formato HTML, los estilos no utilizados también se exportan. Esto da como resultado un mayor tamaño de la salida HTML. Aspose.Cells for Python via Java admite la exclusión de estos estilos durante la conversión del archivo de Excel a HTML. Para esto, el API proporciona la[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)propiedad. Establecer el valor de[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) propiedad a**Verdadero** excluirá todos los estilos no utilizados de la salida HTML.

La siguiente captura de pantalla muestra estilos no utilizados en el archivo HTML que se eliminarán al establecer el valor de[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) propiedad a**Verdadero**.

![todo:imagen_alternativa_texto](HtmlSaveOptions-Exclude-Unused-Styles.png)

El siguiente código de ejemplo muestra la eliminación de estilos no utilizados durante la conversión de Excel a HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
