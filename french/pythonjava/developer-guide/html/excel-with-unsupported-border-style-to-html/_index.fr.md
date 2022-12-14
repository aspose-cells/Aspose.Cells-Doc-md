---
title: Excel avec un style de bordure non pris en charge en HTML
type: docs
weight: 80
url: /fr/python-java/excel-with-unsupported-border-style-to/
---
## **Excel avec un style de bordure non pris en charge en HTML**
Microsoft Excel prend en charge certains types de bordures en pointillés qui ne sont pas pris en charge par les navigateurs Web. Lorsque ces fichiers sont convertis en HTML à l'aide de Aspose.Cells, ces bordures sont supprimées. Cependant, Aspose.Cells pour Python via Java prend en charge l'affichage de bordures similaires avec[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)propriété. Vous pouvez définir la valeur de[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) propriété à**Vrai**pour exporter les bordures non prises en charge.

L'exemple de code suivant charge le[exemple de fichier Excel](sampleExportSimilarBorderStyle.xlsx)contenant des bordures non prises en charge, comme illustré dans la capture d'écran suivante. La capture d'écran illustre davantage l'effet de[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)propriété à l'intérieur du[sortie HTML](outputExportSimilarBorderStyle.zip).

![tâche : image_autre_texte](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
