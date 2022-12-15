---
title: Rechercher si la feuille de calcul est une feuille de dialogue
type: docs
weight: 70
url: /fr/python-java/find-if-the-worksheet-is-dialog-sheet/
---
## **Scénarios d'utilisation possibles**
La feuille de dialogue est un ancien format de la feuille qui contient une boîte de dialogue. Une telle feuille pourrait être insérée par une ancienne version d'Excel Microsoft, par exemple 2003, comme indiqué dans cette capture d'écran. Il peut également être inséré avec VBA dans les versions plus récentes, par exemple Microsoft Excel 2016.

![tâche : image_autre_texte](DialogSheet.png)
## **Rechercher si la feuille de calcul est une feuille de dialogue**
Aspose.Cells for Python via Java vous permet de vérifier si la feuille de calcul est une feuille de dialogue. Pour cela, il fournit la[Feuille de travail.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)propriété. Si[Feuille de travail.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)renvoie la valeur d'énumération[SheetType.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG), cela signifie que vous avez affaire à une feuille de dialogue.

L'extrait de code suivant montre comment rechercher une feuille de boîte de dialogue. La sortie de la console générée par le code est donnée ci-dessous pour référence.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **Sortie console**
La feuille de calcul est une feuille de dialogue.
