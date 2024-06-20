---
title: Exporter la plage de zone d impression au format HTML
type: docs
weight: 60
url: /fr/java/export-print-area-range-to-html/
---

## Scénarios d'utilisation possibles

Il s'agit d'un scénario très courant où nous devons exporter uniquement la zone d'impression, c'est-à-dire la plage de cellules sélectionnée au lieu de la feuille entière, au format HTML. Cette fonctionnalité est déjà disponible pour le rendu PDF, cependant, vous pouvez désormais effectuer cette tâche également pour le HTML. Définissez d'abord la zone d'impression dans l'objet de mise en page de la feuille de calcul. Ensuite, utilisez la propriété [**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly) pour n'exporter que la plage sélectionnée.

## Code Java pour exporter la plage de la zone d'impression au format HTML

Le code d'exemple suivant charge un classeur puis exporte la zone d'impression vers le HTML. Le fichier d'exemple pour tester cette fonctionnalité peut être téléchargé depuis le lien suivant :

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

