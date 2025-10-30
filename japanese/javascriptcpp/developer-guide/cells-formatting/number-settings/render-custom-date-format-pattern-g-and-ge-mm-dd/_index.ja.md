---
title: gおよびge mm ddのカスタム日付形式パターンをレンダリングする
linktitle: gおよびge mm ddのカスタム日付形式パターンをレンダリングする  
description: スプレッドシート内の日付表示を制御するために、カスタム日付フォーマットパターン g と ge をAspose.Cells for JavaScriptをC++でレンダリングする方法を学びます。  
keywords: Aspose.Cells、JavaScriptライブラリ、電子スプレッドシート、カスタム日付フォーマット、レンダリング、パターン g 、パターン ge 、コントロール表示    
type: docs  
weight: 160  
url: /ja/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/  
---  

{{% alert color="primary" %}}  

Aspose.Cellsは、今やgやge.mm.ddなどのカスタム日付形式パターンをレンダリングすることができます。参考のために、添付の[source excel file](5112361.xlsx)とAspose.Cellsによる変換された[PDF](5112360.pdf)をご確認ください。

{{% /alert %}}  

以下のサンプルコードは、gやge.mm.ddなどのカスタム形式パターンを含む[source excel file](5112361.xlsx)を変換し、[output PDF](5112360.pdf)に変換します。  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomDateFormat_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
