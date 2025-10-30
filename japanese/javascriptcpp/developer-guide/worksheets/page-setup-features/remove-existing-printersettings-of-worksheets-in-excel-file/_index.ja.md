---
title: Excelファイル内のワークシートの既存のPrinterSettingsをJavaScriptとC++を使用して削除
linktitle: Excelファイルのワークシートの既存のPrinterSettingsを削除する方法
type: docs
weight: 60
url: /ja/javascript-cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: この記事では、C++経由のAspose.Cells for JavaScriptを使用してExcelファイル内のワークシートのPrinterSettingsをプログラムで削除する方法を学びます。
keywords: C++経由のJavaScriptを使ったワークシートのプリンタ設定の削除、Excelワークシートのプリンタ設定の削除  JavaScriptとC++
---

## **可能な使用シナリオ**
開発者は、保存されたXLSXファイルにプリンター設定の*.bin*ファイルを含めないようにすることを望むことがあります。プリンター設定ファイルは*「[file "root"]\xl\printerSettings」*の下にあります。この文書では、Aspose.Cells APIを使用して既存のプリンター設定を削除する方法について説明しています。

## **Excelファイルのワークシートの既存のPrinterSettingsを削除する**
Aspose.Cellsを使用して、Excelファイルの異なるシートに指定された既存のプリンター設定を削除することができます。以下のサンプルコードは、ワークブック内のすべてのワークシートの既存のプリンター設定を削除する方法を示します。参考のために、[sample Excel file](45056020.xlsx)、[output Excel file](45056021.xlsx)、コンソール出力、およびスクリーンショットをご覧ください。

## **スクリーンショット**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **サンプルコード**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Printer Settings</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #result { margin-top: 15px; white-space: pre-wrap; }
            input, button { margin-top: 10px; display: block; }
        </style>
    </head>
    <body>
        <h1>Remove Existing Printer Settings Of Worksheets</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Get the sheet counts of the workbook
            const sheetCount = wb.worksheets.count;

            const messages = [];
            // Iterate all sheets
            for (let i = 0; i < sheetCount; i++) {
                // Access the i-th worksheet
                const ws = wb.worksheets.get(i);

                // Access worksheet page setup
                const ps = ws.pageSetup;

                // Check if printer settings for this worksheet exist
                if (ps.printerSettings != null) {
                    // Print the following message
                    console.log("PrinterSettings of this worksheet exist.");
                    messages.push("PrinterSettings of this worksheet exist.");

                    // Print sheet name and its paper size
                    console.log("Sheet Name: " + ws.name);
                    console.log("Paper Size: " + ps.paperSize);
                    messages.push("Sheet Name: " + ws.name);
                    messages.push("Paper Size: " + ps.paperSize);

                    // Remove the printer settings by setting them null
                    ps.printerSettings = null;
                    console.log("Printer settings of this worksheet are now removed by setting it null.");
                    messages.push("Printer settings of this worksheet are now removed by setting it null.");
                    messages.push("");
                }
            }

            // Save the workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRemoveExistingPrinterSettingsOfWorksheets.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p><pre>' + messages.join('\n') + '</pre>';
        });
    </script>
    </body>
</html>
```

## **コンソール出力**
{{< highlight javascript >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
