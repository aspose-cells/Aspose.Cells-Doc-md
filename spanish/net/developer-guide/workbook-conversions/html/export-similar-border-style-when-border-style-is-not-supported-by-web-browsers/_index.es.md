---
title: Exporte un estilo de borde similar cuando los navegadores web no admitan el estilo de borde
type: docs
weight: 70
url: /es/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---
## **Posibles escenarios de uso**

Microsoft Excel admite algún tipo de bordes discontinuos que no son compatibles con los navegadores web. Cuando convierte un archivo de Excel de este tipo en HTML usando Aspose.Cells, dichos bordes se eliminan. Sin embargo, Aspose.Cells también puede admitir la visualización de dichos bordes con[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) propiedad. Por favor, establezca su valor como**verdadero**y los bordes no admitidos también se exportarán al archivo HTML.

## **Exporte un estilo de borde similar cuando los navegadores web no admitan el estilo de borde**

El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](64716806.xlsx) que contiene algunos bordes no admitidos, como se muestra en la siguiente captura de pantalla. La captura de pantalla ilustra aún más el efecto de[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle)propiedad dentro de la[salida HTML](64716804.zip).

![todo:imagen_alternativa_texto](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
