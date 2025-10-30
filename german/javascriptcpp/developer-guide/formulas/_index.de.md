---
title: Formeln von Excel Dateien mit JavaScript über C++ verwalten
linktitle: Formeln
type: docs
weight: 122
url: /de/javascript-cpp/using-formulas-or-functions-to-process-data/
description: Erfahren Sie, wie Sie Formeln von Excel Dateien mit Aspose.Cells for JavaScript in C++ verwalten. Aspose.Cells kann Formeln in Excel Dateien einfach abrufen, setzen und berechnen.
keywords: Wie man Formeln in JavaScript über C++ berechnet, Formeln und Funktionen mit JavaScript über C++, JavaScript über C++ integrierte Funktionen verwalten, Add in Funktionen mit JavaScript über C++ verwenden, Array Formel mit via JavaScript in C++ verwenden, R1C1 Formel in JavaScript über C++ verwenden.
---

## **Einführung**

Eines der überzeugenden Merkmale von Microsoft Excel ist seine Fähigkeit, Daten mit Formeln und Funktionen zu verarbeiten. Microsoft Excel bietet eine Reihe integrierter Funktionen und Formeln, die Benutzern helfen, komplexe Berechnungen schnell durchzuführen. Aspose.Cells bietet ebenfalls eine große Menge an integrierten Funktionen und Formeln, die Entwicklern helfen, Werte einfach zu berechnen. Aspose.Cells unterstützt auch Add-In-Funktionen. Zudem unterstützt Aspose.Cells Array- und R1C1-Formeln.

## **Wie man Formeln und Funktionen verwendet**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) bietet eine [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-Sammlung. Jedes Element in der Cells-Sammlung repräsentiert ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Es ist möglich, Formeln auf Zellen anzuwenden, indem Eigenschaften und Methoden verwendet werden, die von der Klasse [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) angeboten werden, die im Folgenden näher erläutert werden.

- Verwendung von integrierten Funktionen.
- Verwendung von Add-In-Funktionen.
- Arbeit mit Array-Formeln.
- Erstellen einer R1C1-Formel.

## **Verwendung von integrierten Funktionen**

Integrierte Funktionen oder Formeln sind als fertige Funktionen vorhanden, um den Aufwand und die Zeit der Entwickler zu reduzieren. siehe [Liste der integrierten Funktionen](/cells/de/javascript-cpp/supported-formula-functions/), unterstützt von Aspose.Cells. Die Funktionen sind alphabetisch aufgeführt. Weitere Funktionen werden in Zukunft unterstützt.

Aspose.Cells unterstützt die meisten der von Microsoft Excel angebotenen Formeln oder Funktionen. Entwickler können diese Formeln über die API oder [Designer-Spreadsheets](/cells/de/javascript-cpp/what-is-a-designer-spreadsheet/) verwenden. Aspose.Cells bietet eine große Auswahl an mathematischen, String-, Booleschen, Datums-/Uhrzeit-, Statistik-, Datenbank-, Nachschlage- und Referenzformeln.

Verwenden Sie die [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Eigenschaft der Klasse [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--), um einer Zelle eine Formel hinzuzufügen. **Komplexe Formeln**, zum Beispiel

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, werden auch von Aspose.Cells unterstützt. Beim Anwenden einer Formel auf eine Zelle beginnen Sie immer die Zeichenfolge mit einem Gleichheitszeichen (=), wie Sie es bei der Erstellung einer Formel in Microsoft Excel tun, und verwenden ein Komma (,) zur Trennung der Funktionsparameter.

Im folgenden Beispiel wird eine komplexe Formel auf die erste Zelle der [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung eines Arbeitsblatts angewendet. Die Formel verwendet eine integrierte **IF**-Funktion von Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            worksheet.cells.get("A1").putValue(1);

            // Adding a value to "A2" cell
            worksheet.cells.get("A2").putValue(2);

            // Adding a value to "A3" cell
            worksheet.cells.get("A3").putValue(3);

            // Adding a SUM formula to "A4" cell
            worksheet.cells.get("A4").formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated A4 value: ${value}. Click the download link to get the generated file.</p>`;
        });
    </script>
</html>
```

## **Verwendung von Add-in-Funktionen**

Wir können einige benutzerdefinierte Formeln haben, die wir als Excel-Add-in einbinden möchten. Beim Setzen der cell.formula-Funktion funktionieren integrierte Funktionen einwandfrei, jedoch besteht die Notwendigkeit, benutzerdefinierte Funktionen oder Formeln mithilfe der Add-in-Funktionen zu setzen.

Aspose.Cells bietet Funktionen, um Add-in-Funktionen mit [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-) zu registrieren. Danach enthält die Ausgabedatei beim Setzen von cell.formula = anyFunctionFromAddIn den berechneten Wert der AddIn-Funktion.

Die folgende XLAM-Datei soll zum Registrieren der Add-In-Funktion verwendet werden im untenstehenden Beispielcode. Ebenso kann die Ausgabedatei "test_udf.xlsx" heruntergeladen werden, um die Ausgabe zu überprüfen.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Register Add-In Function Example</title>
    </head>
    <body>
        <h1>Register Add-In Function Example</h1>
        <p>Select the add-in file (.xlam/.xla) that contains the UDFs to register:</p>
        <input type="file" id="addInInput" accept=".xlam,.xla" />
        <button id="runExample">Register Add-In & Create Workbook</button>
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
            const fileInput = document.getElementById('addInInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an add-in file (.xlam/.xla).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const addinData = new Uint8Array(arrayBuffer);

            // Create empty workbook
            const workbook = new Workbook();

            // Register macro enabled add-in along with the function name
            const id = workbook.worksheets.registerAddInFunction(addinData, "TEST_UDF", false);

            // Register more functions in the file (if any)
            workbook.worksheets.registerAddInFunction(id, "TEST_UDF1");

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first cell
            const cell = worksheet.cells.get("A1");

            // Set formula name present in the add-in
            cell.formula = "=TEST_UDF()";

            // Save workbook to output XLSX format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'test_udf.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Add-in registered and formula set successfully! Click the download link to get the workbook.</p>';
        });
    </script>
</html>
```

## **Verwendung von Array-Formel**

Array-Formeln sind Formeln, die Arrays anstelle von einzelnen Zahlen als Argumente für die Funktionen, die die Formel bilden, verwenden. Wenn eine Array-Formel angezeigt wird, ist sie von geschweiften Klammern ({}) umgeben.

Einige Microsoft Excel-Funktionen geben Arrays von Werten zurück. Um mehrere Ergebnisse mit einer Array-Formel zu berechnen, geben Sie das Array in einen Zellenbereich mit derselben Anzahl von Zeilen und Spalten wie die Array-Argumente ein.

Es ist möglich, einer Zelle eine Array-Formel durch Aufruf der Methode [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-) der Klasse [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) anzuwenden. Die Methode [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-) nimmt die folgenden Parameter an:

- **Array-Formel**, die Array-Formel.
- **Anzahl der Zeilen**, die Anzahl der Zeilen zum Ausfüllen des Ergebnisses der Array-Formel.
- **Anzahl der Spalten**, die Anzahl der Spalten zum Ausfüllen des Ergebnisses der Array-Formel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LINEST Example</h1>
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding values to cells
            worksheet.cells.get("A1").value = 1;
            worksheet.cells.get("A2").value = 2;
            worksheet.cells.get("A3").value = 3;

            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 5;
            worksheet.cells.get("B3").value = 6;

            worksheet.cells.get("C1").value = 7;
            worksheet.cells.get("C2").value = 8;
            worksheet.cells.get("C3").value = 9;

            // Adding a SUM/LINEST array formula to "A6" cell
            worksheet.cells.get("A6").arrayFormula = { formula: "=LINEST(A1:A3,B1:C3,TRUE,TRUE)", rows: 5, cols: 3 };

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A6").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value: ${value}</p>`;
        });
    </script>
</html>
```

## **Verwendung der R1C1-Formel**

Fügen Sie einer Zelle mit der [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) Klasse die Eigenschaft [**r1C1Formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#r1C1Formula--) hinzu.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set R1C1 Formula Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting an R1C1 formula on the "A11" cell,
            // Row and Column indices are relative to destination index
            const cell = worksheet.cells.get("A11");
            cell.r1C1Formula = "=SUM(R[-10]C[0]:R[-7]C[0])";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">R1C1 formula set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Erweiterte Themen**
- [Vorgänger und Abhängige](/cells/de/javascript-cpp/precedents-and-dependents/)
- [Externe Verknüpfungen in Formeln festlegen](/cells/de/javascript-cpp/set-external-links-in-formulas/)
- [Formel in Tabelle oder List-Objekt automatisch propagieren, während neue Zeilen eingegeben werden](/cells/de/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Formel für benanntes Bereich setzen](/cells/de/javascript-cpp/setting-formula-for-named-range/)
- [Formeln einstellen - Hinweis für nicht englischsprachige Benutzer](/cells/de/javascript-cpp/setting-formulas-notice-for-non-english-users/)
- [Gemeinsame Formel festlegen](/cells/de/javascript-cpp/setting-shared-formula/)
- [Maximale Zeilen der gemeinsamen Formel angeben](/cells/de/javascript-cpp/specify-maximum-rows-of-shared-formula/)
- [Unterstützte Excel-Funktionen](/cells/de/javascript-cpp/supported-formula-functions/)
