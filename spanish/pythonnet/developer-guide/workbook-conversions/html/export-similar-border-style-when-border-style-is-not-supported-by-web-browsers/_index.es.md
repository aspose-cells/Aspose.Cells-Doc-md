---
title: Exportar un Estilo de Borde Similar cuando el Estilo de Borde no es compatible con los Navegadores Web
type: docs
weight: 70
url: /es/python-net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Escenarios de uso posibles**

Microsoft Excel soporta algunos tipos de bordes discontinuos que no son soportados por navegadores web. Cuando conviertes un archivo Excel con estos bordes en HTML usando Aspose.Cells para Python via .NET, estos bordes se eliminan. Sin embargo, Aspose.Cells para Python via .NET también soporta mostrar estos bordes con la propiedad [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style). Configúrala en **true** y los bordes no soportados también se exportarán a HTML.

## **Exportar un estilo de borde similar cuando el estilo de borde no es soportado por los navegadores web**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716806.xlsx) que contiene algunos bordes no soportados como se muestra en la captura de pantalla siguiente. La captura de pantalla ilustra además el efecto de la propiedad [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style) dentro del [HTML de salida](64716804.zip).

![todo:image_alt_text](1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportSimilarBorderStyle.py" >}}
{{< app/cells/assistant language="python-net" >}}
