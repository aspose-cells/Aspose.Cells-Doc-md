---
title: Implémentez les erreurs et la valeur booléenne en russe ou dans toute autre langue avec Node.js via C++
linktitle: Implémenter des erreurs et des valeurs booléennes en russe ou dans une autre langue
type: docs
weight: 40
url: /fr/nodejs-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Apprenez comment implémenter les erreurs et les valeurs booléennes dans différentes langues en utilisant Aspose.Cells for Node.js via C++. 
---

## **Scénarios d'utilisation possibles**

Si vous utilisez Microsoft Excel en locale ou langue russe ou dans toute autre locale ou langue, il affichera les erreurs et les valeurs booléennes selon cette locale ou langue. Vous pouvez obtenir un comportement similaire avec Aspose.Cells for Node.js via C++ en utilisant la propriété [**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--). Vous devrez remplacer les méthodes suivantes de la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings).

- [**GlobalizationSettings.getErrorValueString(string)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getErrorValueString-string-)
- [**GlobalizationSettings.getBooleanValueString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getBooleanValueString-boolean-)

## **Mettre en œuvre des erreurs et des valeurs booléennes en russe ou dans une autre langue**

Le code d'exemple suivant illustre comment mettre en œuvre des erreurs et des valeurs booléennes en russe ou dans une autre langue. Veuillez consulter le [Fichier Excel exemple](73990159.xlsx) utilisé dans ce code et son [Fichier PDF de sortie](73990160.pdf). La capture d'écran montre la différence entre le fichier Excel exemple et le fichier PDF de sortie pour référence.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Code d'exemple**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Russian Globalization
class RussianGlobalization extends AsposeCells.GlobalizationSettings {
getErrorValueString(err) {
switch (err.toUpperCase()) {
case "#NAME?":
return "#RussianName-имя?";
}
return "RussianError-ошибка";
}

getBooleanValueString(bv) {
return bv ? "RussianTrue-правда" : "RussianFalse-ложный";
}
}

//--------------------------------
//--------------------------------

class ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage {
static run() {
// Load the source workbook
const workbook = new AsposeCells.Workbook("sampleRussianGlobalization.xlsx");

// Set GlobalizationSettings in Russian Language
workbook.getSettings().setGlobalizationSettings(new RussianGlobalization());

// Calculate the formula
workbook.calculateFormula();

// Save the workbook in pdf format
workbook.save("outputRussianGlobalization.pdf");
}
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
