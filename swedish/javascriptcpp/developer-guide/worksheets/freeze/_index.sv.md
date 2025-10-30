---
title: Frysa rut världen av Excel med JavaScript via C++
linktitle: Frysa rader
type: docs
weight: 190
url: /sv/javascript-cpp/how-to-freeze-panes-of-excel-worksheet
description: I denna artikel lär du dig hur man fryser rutor i Excel ark programmässigt med Aspose.Cells for JavaScript via C++.
keywords: Frys paneor, Frys fönster.
---

## **Introduktion**  

I den här artikeln lär vi oss Hur man fryser paneor. När du har en stor mängd data under en gemensam rubrik kan du inte se rubriken när du scrollar ner i kalkylbladet. Och varje post innehåller mycket data. Du kan frysa paneor så att du kan se den frysta delen även när resten av datan scrollas. Du kan enkelt se rubriker i de översta raderna eller första kolumnerna. Att frysa och avfrysa paneor ändrar bara vy av datan utan att ändra själva datan.  

## **I Excel**  

**![Frys rader i Excel](Frys-panor.png)**  

1. Om du vill frysa paneor, frysa rader och kolumner, välj först en cell (som B2).  
2. Klicka på Visa > Frysa rader.  
3. I rullgardinsmenyn klickar du på Frysa rader.  
4. Om du scrollar ner eller till höger, är den första raden och kolumnen frysta.  

**![Frysade paneor](Frozen-Panes.png)**  

Som du kan se är den första raden och kolumn A frysta, den andra raden är 32 och den andra synliga kolumnen är D.  

Frys paneor låter dig visa din stora data utan att hålla koll på rad- eller kolumnetiketter.  

## **Frys rutor med Aspose.Cells for JavaScript via C++**  
Det är enkelt att frysa rutor med Aspose.Cells for JavaScript via C++. Använd [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-)-metoden för att frysa rutor vid den markerade cellen.  
1. Konstruera Arbetsbok för att öppna filen eller skapa en tom fil.  
2. Frysa fönster med Worksheet.freezePanes()-metoden.  
3. Spara filen.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <p>Select an Excel file (Freeze.xlsx) and click "Run Example" to freeze panes at B2.</p>
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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Freezing panes at the cell B2
            worksheet.freezePanes("B2", 1, 1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Panes frozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```  

Bifogad [provkälla Excel-fil](Frys.xlsx).
