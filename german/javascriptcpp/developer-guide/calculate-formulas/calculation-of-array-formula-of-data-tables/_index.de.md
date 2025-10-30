---
title: Berechnung der Array Formel von Datentabellen mit JavaScript via C++
linktitle: Berechnung der Array Formel von DatenTabellen
description: So verwenden Sie die Aspose.Cells Bibliothek, um Array Formeln für eine Datentabelle in Microsoft Excel mit JavaScript via C++ zu berechnen. Laden oder erstellen Sie eine Excel Datei, berechnen Sie die Array Formel und speichern Sie die modifizierte Datei.
keywords: Aspose.Cells, Excel, Datentabellen, Array Formeln, Berechnungen JavaScript via C++
type: docs
weight: 70
url: /de/javascript-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Sie können eine Datentabelle in Microsoft Excel mit Data > What-If Analysis > Data Table... erstellen. Aspose.Cells ermöglicht jetzt die Berechnung der Array-Formel einer Datentabelle. Verwenden Sie [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) wie gewohnt zur Berechnung aller Arten von Formeln.

{{% /alert %}}

Im folgenden Beispiellcode haben wir die [Quellexceldatei](5115535.xlsx) verwendet. Wenn Sie den Wert von Zelle B1 auf 100 ändern, werden die Werte der Datentabelle, die mit Gelb gefüllt sind, wie in den folgenden Bildern gezeigt, zu 120. Der Beispiellcode generiert die [Ausgabepdf](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>DataTable Calculation Example</h1>
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

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
            const cell = worksheet.cells.get("B1");
            cell.putValue(100);

            // Calculate formula, now it also calculates Data Table array formula
            workbook.calculateFormula();

            // Save the workbook in pdf format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
