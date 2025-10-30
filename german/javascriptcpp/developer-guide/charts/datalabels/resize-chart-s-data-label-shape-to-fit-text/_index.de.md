---
title: Diagramm Datenbeschriftungsform anpassen, um Text mit JavaScript via C++ anzupassen
linktitle: Größe der Beschriftungsform des Diagramms anpassen, um den Text anzupassen
description: Erfahren Sie, wie Sie die Form der Datenbeschriftung in einem Diagramm anpassen, um den Text in Aspose.Cells for JavaScript via C++ einzupassen. Unser Leitfaden zeigt, wie Sie die Größe und Form des Beschriftungscontainers anpassen, um eine korrekte Anzeige ohne Trunkierung oder Überlappung zu gewährleisten.
keywords: Aspose.Cells for JavaScript via C++, Diagrammerstellung, Datenbeschriftungen, Formen anpassen, Text schnell einpassen, Trunkierung, Überlappung.
type: docs
weight: 220
url: /de/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}  
Die Excel-Anwendung bietet die Option **Form an Text anpassen** für Diagrammdatenbeschriftungen, um die Größe der Form zu erhöhen, damit der Text hineinpasst.  
{{% /alert %}}  

## **So passen Sie die Form der Datenbeschriftung in einem Diagramm an, damit der Text in Microsoft Excel passt**  

Diese Option kann in der Excel-Benutzeroberfläche durch Auswahl einer beliebigen Datenbeschriftung im Diagramm aufgerufen werden. Klicken Sie mit der rechten Maustaste und wählen Sie das Menü **Datenbeschriftungen formatieren**. Unter dem Tab **Größe & Eigenschaften** expandieren Sie **Ausrichtung**, um die zugehörigen Eigenschaften einschließlich der Option **Form ändern, um Text anzupassen** anzuzeigen.  

## **Wie man die Form der Datenbeschriftung im Diagramm anpasst, um den Text mit Aspose.Cells for JavaScript via C++ einzufügen**  

Um die Excel-Funktion nachzuahmen, die die Formen der Datenbeschriftungen an den Text anpasst, haben die Aspose.Cells APIs die boolesche Eigenschaft [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--) freigegeben. Der folgende Code zeigt ein einfaches Nutzungsszenario der [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--)-Eigenschaft.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Data Labels Resize Example</h1>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet that contains the Chart
            const sheet = workbook.worksheets.get(0);

            for (let c = 0; c < sheet.charts.count; c++) {
                // Access the Chart
                const chart = sheet.charts.get(c);

                for (let index = 0; index < chart.nSeries.count; index++) {
                    // Access the DataLabels of indexed NSeries
                    const labels = chart.nSeries.get(index).dataLabels;

                    // Set ResizeShapeToFitText property to true
                    labels.isResizeShapeToFitText = true;
                }

                // Calculate Chart
                chart.calculate();
            }

            // Save the result
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
