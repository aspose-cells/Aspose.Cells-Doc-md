---
title: Exporter un style de bordure similaire lorsque le style de bordure n est pas pris en charge par les navigateurs Web
type: docs
weight: 70
url: /fr/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Scénarios d'utilisation possibles**

Microsoft Excel prend en charge certains types de bordures en pointillés qui ne sont pas pris en charge par les navigateurs Web. Lorsque vous convertissez un tel fichier Excel en HTML à l'aide d'Aspose.Cells, ces bordures sont supprimées. Cependant, Aspose.Cells peut également prendre en charge l'affichage de ces bordures avec la propriété [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle). Veuillez définir sa valeur sur **true** et les bordures non prises en charge seront également exportées dans le fichier HTML.

## **Exporter un style de bordure similaire lorsque le style de bordure n'est pas pris en charge par les navigateurs Web**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716806.xlsx) qui contient des bordures non prises en charge comme indiqué dans la capture d'écran suivante. La capture d'écran illustre également l'effet de la propriété [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) à l'intérieur du [HTML de sortie](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
{{< app/cells/assistant language="csharp" >}}
