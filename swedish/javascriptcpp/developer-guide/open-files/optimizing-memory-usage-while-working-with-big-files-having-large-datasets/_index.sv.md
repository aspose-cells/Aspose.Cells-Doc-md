---
title: Optimera minnesanvändningen vid arbete med stora filer med stora datamängder med JavaScript via C++
linktitle: Optimera minnesanvändningen vid arbete med stora filer med stora dataset
type: docs
weight: 180
url: /sv/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

 När du bygger ett arbetsbok med stora datamängder eller läser en stor Microsoft Excel-fil är den totala mängden RAM som processen kommer att ta alltid en oro. Det finns åtgärder som kan anpassas för att hantera utmaningen. Aspose.Cells for JavaScript via C++ ger några relevanta alternativ och API-anrop för att minska, reducera och optimera minnesanvändningen. Det kan också hjälpa processen att arbeta mer effektivt och köras snabbare.

Använd [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) för att optimera minnesanvändningen för celldata och minska den totala minneskostnaden. När man bygger en stor datamängd för celler kan det spara en viss mängd minne jämfört med att använda standardinställningen ([**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)).

{{% /alert %}}

## **Optimera minne**

### **Läsning av stora Excel-filer**

Det följande exemplet visar hur man läser en stor Microsoft Excel-fil i optimerat läge.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - LoadOptions MemorySetting</title>
    </head>
    <body>
        <h1>LoadOptions MemorySetting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, MemorySetting, SaveFormat, Utils } = AsposeCells;

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

            // Specify the LoadOptions
            const opt = new LoadOptions();
            // Set the memory preferences (converted from setMemorySetting)
            opt.memorySetting = MemorySetting.MemoryPreference;

            // Instantiate the Workbook - load the big Excel file with options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opt);

            // Save the workbook to XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook loaded with MemoryPreference. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Skrivning av stora Excel-filer**

Det följande exemplet visar hur man skriver en stor datamängd till en arbetsbok i optimerat läge.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Memory Setting Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Memory Setting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
                // If no file is selected, create a new workbook (similar to new AsposeCells.Workbook() in Node)
                // and proceed to set memory settings and populate sheets.
            }

            // Load workbook from file if provided, otherwise create empty workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Set the memory preferences on the workbook settings
            workbook.settings.memorySetting = AsposeCells.MemorySetting.MemoryPreference;

            // Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook
            // To change the memory setting of existing sheets, change memory setting for them manually:
            let cells = workbook.worksheets.get(0).cells;
            cells.memorySetting = AsposeCells.MemorySetting.MemoryPreference;

            // Input large dataset into the cells of the worksheet.
            // Your code goes here.
            // Example: populate a few cells to demonstrate
            const firstCell = cells.get(0, 0);
            firstCell.value = "Sample Data 1";
            cells.get(1, 0).value = "Sample Data 2";

            // Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
            const sheet2 = workbook.worksheets.add("Sheet2");
            const cells2 = sheet2.cells;
            // .........
            // Input large dataset into the cells of the worksheet.
            // Your code goes here.
            // Example: populate a few cells in Sheet2
            cells2.get(0, 0).value = "Sheet2 Data 1";
            cells2.get(1, 0).value = "Sheet2 Data 2";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Försiktighet**

Det förvalda alternativet, [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/), tillämpas för alla versioner. För vissa situationer, som att bygga ett kalkblad med en stor datamängd för celler, kan [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)-alternativet optimera minnesanvändningen och minska minneskostnaden för applikationen. Dock kan detta alternativ försämra prestandan i vissa speciella fall såsom följande.

1. **Få åtkomst till celler slumpmässigt och upprepade gånger**: Den mest effektiva sekvensen för att komma åt cellsamlingen är cell för cell i en rad, och därefter rad för rad. Speciellt om du når rader/celler via Enumerator som erhålls från [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells), [**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection) och [**Row**](https://reference.aspose.com/cells/javascript-cpp/row), maximeras prestandan med [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).
2. **Infoga & Ta bort celler & rader**: Observera att om det finns många insättnings-/raderingsoperationer för Cell/Rows, kommer prestandaförlusten att bli märkbar för *MemoryPreference*-läget jämfört med *Normal*-läget.
3. **Att arbeta på olika celltyper**: Om de flesta celler innehåller strängvärden eller formler, kommer minneskostnaden att vara samma som *Normal*-läget, men om det finns många tomma celler eller cellvärden som är numeriska, booleska, etc., ger [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)-alternativet bättre prestanda.
