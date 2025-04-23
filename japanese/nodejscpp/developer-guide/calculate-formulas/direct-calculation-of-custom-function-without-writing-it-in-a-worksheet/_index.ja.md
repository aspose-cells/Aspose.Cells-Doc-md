---
title: Node.jsをC++経由でカスタム関数をワークシートに記述せずに直接計算する
linktitle: ワークシートに書き込まずにカスタム関数を直接計算する
description: この記事では、Node.jsをC++経由で使用して、Excelのワークシートに関数を書き込まずにカスタム関数を直接計算する方法を紹介します。既存のExcelファイルを読み込むか新規作成し、カスタム関数を計算し、変更したファイルを保存します。
keywords: Aspose.Cells、Excel、カスタム関数、直接計算、Node.jsをC++経由で、書き込む必要なし、ワークシート
type: docs
weight: 90
url: /ja/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **ワークシートに書き込まずにカスタム機能を直接計算する**

このトピックでは、ワークシートに書き込むことなく直接カスタム関数を計算する方法を説明します。これには、[**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-CalculationOptions-)メソッドを使用してください。

このメソッドの利用法を示す次のサンプルコードをご覧ください。私たちは自社のカスタム関数MyCompany.CustomFunction()を使用し、計算エンジンによって"Aspose.Cells."としてその値を計算し、最終的な計算値として"Welcome to Aspose.Cells."が返されます。コードに示されている通り、カスタム機能をワークシートに書き込んでいないことがわかりますが、カスタムロジックで直接計算されています。

### **プログラミングサンプル**

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomEngine extends AsposeCells.AbstractCalculationEngine {
// Override the Calculate method with custom logic
calculate(data) {
// Check the formula name and calculate it yourself
if (data.getFunctionName() === "MyCompany.CustomFunction") {
// This is our calculated value
data.setCalculatedValue("Aspose.Cells.");
}
}
}

class ImplementDirectCalculationOfCustomFunction {
static run() {
// Create a workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Add some text in cell A1
ws.getCells().get("A1").putValue("Welcome to ");

// Create a calculation options with custom engine
const opts = new AsposeCells.CalculationOptions();
opts.setCustomEngine(new CustomEngine());

// This line shows how you can call your own custom function without
// a need to write it in any worksheet cell
// After the execution of this line, it will return
// Welcome to Aspose.Cells.
const ret = ws.calculateFormula("=A1 & MyCompany.CustomFunction()", opts);

// Print the calculated value
console.log("Calculated Value: " + ret);
}
}

// Example invocation
ImplementDirectCalculationOfCustomFunction.run();
```

### **コンソール出力**

上記のサンプルコードのコンソール出力は以下の通りです。

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **関連記事**

{{% alert color="primary" %}}

[Aspose.Cellsのデフォルト計算エンジンを拡張するためのカスタム計算エンジンの実装](/cells/ja/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
