---
title: Node.jsを使ったC++経由でのエラーとブール値のロシア語またはその他の言語での実装
linktitle: ロシア語または他の言語でエラーおよび真偽値を実装する
type: docs
weight: 40
url: /ja/nodejs-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Aspose.Cells for Node.js via C++を使用して、異なる言語でエラーとブール値を実装する方法を学びましょう。 
---

## **可能な使用シナリオ**

Microsoft Excelをロシア語ロケールや他のロケールや言語で使用している場合、それに応じてエラーとブール値が表示されます。これに似た動作はAspose.Cells for Node.js via C++を使い[**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--)プロパティで実現できます。[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)クラスの以下のメソッドをオーバーライドする必要があります。

- [**GlobalizationSettings.getErrorValueString(string)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getErrorValueString-string-)
- [**GlobalizationSettings.getBooleanValueString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getBooleanValueString-boolean-)

## **ロシア語または他の言語でエラーおよび真偽値を実装する**

下記のサンプルコードは、ロシア語または他の言語でのエラーおよび真偽値の実装方法を説明しています。このコードで使用される [サンプルExcelファイル](73990159.xlsx) およびその [出力PDF](73990160.pdf) を確認してください。スクリーンショットは、サンプルExcelファイルと出力PDFの違いを参照用に示しています。

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **サンプルコード**

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
