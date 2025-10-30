---
title: Infoga Tidslinje
linktitle: Tidslinjer
type: docs
weight: 170
url: /sv/javascript-cpp/create-timeline/
description: Lär dig hur du skapar en tidslinje med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**

I stället för att justera filter för att visa datum kan du använda en PivotTable Tidslinje – ett dynamiskt filteralternativ som gör att du enkelt kan filtrera efter datum/tid och zooma in på perioden du vill ha med en skjutreglage. Microsoft Excel låter dig skapa tidslinje genom att välja en pivottabell och sedan klicka på *Infoga > Tidslinje*. Aspose.Cells for JavaScript via C++ tillåter också att skapa tidslinje med hjälp av [**Worksheet.timelines.add()**](https://reference.aspose.com/cells/javascript-cpp/timelinecollection/#add-pivottable-number-number-string-)-metoden.

## **Skapa tidslinje till en Pivot-tabell**

Se följande exempel. Det laddar den [exempel-Excel-filen](input.xlsx) som innehåller pivottabellen. Det skapar sedan tidslinjen baserat på det första grundläggande pivottjänstfältet. Slutligen sparar det arbetsboken i [utdata XLSX](output.xlsx) format. Följande skärmavbild visar tidslinjen som skapats av Aspose.Cells for JavaScript via C++ i output Excel-filen.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Timeline to Pivot Table</title>
    </head>
    <body>
        <h1>Add Timeline to Pivot Table</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access second worksheet (index 1)
            const sheet = workbook.worksheets.get(1);

            // Access first pivot table inside the worksheet
            const pivot = sheet.pivotTables.get(0);

            // Add timeline relating to pivot table (positioned at column 15, row 1) with caption "Ship Date"
            const index = sheet.timelines.add(pivot, 15, 1, "Ship Date");

            // Access the newly added timeline from timeline collection
            const timeline = sheet.timelines.get(index);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Timeline added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
