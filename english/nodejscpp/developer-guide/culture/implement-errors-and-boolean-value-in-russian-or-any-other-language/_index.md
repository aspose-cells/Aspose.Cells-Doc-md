---
title: Implement Errors and Boolean Value in Russian or Any Other Language with Node.js via C++
linktitle: Implement Errors and Boolean Value in Russian or Any Other Language
type: docs
weight: 40
url: /nodejs-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Learn how to implement Errors and Boolean values in different languages using Aspose.Cells for Node.js via C++. 
---

## **Possible Usage Scenarios**

If you are using Microsoft Excel in Russian Locale or Language or any other Locale or Language, it will display Errors and Boolean values according to that Locale or Language. You can achieve a similar behavior using Aspose.Cells for Node.js via C++ by using the [**Workbook.settings.globalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#globalizationSettings) property. You will have to override the following methods of the [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) class.

- [**GlobalizationSettings.getErrorValueString()**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getErrorValueString)
- [**GlobalizationSettings.getBooleanValueString()**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getBooleanValueString)

## **Implement Errors and Boolean Value in Russian or Any Other Language**

The following sample code illustrates how to implement Errors and Boolean Value in Russian or Any Other Language. Please check the [Sample Excel File](73990159.xlsx) used in this code and its [Output PDF](73990160.pdf). The screenshot shows the difference between Sample Excel File and the Output PDF for a reference.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Sample Code**

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
