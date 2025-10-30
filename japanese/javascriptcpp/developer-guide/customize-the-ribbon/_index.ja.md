---
title: JavaScriptを使用したリボンXMLのカスタマイズをC++で行う方法
linktitle: Excelメニューのカスタマイズ
type: docs
weight: 1500
url: /ja/javascript-cpp/customizing-the-ribbon-xml/
description: C++を使ったAspose.Cells for JavaScriptでExcelのリボンXMLをカスタマイズする方法を学ぶ。 
---

{{% alert color="primary" %}} 

Microsoft Officeは、2007年以降、アプリケーションウィンドウの上部にリボンを置き換え、メニューやツールバーを置き換えました。リボンはカスタマイズ可能です。 
C++を使用したAspose.Cells for JavaScriptは、

- リボンXMLを解析せずに保持できます。
- リボンXMLを解析せずに読み書きできます。
- リボンXMLデータの取得と設定ができます。

リボンXMLを変更する場合は、XMLパーサーまたは他のリボンXMLツールで解析する必要があります。

{{% /alert %}} 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set Ribbon XML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set custom ribbon XML
            const ribbonXml = `<customUI xmlns="http://schemas.microsoft.com/office/2006/01/customui"></customUI>`;
            workbook.ribbonXml = ribbonXml;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            const outputFileName = 'output_' + (file.name || 'modified.xlsx');
            downloadLink.download = outputFileName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Ribbon XML set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
