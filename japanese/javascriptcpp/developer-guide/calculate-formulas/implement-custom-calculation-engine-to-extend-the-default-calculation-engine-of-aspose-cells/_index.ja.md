---
title: JavaScriptを介したC++を使用して、Aspose.Cellsのデフォルト計算エンジンを拡張するカスタム計算エンジンを実装します。既存のExcelファイルを読み込むか、新しいExcelファイルを作成して、提供されるメソッドを使用し、変更後のExcelファイルを保存します。
linktitle: Aspose.Cellsのデフォルトの計算エンジンを拡張するためにカスタム計算エンジンを実装する
description: この文章では、JavaScriptを用いてAspose.CellsライブラリをC++で操作し、デフォルトの計算エンジンを拡張する方法について説明します。既存のExcelファイルを読み込むか新規作成し、提供されたメソッドを利用して、修正されたExcelファイルを保存します。
keywords: Aspose.Cells、Excel、カスタム計算エンジン、JavaScriptを介したC++
type: docs
weight: 80
url: /ja/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **カスタム計算エンジンの実装**

Aspose.CellsにはほとんどすべてのMicrosoft Excel式を計算できる強力な計算エンジンがあります。それにもかかわらず、デフォルトの計算エンジンを拡張することが可能であり、より大きな力と柔軟性を提供します。

この機能の実装に使用される次のプロパティとクラスは次のとおりです。

- [**CalculationOptions.customEngine**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#customEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/javascript-cpp/calculationdata)

以下のコードはカスタム計算エンジンの実装例です。インターフェース[**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine)を実装し、[**calculate(CalculationData data)**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine/#calculate-calculationdata-)メソッドを持ちます。このメソッドはすべての数式に対して呼び出されます。この中で、**TODAY**関数を検出し、システム日付に1日を加えます。例えば現在の日付が2023年7月27日の場合、カスタムエンジンはTODAY()を2023年7月28日として計算します。

### **プログラミングサンプル**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Custom Calculation Engine Example</title>
    </head>
    <body>
        <h1>Custom Calculation Engine Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CalculationOptions, CellsHelper } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').disabled = false;
        });

        // Create a new class derived from AbstractCalculationEngine
        class CustomEngine extends AsposeCells.AbstractCalculationEngine {
            constructor() {
                super();
                // Indicate processing built-in functions
                this.processBuiltInFunctions = true;
            }

            // Override the Calculate method with custom logic
            calculate(data) {
                // Check the formula name and change the implementation
                if (data.functionName.toUpperCase() === "TODAY") {
                    // Assign the CalculationData.CalculatedValue: add one day offset for the date
                    data.calculatedValue = CellsHelper.getDoubleFromDateTime(new Date(), false) + 1.0;
                }
            }
        }

        class ImplementCustomCalculationEngine {
            static run() {
                // Create an instance of Workbook
                const workbook = new Workbook();

                // Access first Worksheet from the collection
                const sheet = workbook.worksheets.get(0);

                // Access Cell A1 and put a formula to sum values of B1 to B2
                const a1 = sheet.cells.get("A1");
                const style = a1.style;
                style.number = 14;
                a1.style = style;

                a1.formula = "=TODAY()";

                // Calculate all formulas in the Workbook 
                workbook.calculateFormula();

                // The result of A1 with default calculation engine
                console.log("The value of A1 with default calculation engine: " + a1.stringValue);

                // Create an instance of CustomEngine
                const engine = new CustomEngine();

                // Create an instance of CalculationOptions
                const opts = new CalculationOptions();

                // Assign the CalculationOptions.CustomEngine property to the instance of CustomEngine
                opts.customEngine = engine;

                // Recalculate all formulas in Workbook using the custom calculation engine
                workbook.calculateFormula(opts);

                // The result of A1 with custom calculation engine
                console.log("The value of A1 with custom calculation engine: " + a1.stringValue);

                console.log("Press any key to continue...");

                document.getElementById('result').innerHTML = '<p style="color: green;">Calculation completed. Check console for output.</p>';
            }
        }

        document.getElementById('runExample').addEventListener('click', () => {
            ImplementCustomCalculationEngine.run();
        });
    </script>
</html>
```

### **結果**

上記サンプルコードのコンソール出力を確認してください。カスタムエンジンを使用したA1の値（日付時刻）は、通常の結果より1日遅くなっているはずです。

### **関連記事**

{{% alert color="primary" %}}

[ワークシートに書き込まずにカスタム関数を直接計算する方法](/cells/ja/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
