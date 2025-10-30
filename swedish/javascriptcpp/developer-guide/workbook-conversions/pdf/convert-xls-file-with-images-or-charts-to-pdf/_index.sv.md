---
title: Konvertera XLS fil med bilder eller diagram till PDF med JavaScript via C++
linktitle: Konvertera XLS fil med bilder eller diagram till PDF
type: docs
weight: 50
url: /sv/javascript-cpp/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells stöder konvertering av XLS-filer som innehåller bilder och diagram till PDF-dokument. Aspose.Cells for JavaScript via C++ kan fungera självständigt för att konvertera ett kalkylblad till PDF: Aspose.PDF för JavaScript via C++ krävs inte för konverteringen. Processen kan göras i minnet eftersom den inte är beroende av tillfälliga eller mellanliggande XML-filer. Detta innebär att stora Excel-filer, till exempel med bilder, diagram och andra ritobjekt, kan konverteras snabbt och effektivt.

{{% /alert %}} 
## **Exempelkod**


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

Om kalkylbladet innehåller formler är det bäst att anropa [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) precis innan du konverterar till PDF. Doing så säkerställer att formelberoende värden omräknas, och de korrekta värdena visas i PDF.

{{% /alert %}}
