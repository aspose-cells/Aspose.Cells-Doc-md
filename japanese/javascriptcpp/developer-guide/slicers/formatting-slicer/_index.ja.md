---
title: JavaScriptをC++経由で使用してスライサーのフォーマット設定を行う
linktitle: スライサーの書式を設定する
type: docs
weight: 20
url: /ja/javascript-cpp/formatting-slicer/
---

## **可能な使用シナリオ**

Microsoft Excelでスライサーの列数やスタイルを設定することで、フォーマットできます。Aspose.Cells for JavaScriptをC++経由で使用して、これを[**Slicer.numberOfColumns**](https://reference.aspose.com/cells/javascript-cpp/slicer/#numberOfColumns--)および[**Slicer.styleType**](https://reference.aspose.com/cells/javascript-cpp/slicer/#styleType--)のプロパティを使って行うことも可能です。

## **スライサーの書式設定**

以下のコードを参照してください。これは、スライサーを含む[サンプルExcelファイル](67338473.xlsx)を読み込み、スライサーにアクセスし、その列数とスタイルタイプを設定し、[出力Excelファイル](67338474.xlsx)として保存します。スクリーンショットは、サンプルコード実行後のスライサーの外観を示しています。

![todo:image_alt_text](formatting-slicer_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Slicer Formatting Example</title>
    </head>
    <body>
        <h1>Slicer Formatting Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Set the number of columns of the slicer
            slicer.numberOfColumns = 2;

            // Set the type of slicer style
            slicer.styleType = AsposeCells.SlicerStyleType.SlicerStyleLight6;

            // Save the workbook in output XLSX format
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputFormattingSlicer.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer formatting updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
