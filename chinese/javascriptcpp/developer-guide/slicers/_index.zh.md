---
title: 插入切片器
linktitle: 切片器
type: docs
weight: 170
url: /zh/javascript-cpp/create-slicer/
description: 通过C++管理带有Aspose.Cells for JavaScript的Excel文件的切片器。
---

## **可能的使用场景**

切片器用于快速筛选数据。它可以用于筛选表格或数据透视表中的数据。Microsoft Excel允许您通过选择表格或数据透视表，然后点击 *插入 > 切片器* 来创建切片器。Aspose.Cells for JavaScript via C++还允许您使用 [**Worksheet.slicers.add()**](https://reference.aspose.com/cells/javascript-cpp/slicercollection/#add-pivottable-string-string-) 方法创建切片器。

## **为数据透视表创建切片器**

请查看以下示例代码。它加载包含数据透视表的[示例Excel文件](67338470.xlsx)，然后基于第一个基础数据透视字段创建切片器，最后将工作簿保存为[输出 XLSX](67338471.xlsx)和[输出 XLSB](67338472.xlsb)格式。下图显示了由Aspose.Cells for JavaScript via C++在输出Excel文件中创建的切片器。

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Create Slicer to PivotTable</title>
    </head>
    <body>
        <h1>Create Slicer to PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.csv" />
        <button id="runExample">Run Example</button>
        <br/><br/>
        <a id="downloadXlsxLink" style="display: none;">Download XLSX Result</a>
        <br/>
        <a id="downloadXlsbLink" style="display: none;">Download XLSB Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (e.g., sampleCreateSlicerToPivotTable.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Access first pivot table inside the worksheet.
            const pt = ws.pivotTables.get(0);

            // Add slicer relating to pivot table with first base field at cell B22.
            const idx = ws.slicers.add(pt, "B22", pt.baseFields.get(0));

            // Access the newly added slicer from slicer collection.
            const slicer = ws.slicers.get(idx);

            // Save the workbook in output XLSX format.
            const outputDataXlsx = wb.save(SaveFormat.Xlsx);
            const blobXlsx = new Blob([outputDataXlsx]);
            const downloadXlsxLink = document.getElementById('downloadXlsxLink');
            downloadXlsxLink.href = URL.createObjectURL(blobXlsx);
            downloadXlsxLink.download = 'outputCreateSlicerToPivotTable.xlsx';
            downloadXlsxLink.style.display = 'inline';
            downloadXlsxLink.textContent = 'Download outputCreateSlicerToPivotTable.xlsx';

            // Save the workbook in output XLSB format.
            const outputDataXlsb = wb.save(SaveFormat.Xlsb);
            const blobXlsb = new Blob([outputDataXlsb]);
            const downloadXlsbLink = document.getElementById('downloadXlsbLink');
            downloadXlsbLink.href = URL.createObjectURL(blobXlsb);
            downloadXlsbLink.download = 'outputCreateSlicerToPivotTable.xlsb';
            downloadXlsbLink.style.display = 'inline';
            downloadXlsbLink.textContent = 'Download outputCreateSlicerToPivotTable.xlsb';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer created and files are ready for download.</p>';
        });
    </script>
</html>
```

## **为Excel表创建切片器**

请查看以下示例代码。它加载包含数据表的[sample Excel file](sampleCreateSlicerToExcelTable.xlsx)，然后基于第一列创建切片器。最后，将工作簿保存为[output XLSX](outputCreateSlicerToExcelTable.xlsx)格式。

### **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Create Slicer to Excel Table Example</title>
    </head>
    <body>
        <h1>Create Slicer to Excel Table Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        let asposeReady = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            asposeReady = true;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            if (!asposeReady) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first table inside the worksheet.
            const table = worksheet.listObjects.get(0);

            // Add slicer
            const idx = worksheet.slicers.add(table, 0, "H5");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCreateSlicerToExcelTable.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
