---
title: Implémenter des erreurs et des valeurs booléennes en russe ou dans une autre langue
type: docs
weight: 40
url: /fr/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **Scénarios d'utilisation possibles**

Si vous utilisez Microsoft Excel dans la locale ou la langue russe ou toute autre locale ou langue, il affichera des erreurs et des valeurs booléennes selon cette locale ou langue. Vous pouvez obtenir un comportement similaire en utilisant Aspose.Cells en utilisant la propriété [**Workbook.Settings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings). Vous devrez remplacer les méthodes suivantes de la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings).

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **Mettre en œuvre des erreurs et des valeurs booléennes en russe ou dans une autre langue**

Le code d'exemple suivant illustre comment mettre en œuvre des erreurs et des valeurs booléennes en russe ou dans une autre langue. Veuillez consulter le [Fichier Excel exemple](73990159.xlsx) utilisé dans ce code et son [Fichier PDF de sortie](73990160.pdf). La capture d'écran montre la différence entre le fichier Excel exemple et le fichier PDF de sortie pour référence.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
