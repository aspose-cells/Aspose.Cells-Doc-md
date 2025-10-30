---
title: AutoAnpassa Rader för Rendering med JavaScript via C++
linktitle: Autoanpassa rader för rendering
type: docs
weight: 130
url: /sv/javascript-cpp/autofit-rows-for-rendering/
description: Lära dig hur man auto anpassar rader för rendering i Excel med hjälp av Aspose.Cells for JavaScript via C++. Förhindra textklippning i sparade PDF filer.
---

Generellt, när du vill visa all text i en cell kan du autofitta raden i Normalvy med 100% zoom i Microsoft Excel. Detta gör att texten är fullt synlig i Normalvy, och även när du skriver ut eller sparar filen som PDF, visas texten korrekt.

Men, i vissa fall fungerar autofittning av raden bra i Normalvy, men när du växlar till utskriftsvy eller sparar filen som PDF, klipps texten. Kontrollera källfilen [Book1.xlsx](Book1.xlsx) och skärmbilder.

![text klipps i utskriftsvyn](text_klipps_i_utskriftsvyn.png)

Om du vill förhindra att text klipps i den sparade PDF-filen, kan du auto-anpassa raden med [AutoFitterOptions.forRendering](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#forRendering--) alternativet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows and Save as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, AutoFitterOptions, SaveFormat, Utils } = AsposeCells;

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

            // Init workbook instance from uploaded file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set autofit options for rendering.
            const autoFitterOptions = new AutoFitterOptions();
            autoFitterOptions.forRendering = true;

            // Autofit rows with options on first worksheet.
            const worksheet = workbook.worksheets.get(0);
            worksheet.autoFitRows(autoFitterOptions);

            // Save to pdf.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

Nu är texten inte klippt i den här PDF-filen.

![text klipps inte i sparad pdf](text_klipps_inte_i_sparad_pdf.png)
