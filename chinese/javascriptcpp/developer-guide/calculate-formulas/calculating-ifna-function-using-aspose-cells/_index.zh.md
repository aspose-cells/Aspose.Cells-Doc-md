---
title: 使用 C++ 通过 Script 计算 IFNA 函数 Aspose.Cells for Java
description: 如何使用 Aspose.Cells 库通过 C++ 的 JavaScript 计算 IFNA 函数。加载现有 Excel 文件或创建新文件，并计算 IFNA 函数以获取结果。最后保存修改后的 Excel 文件到磁盘。
keywords: Aspose.Cells，Excel，IFNA 函数，计算，JavaScript via C++
type: docs
weight: 40
url: /zh/javascript-cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells支持计算Excel中的IFNA函数。如果公式返回#N/A错误值，IFNA函数会返回你指定的值，否则返回公式的结果。

{{% /alert %}} 
## **使用 C++  Script 计算 IFNA 函数 Aspose.Cells for Java**
以下示例代码演示了如何使用 C++ Script 计算 IFNA 函数。 


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VLOOKUP IFNA Example</h1>
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

            // Loads the workbook which may contain hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add data for VLOOKUP
            worksheet.cells.get("A1").value = "Apple";
            worksheet.cells.get("A2").value = "Orange";
            worksheet.cells.get("A3").value = "Banana";

            // Access cell A5 and A6
            const cellA5 = worksheet.cells.get("A5");
            const cellA6 = worksheet.cells.get("A6");

            // Assign IFNA formula to A5 and A6
            cellA5.formula = '=IFNA(VLOOKUP("Pear",$A$1:$A$3,1,0),"Not found")';
            cellA6.formula = '=IFNA(VLOOKUP("Orange",$A$1:$A$3,1,0),"Not found")';

            // Calculate the formula of workbook
            workbook.calculateFormula();

            // Get the string values of A5 and A6
            const valueA5 = cellA5.stringValue;
            const valueA6 = cellA6.stringValue;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = `<p style="color: green;">A5: ${valueA5}</p><p style="color: green;">A6: ${valueA6}</p>`;
        });
    </script>
</html>
```
## **控制台输出**


{{< highlight javascript >}}
 Not found

Orange
{{< /highlight >}}
