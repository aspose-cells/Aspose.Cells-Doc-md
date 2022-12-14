---
title: Excluir estilos no utilizados durante la conversión de Excel a HTML
type: docs
weight: 30
url: /es/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Excluir estilos no utilizados durante la conversión de Excel a HTML**
Microsoft Los archivos de Excel pueden contener muchos estilos sin usar. Cuando estos archivos se exportan a formato HTML, los estilos no utilizados también se exportan. Esto da como resultado un mayor tamaño del HTML de salida. Aspose.Cells para Python a través de Java admite la exclusión de estos estilos durante la conversión de archivos de Excel a HTML. Para esto, el API proporciona el[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)propiedad. Establecer el valor de[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) propiedad a**Verdadero** excluirá todos los estilos no utilizados del HTML de salida.

La siguiente captura de pantalla muestra estilos no utilizados en el archivo HTML que se eliminarán al establecer el valor de[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) propiedad a**Verdadero**.

![todo:imagen_alternativa_texto](HtmlSaveOptions-Exclude-Unused-Styles.png)

El siguiente código de ejemplo demuestra la eliminación de estilos no utilizados durante la conversión de Excel a HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
