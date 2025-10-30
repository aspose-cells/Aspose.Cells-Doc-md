---
title: Använd Sheet.SheetId egenskapen av OpenXml med Aspose.Cells for JavaScript via C++
linktitle: Använd Sheet.SheetId egenskapen i OpenXml med hjälp av Aspose.Cells
type: docs
weight: 200
url: /sv/javascript-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Denna artikel visar hur man använder Sheet.SheetId egenskapen i OpenXml med Excel manipulation med Aspose.Cells for JavaScript via C++ programmässigt.
keywords: blad id egenskapen för openxml JavaScript via C++, blad id för Excel Arbetsblad JavaScript via C++
---

## **Möjliga användningsscenario**

*Sheet.SheetId* egenskapen är tillgänglig inom *DocumentFormat.OpenXml.Spreadsheet* modul och är en del av OpenXml. Du kan se denna egenskap och dess värde i *workbook.xml* som visas i följande skärmskärm. Aspose.Cells tillhandahåller motsvarande egenskap som [**Worksheet.tabId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#tabId--).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Använd Sheet.SheetId-egenskapen i OpenXml med Aspose.Cells for JavaScript via C++**

Följande exempelkod laddar [provs-exelfilen](51740716.xlsx), läser av dess flik- eller flik-id, tilldelar det ett nytt flik-id och sparar det som [utdata-exelfil](51740717.xlsx). Se även konsolens utmatning för kodreferens.

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sheet Id Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Print its Sheet or Tab Id on console and show in page
            console.log("Sheet or Tab Id: " + ws.tabId);
            resultDiv.innerHTML = `<p>Original Sheet or Tab Id: ${ws.tabId}</p>`;

            // Change Sheet or Tab Id
            ws.tabId = 358;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSheetId.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += `<p style="color: green;">Sheet Id changed to ${ws.tabId}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

## **Konsoloutput**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
