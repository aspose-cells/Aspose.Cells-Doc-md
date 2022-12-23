---
title: Excluir estilos no utilizados durante la conversión de Excel a HTML
type: docs
weight: 30
url: /es/net/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Posibles escenarios de uso**

Microsoft El archivo de Excel puede contener muchos estilos sin usar. Cuando exporta el archivo de Excel al formato HTML, estos estilos no utilizados también se exportan. Esto puede aumentar el tamaño de HTML. Puede excluir los estilos no utilizados durante la conversión del archivo de Excel a HTML usando el[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) propiedad. cuando lo configuras**verdadero**, todos los estilos no utilizados se excluyen de la salida HTML. La siguiente captura de pantalla muestra un estilo no utilizado de muestra dentro de la salida HTML.

![todo:imagen_alternativa_texto](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Excluir estilos no utilizados durante la conversión de Excel a HTML**

El siguiente código de ejemplo crea un libro de trabajo y también crea un estilo con nombre no utilizado. Desde el[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) se establece en**verdadero** , este estilo con nombre no utilizado no se exportará a[salida HTML](61767778.zip) . Pero si lo configuras en**falso**, entonces este estilo no utilizado estará presente dentro de la salida HTML que luego puede ver en el marcado HTML como se muestra en la captura de pantalla anterior.

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExcludeUnusedStylesInExcelToHTML.cs" >}}
