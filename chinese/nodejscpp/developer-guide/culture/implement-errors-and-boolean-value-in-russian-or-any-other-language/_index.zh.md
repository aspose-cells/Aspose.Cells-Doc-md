---
title: 用 Node.js 通过 C++ 实现错误和布尔值的本地化（如俄语或其他语言）
linktitle: 以俄语或其他任何语言实现错误和布尔值
type: docs
weight: 40
url: /zh/nodejs-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: 学习如何用 Aspose.Cells for Node.js via C++ 在不同语言环境中实现错误和布尔值。 
---

## **可能的使用场景**

 如果你在使用俄语地区或语言的 Microsoft Excel，错误和布尔值会根据该地区或语言显示。你可以用 Aspose.Cells for Node.js via C++ 实现类似功能，需重写 [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) 类的以下方法。

- [**GlobalizationSettings.getErrorValueString(string)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getErrorValueString-string-)
- [**GlobalizationSettings.getBooleanValueString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getBooleanValueString-boolean-)

## **以俄语或其他任何语言实现错误和布尔值**

以下示例代码说明了如何在俄语或其他任何语言中实现错误和布尔值。请查看此代码中使用的[Sample Excel File](73990159.xlsx)及其[Output PDF](73990160.pdf)。屏幕截图显示了示例Excel文件和输出PDF之间的差异作为参考。

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **示例代码**

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
