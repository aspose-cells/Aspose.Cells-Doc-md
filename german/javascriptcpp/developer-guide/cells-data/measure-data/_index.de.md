---
title: Messung der Breite und Höhe des Zellenwerts in Pixeln
linktitle: Messung der Größe
type: docs
weight: 260
url: /de/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: Erfahren Sie, wie man die Breite und Höhe des Zellwerts in Pixeln mit dem Aspose.Cells for JavaScript via C++ misst.
keywords: Messen der Breite des Zellwerts in Pixeln JavaScript via C++, Messen der Höhe des Zellwerts in Pixeln JavaScript via C++, Erhalten der Breite des Zellwerts in Pixeln JavaScript via C++, Erhalten der Höhe des Zellwerts in Pixeln JavaScript via C++
---

{{% alert color="primary" %}}  

Manchmal müssen Sie die Breite und Höhe des Zellwerts berechnen, um den Zellwert in die Zelle zu passen. Aspose.Cells bietet [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) und [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--) Methoden für diesen Zweck. Durch die Verwendung dieser Methoden können Sie die Breite und Höhe des Zellwerts berechnen und dann die Breite der Spalte und die Höhe der Zeile dieser Zelle entsprechend setzen. Dadurch wird der Zellwert dann in die Zelle passt.  

Alternativ können Sie auch [Zeilen und Spalten Ihrer Zelle oder des Zellbereichs automatisch anpassen](/cells/de/javascript-cpp/autofit-rows-and-columns/) mithilfe der Aspose.Cells-APIs.  

{{% /alert %}}  

 Der folgende Code erklärt die Verwendung der [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) und [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--) Methoden.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Size Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell B2 and add some value inside it
            const cell = worksheet.cells.get("B2");
            cell.value = "Welcome to Aspose!";

            // Enlarge its font to size 16
            const style = cell.style;
            style.font.size = 16;
            cell.style = style;

            // Calculate the width and height of the cell value in unit of pixels
            const widthOfValue = cell.widthOfValue;
            const heightOfValue = cell.heightOfValue;

            // Print both values to the page
            document.getElementById('result').innerHTML = `<p>Width of Cell Value: ${widthOfValue}</p><p>Height of Cell Value: ${heightOfValue}</p>`;

            // Set the row height and column width to adjust/fit the cell value inside cell
            worksheet.cells.setColumnWidthPixel(1, widthOfValue);
            worksheet.cells.setRowHeightPixel(1, heightOfValue);

            // Save the output excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```


## **Erweiterte Themen**  
- [Breite des Zellenwerts abrufen](/cells/de/javascript-cpp/get-text-width-of-cell-value/)
