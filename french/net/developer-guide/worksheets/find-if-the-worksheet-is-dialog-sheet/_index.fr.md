---
title: Vérifier si la feuille de calcul est une feuille de dialogue
type: docs
weight: 90
url: /fr/net/find-if-the-worksheet-is-dialog-sheet/
description: Une feuille de dialogue est un ancien format de feuille. Cet article fournit des instructions et un code d exemple pour déterminer de manière programmative si une feuille de calcul Excel est une feuille de dialogue en utilisant l API C# ou la bibliothèque .NET.
keywords: trouver le type de feuille de dialogue Excel c#, feuille de dialogue c#
---

## **Scénarios d'utilisation possibles**

La feuille de dialogue est un ancien format de feuille qui contient une boîte de dialogue. Une telle feuille peut être insérée par une ancienne version de Microsoft Excel, par exemple 2003 comme le montre cette capture d'écran. Elle peut également être insérée avec VBA dans des versions plus récentes comme Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Vous pouvez savoir si la feuille est une feuille de dialogue ou un autre type de feuille avec la propriété [**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type) fournie par Aspose.Cells. Si elle retourne la valeur d'énumération [**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype), cela signifie que vous traitez avec une feuille de dialogue.

## **Trouver si la Feuille de calcul est une Feuille de dialogue**

Le code d'exemple suivant charge le fichier Excel d'exemple (64716820.xlsx) qui contient une feuille de dialogue. Il vérifie la propriété [**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type) la compare avec [**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) et affiche ensuite le message. Veuillez consulter la sortie de la console du code d'exemple ci-dessous pour plus d'aide.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **Sortie console**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
