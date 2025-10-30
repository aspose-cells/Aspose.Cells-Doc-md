---
title: Autotryck radens höjd automatiskt vid inläsning av fil med JavaScript via C++
linktitle: Autofit radhöjden automatiskt när filen laddas
type: docs
weight: 120
url: /sv/javascript-cpp/autofit-row-height/
description: Lär dig att anpassa rader vars höjd inte är anpassad när du laddar en fil med Aspose.Cells for JavaScript via C++.
keywords: AutoAnpassa Radhöjd vid inläsning av fil JavaScript via C++, automatiskt justera radens höjd vid öppnande av Excel fil JavaScript via C++ 
---

## **Möjliga användningsscenario**
 Radhöjden matchar automatiskt teckensnittet i innehållet, men när höjden på den cachelagrade raden inte matchar innehållets höjd i filen, kommer MS Excel automatiskt att justera radens höjd vid inläsning av filen, medan Aspose.Cells for JavaScript via C++ inte kommer att justera den automatiskt för bättre prestanda. Om du behöver använda Aspose.Cells-programmet för att automatiskt matcha radlinjehöjder vid inläsning av filer, kan du åstadkomma detta via parametern [autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) i din kod.

Vänligen referera till följande bilddata. Vi kan observera att den cachelagrade radhöjden i rad 11 är 15, men Excel justerade automatiskt radhöjden när filen laddades.
<br>
<img src="1.png" width=70% />

## **Justera radhöjd med Aspose.Cells for JavaScript via C++**
Om du laddar filen direkt och sparar den som PDF, kommer datan inte att visas helt i PDF eftersom dess cachelagrade radhöjd är endast 15.
<br>
<img src="2.png" width=70% />
<br>
Om du sätter parametern [autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) till true när du laddar filen, kommer Aspose.Cells automatiskt att justera radens höjd. Den justerade radlinjehöjden kan effektivt möta textvisningskraven.
<br>
<img src="3.png" width=70% />

## **Exempelkod i JavaScript**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LoadOptions & AutoFitter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none;">Download out.pdf</a>
        </div>
        <div>
            <a id="downloadLink2" style="display: none;">Download out2.pdf</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, AutoFitterOptions } = AsposeCells;

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
            const downloadLink1 = document.getElementById('downloadLink1');
            const downloadLink2 = document.getElementById('downloadLink2');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const data = new Uint8Array(arrayBuffer);

            // Load workbook and save as out.pdf
            const workbook = new Workbook(data);
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            downloadLink1.href = URL.createObjectURL(blob);
            downloadLink1.download = 'out.pdf';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download out.pdf';

            // Prepare LoadOptions with AutoFitterOptions and onlyAuto = true
            const loadOptions = new LoadOptions();
            loadOptions.autoFitterOptions = new AutoFitterOptions();
            loadOptions.autoFitterOptions.onlyAuto = true;

            // Load workbook with loadOptions and save as out2.pdf
            const book = new Workbook(data, loadOptions);
            const outputData2 = book.save(SaveFormat.Pdf);
            const blob2 = new Blob([outputData2], { type: 'application/pdf' });
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'out2.pdf';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download out2.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download links to get the generated PDF files.</p>';
        });
    </script>
</html>
```
