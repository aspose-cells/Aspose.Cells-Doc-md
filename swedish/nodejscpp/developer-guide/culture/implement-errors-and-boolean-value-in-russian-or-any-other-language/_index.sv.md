---
title: Implementera Fel och Booleska värden på ryska eller andra språk med Node.js via C++
linktitle: Implementera fel och booleska värden på ryska eller något annat språk
type: docs
weight: 40
url: /sv/nodejs-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Lär dig hur du implementerar Fel och Booleska värden på olika språk med Aspose.Cells for Node.js via C++. 
---

## **Möjliga användningsscenario**

Om du använder Microsoft Excel på ryskt lokalt eller språk eller något annat, kommer det att visa Fel och Booleska värden enligt det språket. Du kan åstadkomma liknande beteende med Aspose.Cells for Node.js via C++ genom att använda [**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--)-egenskapen. Du måste åsidosätta följande metoder i [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)-klassen.

- [**GlobalizationSettings.getErrorValueString(string)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getErrorValueString-string-)
- [**GlobalizationSettings.getBooleanValueString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getBooleanValueString-boolean-)

## **Implementera fel och booleska värden på ryska eller något annat språk**

Följande exempelkod illustrerar hur man implementerar fel och booleskt värde på ryska eller något annat språk. Kontrollera den [Exempel Excel-filen](73990159.xlsx) som används i denna kod och dess [Utdata-PDF](73990160.pdf). Skärmbilden visar skillnaden mellan Exempel Excel-filen och Utdata-PDF för referens.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Exempelkod**

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
