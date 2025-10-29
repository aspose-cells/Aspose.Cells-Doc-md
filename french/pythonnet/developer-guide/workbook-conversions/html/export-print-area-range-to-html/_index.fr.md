---
title: Exporter la plage de zone d impression au format HTML
type: docs
weight: 60
url: /fr/python-net/export-print-area-range-to/
---

## **Scénarios d'utilisation possibles**

Il s'agit d'un scénario courant où nous devons exporter uniquement la zone d'impression, c'est-à-dire la plage de cellules sélectionnée au lieu de l'ensemble de la feuille au format HTML. Cette fonctionnalité est déjà disponible pour le rendu PDF, cependant, vous pouvez maintenant effectuer cette tâche pour HTML également. Définissez d'abord la zone d'impression dans l'objet de configuration de page de la feuille de calcul. Ensuite, utilisez le drapeau [**HtmlSaveOptions.export_print_area_only**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_print_area_only) pour n'exporter que la plage sélectionnée.

## Code d'exemple

Le code d'exemple suivant charge un classeur puis exporte la zone d'impression au format HTML. Le fichier d'exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportPrintAreaToHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
