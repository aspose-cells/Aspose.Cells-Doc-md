---
title: Hämta pappersbredd och höjd för sidinställningen för arbetsblad med JavaScript via C++
linktitle: Hämta papperets bredd och höjd för sidbildningsinställningen för arket
type: docs
weight: 50
url: /sv/javascript-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Upptäck hur man får Excel arks Sidinställning Pappersbredd och höjd med JavaScript via C++ programmatisk.
keywords: excel sidinställning pappersbredd JavaScript via C++, excel sidinställning papperhöjd JavaScript via C++
---

## **Möjliga användningsscenario**

Ibland behöver du veta bredden och höjden på papperstorleken som har anpassats i siduppställningen för arbetsbladet. Använd [**PageSetup.paperWidth**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperWidth--)- och [**PageSetup.paperHeight**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperHeight--)-egenskaperna för detta ändamål.

## **Hämta pappersbredd och höjd i sidinställningen för kalkylblad**

Följande exempel förklarar användningen av [**PageSetup.paperWidth**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperWidth--) och [**PageSetup.paperHeight**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperHeight--)-egenskaperna. Det ändrar först pappersstorleken till *A2* och hittar sedan bredden och höjden på papperet, därefter ändrar det till *A3*, *A4*, *Letter* och hittar respektive bredd och höjd på papperet.

### **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Paper Size Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // If a file is selected, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Set paper size to A2 and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA2;
            console.log("PaperA2: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            // Set paper size to A3 and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA3;
            console.log("PaperA3: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            // Set paper size to A4 and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA4;
            console.log("PaperA4: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            // Set paper size to Letter and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperLetter;
            console.log("PaperLetter: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            const outputLines = [
                "PaperA2: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight,
                "PaperA3: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight,
                "PaperA4: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight,
                "PaperLetter: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight
            ];

            document.getElementById('result').innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
        });
    </script>
</html>
```

### **Konsoloutput**



{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
