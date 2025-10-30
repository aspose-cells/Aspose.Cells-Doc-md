---
title: Filtern Sie das VBA Projekt beim Laden einer Arbeitsmappe mit JavaScript über C++
linktitle: Filtern des VBA Projekts beim Laden einer Arbeitsmappe
type: docs
weight: 140
url: /de/javascript-cpp/filter-vba-project-while-loading-a-workbook/
description: Erfahren Sie, wie Sie VBA Projekte beim Laden von Excel Arbeitsmappen mit Aspose.Cells for JavaScript über C++ filtern.
---

## **VBA-Projekt beim Laden einer Excel-Arbeitsmappe in JavaScript via C++ filtern**

Einige .xlsm/.xslb-Dateien enthalten eine äußerst große Anzahl an Makros (oder sehr, sehr lange Makros). Aspose.Cells for JavaScript via C++ lädt diese (Meta-)Daten beim Öffnen solcher Arbeitsmappen unconditional. Möglicherweise müssen Sie dies jedoch kontrollieren [**LoadDataFilterOptions**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions), wenn Sie nur Sheet-Namen für eine große Anzahl von Arbeitsmappen extrahieren möchten, um solche unnötigen Inhalte zu überspringen. Dieser Filter wird durch die Einführung einer neuen Option [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions) bereitgestellt.

## **Beispielcode**

Der folgende Beispielscode lädt eine Arbeitsmappe so, dass nur das VBA gefiltert wird. Eine Testdatei für dieses Feature können Sie über den folgenden Link herunterladen:

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
