---
title: Implémenter les erreurs et la valeur booléenne en russe ou dans toute autre langue
type: docs
weight: 40
url: /fr/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---
## **Scénarios d'utilisation possibles**

Si vous utilisez Microsoft Excel dans les paramètres régionaux ou la langue russe ou tout autre paramètre régional ou langue, il affichera les erreurs et les valeurs booléennes en fonction de ces paramètres régionaux ou de cette langue. Vous pouvez obtenir un comportement similaire en utilisant Aspose.Cells en utilisant le**[Classeur.Paramètres.GlobalizationSettings**] (https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) propriété. Vous devrez remplacer les méthodes suivantes de[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)classer.

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **Implémenter les erreurs et la valeur booléenne en russe ou dans toute autre langue**

 L'exemple de code suivant illustre comment implémenter les erreurs et la valeur booléenne en russe ou dans toute autre langue. S'il vous plaît, vérifiez le[Exemple de fichier Excel](73990159.xlsx) utilisé dans ce code et ses[Sortie PDF](73990160.pdf)La capture d'écran montre la différence entre l'exemple de fichier Excel et le PDF de sortie pour une référence.

![tâche : image_autre_texte](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
