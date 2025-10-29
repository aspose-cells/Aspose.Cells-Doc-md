---
title: 不用在工作表中编写，直接用JavaScript用C++进行自定义函数的计算
linktitle: 直接计算自定义函数，无需先将其编写在工作表中
description: 本文介绍如何使用Aspose.Cells库，允许用JavaScript用C++在Microsoft Excel中直接计算自定义函数，无需在工作表中编写函数。加载现有Excel文件或新建一个，计算自定义函数，并保存修改后的文件。
keywords: Aspose.Cells，Excel，自定义函数，直接计算，JavaScript用C++，无需写入，工作表
type: docs
weight: 90
url: /zh/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **在不将其写入工作表的情况下直接计算自定义函数**

本主题介绍如何在不先写入工作表的情况下直接计算自定义函数。请使用[**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-CalculationOptions-)方法实现此目的。

请参阅以下示例代码，演示了如何使用此方法。我们使用了一个名为 MyCompany.CustomFunction() 的自定义函数，并且通过自己的自定义逻辑计算其值为 "Aspose.Cells."，然后该值由计算引擎自动地与单元格 A1 的值 "Welcome to " 进行连接，最终计算的值返回为 "Welcome to Aspose.Cells."。从代码中可以看到，我们并未在工作表中编写自定义函数，而是直接通过我们自己的自定义逻辑进行计算。

### **编程示例**

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

### **控制台输出**

以下是上面示例代码的控制台输出。

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **相关文章**

{{% alert color="primary" %}}

[实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎](/cells/zh/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
