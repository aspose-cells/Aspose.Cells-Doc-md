---
title: CSV Datei mit mehreren Kodierungen mit JavaScript via C++ lesen
linktitle: CSV Datei mit mehreren Codierungen lesen
type: docs
weight: 200
url: /de/javascript-cpp/reading-csv-file-with-multiple-encodings/
description: Erfahren Sie, wie Sie CSV Dateien mit mehreren Kodierungen mit Aspose.Cells for JavaScript via C++ lesen.
---

{{% alert color="primary" %}}

Manchmal enthält Ihre CSV-Datei mehrere Kodierungen (Unicode, ANSI, UTF8, UTF7 usw.). Aspose.Cells ermöglicht es, solche CSV-Dateien zu laden und in andere Formate umzuwandeln, z.B. PDF oder XLSX.

{{% /alert %}}

Aspose.Cells bietet die [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--)-Eigenschaft, die du auf **true** setzen musst, um deine CSV-Datei mit mehreren Kodierungen korrekt zu laden.

Der folgende Screenshot zeigt eine Beispiel-CSV-Datei, die zwei Zeilen enthält. Die erste Zeile ist in **ANSI**-Codierung und die zweite Zeile ist in **Unicode**-Codierung

|**Eingabedatei**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Das folgende Beispiel zeigt die XLSX-Datei, die aus der oben genannten CSV-Datei konvertiert wurde, ohne die [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--)-Eigenschaft auf **true** zu setzen. Wie du sehen kannst, wurde der Unicode-Text nicht korrekt konvertiert.

|**Ausgabedatei 1: keine Berücksichtigung mehrerer Codierungen**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Der folgende Screenshot zeigt die XSLX-Datei, die aus der oben genannten CSV-Datei nach Setzen der [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--)-Eigenschaft auf **true** konvertiert wurde. Wie Sie sehen, wird der Unicode-Text jetzt korrekt umgewandelt.

|**Ausgabedatei 2: IsMultiEncoded ist auf true gesetzt**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Im Folgenden finden Sie den Beispielcode, der die obige CSV-Datei ordnungsgemäß in das XLSX-Format konvertiert.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Multi-Encoded CSV to XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Convert to XLSX</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create TxtLoadOptions and set isMultiEncoded property
            const options = new TxtLoadOptions();
            options.isMultiEncoded = true;

            // Load the CSV into a Workbook using the options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const outName = file.name.replace(/(\.[^/.]+)$/, '$1.out.xlsx');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = outName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to save the XLSX file.</p>';
        });
    </script>
</html>
```

## Verwandte Artikel

- [Öffnen von CSV-Dateien](/cells/de/javascript-cpp/opening-files-with-different-formats/#opening-csv-files)
