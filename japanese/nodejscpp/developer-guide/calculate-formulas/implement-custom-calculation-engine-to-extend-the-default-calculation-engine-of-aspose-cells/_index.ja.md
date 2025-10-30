---
title: Node.jsをC++経由で使用してAspose.Cellsのデフォルト計算エンジンを拡張するカスタム計算エンジンの実装
linktitle: Aspose.Cellsのデフォルトの計算エンジンを拡張するためにカスタム計算エンジンを実装する
description: この記事では、Node.jsをC++経由で使用してAspose.Cellsライブラリのためのカスタム計算エンジンを実装し、デフォルトの計算エンジンを拡張する方法を説明します。既存のExcelファイルを読み込むか新規作成し、提供されたメソッドを使用して編集後のExcelファイルを保存します。
keywords: Aspose.Cells、Excel、カスタム計算エンジン、Node.jsをC++経由で
type: docs
weight: 80
url: /ja/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **カスタム計算エンジンの実装**

Aspose.CellsにはほとんどすべてのMicrosoft Excel式を計算できる強力な計算エンジンがあります。それにもかかわらず、デフォルトの計算エンジンを拡張することが可能であり、より大きな力と柔軟性を提供します。

この機能の実装に使用される次のプロパティとクラスは次のとおりです。

- [**CalculationOptions.getCustomEngine()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getCustomEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/nodejs-cpp/calculationdata)

以下のコードはカスタム計算エンジンの実装例です。インターフェース[**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine)を実装し、[**calculate(CalculationData data)**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine/#calculate-calculationdata-)メソッドを持ちます。このメソッドはすべての数式に対して呼び出されます。この中で、**TODAY**関数を検出し、システム日付に1日を加えます。例えば現在の日付が2023年7月27日の場合、カスタムエンジンはTODAY()を2023年7月28日として計算します。

### **プログラミングサンプル**

```javascript
const AsposeCells = require("aspose.cells.node");

// Create a new class derived from AbstractCalculationEngine
class CustomEngine extends AsposeCells.AbstractCalculationEngine {
// Override the Calculate method with custom logic
calculate(data) {
// Check the formula name and change the implementation
if (data.getFunctionName().toUpperCase() === "TODAY") {
// Assign the CalculationData.CalculatedValue: add one day offset for the date
data.setCalculatedValue(AsposeCells.CellsHelper.getDoubleFromDateTime(new Date(), false) + 1.0);
}
}
getProcessBuiltInFunctions() {
return true;
}
}

class ImplementCustomCalculationEngine {
static run() {
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook();

// Access first Worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Access Cell A1 and put a formula to sum values of B1 to B2
const a1 = sheet.getCells().get("A1");
const style = a1.getStyle();
style.setNumber(14);
a1.setStyle(style);

a1.setFormula("=TODAY()");

// Calculate all formulas in the Workbook 
workbook.calculateFormula();

// The result of A1 should be 20 as per default calculation engine
console.log("The value of A1 with default calculation engine: " + a1.getStringValue());

// Create an instance of CustomEngine
const engine = new CustomEngine();

// Create an instance of CalculationOptions
const opts = new AsposeCells.CalculationOptions();

// Assign the CalculationOptions.CustomEngine property to the instance of CustomEngine
opts.setCustomEngine(engine);

// Recalculate all formulas in Workbook using the custom calculation engine
workbook.calculateFormula(opts);

// The result of A1 will be 50 as per custom calculation engine
console.log("The value of A1 with custom calculation engine: " + a1.getStringValue());

console.log("Press any key to continue...");
}
}

// Call the run method to execute the example
ImplementCustomCalculationEngine.run();
```

### **結果**

上記サンプルコードのコンソール出力を確認してください。カスタムエンジンを使用したA1の値（日付時刻）は、通常の結果より1日遅くなっているはずです。

### **関連記事**

{{% alert color="primary" %}}

[ワークシートに書き込まずにカスタム関数を直接計算](/cells/ja/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
