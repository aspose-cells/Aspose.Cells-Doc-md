---
title: AbstractCalculationEngineを使用して値の範囲を返すNode.jsをC++経由の例
linktitle: AbstractCalculationEngineを使用して値の範囲を返す
description: この記事では、Aspose.Cellsライブラリを使用してNode.jsをC++経由でExcel内の値の範囲を返す抽象計算エンジンの方法を紹介します。Excelファイルを読み込むか作成し、変更をディスクに保存する方法を学びます。
keywords: Aspose.Cells、Excel、値を返す抽象計算エンジン、Node.jsをC++経由で、カスタム関数
type: docs
weight: 55
url: /ja/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cellsは、Microsoft Excelの組み込み関数としてサポートされていないユーザー定義またはカスタム関数を実装するために使用される[**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine)クラスを提供します。

この記事では、[**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine)から値の範囲を返す方法について説明します。

{{% /alert %}}

以下のコードは、[**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine)クラスの使用例を示し、そのメソッドを通じて値の範囲を返します。

*calculateCustomFunction*という関数を持つクラスを作成します。このクラスは [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) を実装します。

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomFunctionStaticValue extends AsposeCells.AbstractCalculationEngine {
calculate(data) {
data.setCalculatedValue([
[new Date(2015, 5, 12, 10, 6, 30), 2],
[3.0, "Test"]
]);
}
}
```

上記の関数をプログラムで使用します。

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomFunctionStaticValue extends AsposeCells.AbstractCalculationEngine {
calculate(data) {
data.setCalculatedValue([
[new Date(2015, 5, 12, 10, 6, 30), 2],
[3.0, "Test"]
]);
}
}

try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const workbook = new AsposeCells.Workbook();
const cells = workbook.getWorksheets().get(0).getCells();

// Set formula
const cell = cells.get(0, 0);
cell.setArrayFormula("=MYFUNC()", 2, 2);

const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);

// Set calculation options for formula
const calculationOptions = new AsposeCells.CalculationOptions();
calculationOptions.setCustomEngine(new CustomFunctionStaticValue());
workbook.calculateFormula(calculationOptions);

// Save to xlsx by setting the calc mode to manual
workbook.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);
workbook.save(dataDir + "output_out.xlsx");

// Save to pdf
workbook.save(dataDir + "output_out.pdf");
} catch (error) {
console.error(`Test failed: ${error.message}`);
throw error;
}
```
