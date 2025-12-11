---
title: Implement Errors and Boolean Values in Russian or Any Other Language with Node.js via C++
linktitle: Implement Errors and Boolean Values in Russian or Any Other Language
type: docs
weight: 40
url: /nodejs-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Learn how to implement errors and Boolean values in different languages using Aspose.Cells for Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

If you are using Microsoft Excel in the Russian locale or language, or any other locale or language, it will display errors and Boolean values according to that locale or language. You can achieve a similar behavior using Aspose.Cells for Node.js via C++ by using the [**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--) property. You will have to override the following methods of the [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) class.

- [**GlobalizationSettings.getErrorValueString(string)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getErrorValueString-string-)
- [**GlobalizationSettings.getBooleanValueString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getBooleanValueString-boolean-)

## **Implement Errors and Boolean Values in Russian or Any Other Language**

The following sample code illustrates how to implement errors and Boolean values in Russian or any other language. Please check the [Sample Excel File](73990159.xlsx) used in this code and its [Output PDF](73990160.pdf). The screenshot shows the difference between the sample Excel file and the output PDF for reference.

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

        // Set GlobalizationSettings in Russian language
        workbook.getSettings().setGlobalizationSettings(new RussianGlobalization());

        // Calculate the formula
        workbook.calculateFormula();

        // Save the workbook in PDF format
        workbook.save("outputRussianGlobalization.pdf");
    }
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
