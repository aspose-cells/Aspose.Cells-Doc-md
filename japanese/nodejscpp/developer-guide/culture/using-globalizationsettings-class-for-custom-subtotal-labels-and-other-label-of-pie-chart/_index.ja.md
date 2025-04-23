---
title: GlobalizationSettingsクラスを使用した、パイチャートのカスタム小計ラベルやその他のラベルのNode.js経由の設定
linktitle: ピーグラフのカスタムサブトータルラベルおよびその他のラベル用のGlobalizationSettingsクラスの使用
type: docs
weight: 70
url: /ja/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: Aspose.Cells for Node.js via C++を使用して小計ラベルや円グラフのその他のラベルをカスタマイズする方法も学びます。
---

## **可能な使用シナリオ**

Aspose.CellsのAPIは、スプレッドシート内で小計のカスタムラベルを使用したい場合のシナリオを処理するための[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)クラスを公開しています。さらに、[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)クラスは、ワークシートやチャートをレンダリングする際に**Other**ラベルを修正するためにも使用できます。

## **GlobalizationSettingsクラスの紹介**

[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)クラスは現在、合計のラベルを取得したり、円グラフの「その他」ラベルのカスタムテキストをレンダリングしたりするためにカスタムクラスでオーバーライドできる次の3つのメソッドを提供しています。

1. [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-): 関数の合計名を取得します。
1. [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-): 関数のグランドトータル名を取得します。


### **サブトータルのカスタムラベル**

[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)クラスは、今後示す[**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-)と[**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-)のメソッドをオーバーライドすることで、サブトータルラベルをカスタマイズするために使用できます。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Defines a custom class derived from GlobalizationSettings class
class CustomSettings extends AsposeCells.GlobalizationSettings {
// Overrides the GetTotalName method
getTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "AVG";
// Handle other cases as per requirement
default:
return super.getTotalName(functionType);
}
}

// Overrides the GetGrandTotalName method
getGrandTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "GRD AVG";
// Handle other cases as per requirement
default:
return super.getGrandTotalName(functionType);
}
}
}
```

カスタムラベルを注入するには、サブトータルをワークシートに追加する前に、上記で定義した**CustomSettings**クラスのインスタンスに[**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--)プロパティを割り当てる必要があります。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// Defines a custom class derived from GlobalizationSettings class
class CustomSettings extends AsposeCells.GlobalizationSettings {
// Overrides the GetTotalName method
getTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "AVG";
// Handle other cases as per requirement
default:
return super.getTotalName(functionType);
}
}

// Overrides the GetGrandTotalName method
getGrandTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "GRD AVG";
// Handle other cases as per requirement
default:
return super.getGrandTotalName(functionType);
}
}
}

try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads an existing spreadsheet containing some data
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Assigns the GlobalizationSettings property of the WorkbookSettings class to a custom class created
workbook.getSettings().setGlobalizationSettings(new CustomSettings());

// Accesses the 1st worksheet from the collection which contains data that resides in the cell range A2:B9
const sheet = workbook.getWorksheets().get(0);

// Adds Subtotal of type Average to the worksheet
sheet.getCells().subtotal(AsposeCells.CellArea.createCellArea("A2", "B9"), 0, AsposeCells.ConsolidationFunction.Average, [1]);

// Calculates Formulas
workbook.calculateFormula();

// Auto fits all columns
sheet.autoFitColumns();

// Saves the workbook on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
} catch (error) {
console.error(`Test failed: ${error.message}`);
throw error;
}
```

{{% alert color="primary" %}}

[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)クラスは、新しいサブトータルを追加するためだけに機能します。既にサブトータルが含まれているスプレッドシートのラベルは変更できません。

{{% /alert %}}

