---
title: Unicode Ergänzungszeichen im Ausgabepdf mit Aspose.Cells for JavaScript über C++ rendern
linktitle: Unicode Supplementary Zeichen im Ausgabe PDF durch Aspose.Cells rendern
type: docs
weight: 350
url: /de/javascript-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Lernen Sie, wie Sie Unicode Ergänzungszeichen im Ausgabepdf mit Aspose.Cells for JavaScript über C++ rendern. 
---

{{% alert color="primary" %}}

Normale Unicode-Zeichen sind 2 Byte lang, während Unicode-Supplementary-Zeichen 4 Byte lang sind. Aspose.Cells unterstützt jetzt das Rendern dieser 4-Byte-Unicode-Zeichen.

Im Unicode-Standard für Zeichen handelt es sich bei den Supplementary-Zeichen um Zeichen, denen die Codepunkte von U+10000 bis U+10FFFF zugewiesen sind. Mit anderen Worten, dies sind die Unicode-Zeichen größer als U+FFFF.

- In UTF-8 sind diese Zeichen jeweils 4 Bytes lang.
- In UTF-16 benötigen diese Zeichen 2 Ersatzzeichen (16-Bit-Einheiten).

{{% /alert %}}

## Unicode-Supplementary-Zeichen im AusgabepDF durch Aspose.Cells for JavaScript via C++ rendern

Das folgende Bildschirmfoto zeigt, wie Aspose.Cells die [Quelldatei Excel](5115563.xlsx) in das [Ausgabepdf](5115564.pdf) gerendert hat. Wie Sie sehen können, wurden alle drei Unicode-Zusatzzeichen exakt so gerendert, wie es Microsoft Excel tut.

![todo:image_alt_text](output.png)

## Beispielcode

Sie können diesen Beispiellcode verwenden, um die [Quellexceldatei](5115563.xlsx) in die [Ausgabepdf](5115564.pdf) zu konvertieren.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Unicode Supplementary Characters to PDF</title>
    </head>
    <body>
        <h1>Render Unicode Supplementary Characters to PDF</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RenderUnicodeInOutput_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
