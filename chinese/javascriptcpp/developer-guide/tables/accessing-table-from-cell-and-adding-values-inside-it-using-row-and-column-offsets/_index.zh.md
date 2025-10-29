---
title: 利用 JavaScript 和 C++ 访问单元格中的表格，并通过行列偏移添加值
linktitle: 从单元格访问表格并使用行和列偏移添加值
type: docs
weight: 230
url: /zh/javascript-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}  

通常，您可以使用 [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) 方法向表格或列表对象中添加值。但有时，您可能需要使用行和列偏移向表格或列表对象中添加值。  

要从单元格访问表格或列表对象，使用 [**Cell.table**](https://reference.aspose.com/cells/javascript-cpp/cell/#table--) 属性。若想通过行列偏移在其中添加值，使用 [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/javascript-cpp/listobject/#putCellValue-number-number-object-) 方法。  

{{% /alert %}}  

以下截图显示了代码中使用的源 Excel 文件。文件包含空表格，并突出显示位于表格内的 D5 单元格。我们将利用 [**Cell.table**](https://reference.aspose.com/cells/javascript-cpp/cell/#table--) 属性访问该表格中的 D5 单元格，然后用 [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) 和 [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/javascript-cpp/listobject/#putCellValue-number-number-object-) 方法在其中添加值。  

## 示例  

### 比较源文件和输出文件的截图  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

以下截图显示了代码生成的输出Excel文件。您可以看到单元格D5具有一个值，而位于表格偏移2,2的单元格F6也具有一个值。  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### 使用 JavaScript 通过单元格访问表格并用行列偏移添加值的示例代码  

以下示例代码加载了上面截图中显示的源Excel文件，并向表格内添加值，并生成了上面所示的输出Excel文件。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Accessing Table Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell D5 which lies inside the table
            const cell = worksheet.cells.get("D5");

            // Put value inside the cell D5
            cell.value = "D5 Data";

            // Access the Table from this cell
            const table = cell.table;

            // Add some value using Row and Column Offset
            table.putCellValue(2, 2, "Offset [2,2]");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
