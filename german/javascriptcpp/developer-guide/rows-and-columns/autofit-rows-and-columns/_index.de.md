---
title: Zeilen und Spalten mit JavaScript über C++ automatisch anpassen
linktitle: Zeilen und Spalten automatisch anpassen
type: docs
weight: 20
url: /de/javascript-cpp/autofit-rows-and-columns/
description: Dieser Artikel zeigt, wie man Zeilen, Spalten, verschmolzene Zellzeilen und Zeilen in einem Zellbereich mit Aspose.Cells for JavaScript über C++ automatisch anpasst.
keywords: Zeilen automatisch anpassen mit JavaScript über C++, Spalten automatisch anpassen JavaScript über C++, Zeile in einem Zellbereich automatisch anpassen JavaScript über C++, Zeilen verschmolzener Zellen automatisch anpassen JavaScript über C++
---

{{% alert color="primary" %}}  
Microsoft Excel ermöglicht es, die Breite und Höhe der Zellen automatisch an deren Inhalt anzupassen. Dieses Feature ist auch über Aspose.Cells for JavaScript über C++ verfügbar, sodass Entwickler die Dimensionen einer Zelle zur Laufzeit automatisch anpassen können.  
{{% /alert %}}  

## **Automatische Anpassung**  

Aspose.Cells stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) bereit, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) enthält eine Sammlung [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), die Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung eines Arbeitsblatts. Dieser Artikel beschäftigt sich mit der Verwendung der Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet), um Zeilen oder Spalten automatisch anzupassen.  

### **AutoFit Zeile - Einfach**  

Der einfachste Ansatz, um die Breite und Höhe einer Zeile automatisch anzupassen, besteht darin, die Methode [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) der [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-)-Klasse aufzurufen. Die [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-)-Methode nimmt einen Zeilenindex (der Zeile, die angepasst werden soll) als Parameter.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoFit Row</title>
    </head>
    <body>
        <h1>AutoFit Row Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the 3rd row of the worksheet (row index 1 is the 2nd row; original code used 1)
            worksheet.autoFitRow(1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Wie man eine Zeile in einem Zellenbereich automatisch anpasst**  

Eine Zeile besteht aus vielen Spalten. Aspose.Cells ermöglicht es Entwicklern, eine Zeile basierend auf den Inhalten innerhalb eines Zellbereichs in der Zeile automatisch anzupassen, indem eine überladene Version der Methode [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-number-number-) aufgerufen wird. Diese nimmt die folgenden Parameter entgegen:  

- **Zeilenindex**, der Index der zu automatisch anzupassenden Zeile.  
- **Erster Spaltenindex**, der Index der ersten Spalte der Zeile.  
- **Letzter Spaltenindex**, der Index der letzten Spalte der Zeile.  

Die [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-number-number-)-Methode überprüft den Inhalt aller Spalten in der Zeile und passt die Zeile entsprechend an.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoFit Row</title>
    </head>
    <body>
        <h1>Auto-Fit Row Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the 3rd row of the worksheet (row index 1, startColumn 0, endColumn 5)
            worksheet.autoFitRow(1, 0, 5);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Wie man eine Spalte in einem Zellenbereich automatisch anpasst**  

Eine Spalte besteht aus vielen Zeilen. Es ist möglich, eine Spalte anhand des Inhalts in einem Bereich von Zellen durch Aufruf einer überladenen Version der Methode [**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-) anzupassen, die die folgenden Parameter akzeptiert:  

- **Spaltenindex**, der Index der zu automatisch anzupassenden Spalte.  
- **Erster Zeilenindex**, der Index der ersten Zeile der Spalte.  
- **Letzter Zeilenindex**, der Index der letzten Zeile der Spalte.  

Die [**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-)-Methode überprüft den Inhalt aller Zeilen in der Spalte und passt die Spalte entsprechend an.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells AutoFit Column Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the Column of the worksheet (column index 4)
            worksheet.autoFitColumn(4);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Wie man Zeilen für zusammengeführte Zellen automatisch anpasst**  

Mit Aspose.Cells ist es möglich, Zeilen automatisch anzupassen, selbst bei Zellen, die zusammengeführt wurden, mithilfe der API [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions). Die Klasse [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) bietet die Eigenschaft [**AutoFitterOptions.autoFitMergedCellsType()**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#autoFitMergedCellsType--), die verwendet werden kann, um Zeilen für zusammengeführte Zellen automatisch anzupassen. [**AutoFitterOptions.autoFitMergedCellsType()**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#autoFitMergedCellsType--) akzeptiert eine [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/javascript-cpp/autofitmergedcellstype) aufzählbare Sammlung, die die folgenden Mitglieder enthält.  

- Keine: Zusammengeführte Zellen ignorieren.  
- ErsteZeile: Erweitert nur die Höhe der ersten Zeile.  
- LetzteZeile: Erweitert nur die Höhe der letzten Zeile.  
- JedeZeile: Erweitert nur die Höhe jeder Zeile.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows for Merged Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoFitterOptions, AutoFitMergedCellsType } = AsposeCells;

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
            let wb;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Get the first (default) worksheet
            const worksheet = wb.worksheets.get(0);

            // Create a range A1:B1
            const range = worksheet.cells.createRange(0, 0, 1, 2);

            // Merge the cells
            range.merge();

            // Insert value to the merged cell A1
            const cell = worksheet.cells.get(0, 0);
            cell.value = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end";

            // Create a style object
            const style = cell.style;

            // Set wrapping text on
            style.isTextWrapped = true;

            // Apply the style to the cell
            cell.style = style;

            // Create an object for AutoFitterOptions
            const options = new AutoFitterOptions();

            // Set auto-fit for merged cells
            options.autoFitMergedCellsType = AutoFitMergedCellsType.EachLine;

            // Autofit rows in the sheet (including the merged cells)
            worksheet.autoFitRows(options);

            // Save the Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AutofitRowsforMergedCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Sie können auch versuchen, die überladenen Versionen der [**autoFitRows**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-) & [**autoFitColumns**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-) Methoden zu verwenden, die eine Reihe von Zeilen/Spalten und eine Instanz von [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) akzeptieren, um die ausgewählten Zeilen/Spalten entsprechend Ihrer gewünschten [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) automatisch anzupassen.  

Die Signaturen der genannten Methoden sind wie folgt:  

1. autoFitZeilen(int startZeile, int endZeile, [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) Optionen)  
1. autoFitSpalten(int ersteSpalte, int letzteSpalte, [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) Optionen)  
{{% /alert %}}  

## **Wichtig zu wissen**  

{{% alert color="primary" %}}  
Wenn eine Zelle zusammengeführt ist, werden die autoFit-Methoden nicht angewendet, was dasselbe Verhalten wie in Microsoft Excel ist. Sie können dies umgehen, indem Sie die Autofilter-API verwenden. Außerdem wird die [**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-) Methode nicht angewendet, wenn der Text in einer Zelle umbrochen ist. Ein weiterer Punkt ist, dass die *autoFit*-Methoden zeitaufwendig sind. Daher sollten Sie diese Methoden so selten wie möglich aufrufen, um die Effizienz Ihrer Anwendung zu gewährleisten.  
{{% /alert %}}  

## **Erweiterte Themen**  
- [Automatisches Anpassen von Zeilen für zusammengeführte Zellen](/cells/de/javascript-cpp/autofit-rows-for-merged-cells/)
