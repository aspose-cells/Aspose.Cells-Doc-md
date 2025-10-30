---
title: ワークシートに書き込まずにJavaScriptを介してカスタム関数を直接計算する方法
linktitle: ワークシートに書き込まずにカスタム関数を直接計算する
description: この記事では、JavaScriptを介したC++でAspose.Cellsライブラリを使用し、ワークシートに関数を書き込まずにMicrosoft Excel内でカスタム関数を直接計算する方法を紹介します。既存のExcelファイルを読み込むか、新しいファイルを作成してカスタム関数を計算し、変更後のファイルを保存します。
keywords: Aspose.Cells、Excel、カスタム関数、直接計算、JavaScriptを介したC++、書き込み不要、ワークシート
type: docs
weight: 90
url: /ja/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **ワークシートに書き込まずにカスタム機能を直接計算する**

このトピックでは、ワークシートに書き込むことなく直接カスタム関数を計算する方法を説明します。これには、[**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-CalculationOptions-)メソッドを使用してください。

このメソッドの利用法を示す次のサンプルコードをご覧ください。私たちは自社のカスタム関数MyCompany.CustomFunction()を使用し、計算エンジンによって"Aspose.Cells."としてその値を計算し、最終的な計算値として"Welcome to Aspose.Cells."が返されます。コードに示されている通り、カスタム機能をワークシートに書き込んでいないことがわかりますが、カスタムロジックで直接計算されています。

### **プログラミングサンプル**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Custom Function Example</title>
    </head>
    <body>
        <h1>Implement Direct Calculation Of Custom Function</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AbstractCalculationEngine, CalculationOptions } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        class CustomEngine extends AbstractCalculationEngine {
            // Override the calculate method with custom logic
            calculate(data) {
                // Check the formula name and calculate it yourself
                if (data.functionName === "MyCompany.CustomFunction") {
                    // This is our calculated value
                    data.calculatedValue = "Aspose.Cells.";
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Add some text in cell A1
            ws.cells.get("A1").putValue("Welcome to ");

            // Create a calculation options with custom engine
            const opts = new CalculationOptions();
            opts.customEngine = new CustomEngine();

            // This line shows how you can call your own custom function without
            // a need to write it in any worksheet cell
            // After the execution of this line, it will return
            // Welcome to Aspose.Cells.
            const ret = ws.calculateFormula("=A1 & MyCompany.CustomFunction()", opts);

            // Write the returned value into B1 for demonstration
            ws.cells.get("B1").putValue(ret);

            // Prepare download of the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculated Value: ' + ret + '</p>';
        });
    </script>
</html>
```

### **コンソール出力**

上記のサンプルコードのコンソール出力は以下の通りです。

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **関連記事**

{{% alert color="primary" %}}

[カスタム計算エンジンを実装して、Aspose.Cellsのデフォルト計算エンジンを拡張する](/cells/ja/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
