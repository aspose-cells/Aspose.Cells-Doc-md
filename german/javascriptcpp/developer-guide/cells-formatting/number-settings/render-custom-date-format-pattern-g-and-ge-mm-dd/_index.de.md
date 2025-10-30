---
title: Benutzerdefiniertes Datum Format g und ge mm tt
linktitle: Benutzerdefiniertes Datum Format g und ge mm tt  
description: Lernen Sie, wie Sie benutzerdefinierte Datumsformatmuster g und ge in Aspose.Cells for JavaScript mittels C++ rendern, um die Datumsausgabe in Tabellenkalkulationen zu steuern.  
keywords: Aspose.Cells, JavaScript Bibliothek, elektronische Tabelle, benutzerdefiniertes Datumsformat, Rendering, Muster g , Muster ge , Steuerung der Anzeige    
type: docs  
weight: 160  
url: /de/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/  
---  

{{% alert color="primary" %}}  

Aspose.Cells kann jetzt benutzerdefinierte Datumsformatmuster wie g, ge.mm.tt und ähnliche rendern. Bitte überprüfen Sie die angehängte [Quellexceldatei](5112361.xlsx) und die [konvertierte PDF-Datei](5112360.pdf) von Aspose.Cells zu Ihrer Referenz.

{{% /alert %}}  

Der folgende Beispielcode wandelt die [Quellexceldatei](5112361.xlsx) um, die Datumsangaben mit benutzerdefinierten Formatmustern wie g und ge.mm.tt enthält, in eine [Ausgabedatei im PDF-Format](5112360.pdf) um.  


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

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomDateFormat_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
