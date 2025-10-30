---
title: Skapa delad arbetsbok med Aspose.Cells for JavaScript via C++
linktitle: Skapa Delad arbetsbok med Aspose.Cells
type: docs
weight: 40
url: /sv/javascript-cpp/create-shared-workbook-with-aspose-cells/
description: Lär dig hur du skapar en delad arbetsbok med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

Microsoft Excel tillåter att du delar arbetsboken som visas i följande skärmbild. När du delar arbetsboken kan flera användare redigera arbetsboken i nätverket. Aspose.Cells for JavaScript via C++ gör det möjligt att skapa en delad arbetsbok med egenskapen [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--).  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Skapa Delad arbetsbok med Aspose.Cells**  

Följande exempel skapar en delad arbetsbok genom att ställa in [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--)-egenskapen till **true**. När du öppnar [utdata Excel-filen](55541786.xlsx) i Microsoft Excel, kommer du att se **Shared** med arbetsbokens namn som visas i denna skärmdump.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Shared Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="createShared" disabled>Create Shared Workbook</button>
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
            document.getElementById('createShared').disabled = false;
        });

        document.getElementById('createShared').addEventListener('click', async () => {
            const wb = new Workbook();

            // Share the Workbook (converted getter/setter to property)
            wb.settings.shared = true;

            // Save the Shared Workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Shared Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared workbook created successfully! Click the download link to save the file.</p>';
        });
    </script>
</html>
```
