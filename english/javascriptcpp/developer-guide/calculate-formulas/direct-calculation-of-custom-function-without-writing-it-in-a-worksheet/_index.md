---
title: Direct calculation of custom function without writing it in a worksheet with JavaScript via C++
linktitle: Direct calculation of custom function without writing it in a worksheet
description: This article introduces how to use Aspose.Cells library to directly calculate custom functions in Microsoft Excel without writing the function in a worksheet using JavaScript via C++. Load an existing Excel file or create a new one, calculate the custom function, and save the modified file.
keywords: Aspose.Cells, Excel, custom functions, direct calculations, JavaScript via C++, no need to write, worksheets
type: docs
weight: 90
url: /javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Direct calculation of custom function without writing it in a worksheet**

This topic explains how you can directly calculate your custom functions without first writing them in a worksheet. Please use the [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-CalculationOptions-) method for this purpose.

Please see the following sample code that illustrates the usage of this method. We use a custom function named `MyCompany.CustomFunction()` and calculate its value as `"Aspose.Cells."` ourselves. This value is then automatically concatenated with the value of cell **A1**, which is `"Welcome to "`, by the calculation engine, and the final calculated result is `"Welcome to Aspose.Cells."`. As you can see, we have not written our custom function in any worksheet; it is calculated directly by our custom logic.

### **Programming Sample**

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
            // the need to write it in any worksheet cell
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

### **Console Output**

Below is the console output of the above sample code.

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Related Article**

{{% alert color="primary" %}}

[Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells](/cells/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}