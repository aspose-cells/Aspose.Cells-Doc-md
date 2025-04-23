---
title: Exportar un Estilo de Borde Similar cuando el Estilo de Borde no es compatible con los Navegadores Web
type: docs
weight: 70
url: /es/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Escenarios de uso posibles**

Microsoft Excel soporta algún tipo de bordes discontínuos que no son soportados por los navegadores web. Cuando convierte este tipo de archivo de Excel a HTML usando Aspose.Cells, dichos bordes son eliminados. Sin embargo, Aspose.Cells también puede soportar la visualización de dichos bordes con la propiedad [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle). Por favor, configura su valor como **true** y los bordes no soportados también serán exportados al archivo HTML.

## **Exportar un estilo de borde similar cuando el estilo de borde no es soportado por los navegadores web**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716806.xlsx) que contiene algunos bordes no soportados como se muestra en la captura de pantalla siguiente. La captura de pantalla ilustra además el efecto de la propiedad [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) dentro del [HTML de salida](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
{{< app/cells/assistant language="csharp" >}}
