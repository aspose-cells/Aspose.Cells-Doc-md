---
title: Exporter la plage de la zone d'impression vers HTML
type: docs
weight: 60
url: /fr/net/export-print-area-range-to/
---
## **Scénarios d'utilisation possibles**

 Il s'agit d'un scénario courant dans lequel nous devons exporter uniquement la zone d'impression, c'est-à-dire la plage de cellules sélectionnée au lieu de la feuille entière vers HTML. Cette fonctionnalité est déjà disponible pour le rendu PDF, cependant, vous pouvez désormais effectuer cette tâche pour HTML également. Définissez d'abord la zone d'impression dans l'objet de mise en page de la feuille de calcul. Plus tard, utilisez[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) flag pour exporter uniquement la plage sélectionnée.

## Exemple de code

L'exemple de code suivant charge un classeur, puis exporte la zone d'impression vers le HTML. Un exemple de fichier pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
