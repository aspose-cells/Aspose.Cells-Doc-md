---
title: Exporter la plage de la zone d'impression vers HTML
type: docs
weight: 60
url: /fr/java/export-print-area-range-to-html/
---
## Scénarios d'utilisation possibles

Il s'agit d'un scénario très courant dans lequel nous devons exporter uniquement la zone d'impression, c'est-à-dire la plage de cellules sélectionnée au lieu de la feuille entière vers HTML. Cette fonctionnalité est déjà disponible pour le rendu PDF, cependant, vous pouvez maintenant effectuer cette tâche pour HTML également. Tout d'abord, définissez la zone d'impression dans l'objet de mise en page de la feuille de calcul. Utilisation ultérieure[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly)propriété pour exporter uniquement la plage sélectionnée.

## Java code pour exporter la plage de la zone d'impression vers HTML

L'exemple de code suivant charge un classeur, puis exporte la zone d'impression vers le HTML. L'exemple de fichier pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

