---
title: Ange DBNum anpassad pattern formatering
linktitle: Ange DBNum anpassad pattern formatering
description: Aspose.Cells är ett bibliotek för JavaScript via C++ som stöder formatering av datum och nummer med hjälp av anpassade formateringsmönster. Denna artikel visar hur man anger det dbnum anpassade formatmönstret för bättre kontroll över nummervisningen.
keywords: Aspose.Cells, JavaScript via C++, elektroniskt kalkylblad, anpassat formatmönster, formatering, dbnum , kontrollera visning
type: docs
weight: 110
url: /sv/javascript-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Möjliga användningsscenario**

Aspose.Cells for JavaScript via C++ stöder det *DBNum* anpassade mönsterformatet. Till exempel, om ditt cellvärde är 123 och du anger dess anpassade formatering som [DBNum2][$-804]Generell kommer det att visas som 壹佰贰拾叁. Du kan specificera din anpassade formatering av cellen med hjälp av [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) metod och [**Style.custom(string)**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) metod.

## **Exempelkod**

Följande exempel visar hur man specificerar anpassad *DBNum*-mönsterformatering. Kontrollera dess [utdata PDF](43352081.pdf) för mer hjälp.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - DBNum Custom Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Access cell A1 and put value 123.
            const cell = ws.cells.get("A1");
            cell.value = 123;

            // Access cell style.
            const st = cell.style;

            // Specifying DBNum custom pattern formatting.
            st.custom = "[DBNum2][$-804]General";

            // Set the cell style.
            cell.style = st;

            // Set the first column width.
            ws.cells.columns.get(0).width = 30;

            // Save the workbook in output pdf format.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDBNumCustomFormatting.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
