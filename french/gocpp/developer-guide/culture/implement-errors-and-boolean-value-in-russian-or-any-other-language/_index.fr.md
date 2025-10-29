---
title: Implémenter des erreurs et des valeurs booléennes en russe ou dans toute autre langue avec Golang via C++
linktitle: Implémenter erreurs et valeurs booléennes
type: docs
weight: 40
url: /fr/go-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Apprenez comment implémenter des erreurs et des valeurs booléennes en russe ou dans toute autre langue en utilisant Aspose.Cells avec Golang via C++.
---

## **Scénarios d'utilisation possibles**

Si vous utilisez Microsoft Excel en localisation ou langue russe ou dans toute autre localisation ou langue, il affichera des erreurs et des valeurs booléennes en fonction de cette localisation ou langue. Vous pouvez obtenir un comportement similaire en utilisant Aspose.Cells avec la propriété [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getglobalizationsettings/). Vous devrez remplacer les méthodes suivantes de la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/).

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getbooleanvaluestring/)

## **Mettre en œuvre des erreurs et des valeurs booléennes en russe ou dans une autre langue**

Le code d'exemple suivant illustre comment mettre en œuvre des erreurs et des valeurs booléennes en russe ou dans une autre langue. Veuillez consulter le [Fichier Excel exemple](73990159.xlsx) utilisé dans ce code et son [Fichier PDF de sortie](73990160.pdf). La capture d'écran montre la différence entre le fichier Excel exemple et le fichier PDF de sortie pour référence.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.go" >}}
