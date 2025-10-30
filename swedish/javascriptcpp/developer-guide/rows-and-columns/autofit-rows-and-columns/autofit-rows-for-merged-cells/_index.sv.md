---
title: AutoAnpassa Rader för Sammanfogade Celler med JavaScript via C++
linktitle: Automatisk anpassning av rader för sammanslagna celler
type: docs
weight: 120
url: /sv/javascript-cpp/autofit-rows-for-merged-cells/
description: Lär dig hur du auto anpassar rader för sammanslagna celler med Aspose.Cells for JavaScript via C++. Implementera auto anpassningsfunktion för sammanslagna celler i kalkylblad.
---

{{% alert color="primary" %}}

Microsoft Excel har en funktion som låter dig automatiskt justera höjden på en cell enligt dess innehåll. Funktionen kallas automatisk anpassning av rader. Microsoft Excel tillämpar inte automatisk anpassning på sammanslagna celler som standard. Ibland blir funktionen viktig för en användare som verkligen behöver implementera automatisk anpassning av rader även på sammanslagna celler.

{{% /alert %}}

## **Hur man använder AutoFitMergedCellsType för att autofita rader**
Aspose.Cells for JavaScript via C++ stöder denna funktion genom [**AutoFitterOptions.autoFitMergedCellsType**](https://reference.aspose.com/cells/javascript-cpp/autofitmergedcellstype/)-API:et. Med detta API är det möjligt att automatiskt anpassa rader i ett kalkylblad inklusive sammanslagna celler. Här är en lista över alla möjliga typer av auto-anpassning av sammanslagna celler:

- Ingen
- Första raden
- Sista raden
- Varje rad

## **Autofit rader för sammanslagna celler**

Se följande kod, den skapar ett arbetsbok-objekt och lägger till flera arbetsblad. Använd olika metoder för autofit-operationer i varje blad. Skärmbilden visar resultaten efter körning av exempel-koden.

<br>
<img src="result.png" width=80% />

## **JavaScript Provkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Merged Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoFitterOptions, AutoFitMergedCellsType, Utils } = AsposeCells;

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
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const sheet1 = workbook.worksheets.get(0);

            // Create a range A1:B2
            const range = sheet1.cells.createRange(0, 0, 2, 2);

            // Merge the cells
            range.merge();

            // Insert value to the merged cell A1
            const cell1 = sheet1.cells.get(0, 0);
            cell1.value = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end";

            // Create a style object
            const style = cell1.style;

            // Set wrapping text on
            style.isTextWrapped = true;

            // Apply the style to the cell
            cell1.style = style;

            // Create an object for AutoFitterOptions
            const options = new AutoFitterOptions();

            // Only expands the height of the first row.
            options.autoFitMergedCellsType = AutoFitMergedCellsType.FirstLine;

            // Autofit rows in the sheet (including the merged cells)
            sheet1.autoFitRows(options);

            let index = workbook.worksheets.add();
            const sheet2 = workbook.worksheets.get(index);
            sheet2.name = "Sheet2";
            // Create a range A1:B2
            const range2 = sheet2.cells.createRange(0, 0, 2, 2);

            // Merge the cells
            range2.merge();

            // Insert value to the merged cell A1
            const cell2 = sheet2.cells.get(0, 0);
            cell2.value = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end";

            // Create a style object
            const style2 = cell2.style;

            // Set wrapping text on
            style2.isTextWrapped = true;

            // Apply the style to the cell
            cell2.style = style2;

            // Create an object for AutoFitterOptions
            const options2 = new AutoFitterOptions();

            // Only expands the height of the last row.
            options2.autoFitMergedCellsType = AutoFitMergedCellsType.LastLine;

            // Autofit rows in the sheet (including the merged cells)
            sheet2.autoFitRows(options2);

            index = workbook.worksheets.add();
            const sheet3 = workbook.worksheets.get(index);
            sheet3.name = "Sheet3";
            // Create a range A1:B2
            const range3 = sheet3.cells.createRange(0, 0, 2, 2);

            // Merge the cells
            range3.merge();

            // Insert value to the merged cell A1
            const cell3 = sheet3.cells.get(0, 0);
            cell3.value = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end";

            // Create a style object
            const style3 = cell3.style;

            // Set wrapping text on
            style3.isTextWrapped = true;

            // Apply the style to the cell
            cell3.style = style3;

            // Create an object for AutoFitterOptions
            const options3 = new AutoFitterOptions();

            // Only expands the height of each row.
            options3.autoFitMergedCellsType = AutoFitMergedCellsType.EachLine;

            // Autofit rows in the sheet (including the merged cells)
            sheet3.autoFitRows(options3);

            index = workbook.worksheets.add();
            const sheet4 = workbook.worksheets.get(index);
            sheet4.name = "Sheet4";
            // Create a range A1:B2
            const range4 = sheet4.cells.createRange(0, 0, 2, 2);

            // Merge the cells
            range4.merge();

            // Insert value to the merged cell A1
            const cell4 = sheet4.cells.get(0, 0);
            cell4.value = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end";

            // Create a style object
            const style4 = cell4.style;

            // Set wrapping text on
            style4.isTextWrapped = true;

            // Apply the style to the cell
            cell4.style = style4;

            // Create an object for AutoFitterOptions
            const options4 = new AutoFitterOptions();

            // Ignore merged cells.
            options4.autoFitMergedCellsType = AutoFitMergedCellsType.None;

            // Autofit rows in the sheet (not including the merged cells)
            sheet4.autoFitRows(options4);

            // Saving the modified Excel file and creating a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
