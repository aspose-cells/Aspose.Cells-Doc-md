---
title: Konvertieren Sie XLS Dateien mit Bildern oder Diagrammen in PDF mit JavaScript via C++
linktitle: Konvertierung von XLS Datei mit Bildern oder Diagrammen in PDF
type: docs
weight: 50
url: /de/javascript-cpp/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells unterstützt die Konvertierung von XLS-Dateien, die Bilder und Diagramme enthalten, in PDF-Dokumente. Aspose.Cells for JavaScript via C++ kann unabhängig arbeiten, um eine Tabelle in PDF zu konvertieren: Für die Konvertierung ist Aspose.PDF für JavaScript via C++ nicht erforderlich. Der Vorgang kann im Arbeitsspeicher durchgeführt werden, da er nicht von temporären oder Zwischen-XML-Dateien abhängt. Dies bedeutet, dass große Excel-Dateien, z.B. solche mit Bildern, Diagrammen und anderen Zeichenobjekten, schnell und effizient konvertiert werden können.

{{% /alert %}} 
## **Beispielcode**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}} 

Wenn die Tabelle Formeln enthält, ist es am besten, die Methode [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) kurz vor der Ausgabe in PDF aufzurufen. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet werden und die korrekten Werte im PDF angezeigt werden.

{{% /alert %}}
