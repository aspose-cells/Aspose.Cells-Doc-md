---
title: Automatisches Anpassen von Spalten und Zeilen beim Laden von HTML in Arbeitsmappe mit JavaScript über C++
linktitle: Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe
type: docs
weight: 120
url: /de/javascript-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Erfahren Sie, wie Sie Spalten und Zeilen automatisch anpassen, während HTML Dateien in einer Arbeitsmappe mit Aspose.Cells for JavaScript über C++ geladen werden.
---

## **Mögliche Verwendungsszenarien**

 Sie können Spalten und Zeilen automatisch anpassen, während Sie Ihre HTML-Datei innerhalb des Workbook-Objekts laden. Setzen Sie dazu die Eigenschaft [**HtmlLoadOptions.autoFitColsAndRows**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#autoFitColsAndRows--) auf **true**.

## **Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe**

Der folgende Beispielcode lädt zuerst eine Beispiel-HTML-Datei in ein Workbook ohne Ladeoptionen und speichert es im XLSX-Format. Anschließend lädt er wieder die HTML-Datei, setzt dabei die Eigenschaft [**HtmlLoadOptions.autoFitColsAndRows**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#autoFitColsAndRows--) auf **true** und speichert erneut im XLSX-Format. Bitte laden Sie beide Ausgabedateien herunter: [Ausgabedatei ohne AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) und [Ausgabedatei mit AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). Das folgende Screenshot zeigt die Auswirkung der [**HtmlLoadOptions.autoFitColsAndRows**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#autoFitColsAndRows--)-Eigenschaft beider Dateien.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Load HTML and Save XLSX</title>
    </head>
    <body>
        <h1>Load HTML String into Workbook and Save</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Result 1</a>
            <a id="downloadLink2" style="display: none;">Download Result 2</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlLoadOptions, Utils } = AsposeCells;

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
            // Sample HTML.
            const sampleHtml = "<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>";

            // Convert HTML string to Uint8Array (memory stream).
            const ms = new TextEncoder().encode(sampleHtml);

            // Load memory stream into workbook.
            const wb1 = new Workbook(ms);

            // Save the workbook in xlsx format.
            const outputData1 = wb1.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'outputWithout_AutoFitColsAndRows.xlsx';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download outputWithout_AutoFitColsAndRows.xlsx';

            // Specify the HTMLLoadOptions and set AutoFitColsAndRows = true.
            const opts = new HtmlLoadOptions();
            opts.autoFitColsAndRows = true;

            // Load memory stream into workbook with the above HTMLLoadOptions.
            const wb2 = new Workbook(ms, opts);

            // Save the workbook in xlsx format.
            const outputData2 = wb2.save(SaveFormat.Xlsx);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'outputWith_AutoFitColsAndRows.xlsx';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download outputWith_AutoFitColsAndRows.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Use the download links to get the generated files.</p>';
        });
    </script>
</html>
```
