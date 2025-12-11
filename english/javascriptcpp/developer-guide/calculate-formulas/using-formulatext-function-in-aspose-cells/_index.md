---  
title: Using FormulaText function in Aspose.Cells for JavaScript via C++  
linktitle: Using FormulaText function in Aspose.Cells  
description: This article introduces how to use the FormulaText function in the Aspose.Cells library to process formulas in Microsoft Excel. Learn to get and set the formula text of cells and save modified Excel files using JavaScript via C++.  
keywords: Aspose.Cells, Excel, FormulaText function, JavaScript via C++  
type: docs  
weight: 60  
url: /javascript-cpp/using-formulatext-function-in-aspose-cells/  
---  

{{% alert color="primary" %}}  

FormulaText is an Excel 2013 and later function. It is not supported by previous versions like Excel 2010 or 2007, etc. As its name suggests, it prints the text of the formula that is present in a given cell. This article will show you how to make use of this function using Aspose.Cells for JavaScript via C++.  

{{% /alert %}}  

The following sample code shows the usage of FormulaText with Aspose.Cells for JavaScript via C++. The code first writes a formula in cell A1 and then prints the text of the formula using FormulaText in cell A2.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - FormulaText</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some formula in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.formula = "=Sum(B1:B10)";

            // Get the text of the formula in cell A2 using FORMULATEXT function
            const cellA2 = worksheet.cells.get("A2");
            cellA2.formula = "=FormulaText(A1)";

            // Calculate the workbook
            workbook.calculateFormula();

            // Print the results of A2; it will now print the text of the formula inside cell A1
            console.log(cellA2.stringValue);

            resultDiv.innerHTML = `<p style="color: green;">Operation completed successfully! Formula text: ${cellA2.stringValue}</p>`;
        });
    </script>
</html>
```  

## **Console Output**  

{{< highlight java >}}  
=SUM(B1:B10)  
{{< /highlight >}}