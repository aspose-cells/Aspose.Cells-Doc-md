---
title: Ta bort befintliga PrinterSettings för kalkylblad i Excel fil med JavaScript via C++
linktitle: Ta bort befintliga utskriftsinställningar för kalkylblad i Excel filen
type: docs
weight: 60
url: /sv/javascript-cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: I denna artikel lär du dig hur man programmässigt tar bort befintliga PrinterSettings för kalkylblad i Excel filen med Aspose.Cells for JavaScript via C++.
keywords: ta bort skrivareinställningar för kalkylblad JavaScript via C++, ta bort skrivareinställningar för Excel kalkylblad JavaScript via C++
---

## **Möjliga användningsscenario**
Ibland vill utvecklare förhindra Excel från att inkludera *.bin*-filer av skrivarinställningar i sparade XLSX-filer. Skrivarinställningsfiler finns under *“[fil "root"]\xl\printerSettings”.* I den här dokumentationen förklaras hur man tar bort befintliga skrivarinställningar med Aspose.Cells-API:er.

## **Ta bort befintliga skrivareinställningar för arbetsblad i Excel-fil**
Aspose.Cells möjliggör att ta bort befintliga skrivarinställningar som är specificerade för olika kalkylblad i Excel-filen. Följande exempelkod illustrerar hur man tar bort befintliga skrivarinställningar för alla kalkylblad i arbetsboken. Se dess [exempelfil för Excel](45056020.xlsx), [utdata för Excel-fil](45056021.xlsx), konsolresultat samt skärmdumpen som referens.

## **Skärmdump**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Exempelkod**
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

## **Konsoloutput**
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
