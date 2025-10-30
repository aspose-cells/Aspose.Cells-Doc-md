---
title: Skapa PdfBookmarkEntry för diagramblad med JavaScript via C++
linktitle: Skapa PdfBookmarkEntry för diagramkalkylblad
type: docs
weight: 50
url: /sv/javascript-cpp/create-pdfbookmarkentry-for-chart-sheet/
description: Lär dig hur man skapar PdfBookmarkEntry för diagramblad med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

Tidigare skapade Aspose.Cells [**PdfBookmarkEntry**](https://reference.aspose.com/cells/javascript-cpp/pdfbookmarkentry) för ett normalt blad. Men nu kan Aspose.Cells också skapa [**PdfBookmarkEntry**](https://reference.aspose.com/cells/javascript-cpp/pdfbookmarkentry) för diagramblad. Eftersom ett diagramblad inte har några andra celler än cell A1, kommer det att skapa ett [**PdfBookmarkEntry**](https://reference.aspose.com/cells/javascript-cpp/pdfbookmarkentry) för endast cell A1.  

## **Skapa PdfBookmarkEntry för diagramblad**  

Följande exempelkod laddar in [prov Excelfil](61767756.xlsx) som har fyra ark. Två av dem är normala ark och de andra två är diagramark. Den skapar fyra bokmärkesposter enligt följande  

- Bokmärke-I  
- Bokmärke-II-Chart1  
- Bokmärke-III  
- Bokmärke-IV-Chart2  

Följande skärmbild visar [utdata PDF](61767757.pdf) genererad av exemplet.  

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create PDF Bookmark Entry for Chart Sheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfBookmarkEntry, PdfSaveOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access all four worksheets
            const sheet1 = workbook.worksheets.get(0);
            const sheet2 = workbook.worksheets.get(1);
            const sheet3 = workbook.worksheets.get(2);
            const sheet4 = workbook.worksheets.get(3);

            // Create Pdf Bookmark Entry for Sheet1
            const ent1 = new PdfBookmarkEntry();
            ent1.destination = sheet1.cells.get("A1");
            ent1.text = "Bookmark-I";

            // Create Pdf Bookmark Entry for Sheet2 - Chart
            const ent2 = new PdfBookmarkEntry();
            ent2.destination = sheet2.cells.get("A1");
            ent2.text = "Bookmark-II-Chart1";

            // Create Pdf Bookmark Entry for Sheet3
            const ent3 = new PdfBookmarkEntry();
            ent3.destination = sheet3.cells.get("A1");
            ent3.text = "Bookmark-III";

            // Create Pdf Bookmark Entry for Sheet4 - Chart
            const ent4 = new PdfBookmarkEntry();
            ent4.destination = sheet4.cells.get("A1");
            ent4.text = "Bookmark-IV-Chart2";

            // Arrange all Bookmark Entries
            const lst = [];
            lst.push(ent2);
            lst.push(ent3);
            lst.push(ent4);

            // Create Pdf Save Options with Bookmark Entries
            const opts = new PdfSaveOptions();
            opts.bookmark = ent1;

            // Save the output Pdf
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCreatePdfBookmarkEntryForChartSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
