---
title: Exporter un style de bordure similaire lorsque le style de bordure n'est pas pris en charge par les navigateurs Web
type: docs
weight: 70
url: /fr/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---
## **Scénarios d'utilisation possibles**

Microsoft Excel prend en charge certains types de bordures en pointillés qui ne sont pas pris en charge par les navigateurs Web. Lorsque vous convertissez un tel fichier Excel en HTML à l'aide de Aspose.Cells, ces bordures sont supprimées. Cependant, Aspose.Cells peut également prendre en charge l'affichage de telles bordures avec[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) propriété. Veuillez définir sa valeur comme**vrai**et les bordures non prises en charge seront également exportées vers un fichier HTML.

## **Exporter un style de bordure similaire lorsque le style de bordure n'est pas pris en charge par les navigateurs Web**

L'exemple de code suivant charge le[exemple de fichier Excel](64716806.xlsx) contenant des bordures non prises en charge, comme illustré dans la capture d'écran suivante. La capture d'écran illustre davantage l'effet de[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle)propriété à l'intérieur du[sortie HTML](64716804.zip).

![tâche : image_autre_texte](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
