---
title: Supprimer les paramètres d'imprimante existants des feuilles de calcul dans le fichier Excel
type: docs
weight: 60
url: /fr/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Dans cet article, vous apprendrez à supprimer les paramètres d'imprimante existants de la feuille de calcul dans le fichier Excel via l'objet Mise en page par programmation avec un exemple de code à l'aide de la bibliothèque C# API ou .NET.
keywords: remove printer settings of worksheet c#, remove printer settings of excel worksheet c#
---
##  **Scénarios d'utilisation possibles**
Parfois, les développeurs veulent empêcher Excel d'inclure*.poubelle* fichiers de paramètres d'imprimante dans les fichiers XLSX enregistrés. Les fichiers de paramètres d'imprimante se trouvent sous*"[fichier "racine"]\xl\printerSettings".* Ce document explique comment supprimer les paramètres d'imprimante existants à l'aide des API Aspose.Cells.
##  **Supprimer les paramètres d'imprimante existants des feuilles de calcul dans le fichier Excel**
Aspose.Cells vous permet de supprimer les paramètres d'imprimante existants spécifiés pour différentes feuilles dans le fichier Excel. L'exemple de code suivant montre comment supprimer les paramètres d'imprimante existants pour toutes les feuilles de calcul du classeur. Veuillez voir son[exemple de fichier Excel](45056020.xlsx), [fichier Excel de sortie](45056021.xlsx)la sortie de la console ainsi que la capture d'écran pour référence.
##  **Capture d'écran**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
##  **Exemple de code**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
##  **Sortie console**
{{< highlight "java" >}}

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
