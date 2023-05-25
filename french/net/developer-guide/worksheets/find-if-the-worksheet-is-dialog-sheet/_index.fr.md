---
title: Rechercher si la feuille de calcul est une feuille de dialogue
type: docs
weight: 90
url: /fr/net/find-if-the-worksheet-is-dialog-sheet/
description: Dialog Sheet est un ancien format de feuille. Cet article fournit des instructions et un exemple de code pour déterminer par programmation si une feuille de calcul Excel est une feuille de dialogue à l'aide de la bibliothèque C# API ou .NET.
keywords: find excel worksheet dialog type c#, worksheet dialog c#
---
##  **Scénarios d'utilisation possibles**

La feuille de dialogue est un ancien format de feuille qui contient une boîte de dialogue. Une telle feuille pourrait être insérée par une ancienne version d'Excel Microsoft, par exemple 2003, comme indiqué dans cette capture d'écran. Il peut également être inséré avec VBA dans les versions plus récentes, par exemple Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Vous pouvez déterminer si la feuille est une feuille de dialogue ou un autre type de feuille avec[**Feuille de travail.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)propriété fournie par Aspose.Cells. Si elle renvoie la valeur d'énumération[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype), cela signifie que vous avez affaire à une feuille de dialogue.

##  **Rechercher si la feuille de calcul est une feuille de dialogue**

 L'exemple de code suivant charge le[exemple de fichier Excel](64716820.xlsx) qui contient une feuille de dialogue. Il vérifie la[**Feuille de travail.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)la propriété le compare avec[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) puis imprime le message. Veuillez consulter la sortie de la console de l'exemple de code ci-dessous pour plus d'aide.

##  **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

##  **Sortie console**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
