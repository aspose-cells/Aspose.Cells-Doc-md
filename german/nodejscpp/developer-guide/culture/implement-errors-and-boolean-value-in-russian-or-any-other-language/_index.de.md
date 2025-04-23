---
title: Implementieren Sie Fehler und boolesche Werte auf Russisch oder in jeder anderen Sprache mit Node.js über C++
linktitle: Fehler und boolesche Werte in Russisch oder einer anderen Sprache implementieren
type: docs
weight: 40
url: /de/nodejs-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Erfahren Sie, wie man Fehler und boolesche Werte in verschiedenen Sprachen mit Aspose.Cells for Node.js via C++ implementiert. 
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Microsoft Excel in russischem Locale oder Sprache oder in einer anderen Region oder Sprache verwenden, werden Fehler und boolesche Werte entsprechend angezeigt. Sie können ein ähnliches Verhalten mit Aspose.Cells for Node.js via C++ durch die Verwendung der [**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--)-Eigenschaft erreichen. Sie müssen die folgenden Methoden der [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)-Klasse überschreiben.

- [**GlobalizationSettings.getErrorValueString(string)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getErrorValueString-string-)
- [**GlobalizationSettings.getBooleanValueString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getBooleanValueString-boolean-)

## **Fehler und boolesche Werte in Russisch oder einer anderen Sprache implementieren**

Der folgende Beispielcode veranschaulicht, wie Fehler und boolesche Werte in Russisch oder einer anderen Sprache implementiert werden. Bitte überprüfen Sie die in diesem Code verwendete [Beispiel Excel-Datei](73990159.xlsx) und deren [Ausgabe-PDF](73990160.pdf). Der Screenshot zeigt den Unterschied zwischen der Beispiel-Excel-Datei und der Ausgabe-PDF zur Referenz.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Beispielcode**

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
