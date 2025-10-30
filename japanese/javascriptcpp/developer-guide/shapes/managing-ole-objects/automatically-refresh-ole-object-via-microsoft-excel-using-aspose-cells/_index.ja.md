---
title: C++を使用し、Microsoft Excel経由でOLEオブジェクトを自動的にリフレッシュ
linktitle: Aspose.Cellsを使用してMicrosoft ExcelでOLEオブジェクトを自動的に更新する
type: docs
weight: 270
url: /ja/javascript-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Aspose.Cells for JavaScriptを使用したExcelのOLEオブジェクトの自動リフレッシュ方法を学びます。
---

{{% alert color="primary" %}}  
Aspose.Cellsは、ExcelファイルがMicrosoft Excelで開かれるときにOLEオブジェクトを再表示するための[**OleObject.autoLoad**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#autoLoad--)プロパティを提供します。このプロパティにより、OLEオブジェクトは、Microsoft Excelによって生成された正しいOLEイメージを表示します。  
{{% /alert %}}  

次のサンプルコードでは、実際のOLEイメージでないOLEオブジェクトを含む[サンプルExcelファイル](5115231.xlsx)を読み込みます。OLEオブジェクトは実際にはMicrosoft Wordドキュメントですが、サンプルExcelファイルではMicrosoft Wordイメージの代わりに動物のイメージが表示されます。しかし、[出力Excelファイル](5115225.xlsx)を開くと、Microsoft Excelが正しいOLEイメージを表示します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh OLE Objects Example</title>
    </head>
    <body>
        <h1>Refresh OLE Objects Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Set auto load property of first ole object to true
            sheet.oleObjects.get(0).autoLoad = true;

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RefreshOLEObjects_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">OLE object autoLoad set to true. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
