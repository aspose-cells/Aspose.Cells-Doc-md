---
title: Läs och manipulera Excel 2016 diagram med JavaScript via C++
linktitle: Läs och hantera Excel 2016 diagram
description: Lär dig hur du läser och manipulerar Excel 2016 diagram med Aspose.Cells for JavaScript via C++. Den här guiden visar hur du får tillgång till och ändrar olika diagramegenskaper.
keywords: Aspose.Cells for JavaScript via C++, Excel 2016 diagram, läs, manipulera, datapunkter, seriefärger, layout, hierarkisk diagram, cirkulärt diagram.
type: docs
weight: 48
url: /sv/javascript-cpp/read-and-manipulate-excel-2016-charts/
---

## **Möjliga användningsscenario**  
Aspose.Cells stöder nu läsning och hantering av Microsoft Excel 2016-diagram som inte finns i Microsoft Excel 2013 eller äldre versioner.  
## **Läs och hantera Excel 2016-diagram**  
Följande exempelkod laddar [källexcelfilen](22774101.xlsx) som innehåller Excel 2016-diagram i det första arbetsbladet. Den läser alla diagram en efter en och ändrar deras titel i enlighet med diagramtypen. Följande skärmdump visar källexcelfilen före kodens utförande. Som du kan se är diagramtiteln densamma för alla diagram.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

Följande skärmbild visar den [slutgiltiga Excel-filen](22774104.xlsx) efter körningen av koden. Som du kan se har diagramrubriken ändrats enligt dess diagramtyp.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **Exempelkod**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read and Update Chart Titles</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read selected file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet which contains the charts
            const sheet = workbook.worksheets.get(0);

            // Access all charts one by one and read their types
            const chartsCount = sheet.charts.count;
            let logHtml = '<ul>';
            for (let i = 0; i < chartsCount; i++) {
                // Access the chart
                const ch = sheet.charts.get(i);

                // Read chart type
                const typeStr = ch.type.toString();
                console.log(typeStr);

                // Change the title of the chart
                ch.title.text = "Chart Type is " + typeStr;

                logHtml += `<li>Chart ${i}: ${typeStr}</li>`;
            }
            logHtml += '</ul>';

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_excel2016Charts.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Charts updated successfully! Click the download link to get the modified file.</p>' + logHtml;
        });
    </script>
</html>
```  
## **Konsoloutput**  


{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **Fortsatta ämnen**  
- [Skapa vattenfalldiagram](/cells/sv/javascript-cpp/creating-waterfall-chart/)  
- [Skapa treemap-diagram](/cells/sv/javascript-cpp/creating-treemap-chart/)  
- [Skapa sunburst-diagram](/cells/sv/javascript-cpp/creating-sunburst-chart/)
