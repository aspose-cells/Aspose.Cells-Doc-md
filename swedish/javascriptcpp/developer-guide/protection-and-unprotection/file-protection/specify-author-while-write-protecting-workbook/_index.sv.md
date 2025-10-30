---
title: Ange författare vid skrivskydd av arbetsbok med JavaScript via C++
linktitle: Ange författare vid skrivskydd av arbetsbok
type: docs
weight: 40
url: /sv/javascript-cpp/specify-author-while-write-protecting-workbook/
description: Ange ett författarnamn vid skrivskydd av arbetsbok med Aspose.Cells for JavaScript via C+ . 
---

## **Möjliga användningsscenario**

Du kan ange ett författarnamn vid skrivskydd av din arbetsbok med Aspose.Cells API. Använd [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--)-egenskapen för detta ändamål.

## **Ange författare vid skrivskydd av arbetsbok**

Följande exempel förklarar användningen av [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--)-egenskapen. Koden skapar en tom arbetsbok, skrivskyddar den med ett lösenord, anger författarnamnet och sparar den som [utdata Excel-fil](67338582.xlsx). Följande skärmbild illustrerar effekten av kodexemplet på utdata Excel-filen för ditt referens.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Author While Write Protecting Workbook</h1>
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
            // Create empty workbook.
            const workbook = new Workbook();

            // Write protect workbook with password.
            workbook.settings.writeProtection.password = "1234";

            // Specify author while write protecting workbook.
            workbook.settings.writeProtection.author = "SimonAspose";

            // Save the workbook in XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and write-protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
