---
title: Vérifier si la feuille de calcul est une feuille de dialogue
type: docs
weight: 100
url: /fr/java/find-if-the-worksheet-is-dialog-sheet/
---

## **Scénarios d'utilisation possibles**

La feuille de dialogue est un ancien format de feuille qui contient une boîte de dialogue. Une telle feuille pourrait être insérée par une ancienne version de Microsoft Excel, par exemple 2003, comme le montre cette capture d'écran. Elle peut également être insérée avec VBA dans des versions plus récentes, par exemple Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Vous pouvez trouver si la feuille est une feuille de dialogue ou un autre type de feuille avec la propriété [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type) fournie par Aspose.Cells. Si elle renvoie la valeur d'énumération [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG), cela signifie que vous traitez avec une feuille de dialogue.

## **Trouver si la Feuille de calcul est une Feuille de dialogue**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716841.xlsx) qui contient une feuille de dialogue. Il vérifie la propriété [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type), la compare avec [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG) et affiche ensuite le message. Veuillez consulter la sortie console de l'exemple de code ci-dessous pour plus d'aide.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **Sortie console**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
