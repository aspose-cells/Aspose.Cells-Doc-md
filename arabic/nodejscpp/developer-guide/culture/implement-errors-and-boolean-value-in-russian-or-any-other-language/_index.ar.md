---
title: تنفيذ الأخطاء وقيم Boolean باللغة الروسية أو أي لغة أخرى باستخدام Node.js عبر C++
linktitle: تنفيذ الأخطاء وقيمة بوليانية باللغة الروسية أو أي لغة أخرى
type: docs
weight: 40
url: /ar/nodejs-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: تعلم كيفية تنفيذ الأخطاء وقيم Boolean بلغات مختلفة باستخدام Aspose.Cells for Node.js via C++. 
---

## **سيناريوهات الاستخدام المحتملة**

 إذا كنت تستخدم Microsoft Excel بالحدود المحلية أو اللغة الروسية أو أي لغة أو منطقة أخرى، فسيعرض الأخطاء وقيم Boolean وفقًا لذلك. يمكنك تحقيق سلوك مشابه باستخدام Aspose.Cells for Node.js via C++ من خلال استخدام خاصية [**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--). ستحتاج إلى تجاوز الطرق التالية لفئة [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings).

- [**GlobalizationSettings.getErrorValueString(string)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getErrorValueString-string-)
- [**GlobalizationSettings.getBooleanValueString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getBooleanValueString-boolean-)

## **تنفيذ الأخطاء والقيمة البوليانية باللغة الروسية أو أي لغة أخرى**

الشيفرة النموذجية التالية توضح كيفية تنفيذ الأخطاء والقيمة البوليانية باللغة الروسية أو أي لغة أخرى. يرجى التحقق من [ملف الإكسل النموذجي](73990159.xlsx) المستخدم في هذا الشيفرة و [PDF الناتج](73990160.pdf) الخاص به. تُظهر اللقطة الفوتوغرافية الفرق بين ملف الإكسل النموذجي والملف الناتج بصيغة PDF للرجوع إليها.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **الكود المثالي**

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
