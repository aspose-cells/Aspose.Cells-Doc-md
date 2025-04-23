---
title: Excluir Estilos No Utilizados durante la conversión de Excel a HTML
type: docs
weight: 30
url: /es/python-net/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Escenarios de uso posibles**

Un archivo de Microsoft Excel puede contener muchos estilos no utilizados. Cuando exportas el archivo de Excel a formato HTML, estos estilos no utilizados también se exportan. Esto puede incrementar el tamaño del HTML. Puedes excluir los estilos no utilizados durante la conversión del archivo de Excel a HTML usando la propiedad [**HtmlSaveOptions.exclude_unused_styles**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/exclude_unused_styles). Cuando la estableces como **true**, todos los estilos no utilizados son excluidos del HTML de salida. La siguiente captura de pantalla muestra un estilo no utilizado de muestra dentro del HTML de salida.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Excluir estilos no utilizados durante la conversión de Excel a HTML**

El siguiente código de muestra crea un libro de trabajo y también crea un estilo con nombre no utilizado. Dado que el [**HtmlSaveOptions.exclude_unused_styles**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/exclude_unused_styles) se establece en **verdadero**, este estilo con nombre no utilizado no se exportará a [HTML de salida](61767778.zip). Pero si lo establece en **falso**, entonces este estilo no utilizado estará presente dentro del HTML de salida, que luego podrá ver en el marcado HTML como se muestra en la captura de pantalla anterior.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
