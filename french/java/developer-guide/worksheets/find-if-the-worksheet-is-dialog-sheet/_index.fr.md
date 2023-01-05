---
title: Rechercher si la feuille de calcul est une feuille de dialogue
type: docs
weight: 100
url: /fr/java/find-if-the-worksheet-is-dialog-sheet/
---
## **Scénarios d'utilisation possibles**

La feuille de dialogue est un ancien format de la feuille qui contient une boîte de dialogue. Une telle feuille pourrait être insérée par une ancienne version d'Excel Microsoft, par exemple 2003, comme indiqué dans cette capture d'écran. Il peut également être inséré avec VBA dans les versions plus récentes, par exemple Microsoft Excel 2016.

![tâche : image_autre_texte](find-if-the-worksheet-is-dialog-sheet_1.png)

Vous pouvez déterminer si la feuille est une feuille de dialogue ou un autre type de feuille avec[**Feuille de travail.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)propriété fournie par Aspose.Cells. Si elle renvoie la valeur d'énumération[**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG), cela signifie que vous avez affaire à une feuille de dialogue.

## **Rechercher si la feuille de calcul est une feuille de dialogue**

L'exemple de code suivant charge le[exemple de fichier Excel](64716841.xlsx)qui contient une feuille de dialogue. Il vérifie la[**Feuille de travail.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)la propriété le compare avec[**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)puis imprime le message. Veuillez consulter la sortie de la console de l'exemple de code ci-dessous pour plus d'aide.

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **Sortie console**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
