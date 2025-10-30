---
title: JavaScriptを通じてセルの切り取りと貼り付け
linktitle: 範囲の切り取りと貼り付け
type: docs
weight: 130
url: /ja/javascript-cpp/cut-and-paste-cells/
description: Aspose.Cells for JavaScriptを使ったワークシート内のセルのカットアンドペースト方法を学びます。
---

## **セルの切り取りと貼り付け**

Aspose.Cells for JavaScriptは、[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells/)コレクションの[**InsertCutCells**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertCutCells-Range-number-number-ShiftType-)メソッドを使用して、ワークシート内のセルを切り取り貼り付ける能力を提供します。[**InsertCutCells**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertCutCells-Range-number-number-ShiftType-)は以下のパラメータを受け入れます。  

- [**Range**](https://reference.aspose.com/cells/javascript-cpp/range/): 切り取るセルの範囲  
- 行インデックス: セルを挿入する行のインデックス  
- 列インデックス: セルを挿入する列のインデックス  
- [**ShiftType**](https://reference.aspose.com/cells/javascript-cpp/shifttype/): 列のシフト方向  

次の例は、ワークシート内でセルを切り取り、貼り付ける方法を示しています。  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Cut and Paste Cells Example</title>
    </head>
    <body>
        <h1>Cut and Paste Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ShiftType } = AsposeCells;

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

            // Create a new workbook
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);

            // Set cell values (columns are zero-based; C is column 2)
            worksheet.cells.get(0, 2).value = 1;
            worksheet.cells.get(1, 2).value = 2;
            worksheet.cells.get(2, 2).value = 3;
            worksheet.cells.get(2, 3).value = 4;

            // Create a named range for the block starting at row 0, column 2, 3 rows, 1 column
            worksheet.cells.createRange(0, 2, 3, 1).name = "NamedRange";

            // Create a range for entire column C and cut/paste it
            const cut = worksheet.cells.createRange("C:C");
            worksheet.cells.insertCutCells(cut, 0, 1, ShiftType.Right);

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CutAndPasteCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
