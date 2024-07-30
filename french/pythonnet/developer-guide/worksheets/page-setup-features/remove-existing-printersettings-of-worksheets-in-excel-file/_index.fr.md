---
title: Supprimer les paramètres d imprimante existants des feuilles de calcul dans le fichier Excel
type: docs
weight: 60
url: /fr/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Dans cet article, vous apprendrez comment supprimer les paramètres d imprimante existants d une feuille de calcul dans le fichier Excel à l aide de l objet de configuration de page de manière programmatique avec un code d exemple en utilisant la bibliothèque Excel Aspose.Cells pour Python.
keywords: Bibliothèque Python Excel, supprimer les paramètres d imprimante d une feuille de calcul en Python, supprimer les paramètres d imprimante d une feuille de calcul Excel en Python.
---

## **Scénarios d'utilisation possibles**
Parfois, les développeurs veulent empêcher Excel d'inclure les fichiers *.bin* des paramètres d'imprimante dans les fichiers XLSX enregistrés. Les fichiers de paramètres d'imprimante sont situés sous *"[fichier "racine"]\xl\printerSettings".* Ce document explique comment supprimer les paramètres d'imprimante existants en utilisant les API Aspose.Cells pour Python via .NET.

## **Supprimer les paramètres d'imprimante existants des feuilles de calcul dans le fichier Excel**
Aspose.Cells pour Python via .NET vous permet de supprimer les paramètres d'imprimante existants spécifiés pour différentes feuilles dans le fichier Excel. Le code d'exemple suivant illustre comment supprimer les paramètres d'imprimante existants pour toutes les feuilles de calcul du classeur. Veuillez consulter son [fichier Excel d'exemple](45056020.xlsx), [fichier Excel de sortie](45056021.xlsx), la sortie de la console ainsi que la capture d'écran pour une référence.

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
