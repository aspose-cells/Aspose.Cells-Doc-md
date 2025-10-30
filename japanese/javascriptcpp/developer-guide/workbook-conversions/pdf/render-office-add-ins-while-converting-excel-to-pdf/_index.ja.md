---
title: JavaScript経由のC++によるExcelからPDFへの変換時にOfficeアドインをレンダリングする
linktitle: ExcelをPDFに変換する際のOffice Add Insのレンダリング
type: docs
weight: 100
url: /ja/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **可能な使用シナリオ**

以前は、Aspose.CellsはExcelファイルをPDF形式に保存するときにOfficeアドインをレンダリングできませんでした。現在、Aspose.Cellsは正常にレンダリングします。出力PDFにOfficeアドインをレンダリングするために、特別な方法やプロパティを使用する必要はありません。ただExcelファイルをPDF形式で保存するだけで、Officeアドインがレンダリングされます。

## **ExcelをPDFに変換する際のOffice Add-Insのレンダリング**

以下のサンプルコードは、Office アドインを含むサンプル Excel ファイル（60489769.xlsx）を保存します。以前のバージョン（例：17.11）で生成された出力 PDF と、新しいバージョン（例：17.12以降）で生成された出力 PDF をご覧ください。前のバージョンの出力 PDF は空白ですが、新しいバージョンは Office アドインを表示します。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Office Add-Ins to PDF Example</title>
    </head>
    <body>
        <h1>Render Office Add-Ins to PDF Example</h1>
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

            // Get Aspose.Cells version (converted from getVersion())
            const version = AsposeCells.CellsHelper.version;

            // Save workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `output-${version}.pdf`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Saved to PDF successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
