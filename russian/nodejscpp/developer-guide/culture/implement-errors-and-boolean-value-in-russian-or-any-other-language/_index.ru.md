---
title: Реализуйте Ошибки и Булевы значения на русском или любом другом языке с помощью Node.js через C++
linktitle: Реализация ошибок и логических значений на русском или на любом другом языке
type: docs
weight: 40
url: /ru/nodejs-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Узнайте, как реализовать Ошибки и булевы значения на разных языках, используя Aspose.Cells for Node.js via C++. 
---

## **Возможные сценарии использования**

Если вы используете Microsoft Excel на русском или другом языке, он будет отображать ошибки и булевы значения в соответствии с этим языком. Вы можете добиться подобного поведения, используя Aspose.Cells for Node.js via C++ и свойство [**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--). Вам потребуется переопределить следующие методы класса [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings).

- [**GlobalizationSettings.getErrorValueString(string)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getErrorValueString-string-)
- [**GlobalizationSettings.getBooleanValueString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getBooleanValueString-boolean-)

## **Реализация ошибок и логических значений на русском или на любом другом языке**

Приведенный ниже образец кода иллюстрирует, как реализовать ошибки и логические значения на русском или на любом другом языке. Пожалуйста, проверьте [используемый образец файл Excel](73990159.xlsx) в этом коде и его [выходной PDF](73990160.pdf). На скриншоте показано различие между образцом файла Excel и выходным PDF для справки.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Образец кода**

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
