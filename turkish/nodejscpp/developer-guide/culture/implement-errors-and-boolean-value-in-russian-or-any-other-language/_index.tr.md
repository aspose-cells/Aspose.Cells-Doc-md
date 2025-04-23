---
title: Node.js ve C++ kullanarak Rusça veya başka herhangi bir dilde Hata ve Boolean Değerlerini Uygarlıklar ile uygulayın
linktitle: Rusça veya başka bir dilde Hataları ve Boolean Değerleri Uygulayın
type: docs
weight: 40
url: /tr/nodejs-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Aspose.Cells for Node.js via C++ kullanarak farklı dillerde Hatalar ve Boolean değerlerini nasıl uygulayacağınızı öğrenin. 
---

## **Olası Kullanım Senaryoları**

Eğer Rusça veya başka herhangi bir dilde Microsoft Excel kullanıyorsanız, Hatalar ve Boolean değerleri o dile göre gösterilecektir. Bunu, [**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--) özelliğini kullanarak Aspose.Cells for Node.js via C++ ile benzer bir davranış elde edebilirsiniz. [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) sınıfının aşağıdaki metodlarını geçersiz kılmanız gerekir.

- [**GlobalizationSettings.getErrorValueString(string)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getErrorValueString-string-)
- [**GlobalizationSettings.getBooleanValueString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getBooleanValueString-boolean-)

## **Rusça veya Başka Bir Dilde Hataları ve Boolean Değerleri Uygulayın**

Aşağıdaki örnek kod, Rusça veya başka bir dilde Hataları ve Boolean Değerleri nasıl uygulayacağınızı göstermektedir. Bu kodda kullanılan bu [Örnek Excel Dosyasını](73990159.xlsx) ve [Çıktı PDF](73990160.pdf) dosyasını kontrol edin. Ekran görüntüsü, Örnek Excel Dosyası ile Çıktı PDF arasındaki farkı göstermektedir.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Örnek Kod**

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
