---
title: Konvertera text till kolumner med Aspose.Cells for JavaScript via C++
linktitle: Konvertera Text till Kolumner
type: docs
weight: 30
url: /sv/javascript-cpp/convert-text-to-columns-using-aspose-cells/
description: Lär dig hur du konverterar text till kolumner i Excel med hjälp av Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

Du kan konvertera din Text till Kolumner med Microsoft Excel. Denna funktion finns under *Dataverktyg* i fliken *Data*. För att dela innehållet i en kolumn till flera kolumner ska datan innehålla en specifik avgränsare som ett kommatecken (eller annan karaktär), baserat på vilken Microsoft Excel delar upp cellens innehåll till flera celler. Aspose.Cells for JavaScript via C++ erbjuder denna funktion också via [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-).  

## **Konvertera Text till Kolumner med Aspose.Cells for JavaScript via C++**  

Följande exempelprogram förklarar användningen av [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-)-metoden. Koden lägger först till några personnamn i kolumn A i det första arbetsbladet. Förnamn och efternamn är separerade med ett mellanslag. Sedan tillämpar den [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-)-metoden på kolumn A och sparar det som en utdata-Excel-fil. Om du öppnar [utdata-Excel-filen](25395213.xlsx) kommer du att se att förnamnen är i kolumn A medan efternamnen är i kolumn B, som visas i skärmbilden.  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Text to Columns Example</h1>
        <p>Select an optional Excel file to start from, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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

            // Basic validation only: file is optional
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Add people name in column A. First name and last name are separated by space.
            ws.cells.get("A1").value = "John Teal";
            ws.cells.get("A2").value = "Peter Graham";
            ws.cells.get("A3").value = "Brady Cortez";
            ws.cells.get("A4").value = "Mack Nick";
            ws.cells.get("A5").value = "Hsu Lee";

            // Create text load options with space as separator.
            const opts = new TxtLoadOptions();
            opts.separator = ' ';

            // Split the column A into two columns using TextToColumns() method.
            // Now column A will have first name and column B will have second name.
            ws.cells.textToColumns(0, 0, 5, opts);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTextToColumns.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
