---
title: Exporter la plage de zones d impression en HTML avec Golang via C++
linktitle: Exporter la plage de la zone d impression en HTML
type: docs
weight: 60
url: /fr/go-cpp/export-print-area-range-to/
description: Apprenez comment exporter la plage de la zone d impression en HTML en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

C’est un scénario courant où nous devons exporter uniquement la zone d'impression, c’est-à-dire une plage sélectionnée de cellules, plutôt que la feuille entière en HTML. Cette fonctionnalité est déjà disponible pour le rendu PDF ; cependant, vous pouvez désormais effectuer cette tâche également pour HTML. Tout d’abord, réglez la zone d’impression dans l’objet mise en page de la feuille. Ensuite, utilisez le drapeau [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportprintareaonly/) pour exporter uniquement la plage sélectionnée.

## **Code d'exemple**

Le code d’exemple suivant charge un classeur puis exporte la zone d’impression en HTML. Le fichier d'essai pour cette fonction peut être téléchargé à partir du lien suivant :

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportPrintAreaRangeToHtml.go" >}}
