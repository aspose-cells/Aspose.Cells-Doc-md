---
title: Lås eller lås upp former med JavaScript via C++
linktitle: Lås eller lås upp figurer
type: docs
weight: 200
url: /sv/javascript-cpp/lock-or-unlock-shapes/
description: Denna artikel visar kod som förklarar hur man låser eller lås upp former för att skydda dem med Aspose.Cells biblioteket för JavaScript via C++.
keywords: JavaScript via C++ Lås former för att skydda dem, hur man låser eller lås upp former med JavaScript via C++, lås eller lås upp former för att skydda dem i JavaScript via C++.
---

## **Möjliga användningsscenario**

Ibland behöver du skydda alla figurer i vissa arbetsblad för att förhindra att de förstörs av oönskade situationer. I så fall måste du låsa alla figurer i det angivna arbetsbladet. 

Att låsa figurer i ett kalkylblad eller dokument kan vara fördelaktigt av flera skäl:
1. Förhindra oavsiktliga ändringar: Att låsa figurer säkerställer att de inte oavsiktligt flyttas, resizeas eller tas bort av användare. Detta är särskilt viktigt i komplexa dokument där figurer kan användas för anteckningar, illustrationer eller som en del av dokumentets design.
1. Bibehåll layout och design: Figurer är ofta avgörande för ett dokuments layout och visuella design. Att låsa dem bevarar det avsedda utseendet, vilket säkerställer att dokumentet förblir professionellt och visuellt tilltalande.
1. Dataintegritet: I kalkylblad kan figurer användas för att markera viktiga datapunkter, lägga till kommentarer eller ge visuella förklaringar. Att låsa dessa figurer säkerställer att den kontextuella information de ger är korrekt och intakt.
1. Konsistens i delade dokument: När man samarbetar om dokument kan olika användare ha varierande nivåer av expertis. Att låsa figurer hjälper till att upprätthålla konsekvensen i hela dokumentet genom att förhindra oavsiktliga ändringar.
1. Säkerhet: I känsliga dokument kan låsta figurer vara en del av en bredare strategi för att skydda information. Till exempel kan låsta figurer användas för att skydda specifika anteckningar eller markeringar som ger kritisk kontext.

Ibland behöver du kunna modifiera vissa figurer i vissa skyddade kalkylblad, i vilket fall du behöver låsa upp dessa figurer. Denna artikel kommer att introducera i detalj hur man låser och låser upp angivna figurer.

## **Hur man låser figurer för att skydda dem i Excel**

Så här låser du celler i Microsoft Excel:

1. Öppna din Excel-fil: Öppna Excel-filen som innehåller figurerna du vill låsa.

1. Välj figuren: Klicka på figuren du vill låsa. Du kan också välja flera figurer genom att hålla nere Ctrl-tangenten och klicka på varje figur.

1. Öppna Fomateringspanelen för figur: Högerklicka på den valda figuren eller figurerna och välj "Storlek och egenskaper." Alternativt kan du gå till "Formatera"-fliken på menyfliksområdet och i "Storlek"-gruppen klicka på dialogikonen för att öppna "Formatera figur"-panelen.
1. Lås figuren: I "Formatera figur"-panelen, gå till fliken "Storlek & Egenskaper" (ikonen ser ut som en kvadrat med pilar). Under avsnittet "Egenskaper", bocka i rutan för "Låst."
<br>
<img src="1.png" width=60% />
1. Skydda arket: Gå till "Granska"-fliken på menyfliksområdet. Klicka på "Skydda blad." Ange ett lösenord (valfritt) och välj de behörigheter du vill tillåta (t.ex. välja låsta celler, formatera celler etc.). Klicka på "OK."
<br>
<img src="2.png" width=60% />

## **Hur man låser alla figurer i ett specifikt ark**

För att skydda alla former i ett specificerat kalkblad, använd metoden `worksheet.protect(ProtectionType.Objects)`, som visas i följande exempel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Lock Shapes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const text = "This is a test";
            const worksheet = workbook.worksheets.get(0);

            let shape = worksheet.shapes.addTextBox(1, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addRectangle(5, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addButton(9, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addOval(13, 0, 1, 0, 50, 100);
            shape.text = text;

            // Protect all shapes in the specified worksheet
            shape.worksheet.protect(ProtectionType.Objects);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shapes locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Hur man låser upp angivna figurer i ett skyddat arbetsblad**

För att låsa upp en specificerad form i ett skyddat kalkblad, använd `shape.isLocked`, som visas i följande exempel.

Notering: `shape.isLocked` är meningsfullt endast när kalkbladet är skyddat.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Unlock Shape</title>
    </head>
    <body>
        <h1>Unlock Shape Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get protected worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the specified shape to be unlocked
            const shape = worksheet.shapes.get("TextBox 1");

            if (!shape) {
                resultDiv.innerHTML = '<p style="color: red;">Shape "TextBox 1" not found.</p>';
                return;
            }

            // Unlock the specified shape
            if (!worksheet.protection.allowEditingObject && shape.isLocked) {
                shape.isLocked = false;
            }

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'UnLocked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape unlocked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
