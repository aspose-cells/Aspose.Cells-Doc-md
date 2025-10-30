---
title: Lesen und Schreiben Sie Tabellen mit Query Table Data Source via JavaScript
linktitle: Tabelle mit Abfrage Tabellendatenquelle lesen und schreiben
type: docs
weight: 30
url: /de/javascript-cpp/read-and-write-table-with-query-table-data-source/
description: Lernen Sie, wie Sie eine Tabelle mit einer QueryTable Datenquelle mit Aspose.Cells for JavaScript über C++ lesen und schreiben. 
---

## **Tabelle mit Abfrage-Tabellendatenquelle lesen und schreiben**
Mit Aspose.Cells for JavaScript über C++ können Sie eine Tabelle lesen und schreiben, die eine QueryTable als Datenquelle hat. Die Unterstützung für dieses Feature ist auch für XLS-Dateien vorhanden. Das folgende Code-Snippet demonstriert das Lesen und Schreiben einer solchen Tabelle, indem die Tabelle zuerst gelesen und dann modifiziert wird, um die Summenzeile hinzuzufügen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>SampleTableWithQueryTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first table (ListObject) in the worksheet
            const table = worksheet.listObjects.get(0);

            // Check the data source type if it is query table
            if (table.dataSourceType === AsposeCells.TableDataSourceType.QueryTable) {
                table.showTotals = true;
            }

            // Save the modified workbook as Excel97To2003 (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleTableWithQueryTable_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Die Quell- und Ausgabedateien sind als Referenz angehängt.

[Quelldatei](96928091.xls)

[Ausgabedatei](96928092.xls)
