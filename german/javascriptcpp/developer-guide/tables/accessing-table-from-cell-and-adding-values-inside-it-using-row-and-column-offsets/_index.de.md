---
title: Zugriff auf Tabelle vom Zellbereich und Werte hinzufügen mit Zeilen und Spaltenversätzen mit JavaScript über C++
linktitle: Zugriff auf Tabelle von Zelle und Hinzufügen von Werten in sie unter Verwendung von Zeilen und Spaltenversatz
type: docs
weight: 230
url: /de/javascript-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}  

Normalerweise fügen Sie Werte in die Tabelle oder das Listenobjekt mit der [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)-Methode ein. Manchmal müssen Sie jedoch Werte in die Tabelle oder das Listenobjekt unter Verwendung des Zeilen- und Spaltenoffsets hinzufügen.  

Um eine Tabelle oder Listenobjekt von einer Zelle aus zuzugreifen, verwenden Sie die [**Cell.table**](https://reference.aspose.com/cells/javascript-cpp/cell/#table--) Eigenschaft. Um Werte mit Zeilen- und Spaltenversätzen hinzuzufügen, verwenden Sie die [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/javascript-cpp/listobject/#putCellValue-number-number-object-) Methode.  

{{% /alert %}}  

Das folgende Screenshot zeigt die Quell-Excel-Datei, die im Code verwendet wird. Es enthält die leere Tabelle und hebt die Zelle D5 hervor, die innerhalb der Tabelle liegt. Wir greifen auf diese Tabelle von Zelle D5 aus mit der [**Cell.table**](https://reference.aspose.com/cells/javascript-cpp/cell/#table--)-Eigenschaft zu und fügen dann die Werte darin mit den Methoden [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) und [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/javascript-cpp/listobject/#putCellValue-number-number-object-) hinzu.  

## Beispiel  

### Screenshots zum Vergleich der Quell- und Ausgabedateien  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

Der folgende Screenshot zeigt die durch den Code generierte Ausgabedatei. Wie Sie sehen können, hat die Zelle D5 einen Wert und die Zelle F6, die sich im Offset 2,2 der Tabelle befindet, hat ebenfalls einen Wert.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### JavaScript-Code, um von einer Zelle aus auf die Tabelle zuzugreifen und Werte mithilfe von Zeilen- und Spaltenversätzen hinzuzufügen  

Der folgende Beispielcode lädt die oben gezeigte Excel-Quelldatei und fügt Werte in die Tabelle ein, um die oben gezeigte Ausgabedatei zu generieren.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Accessing Table Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell D5 which lies inside the table
            const cell = worksheet.cells.get("D5");

            // Put value inside the cell D5
            cell.value = "D5 Data";

            // Access the Table from this cell
            const table = cell.table;

            // Add some value using Row and Column Offset
            table.putCellValue(2, 2, "Offset [2,2]");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
