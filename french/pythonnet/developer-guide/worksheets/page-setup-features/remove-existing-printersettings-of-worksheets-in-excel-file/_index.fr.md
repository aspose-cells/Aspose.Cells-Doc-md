---
title: Supprimer les paramètres d imprimante existants des feuilles de calcul dans le fichier Excel
type: docs
weight: 60
url: /fr/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Dans cet article, vous apprendrez comment supprimer les paramètres d imprimante existants d une feuille dans un fichier Excel via l objet Page Setup de manière programmatique avec un code d exemple utilisant la bibliothèque Excel Aspose.Cells pour Python.
keywords: Bibliothèque Excel en Python, supprimer les paramètres d imprimante de la feuille, supprimer les paramètres d imprimante d une feuille Excel en Python.
---

## **Scénarios d'utilisation possibles**
Parfois, les développeurs veulent empêcher Excel d'inclure les fichiers *.bin* de paramètres d'imprimante dans les fichiers XLSX enregistrés. Les fichiers de paramètres d'imprimante se trouvent sous *“[file "root"]\xl\printerSettings”.* Ce document explique comment supprimer les paramètres d'imprimante existants en utilisant Aspose.Cells pour Python via .NET API.

## **Supprimer les paramètres d'imprimante existants des feuilles de calcul dans le fichier Excel**
Aspose.Cells pour Python via .NET vous permet de supprimer les paramètres d'imprimante existants spécifiés pour différentes feuilles dans le fichier Excel. Le code d'exemple suivant illustre comment supprimer les paramètres d'imprimante pour toutes les feuilles du classeur. Voir le [fichier Excel exemple](45056020.xlsx), [fichier Excel de sortie](45056021.xlsx), la sortie console ainsi qu'une capture d'écran comme référence.

## **Capture d'écran**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Code d'exemple**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.py" >}}

## **Sortie console**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
