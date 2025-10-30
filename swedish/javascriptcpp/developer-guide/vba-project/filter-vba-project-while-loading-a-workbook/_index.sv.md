---
title: Filtrera VBA projekt vid läsning av en arbetsbok med JavaScript via C++
linktitle: Filtrera VBA projekt vid inläsning av en arbetsbok
type: docs
weight: 140
url: /sv/javascript-cpp/filter-vba-project-while-loading-a-workbook/
description: Lär dig hur du filtrerar VBA projekt medan du laddar Excel arbetsböcker med Aspose.Cells for JavaScript via C++.
---

## **Filtrera VBA-projekt vid laddning av en Excel-arbetsbok i JavaScript via C++**

Vissa .xlsm/.xslb-filer har ett extremt stort antal makron (eller mycket, mycket långa makron). Aspose.Cells for JavaScript via C++ laddar villkorslöst denna (metadata) när sådana arbetsböcker öppnas. Du kan behöva kontrollera detta [**LoadDataFilterOptions**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions) när du verkligen bara vill extrahera bladnamn för ett stort antal arbetsböcker, och därmed hoppa över sådant oönskat innehåll. Denna filtrering tillhandahålls genom att införa ett nytt alternativ, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions).

## **Exempelkod**

Följande exempelkod laddar en arbetsbok så att endast VBA filtreras. En testfil för att testa denna funktion kan hämtas från följande länk:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sample Macro-Enabled Workbook to XLSM</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, LoadFilter, LoadDataFilterOptions } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel macro-enabled (.xlsm) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Set the load options, we do not want to load VBA
            const loadOptions = new LoadOptions(LoadFormat.Auto);
            const loadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.VBA);
            loadOptions.loadFilter = loadFilter;

            // Create workbook object from uploaded file using load options
            const book = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Save the output in xlsm format
            const outputData = book.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputSampleMacroEnabledWorkbook.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download OutputSampleMacroEnabledWorkbook.xlsm';

            document.getElementById('result').innerHTML = '<p style="color: green;">Processing completed. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
