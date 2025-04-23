---
title: Vérifier si la feuille de calcul est une feuille de dialogue
type: docs
weight: 90
url: /fr/python-net/find-if-the-worksheet-is-dialog-sheet/
description: La feuille de dialogue est un ancien format de feuille. Cet article fournit des instructions et un code d exemple pour déterminer de manière programmatique si une feuille Excel est une feuille de dialogue en utilisant la bibliothèque Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, type de dialogue de feuille de calcul Excel dans Python.
---

## **Scénarios d'utilisation possibles**

La feuille de dialogue est un ancien format de feuille qui contient une boîte de dialogue. Une telle feuille peut être insérée par une ancienne version de Microsoft Excel, par exemple 2003 comme le montre cette capture d'écran. Elle peut également être insérée avec VBA dans des versions plus récentes comme Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Vous pouvez déterminer si la feuille est une feuille de dialogue ou un autre type de feuille avec la propriété [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/) fournie par Aspose.Cells pour Python via .NET. Si cela renvoie la valeur d'énumération [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/), cela signifie que vous traitez avec une feuille de dialogue.

## **Trouver si la Feuille de calcul est une Feuille de dialogue**

Le code d'exemple suivant charge le fichier Excel d'exemple (64716820.xlsx) qui contient une feuille de dialogue. Il vérifie la propriété [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/) la compare avec [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/) et affiche ensuite le message. Veuillez consulter la sortie de la console du code d'exemple ci-dessous pour plus d'aide.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}

## **Sortie console**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
