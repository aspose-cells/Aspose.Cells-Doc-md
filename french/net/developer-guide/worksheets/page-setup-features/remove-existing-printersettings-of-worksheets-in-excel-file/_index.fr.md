---
title: Supprimer les paramètres d imprimante existants des feuilles de calcul dans le fichier Excel
type: docs
weight: 60
url: /fr/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Dans cet article, vous apprendrez comment supprimer les paramètres d imprimante existants de la feuille de calcul à l intérieur du fichier Excel via l objet de configuration de page programmation avec un code d exemple en utilisant l API C# ou la bibliothèque .NET.
keywords: supprimer les paramètres d imprimante de la feuille de calcul c#, supprimer les paramètres d imprimante de la feuille de calcul Excel c#
---

## **Scénarios d'utilisation possibles**
Parfois, les développeurs souhaitent empêcher Excel d'inclure des fichiers *.bin* de paramètres d'imprimante dans les fichiers XLSX enregistrés. Les fichiers de paramètres d'imprimante se trouvent sous *« [fichier "root"]\xl\printerSettings ».* Ce document explique comment supprimer les paramètres d'imprimante existants à l'aide des API Aspose.Cells.
## **Supprimer les paramètres d'imprimante existants des feuilles de calcul dans le fichier Excel**
Aspose.Cells vous permet de supprimer les paramètres d'imprimante existants spécifiés pour différentes feuilles dans le fichier Excel. Le code d'exemple suivant illustre comment supprimer les paramètres d'imprimante existants pour toutes les feuilles de calcul dans le classeur. Veuillez consulter son [fichier Excel d'exemple](45056020.xlsx), [fichier Excel de sortie](45056021.xlsx), la sortie de la console ainsi que la capture d'écran à titre de référence.
## **Capture d'écran**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
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
{{< app/cells/assistant language="csharp" >}}
