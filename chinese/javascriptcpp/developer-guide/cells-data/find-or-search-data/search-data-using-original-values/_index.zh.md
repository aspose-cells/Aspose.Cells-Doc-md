---
title: 使用原始值搜索数据
type: docs
weight: 380
url: /zh/javascript-cpp/search-data-using-original-values/
description: 学习如何通过Aspose.Cells for JavaScript通过C++ API使用原始值进行数据搜索。
keywords: 通过C++的JavaScript API使用原始值搜索数据，使用JavaScript通过C++查找数据，使用JavaScript通过C++根据原始值搜索数据，使用JavaScript通过C++查找数据。
---

{{% alert color="primary" %}}  

有时，数据的值因为以某种方式格式化而被隐藏。例如，假设单元格 D4 公式为 =Sum(A1:A2) 并且其值为 20 但格式为---，那么值 20 将被隐藏，并且无法使用 Microsoft Excel 查找选项找到。但是，您可以使用 Aspose.Cells 使用 [**LookInType.OriginalValues**](https://reference.aspose.com/cells/javascript-cpp/lookintype) 找到它  

{{% /alert %}}  

以下示例代码说明了上述观点。它会找到无法使用Microsoft Excel的查找选项找到的单元格D4，但Aspose.Cells可以使用[**LookInType.OriginalValues**](https://reference.aspose.com/cells/javascript-cpp/lookintype)找到它。请阅读代码内的注释以获取更多信息。  

## 使用原始值搜索数据的JavaScript示例代码  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Formatted Value</title>
    </head>
    <body>
        <h1>Find Formatted Value Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FindOptions, Worksheet, Cell, Utils } = AsposeCells;

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add 10 in cell A1 and A2
            worksheet.cells.get("A1").value = 10;
            worksheet.cells.get("A2").value = 10;

            // Add Sum formula in cell D4 but customize it as ---
            const cell = worksheet.cells.get("D4");

            let style = cell.style;
            style.custom = "---";
            cell.style = style;

            // The result of formula will be 20 but 20 will not be visible because the cell is formatted as ---
            cell.formula = "=Sum(A1:A2)";

            // Calculate the workbook
            workbook.calculateFormula();

            // Create find options, we will search 20 using original values otherwise 20 will never be found because it is formatted as ---
            const options = new FindOptions();
            options.lookInType = AsposeCells.LookInType.OriginalValues;
            options.lookAtType = AsposeCells.LookAtType.EntireContent;

            let foundCell = null;
            const obj = 20;

            // Find 20 which is Sum(A1:A2) and formatted as ---
            foundCell = worksheet.cells.find(obj, foundCell, options);

            // Print the found cell to the page
            const resultDiv = document.getElementById('result');
            if (foundCell) {
                resultDiv.innerHTML = `<p style="color: green;">Found cell: ${foundCell.name}, value: ${foundCell.value}</p>`;
            } else {
                resultDiv.innerHTML = `<p style="color: red;">Cell not found.</p>`;
            }

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';
        });
    </script>
</html>
```


## 示例代码生成的控制台输出  



{{< highlight java >}}  

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]  

{{< /highlight >}}
