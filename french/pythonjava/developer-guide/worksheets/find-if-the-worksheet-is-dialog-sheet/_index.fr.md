---
title: Vérifier si la feuille de calcul est une feuille de dialogue
type: docs
weight: 70
url: /fr/python-java/find-if-the-worksheet-is-dialog-sheet/
---

## **Scénarios d'utilisation possibles**
La feuille de dialogue est un ancien format de feuille qui contient une boîte de dialogue. Une telle feuille pourrait être insérée par une ancienne version de Microsoft Excel, par exemple 2003, comme le montre cette capture d'écran. Elle peut également être insérée avec VBA dans des versions plus récentes, par exemple Microsoft Excel 2016.

![todo:image_alt_text](DialogSheet.png)
## **Trouver si la Feuille de calcul est une Feuille de dialogue**
Aspose.Cells pour Python via Java vous offre la possibilité de vérifier si la feuille de calcul est une feuille de dialogue. Pour ce faire, il fournit la propriété [Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type). Si [Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type) retourne la valeur d'énumération [SheetType.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG), cela signifie que vous travaillez avec une feuille de dialogue.

Le code suivant montre comment vérifier une feuille de dialogue. La sortie console générée par le code est donnée ci-dessous à titre de référence.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **Sortie console**
{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
