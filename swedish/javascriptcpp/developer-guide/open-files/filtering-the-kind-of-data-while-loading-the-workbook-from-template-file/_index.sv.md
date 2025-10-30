---
title: Filtrering av datatyper vid laddning av arbetsboken från mallfil med JavaScript via C++
linktitle: Filtrera vilken typ av data som ska laddas från mallfilen när arbetsboken laddas
type: docs
weight: 400
url: /sv/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}
 Ibland vill du ange vilken typ av data som ska laddas när du bygger arbetsboken från mallfilen. Filtrering av inläst data kan förbättra prestandan för ditt specifika ändamål, särskilt när du använder [LightCells API:er](/cells/sv/javascript-cpp/using-lightcells-api/). Använd [**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--)-egenskapen för detta ändamål.
{{% /alert %}}

Följande exempel laddar endast formobjekt när arbetsboken laddas från [mallfilen](5115552.xlsx) som du kan ladda ner via länken. Skärmbilden visar innehållet i [mallfilen](5115552.xlsx) och förklarar även att data i rött och med gul bakgrund inte kommer att laddas eftersom egenskapen [**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--) har satts till [**Shape**](https://reference.aspose.com/cells/javascript-cpp/shape/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Följande skärmbild visar [utdata PDF](5115555.pdf) som du kan ladda ned från länken. Här kan du se att datan i rött och gul bakgrund inte finns men alla former är där.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

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

            // Set the load options, we only want to load shapes and do not want to load data
            const loadOptions = new LoadOptions(LoadFormat.Xlsx);
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.Chart);

            // Create workbook object from uploaded excel file using load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Save the output in pdf format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sampleFilterChars_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
