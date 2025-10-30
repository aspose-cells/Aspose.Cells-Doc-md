---
title: ページ設定機能のJavaScript/C++による利用
linktitle: ページ設定機能
type: docs
weight: 60
url: /ja/javascript-cpp/page-setup-features/
description: Aspose.Cells for JavaScriptを用いたページ設定機能を探索しましょう。ページのサイズ、向き、設定の構成方法について学びます。
keywords: ページ設定機能JavaScript（C++）、ページサイズ設定JavaScript（C++）、ページ向き設定JavaScript（C++）
---

## **紹介**
Aspose.Cells for JavaScriptをC++で使用して、Excelワークブックのさまざまなページ設定機能を操作できます。これらの機能にはページサイズ、向き、余白などの設定が含まれ、適切に構成することで印刷や表示が改善されます。

## **ページサイズと向きの設定**
`PageSetup`クラスを使用して、ワークシートのページサイズと向きを指定できます。さまざまなプロパティでページの寸法やレイアウトを管理します。

### **例のコード**
ページサイズと向きの設定方法のサンプルコード例を示します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Setup Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <p>You may optionally upload an existing Excel file to modify. If none is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set the page size to A4 (paperSize = 0)
            worksheet.pageSetup.paperSize = 0;

            // Set the page orientation to Landscape (orientation = 1)
            worksheet.pageSetup.orientation = 1;

            // Save the workbook as XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetupExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **マージンの設定**
同じ`PageSetup`クラスを使って余白も設定可能です。左右、上下の余白を調整できます。

### **例のコード**
ワークシートの余白を設定する方法はこちらです。
