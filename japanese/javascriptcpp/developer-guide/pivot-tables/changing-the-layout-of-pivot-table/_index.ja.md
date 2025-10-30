---
title: ピボットテーブルのレイアウトを変更する
type: docs
weight: 10
url: /ja/javascript-cpp/changing-the-layout-of-pivot-table/
description: Aspose.Cells for JavaScript via C++でピボットテーブルのレイアウトを変更する方法。
keywords: C++を使用したAspose.Cells for JavaScriptでExcelのピボットテーブルのレイアウトを変更します。
---

## **MS-Excelでのピボットテーブルのレイアウトの変更方法**
Microsoft Excelでは、*PivotTable Tools > Design > Report Layout*メニューコマンドを使用してピボットテーブルのレイアウトを変更できます。これらの3つの形式でレイアウトを変更できます

- コンパクト形式で表示
- アウトライン形式で表示
- 表形式で表示

## **C++を使用したAspose.Cells for JavaScriptでピボットテーブルのレイアウトを変更する方法**
C++ライブラリのAspose.Cells for JavaScriptは、これらの三つの形式でピボットテーブルのレイアウトを変更するための[**PivotTable.showInCompactForm()**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#showInCompactForm--)、[**PivotTable.showInOutlineForm()**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#showInOutlineForm--)、[**PivotTable.showInTabularForm()**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#showInTabularForm--)メソッドも提供します。

## **サンプルコード**
次のサンプルコードでは、まずPivot Tableを**コンパクト形式**で表示し、次に**アウトライン形式**でPivot Tableを表示し、最後にPivot Tableを**表形式**で表示します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Display Forms Example</title>
    </head>
    <body>
        <h1>Pivot Table Display Forms Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none; margin-right: 10px;"></a>
            <a id="downloadLink2" style="display: none; margin-right: 10px;"></a>
            <a id="downloadLink3" style="display: none;"></a>
        </div>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first pivot table
            const pivotTable = worksheet.pivotTables.get(0);

            // 1 - Show the pivot table in compact form
            pivotTable.showInCompactForm();
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save the Compact form output
            const outputData1 = workbook.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'CompactForm_out.xlsx';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download CompactForm_out.xlsx';

            // 2 - Show the pivot table in outline form
            pivotTable.showInOutlineForm();
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save the Outline form output
            const outputData2 = workbook.save(SaveFormat.Xlsx);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'OutlineForm_out.xlsx';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download OutlineForm_out.xlsx';

            // 3 - Show the pivot table in tabular form
            pivotTable.showInTabularForm();
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save the Tabular form output
            const outputData3 = workbook.save(SaveFormat.Xlsx);
            const blob3 = new Blob([outputData3]);
            const downloadLink3 = document.getElementById('downloadLink3');
            downloadLink3.href = URL.createObjectURL(blob3);
            downloadLink3.download = 'TabularForm_out.xlsx';
            downloadLink3.style.display = 'inline-block';
            downloadLink3.textContent = 'Download TabularForm_out.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operations completed. Use the links above to download the modified files.</p>';
        });
    </script>
</html>
```
