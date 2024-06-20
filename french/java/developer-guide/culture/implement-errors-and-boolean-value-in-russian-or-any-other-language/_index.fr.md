---
title: Implémenter des erreurs et des valeurs booléennes en russe ou dans une autre langue
type: docs
weight: 30
url: /fr/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **Scénarios d'utilisation possibles**
Si vous utilisez Microsoft Excel en russe ou dans une autre langue, il affichera les erreurs et les valeurs booléennes en fonction de cette langue ou de cette langue. Vous pouvez obtenir un comportement similaire en utilisant la méthode ou la propriété [Workbook.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) d'Aspose.Cells. Vous devrez remplacer les méthodes suivantes de la classe [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **Mettre en œuvre des erreurs et des valeurs booléennes en russe ou dans une autre langue**
Le code d'exemple suivant illustre comment implémenter les erreurs et la valeur booléenne en russe ou dans toute autre langue. Veuillez consulter le fichier Excel d'exemple utilisé dans ce code et son fichier PDF de sortie. La capture d'écran montre la différence entre le [fichier Excel d'exemple](48496697.xlsx) et le [PDF de sortie](48496696.pdf) à titre de référence.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
