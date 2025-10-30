---
title: Siduppläggsfunktioner med JavaScript via C++
linktitle: Siduppsättningsfunktioner
type: docs
weight: 60
url: /sv/javascript-cpp/page-setup-features/
description: Utforska sidinställningsfunktioner med Aspose.Cells for JavaScript via C++. Lär dig hur du konfigurerar sidans dimensioner, orienteringar och inställningar.
keywords: Sidupplägg funktioner JavaScript via C++, konfigurera sidans dimensioner JavaScript via C++, sidorienteringsinställningar JavaScript via C++
---

## **Introduktion**
Med Aspose.Cells for JavaScript via C++ kan du manipulera olika siduppläggsfunktioner av ett Excel-ARBETSBOK. Dessa funktioner inkluderar att ställa in sidstorlek, orientering, marginaler och mer. Rätt konfiguration av dessa funktioner möjliggör bättre utskrifts- och visningsupplevelser.

## **Ställa in sidstorlek och orientering**
Du kan ange sidans storlek och orientering för ett arbetsblad genom att använda `PageSetup`-klassen. Den ger olika egenskaper för att hantera sidans dimensioner och layout.

### **Exempel på kod**
Här är ett kodexempel som visar hur du ställer in sidans storlek och orientering.

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

## **Ställa in marginaler**
Du kan också ställa in marginalerna för sidan med samma `PageSetup`-klass. Marginalerna kan justeras för vänster, höger, topp och botten.

### **Exempel på kod**
Så här ställer du in marginalerna för ett arbetsblad.
