---
title: Frysa första kolumn(er) i Excel kalkylblad med JavaScript via C++
linktitle: Frys kolumner
type: docs
weight: 190
url: /sv/javascript-cpp/how-to-freeze-columns-of-excel-worksheet
description: Lär dig hur du fryser vänstra kolumner av Excel arbetsblad programatiskt med Aspose.Cells for JavaScript via C++.
keywords: Frys vänstra kolumner, Frys första kolumner, Lås kolumnen(n)
---

## **Introduktion**  

I denna artikel lär vi oss hur man fryser vänster kolumn(er). När du har en stor mängd data i en rad kan det vara svårt att se de vänstra kolumnerna när du skrollar horisontellt i arbetsbladet. Du kan frysa och låsa första kolumn(er) så att du kan se den frysta delen även när resten av datan skrollas. Det är enkelt att se rubriker i de vänstra kolumnerna.  

## **Frys kolumner i Excel**  

**![Frys vänster kolumn(er) i Excel](freeze-columns.png)**  

1. Om du vill frysa vänstra kolumn(er), välj först kolumnen under den kolumn som ska frysas.
2. Klicka på Visa > Frysa rader.
3. I rullgardinsmenyn, klicka på Frysa första kolumn.
4. Om du skrollar nedåt, är den första kolumnen alltid i vänster vy.

**![Frysen kolumn](frozen-columns.png)**  

Som du kan se är den första kolumnen fryst, och den första kolumnen är alltid låst högst upp när du skrollar horisontellt.

Frys kolumner låter dig visa din långa data utan besvär med att hålla koll på den första kolumnen.

## **Frys kolumner med Aspose.Cells for JavaScript via C++**  
Det är enkelt att frysa första kolumn(er) med Aspose.Cells for JavaScript via C++.  
Använd metod [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) för att frysa kolumn(er) vid den valda kolumnen.  
1. Konstruera Arbetsbok för att öppna filen eller skapa en tom fil.
2. Frys den första kolumnen med Worksheet.freezePanes() metod.
3. Spara filen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the second column on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("B1", 0, 1);

            // Saving the file and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Bifogad [provkälla Excel-fil](Frys.xlsx).
