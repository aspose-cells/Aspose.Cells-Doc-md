---
title: Hur man skalar ett kalkylblad med JavaScript via C++
linktitle: Hur man skalar ett kalkylblad
type: docs
weight: 130
url: /sv/javascript-cpp/how-to-scale-a-worksheet/
description: Denna artikel visar kod som förklarar hur man skalar ett kalkylblad med Aspose.Cells for JavaScript via C++.
keywords: JavaScript skalar ett kalkylblad, Hur man skalar ett kalkylblad med JavaScript via C++, Skala ett kalkylblad i JavaScript via C++.
---

## **Möjliga användningsscenario**
Att skala ett kalkylblad kan vara användbart av olika skäl, beroende på sammanhanget du arbetar i. Här är några vanliga skäl för att skala ett kalkylblad:
1. Passa på sida: För att säkerställa att allt innehåll får plats på en enda sida eller ett specifikt antal sidor vid utskrift, vilket gör det lättare att läsa och hantera utan att behöva bläddra igenom flera sidor.

1. Presentation: För att få arbetsbladet att se mer organiserat och professionellt ut, särskilt när du delar det med andra i möten eller rapporter.

1. Läslighet: För att justera storleken på texten och andra element för bättre läsbarhet, särskilt för personer som kan ha svårt att läsa mindre teckensnitt.

1. Platsförvaltning: För att optimera användningen av utrymmet på ett arbetsblad, säkerställa att det inte finns onödig tomrum och att all viktig information är synlig utan överdriven scrollning.

1. Data Visualisering: När det gäller diagram och grafer kan skala hjälpa till att göra dem mer förståeliga genom att justera storleken för att passa den tillgängliga platsen lämpligen.

1. Konsekvens: För att upprätthålla ett konsekvent utseende och känsla över flera arbetsblad eller dokument, vilket är särskilt viktigt i professionella och utbildningsinställningar.

## **Hur man skalar ett kalkylblad i Excel**
Att skala ett arbetsblad i Excel kan hjälpa dig att få ditt innehåll att passa på en enda sida eller ett specificerat antal sidor vid utskrift. Här är stegen för att skala ett arbetsblad:

1. Öppna ditt arbetsblad: Öppna Excel-arbetsbladet som du vill skala.

1. Gå till fliken Sidlayout: Klicka på fliken Sidlayout i bandet.

1. Skala för att passa grupp: I fliken Sidlayout, hitta gruppen Skala för att passa. Här har du alternativen för att justera skalan. Bredd: Detta alternativ tillåter dig att specificera hur många sidor bred det utskrivna arbetsbladet ska vara. Höjd: Detta alternativ tillåter dig att specificera hur många sidor högt det utskrivna arbetsbladet ska vara. Skala: Du kan också ange en anpassad procentandel för skalan här.
<br>
<img src="1.png" width=60% />

1. Justera Bredd och Höjd: Ställ in Bredd och Höjd till önskat antal sidor. Till exempel, ställ båda till 1 sida om du vill att arbetsbladet ska passa på en sida.

1. Justera skaleringsprocenten (om nödvändigt): Om du föredrar att ange en specifik skaleringsprocent, justera rutan Skala. Till exempel, att ställa in den till 50% gör att allt blir halvt så stort.


## **Hur man Skalar ett Arbetssheet med JavaScript via C++**
Aspose.Cells for JavaScript via C++ är ett kraftfullt bibliotek för att arbeta med Excel-filer programmässigt. För att skala ett arbetsblad med Aspose.Cells måste du följa dessa steg: ladda [provfil](sample.xlsx) och justera utskriftsinställningarna så att innehållet passar till det önskade antalet sidor eller en specifik procentandel av originalstorleken.

### **Exempel: Passa till sida**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Fit To Page Example</title>
    </head>
    <body>
        <h1>Fit Worksheet to One Page</h1>
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

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the worksheet to fit to 1 page wide and 1 page tall
            pageSetup.fitToPagesWide = 1;
            pageSetup.fitToPagesTall = 1;

            // Saving the modified workbook and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_fit_to_page.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet fitted to one page. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="3.png" width=60% />

### **Exempel: Skala till procentandel**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Scale Worksheet</title>
    </head>
    <body>
        <h1>Scale Worksheet Example</h1>
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

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the scaling to a specific percentage (e.g., 75%)
            pageSetup.zoom = 75;

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_scaled_percentage.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Scaled Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Scaling applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="2.png" width=60% />
