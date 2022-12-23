---
title: Implémenter les erreurs et la valeur booléenne en russe ou dans toute autre langue
type: docs
weight: 30
url: /fr/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---
## **Scénarios d'utilisation possibles**
Si vous utilisez Microsoft Excel dans les paramètres régionaux ou la langue russe ou tout autre paramètre régional ou langue, il affichera les erreurs et les valeurs booléennes en fonction de ces paramètres régionaux ou de cette langue. Vous pouvez obtenir un comportement similaire en utilisant Aspose.Cells[Classeur.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) méthode ou propriété. Vous devrez remplacer les méthodes suivantes de[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)classe.

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **Implémenter les erreurs et la valeur booléenne en russe ou dans toute autre langue**
 L'exemple de code suivant illustre comment implémenter les erreurs et la valeur booléenne en russe ou dans toute autre langue. Veuillez vérifier l'exemple de fichier Excel utilisé dans ce code et sa sortie PDF. La capture d'écran montre la différence entre[Exemple de fichier Excel](48496697.xlsx) et le[Sortie PDF](48496696.pdf) pour une référence.

![tâche : image_autre_texte](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
