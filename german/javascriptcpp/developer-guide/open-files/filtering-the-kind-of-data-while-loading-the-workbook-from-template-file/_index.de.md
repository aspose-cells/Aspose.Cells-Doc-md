---
title: Filtern der Art der Daten beim Laden der Arbeitsmappe aus einer Vorlagendatei mit JavaScript über C++
linktitle: Filtern der Art der Daten beim Laden des Arbeitsbuches aus der Vorlagendatei
type: docs
weight: 400
url: /de/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}
Manchmal möchten Sie angeben, welche Art von Daten beim Erstellen der Arbeitsmappe aus der Vorlage geladen werden soll. Das Filtern geladener Daten kann die Leistung für Ihren speziellen Zweck verbessern, insbesondere bei Verwendung der [LightCells APIs](/cells/de/javascript-cpp/using-lightcells-api/). Bitte verwenden Sie zu diesem Zweck die Eigenschaft [**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--).
{{% /alert %}}

Der folgende Beispielcode lädt nur Shape-Objekte beim Laden der Arbeitsmappe aus der [Vorlagendatei](5115552.xlsx), die Sie über den angegebenen Link herunterladen können. Der folgende Screenshot zeigt die Inhalte der [Vorlagendatei](5115552.xlsx) und erklärt auch, dass die in Rot gefärbten Daten und der gelbe Hintergrund nicht geladen werden, da die Eigenschaft [**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--) auf [**Shape**](https://reference.aspose.com/cells/javascript-cpp/shape/) gesetzt wurde.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Der folgende Screenshot zeigt das [Ausgabe-PDF](5115555.pdf), das Sie aus dem angegebenen Link herunterladen können. Hier sehen Sie, dass die Daten in roter Farbe und gelbem Hintergrund nicht vorhanden sind, aber alle Formen sind vorhanden.

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
