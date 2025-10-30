---
title: Ändra cells justering och behåll befintlig formatering
linktitle: Ändra cells justering och behåll befintlig formatering
description: Använd Aspose.Cells biblioteket för att ändra celljustering och bevara befintlig formatering i JavaScript via C++
keywords: Aspose.Cells, JavaScript via C++, Celljustering, Bevara befintlig formatering
type: docs
weight: 340
url: /sv/javascript-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Möjliga användningsscenario**

Ibland vill du ändra justeringen av flera celler men också behålla befintlig formatering. Aspose.Cells for JavaScript via C++ tillåter dig att göra detta med hjälp av [**StyleFlag.alignments(boolean)**](https://reference.aspose.com/cells/javascript-cpp/styleflag/#alignments-boolean-) metoden. Om du ställer in det **true**, kommer justeringsändringar att äga rum, annars inte. Observera att [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) objektet passeras som parameter till [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/range/#applyStyle-style-styleflag-) metoden som faktiskt tillämpar formateringen på ett cellområde.

## **Ändra cellers justering och behåll befintlig formatering**

Den följande exempelkoden läser in den [exempel Excel-filen](67338585.xlsx), skapar området och centrera justerar det horisontellt och vertikalt och behåller den befintliga formateringen intakt. Följande skärmdump jämför exempel Excel-filen och [utdata Excel-filen](67338586.xlsx) och visar att all befintlig formatering av cellerna är densamma förutom att cellerna nu är centralt justerade horisontellt och vertikalt.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Cells Alignment and Keep Existing Formatting</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, TextAlignmentType, Utils } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create cells range
            const range = worksheet.cells.createRange("B2:D7");

            // Create style object
            const style = workbook.createStyle();

            // Set the horizontal and vertical alignment to center using property assignments
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            // Create style flag object
            const flag = new StyleFlag();
            flag.alignments = true; // Set style flag alignments true

            // Apply style to range of cells
            range.applyStyle(style, flag);

            // Save the workbook in XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
