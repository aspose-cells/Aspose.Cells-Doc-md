---
title: Excluir Estilos No Utilizados durante la conversión de Excel a HTML
type: docs
weight: 30
url: /es/java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Escenarios de uso posibles**

Un archivo de Microsoft Excel puede contener muchos estilos no utilizados. Al exportar el archivo Excel a formato HTML, también se exportan estos estilos no utilizados. Esto puede aumentar el tamaño del HTML. Puede excluir los estilos no utilizados durante la conversión del archivo Excel a HTML utilizando la propiedad [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles). Cuando se establece como **true**, se excluyen todos los estilos no utilizados del HTML de salida. La siguiente captura de pantalla muestra un ejemplo de estilo no utilizado dentro del HTML de salida.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Excluir estilos no utilizados durante la conversión de Excel a HTML**

El siguiente código de ejemplo crea un libro de trabajo y también crea un estilo con nombre no utilizado. Dado que [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles) se establece como **true**, este estilo con nombre no utilizado no se exportará a [HTML de salida](61767781.zip). Pero si se establece como **false**, entonces este estilo no utilizado estará presente dentro del HTML de salida, lo cual podrá verse en el marcado HTML tal como se muestra en la captura de pantalla anterior.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
