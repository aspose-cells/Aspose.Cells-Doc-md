---
title: Optimera minnesanvändningen vid arbete med stora filer med stora dataset
type: docs
weight: 110
url: /sv/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

När man bygger en arbetsbok med stora dataset eller läser in en stor Microsoft Excel-fil är den totala mängden RAM som processen tar alltid ett bekymmer. Det finns åtgärder som kan anpassas för att hantera utmaningen. Aspose.Cells tillhandahåller några relevanta alternativ och API-anrop för att minska, minska och optimera minnesanvändningen. Dessutom kan det hjälpa processen att arbeta mer effektivt och köra snabbare.

Använd [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)-alternativet för att optimera minnet som används för celldata för att minska den totala minneskostnaden. Vid uppbyggnad av stora dataset för celler kan det spara en viss mängd minne jämfört med att använda standardinställningen [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).

{{% /alert %}}

## **Optimera minne**

 Följande exempel visar hur man optimerar minnesanvändningen vid arbete med stora data i Aspose.Cells for JavaScript via C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Optimize Memory Usage Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, MemorySetting } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file or leave empty to create a new one.</p>';
                // Allow creating a new workbook even if no file selected; return only if user explicitly requires file.
            }

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // apply the setting to existing "Sheet1"
            workbook.worksheets.get(0).cells.memorySetting = MemorySetting.MemoryPreference;

            // apply the setting globally
            workbook.settings.memorySetting = MemorySetting.MemoryPreference;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Memory settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Försiktighet**

Standardalternativet [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) tillämpas för alla versioner. För vissa situationer, som att bygga en arbetsbok med ett stort dataset för celler, kan alternativet [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) optimera minnesanvändningen och minska minneskostnaden för programmet. Detta alternativ kan emellertid försämra prestandan i vissa specialfall såsom följer.

1. **Åtkomst av celler slumpmässigt och upprepade gånger**: Den mest effektiva sekvensen för att komma åt cellernas samling är cell för cell i en rad, och sedan rad för rad. Särskilt om du får åtkomst till rader/celler via uppräknaren som erhållits från [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection) och [**Row**](https://reference.aspose.com/cells/javascript-cpp/row), kommer prestandan att maximera med [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).
1. **Infoga & Ta bort celler & rader**: Observera att om det finns många infogningar/raderingar för celler/rader kommer prestandanedgraderingen att vara märkbar för [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)-läget jämfört med [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)-läget.
1. **Arbete med olika celltyper**: Om de flesta cellerna innehåller strängvärden eller formler kommer minneskostnaden att vara densamma som [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)-läge, men om det finns många tomma celler eller cellvärden är numeriska, booleska och så vidare, kommer [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)-alternativet att ge bättre prestanda.
