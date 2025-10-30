---
title: Ladda arbetsbok med angiven pappersstorlek för skrivare via JavaScript och C++
linktitle: Ladda arbetsboken med angiven skrivarpappersstorlek
type: docs
weight: 430
url: /sv/javascript-cpp/load-workbook-with-specified-printer-paper-size/
description: Lär dig att ställa in skrivarpapperstorlek när du laddar en arbetsbok med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}
 Du kan ange den skrivarpapperstorlek du vill ha när du laddar din arbetsbok med [**LoadOptions.paperSize(PaperSizeType)**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#paperSize-papersizetype-)-egenskapen. Observera att om du skapar en ny fil i MS Excel, är pappersstorleken densamma som inställningen för standardskrivaren på din dator.
{{% /alert %}}

 Följande exempel kod illustrerar användningen av [**LoadOptions.paperSize(PaperSizeType)**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#paperSize-papersizetype-)-egenskapen. Den skapar först en arbetsbok, sparar den i ett minnesflöde i XLSX-format. Sedan laddar den den med A5-pappersstorlek och sparar den i PDF-format. Sedan laddar den den igen med A3-pappersstorlek och sparar den i PDF-format igen. Om du öppnar utdata-PDF:erna och kontrollerar deras pappersstorlek, kommer du att se att de är olika. Den ena är A5 och den andra är A3. Vänligen ladda ner [A5-utdata PDF](5115234.pdf) och [A3-utdata PDF](5115233.pdf) genererade av koden för referens.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Load Workbook With Printer Size Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLinkA5" style="display: none; margin-right: 10px;">Download A5 PDF</a>
        <a id="downloadLinkA3" style="display: none;">Download A3 PDF</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, PaperSizeType, SaveFormat, Utils } = AsposeCells;

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
            // This example does not require a file input; file input is present per template.
            const resultDiv = document.getElementById('result');

            // Create a sample workbook and add some data inside the first worksheet
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("P30");
            cell.value = "This is sample data.";

            // Save the workbook into a byte array (in-memory)
            const msData = workbook.save(SaveFormat.Xlsx);

            // Load the workbook from memory with A5 paper size
            const opts = new LoadOptions(LoadFormat.Xlsx);
            opts.paperSize = PaperSizeType.PaperA5;
            const workbookA5 = new Workbook(msData, opts);

            // Save the workbook in PDF format (A5)
            const outputDataA5 = workbookA5.save(SaveFormat.Pdf);
            const blobA5 = new Blob([outputDataA5], { type: 'application/pdf' });
            const downloadLinkA5 = document.getElementById('downloadLinkA5');
            downloadLinkA5.href = URL.createObjectURL(blobA5);
            downloadLinkA5.download = 'LoadWorkbookWithPrinterSize-a5_out.pdf';
            downloadLinkA5.style.display = 'inline-block';
            downloadLinkA5.textContent = 'Download A5 PDF';

            // Load the workbook again from the same memory data with A3 paper size
            opts.paperSize = PaperSizeType.PaperA3;
            const workbookA3 = new Workbook(msData, opts);

            // Save the workbook in PDF format (A3)
            const outputDataA3 = workbookA3.save(SaveFormat.Pdf);
            const blobA3 = new Blob([outputDataA3], { type: 'application/pdf' });
            const downloadLinkA3 = document.getElementById('downloadLinkA3');
            downloadLinkA3.href = URL.createObjectURL(blobA3);
            downloadLinkA3.download = 'LoadWorkbookWithPrinterSize-a3_out.pdf';
            downloadLinkA3.style.display = 'inline-block';
            downloadLinkA3.textContent = 'Download A3 PDF';

            resultDiv.innerHTML = '<p style="color: green;">PDF files generated successfully. Use the links above to download the A5 and A3 PDFs.</p>';
        });
    </script>
</html>
```
