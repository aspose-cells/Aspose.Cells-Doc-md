---
title: Supprimer les paramètres d imprimante existants des feuilles de calcul dans le fichier Excel
type: docs
weight: 40
url: /fr/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---

## **Scénarios d'utilisation possibles**
Parfois, les développeurs veulent empêcher Excel d'inclure des fichiers de paramètres d'imprimante *.bin* dans les fichiers XLSX enregistrés. Les fichiers de paramètres d'imprimante se trouvent sous *“[file "root"]\xl\printerSettings”*. Ce document explique comment supprimer les paramètres d'imprimante existants en utilisant les APIs Aspose.Cells.
## **Supprimer les paramètres d'imprimante existants des feuilles de calcul dans le fichier Excel**
Aspose.Cells vous permet de supprimer les paramètres d'imprimante existants spécifiés pour différentes feuilles du fichier Excel. Le code d'exemple suivant illustre comment supprimer les paramètres d'imprimante existants pour toutes les feuilles de calcul dans le classeur. Veuillez consulter son [fichier Excel d'exemple](45056023.xlsx), [fichier Excel de sortie](45056024.xlsx), la sortie de la console ainsi qu'une capture d'écran à titre de référence.
## **Capture d'écran**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **Sortie console**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: 5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: 34

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: 70

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: 8

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
