---
title: Kopiera Sparkline genom att specificera dataområde och plats för Sparkline grupp med JavaScript via C++
linktitle: Kopiera sparkline genom att ange dataområde och plats för sparklinegrupp
type: docs
weight: 300
url: /sv/javascript-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Lär dig hur du kopierar en sparkline i Excel genom att specificera dataområde och plats för sparkline grupp med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}
Microsoft Excel tillåter dig att kopiera en sparkline genom att ange dataområde och plats för en sparklinegrupp. Aspose.Cells stöder denna funktion.
{{% /alert %}}

För att kopiera en sparkline till andra celler i Microsoft Excel:

1. Välj cellen som innehåller sparklinen.  
2. Välj **Redigera data** från **Sparkline**-avsnittet på fliken **Design**.  
3. Välj **Redigera gruppplats och data**.  
4. Ange dataområdet och platsen.  
1. Klicka på **OK**.

Aspose.Cells tillhandahåller `SparklineCollection.add(dataRange, row, column)`-metoden för att ange dataintervall och plats för ett sparkline-grupp. Följande exempel kod laddar källfärgboken som visas i skärmbilden ovan, och tillgår sedan den första sparkline-gruppen och lägger till dataintervall och platsar i sparkline-gruppen. Slutligen skriver den ut resultatet som en Excel-fil på disken, vilket också visas i skärmbilden ovan.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sparkline Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first sparkline group
            const group = worksheet.sparklineGroups.get(0);

            // Add Data Ranges and Locations inside this sparkline group
            group.sparklines.add("Sheet1!D5:O5", 4, 15);
            group.sparklines.add("Sheet1!D6:O6", 5, 15);
            group.sparklines.add("Sheet1!D7:O7", 6, 15);
            group.sparklines.add("Sheet1!D8:O8", 7, 15);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sparklines added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
