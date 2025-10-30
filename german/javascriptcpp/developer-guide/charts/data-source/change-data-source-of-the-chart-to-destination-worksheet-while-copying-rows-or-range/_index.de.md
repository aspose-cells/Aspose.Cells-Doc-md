---
title: Ändern Sie die Datenquelle des Diagramms auf das Zielarbeitsblatt, während Sie Zeilen oder Bereiche mit JavaScript über C++ kopieren
linktitle: Ändern Sie die Datenquelle des Diagramms in das Zieltabellenblatt beim Kopieren von Zeilen oder Bereich
description: Lernen Sie, wie Sie die Datenquelle eines Diagramms beim Kopieren von Zeilen oder einem Bereich in Aspose.Cells for JavaScript via C++ in ein Zielarbeitsblatt ändern. Diese Anleitung zeigt, wie Sie den Datenbereich des Diagramms aktualisieren und es mit dem Zielarbeitsblatt verknüpfen.
keywords: Aspose.Cells for JavaScript via C++, Diagrammerstellung, Datenquelle, Zielarbeitsblatt, Zeilen, Bereich, Kopieren, Aktualisieren, Datenbereich, Verlinkung.
type: docs
weight: 440
url: /de/javascript-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Mögliche Verwendungsszenarien**

 Wenn Sie Zeilen oder Bereiche mit Diagrammen in ein neues Arbeitsblatt kopieren, ändert sich die Datenquelle des Diagramms nicht. Wenn die Datenquelle z.B. `=Sheet1!$A$1:$B$4` ist, bleibt sie nach dem Kopieren in ein neues Arbeitsblatt unverändert, also `=Sheet1!$A$1:$B$4`. Es verweist weiterhin auf das alte Arbeitsblatt, also Sheet1. Dies ist auch das Verhalten in Microsoft Excel. Wenn Sie möchten, dass es auf das neue Zielarbeitsblatt verweist, verwenden Sie bitte die Eigenschaft [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--) und setzen sie auf **true** beim Aufrufen der Methode [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-). Wenn Ihr Zielarbeitsblatt DestSheet ist, ändert sich die Datenquelle Ihres Diagramms von `=Sheet1!$A$1:$B$4` zu `=DestSheet!$A$1:$B$4`.

## **Ändern der Datenquelle des Diagramms zur Zieltabelle beim Kopieren von Zeilen oder Bereichen**

Der folgende Beispielcode erläutert die Verwendung der [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--)-Eigenschaft beim Kopieren von Zeilen oder Bereichen mit Diagrammen in ein neues Arbeitsblatt. Der Code nutzt die [Beispieldatei](5113699.xlsx) und erzeugt die [Ausgabedatei](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Worksheet with Charts</title>
    </head>
    <body>
        <h1>Copy Worksheet with Charts Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first sheet which contains chart
            const source = wb.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = wb.worksheets.add("DestSheet");

            // Set CopyOptions.referToDestinationSheet to true
            const options = new AsposeCells.CopyOptions();
            options.referToDestinationSheet = true;

            // Copy all the rows of source worksheet to destination worksheet which includes chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options);

            // Save workbook in xlsx format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
