---
title: Exporter un style de bordure similaire lorsque le style de bordure n est pas pris en charge par les navigateurs Web
type: docs
weight: 70
url: /fr/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Scénarios d'utilisation possibles**

Microsoft Excel prend en charge certains types de bordures en pointillés non pris en charge par les navigateurs Web. Lorsque vous convertissez un tel fichier Excel en HTML à l'aide d'Aspose.Cells, ces bordures sont supprimées. Cependant, Aspose.Cells peut également prendre en charge l'affichage de bordures similaires avec la propriété [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle). Veuillez définir sa valeur sur **true** et les bordures non prises en charge seront également exportées dans le fichier HTML.

## **Exporter un style de bordure similaire lorsque le style de bordure n'est pas pris en charge par les navigateurs Web**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716832.xlsx) qui contient certaines bordures non prises en charge comme indiqué dans la capture d'écran suivante. La capture d'écran illustre en outre l'effet de la propriété [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle) à l'intérieur de la [fichier HTML de sortie](64716831.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
{{< app/cells/assistant language="java" >}}
