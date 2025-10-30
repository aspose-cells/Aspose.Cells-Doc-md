---
title: Hantering av TextBox med JavaScript via C++
linktitle: Hantera textruta
type: docs
weight: 50
url: /sv/javascript-cpp/managing-textbox-of-excel/
description: Lär dig hur man hanterar TextBox i Excel med Aspose.Cells for JavaScript via C++. 
keywords: Hantera TextBox i Excel JavaScript via C++
---

## **Möjliga användningsscenario**
Det finns scenarier där du kan behöva lägga till, uppdatera eller manipulera TextBox-objekt i ett Excel-ark. Detta kan vara användbart för att lägga till kommentarer, ledande texter eller annan tilläggsinformation som hjälper till vid datavisning. Aspose.Cells for JavaScript via C++ erbjuder robust funktionalitet för att hantera TextBox i Excel-dokument. 

## **Hantering av TextBox med Aspose.Cells for JavaScript via C++**
Detta exempel visar hur man:

1. Skapa en ny arbetsbok.
2. Lägg till en TextBox-form.
3. Ändra TextBox-egenskaper efter behov.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TextBox Example</title>
    </head>
    <body>
        <h1>TextBox Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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

            // Adding a TextBox shape
            const textBox = worksheet.shapes.addTextBox(2, 2, 100, 100);

            // Set TextBox properties (converted getters/setters to properties)
            textBox.text = "This is a TextBox.";
            textBox.fontSize = 12;
            textBox.fillColor = Color.fromArgb(255, 255, 255); // White background

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'TextBoxExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Den här koden visar hur man skapar och konfigurerar en TextBox i ett Excel-ark, hur man justerar dess storlek, position och formaterar den efter dina krav.

Tänk på att interaktioner med Textrutor kan variera beroende på specifika användningsfall, så hänvisa till Aspose.Cells for JavaScript via C++ dokumentationen för ytterligare metoder och egenskaper.
