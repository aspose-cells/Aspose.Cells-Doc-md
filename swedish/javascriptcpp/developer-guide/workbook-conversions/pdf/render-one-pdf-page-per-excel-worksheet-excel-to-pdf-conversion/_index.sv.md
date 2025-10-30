---
title: Rendera en PDF sida per Excel arbetsblad  Excel till PDF konvertering med JavaScript via C++
linktitle: Rendera en PDF sida per Excel ark  Konvertering av Excel till PDF
type: docs
weight: 100
url: /sv/javascript-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

När du arbetar med stora Microsoft Excel-filer (till exempel en arbetsbok med många blad, varje med 50 kolumner och 300 eller fler rader data), vill du kanske att PDF-utgången visar en sida per arbetsblad, oavsett storleken på arbetsbladet. Detta innebär att varje sida sannolikt kommer att ha en radikalt annorlunda sidstorlek. Detta kan uppnås genom att använda Aspose.Cells for JavaScript via C++.

{{% /alert %}}

Se följande exempel på kod som konverterar en Excel-fil med flera kalkylblad till PDF.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Excel to PDF</title>
    </head>
    <body>
        <h1>Convert Excel to PDF (One Page Per Worksheet)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Initialize a new Workbook by opening the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement one page per worksheet option
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.onePagePerSheet = true;

            // Save the PDF file (returns binary data)
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Om [PdfSaveOptions.onePagePerSheet](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--) är aktiverat till **true**, kommer allt bladinnehåll att renderas till en PDF-sida.

{{% /alert %}} {{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler är det bäst att ringa [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) precis innan du renderar kalkylbladet till PDF. Detta säkerställer att de formelberoende värdena omberäknas, och de korrekta värdena visas i PDF:en.

{{% /alert %}}
