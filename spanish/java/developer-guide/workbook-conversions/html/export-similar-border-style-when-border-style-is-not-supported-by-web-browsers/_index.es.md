---
title: Exportar un Estilo de Borde Similar cuando el Estilo de Borde no es compatible con los Navegadores Web
type: docs
weight: 70
url: /es/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Escenarios de uso posibles**

Microsoft Excel admite ciertos tipos de bordes discontinuos que no son compatibles con los navegadores web. Cuando conviertes un archivo de Excel en HTML usando Aspose.Cells, esos bordes son eliminados. Sin embargo, Aspose.Cells también puede mostrar bordes similares con la propiedad [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle). Por favor establece su valor en **true** y los bordes no admitidos también se exportarán al archivo HTML.

## **Exportar un estilo de borde similar cuando el estilo de borde no es soportado por los navegadores web**

El siguiente código de muestra carga el [archivo de Excel de muestra](64716832.xlsx) que contiene algunos bordes no admitidos como se muestra en la siguiente captura de pantalla. La captura de pantalla ilustra aún más el efecto de la propiedad [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle) dentro del [HTML de salida](64716831.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
