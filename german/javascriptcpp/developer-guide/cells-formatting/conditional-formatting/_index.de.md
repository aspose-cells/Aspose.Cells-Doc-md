---
title: Setzen von bedingten Formatierungen für Excel und ODS Dateien
linktitle: Bedingte Formate
type: docs
weight: 60
url: /de/javascript-cpp/conditional-formatting/
description: So wenden Sie bedingte Formate in Excel und ODS Dateien in JavaScript über C++ an.
keywords: Bedingte Formate in JavaScript über C++ anwenden
---

## **Einführung**

Bedingte Formatierung ist eine erweiterte Funktion, die es ermöglicht, Formate auf eine Zelle oder einen Zellbereich anzuwenden und diese Formatierung je nach Wert der Zelle oder einer Formel zu ändern. Zum Beispiel kann eine Zelle nur fett erscheinen, wenn der Wert der Zelle größer als 500 ist. Wenn der Wert der Zelle die Bedingung erfüllt, wird das angegebene Format auf die Zelle angewendet. Wenn die Bedingung nicht erfüllt ist, nutzt die Zelle die Standardformatierung. In Microsoft Excel wählen Sie **Format**, dann **Bedingte Formatierung**, um den Dialog für bedingte Formatierungen zu öffnen.

Aspose.Cells unterstützt die Anwendung von bedingten Formatierungen auf Zellen zur Laufzeit. Dieser Artikel erklärt wie. Er erklärt auch, wie die von Excel für die bedingte Formatierung mit Farbskala verwendete Farbe berechnet wird.

## **Anwendung von bedingten Formaten**

Aspose.Cells unterstützt bedingte Formatierungen auf verschiedene Weise:

- Verwenden der Designer-Tabelle
- Verwenden der Kopiermethode
- Erstellen bedingter Formatierungen zur Laufzeit

### **Verwenden der Designer-Tabelle**

Entwickler können eine Designer-Tabelle erstellen, die bedingte Formatierungen in Microsoft Excel enthält, und dann diese Tabelle mit Aspose.Cells öffnen. Aspose.Cells lädt und speichert die Designer-Tabelle und behält dabei alle bedingten Formatierungseinstellungen bei.

### **Verwenden der Kopiermethode**

Aspose.Cells ermöglicht Entwicklern, bedingte Formatierungseinstellungen von einer Zelle auf eine andere im Arbeitsblatt zu kopieren, indem sie die Methode [**Range.copy()**](https://reference.aspose.com/cells/javascript-cpp/range/#copy-range-) aufrufen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get image data from the icon
            const imageData = icon.imageData;

            // Create a blob and provide download link for the image
            const blob = new Blob([imageData], { type: "image/jpeg" });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            resultDiv.innerHTML = '<p style="color: green;">Image extracted successfully! Click the download link to save the image.</p>';
        });
    </script>
</html>
```


## **Bedingte Formatierung zur Laufzeit anwenden**

Mit Aspose.Cells können Sie bedingte Formatierungen zur Laufzeit sowohl hinzufügen als auch entfernen. Die unten stehenden Codebeispiele zeigen, wie bedingte Formatierungen festgelegt werden:

1. Instanziieren Sie ein Arbeitsbuch.
1. Fügen Sie eine leere bedingte Formatierung hinzu.
1. Legen Sie den Bereich fest, auf den die Formatierung angewendet werden soll.
1. Definieren Sie die Formatierungsbedingungen.
1. Speichern Sie die Datei.

Nach diesem Beispiel folgen mehrere kleinere Beispiele, die zeigen, wie Schriftart-Einstellungen, Rand-Einstellungen und Muster angewendet werden.

Microsoft Excel 2007 hat erweiterte bedingte Formatierung eingeführt, die auch von Aspose.Cells unterstützt wird. Die Beispiele hier veranschaulichen die Verwendung einfacher Formatierung, während die Microsoft Excel 2007-Beispiele zeigen, wie man erweiterte bedingte Formatierungen anwendet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Conditional Formatting Example</h1>
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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Adds an empty conditional formatting
            const index = sheet.conditionalFormattings.count;
            const fcs = sheet.conditionalFormattings.get(index);

            // Sets the conditional format range.
            let ca = AsposeCells.CellArea.createCellArea(0, 0, 0, 0);
            fcs.addArea(ca);

            ca = AsposeCells.CellArea.createCellArea(1, 1, 1, 1);
            fcs.addArea(ca);

            // Adds condition.
            const conditionIndex = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "=A2", "100");

            // Adds condition.
            const conditionIndex2 = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "50", "100");

            // Sets the background color.
            const fc = fcs.get(conditionIndex);
            fc.style.backgroundColor = AsposeCells.Color.Red;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **Schriftart festlegen**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get the image data from the icon
            const imageData = icon.imageData;

            // Create a Blob and provide a download link for the image
            const blob = new Blob([imageData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            resultDiv.innerHTML = '<p style="color: green;">Image extracted successfully! Click the download link to save the image.</p>';
        });
    </script>
</html>
```



{{% alert color="primary" %}}

Sie können nur die Schriftart, die Textfarbe, den Unterstrichstil und den Durchstreichstil ändern.

{{% /alert %}}

### **Rahmen festlegen**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Conditional Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, FormatConditionType, OperatorType, BorderType, CellBorderType, Color } = AsposeCells;

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
            // This example creates a new workbook, adds conditional formatting and offers the result for download.
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);

            // Adds an empty conditional formatting
            const index = sheet.conditionalFormattings.add();
            const fcs = sheet.conditionalFormattings.get(index);

            // Sets the conditional format range.
            const ca = CellArea.createCellArea(0, 0, 5, 3);
            fcs.addArea(ca);

            // Adds condition.
            const conditionIndex = fcs.addCondition(FormatConditionType.CellValue, OperatorType.Between, "50", "100");

            // Sets the borders' line style to dashed and colors
            const fc = fcs.get(conditionIndex);
            fc.style.borders.get(BorderType.LeftBorder).lineStyle = CellBorderType.Dashed;
            fc.style.borders.get(BorderType.RightBorder).lineStyle = CellBorderType.Dashed;
            fc.style.borders.get(BorderType.TopBorder).lineStyle = CellBorderType.Dashed;
            fc.style.borders.get(BorderType.BottomBorder).lineStyle = CellBorderType.Dashed;

            fc.style.borders.get(BorderType.LeftBorder).color = new Color(0, 255, 255);
            fc.style.borders.get(BorderType.RightBorder).color = new Color(0, 255, 255);
            fc.style.borders.get(BorderType.TopBorder).color = new Color(0, 255, 255);
            fc.style.borders.get(BorderType.BottomBorder).color = new Color(255, 255, 0);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}

Sie können nur dünne Linienstile für die Outline-Grenze verwenden. Diagonale Linien sind nicht erlaubt.

{{% /alert %}}

### **Muster festlegen**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Add Conditional Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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
            const file = fileInput.files && fileInput.files.length ? fileInput.files[0] : null;

            // Instantiate workbook from uploaded file or create a new one
            let workbook;
            if (file) {
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Adds an empty conditional formatting
            const index = sheet.conditionalFormattings.add();
            const fcs = sheet.conditionalFormattings.get(index);

            // Sets the conditional format range.
            const ca = AsposeCells.CellArea.createCellArea(0, 0, 5, 3);
            fcs.addArea(ca);

            // Adds condition.
            const conditionIndex = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "50", "100");
            const fc = fcs.get(conditionIndex);

            // Apply style using property assignments (getter/setter conversion)
            fc.style.pattern = AsposeCells.BackgroundType.ReverseDiagonalStripe;
            fc.style.foregroundColor = new AsposeCells.Color(255, 255, 0);
            fc.style.backgroundColor = new AsposeCells.Color(0, 255, 255);

            // Save workbook to browser downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting added. Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```



## **Erweiterte Themen**  
- [Hinzufügen von 2-Farben-Skalen und 3-Farben-Skalen bedingter Formatierungen](/cells/de/javascript-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)  
- [Bedingte Formatierung in Arbeitsblättern anwenden](/cells/de/javascript-cpp/apply-conditional-formatting-in-worksheets/)  
- [Abwechselnde Zeilen und Spalten mit bedingter Formatierung schattieren](/cells/de/javascript-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)  
- [Generieren von Datenleistungsimages für bedingte Formatierungen](/cells/de/javascript-cpp/generate-conditional-formatting-databars-images/)  
- [Erhalten von Symbolsets, Datenleisten oder Farbskalenobjekten, die bei der bedingten Formatierung verwendet werden](/cells/de/javascript-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)
