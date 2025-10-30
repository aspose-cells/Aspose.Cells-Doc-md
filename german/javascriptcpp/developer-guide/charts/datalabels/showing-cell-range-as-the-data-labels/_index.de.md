---
title: Anzeige des Zellbereichs als Datenbeschriftungen mit JavaScript via C++
linktitle: Anzeige des Zellenbereichs als Datenbeschriftungen
description: Erfahren Sie, wie Sie einen Zellbereich als Datenbeschriftungen in Diagrammen mit Aspose.Cells for JavaScript via C++ anzeigen. Unser Leitfaden zeigt, wie Sie die Beschriftungen mit Ihrer Datenquelle verknüpfen und formatieren, um genaue und aussagekräftige Informationen in Ihren Diagrammen bereitzustellen.
keywords: Aspose.Cells for JavaScript via C++, Diagrammerstellung, Datenbeschriftungen, Zellbereich, Datenquelle, Formatierung, Genauigkeit, aussagekräftige Informationen.
type: docs
weight: 130
url: /de/javascript-cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}
In Microsoft Excel 2013 können Sie einen Zellbereich für Datenbeschriftungen anzeigen. Aspose.Cells for JavaScript via C++ unterstützt dieses Feature.
{{% /alert %}}

## **Kontrollkästchen zum Anzeigen des Zellenbereichs als Datenbeschriftungen**

So zeigen Sie den Zellenbereich als Datenbeschriftungen in Microsoft Excel:

1. Wählen Sie die Seriendatenbeschriftungen aus und klicken Sie mit der rechten Maustaste, um das Kontextmenü zu öffnen.  
1. Wählen Sie **Datenelemente formatieren** aus. Beschriftungsoptionen werden angezeigt.  
1. Wählen oder deaktivieren Sie die Option **Beschriftung enthält - Wert aus Zellen**.  

Der folgende Beispielcode greift auf die Datenbeschriftungen einer Diagrammserie zu und setzt die [**DataLabels.showCellRange**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#showCellRange--) Eigenschaft auf **true**, um die Option **Beschriftung enthält - Wert aus Zellen** auszuwählen.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Show Range in Data Labels</title>
    </head>
    <body>
        <h1>Show Range in Data Labels Example</h1>
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

            // Create workbook from the source Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Check the "Label Contains - Value From Cells"
            const dataLabels = chart.nSeries.get(0).dataLabels;
            dataLabels.showCellRange = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
