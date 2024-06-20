---
title: Excel avec un style de bordure non pris en charge en HTML
type: docs
weight: 80
url: /fr/python-java/excel-with-unsupported-border-style-to/
---

## **Excel avec un style de bordure non pris en charge en HTML**
Microsoft Excel prend en charge certains types de bordures en pointillés qui ne sont pas pris en charge par les navigateurs Web. Lorsque de tels fichiers sont convertis en HTML à l'aide d'Aspose.Cells, ces bordures sont supprimées. Cependant, Aspose.Cells for Python via Java prend en charge l'affichage de bordures similaires avec la propriété [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle). Vous pouvez définir la valeur de la propriété [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) sur **True** pour exporter les bordures non prises en charge.

Le code d'exemple suivant charge le [fichier Excel d'exemple](sampleExportSimilarBorderStyle.xlsx) qui contient certaines bordures non prises en charge comme le montre la capture d'écran suivante. La capture d'écran illustre davantage l'effet de la propriété [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) à l'intérieur du [fichier HTML de sortie](outputExportSimilarBorderStyle.zip).

![todo:image_alt_text](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
