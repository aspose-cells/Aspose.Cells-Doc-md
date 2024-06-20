---
title: Exporter la plage de zone d impression au format HTML
type: docs
weight: 60
url: /fr/net/export-print-area-range-to/
---

## **Scénarios d'utilisation possibles**

Il s'agit d'un scénario courant où nous devons exporter uniquement la zone d'impression, c'est-à-dire la plage de cellules sélectionnée au lieu de l'ensemble de la feuille au format HTML. Cette fonctionnalité est déjà disponible pour le rendu PDF, cependant, vous pouvez maintenant effectuer cette tâche pour HTML également. Définissez d'abord la zone d'impression dans l'objet de configuration de page de la feuille de calcul. Ensuite, utilisez le drapeau [**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) pour n'exporter que la plage sélectionnée.

## Code d'exemple

Le code d'exemple suivant charge un classeur puis exporte la zone d'impression au format HTML. Le fichier d'exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
