---
title: Exporter un style de bordure similaire lorsque le style de bordure n est pas pris en charge par les navigateurs Web
type: docs
weight: 70
url: /fr/python-net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Scénarios d'utilisation possibles**

Microsoft Excel supporte certains types de bordures en pointillés qui ne sont pas supportés par les navigateurs Web. Lors de la conversion de tels fichiers Excel en HTML avec Aspose.Cells pour Python via .NET, ces bordures sont supprimées. Toutefois, Aspose.Cells pour Python via .NET peut également supporter l’affichage de ces bordures en utilisant la propriété [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style). Veuillez définir sa valeur sur **true** et les bordures non supportées seront aussi exportées en HTML.

## **Exporter un style de bordure similaire lorsque le style de bordure n'est pas pris en charge par les navigateurs Web**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716806.xlsx) qui contient des bordures non prises en charge comme indiqué dans la capture d'écran suivante. La capture d'écran illustre également l'effet de la propriété [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style) à l'intérieur du [HTML de sortie](64716804.zip).

![todo:image_alt_text](1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportSimilarBorderStyle.py" >}}
{{< app/cells/assistant language="python-net" >}}
