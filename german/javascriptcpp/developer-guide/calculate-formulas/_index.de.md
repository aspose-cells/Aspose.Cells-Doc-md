---
title: Formeln mit JavaScript über C++ berechnen
linktitle: Berechnung von Formeln
description: Dieser Artikel erklärt, wie man die Aspose.Cells Bibliothek benutzt, um Formeln in Microsoft Excel mit JavaScript über C++ zu berechnen. Durch das Laden einer bestehenden Excel Datei oder das Erstellen einer neuen Excel Datei können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um die Formel zu berechnen und das Ergebnis zu erhalten. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, Formeln, Berechnungen, Direkte Formelberechnung, Formeln wiederholt berechnen, Formeln in JavaScript via C++ hinzufügen
type: docs
weight: 125
url: /de/javascript-cpp/calculate-formulas/
---

## **Hinzufügen von Formeln & Berechnen von Ergebnissen**

Aspose.Cells verfügt über eine eingebaute Formelrechnungs-Engine. Es kann nicht nur Formeln, die aus Designer-Vorlagen importiert wurden, neu berechnen, sondern auch die Ergebnisse von Formeln, die zur Laufzeit hinzugefügt wurden, berechnen.

Aspose.Cells unterstützt die meisten Formeln oder Funktionen, die Teil von Microsoft Excel sind (Liste der von der Rechenmaschine unterstützten Funktionen lesen [hier](/cells/de/javascript-cpp/supported-formula-functions/)). Diese Funktionen können über die APIs oder Designer-Tabellen verwendet werden. Aspose.Cells unterstützt eine große Reihe mathematischer, String-, boolescher, Datums-/Uhrzeit-, statistischer, Datenbank-, Lookup- und Referenzformeln.

Verwenden Sie die [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--)-Eigenschaft oder [**formula(string, object)**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula-string-object-)-Methoden der [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Klasse, um eine Formel in eine Zelle einzufügen. Beim Anwenden einer Formel beginnt der String immer mit einem Gleichheitszeichen (=), so wie Sie es beim Erstellen einer Formel in Microsoft Excel tun, und verwenden Sie ein Komma (,) zur Trennung der Funktionsparameter.

Um die Ergebnisse von Formeln zu berechnen, kann der Benutzer die [**calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)-Methode der [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse aufrufen, die alle in einer Excel-Datei eingebetteten Formeln verarbeitet. Oder, der Benutzer kann die [**calculateFormula(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-)-Methode der [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse aufrufen, die alle in einem Blatt eingebetteten Formeln verarbeitet. Oder der Benutzer kann auch die [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/javascript-cpp/cell/#calculate-calculationoptions-)-Methode der [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Klasse aufrufen, die die Formel einer einzelnen Zelle verarbeitet:

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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Add a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 1;

            // Adding a value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 2;

            // Adding a value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 3;

            // Adding a SUM formula to "A4" cell
            const cellA4 = worksheet.cells.get("A4");
            cellA4.formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value in A4: ${value}. Click the download link to get the file.</p>`;
        });
    </script>
</html>
```

### **Wichtiges zu Formeln**

{{% alert color="primary" %}}

Die **Formel**-Eigenschaft und die **formel(...)**-Methoden der [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Klasse unterscheiden sich von den **berechnen**-Methoden der Klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) und [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). Die **Formel**-Eigenschaft und die **formel(...)**-Methoden fügen die Formel nur einer Zelle hinzu, berechnen das Ergebnis jedoch nicht zur Laufzeit. Um das Ergebnis der Formeln zu erhalten, rufen Sie bitte die **berechnen**-Methoden auf.

{{% /alert %}}

## **Direkte Berechnung von Formeln**

Aspose.Cells verfügt über einen eingebetteten Formelberechnungsmotor. Neben der Berechnung von Formeln, die aus einer Designerdatei importiert wurden, kann Aspose.Cells auch Formelergebnisse direkt berechnen.

Manchmal müssen Sie Formelergebnisse direkt berechnen, ohne sie in ein Arbeitsblatt einzufügen. Die Werte der in der Formel verwendeten Zellen sind bereits in einem Arbeitsblatt vorhanden, und alles, was Sie brauchen, ist, das Ergebnis dieser Werte basierend auf einer Microsoft-Excel-Formel zu finden, ohne die Formel ins Arbeitsblatt einzufügen.

Sie können die APIs der Aspose.Cells-Formelberechnung engine für [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) bis [**calculateFormula(string, FormulaParseOptions, CalculationOptions, number, number, CalculationData)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-formulaparseoptions-calculationoptions-number-number-calculationdata-) nutzen, um die Ergebnisse solcher Formeln zu ermitteln, ohne sie ins Arbeitsblatt einzufügen:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Calculate Sum</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put 20 in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 20;

            // Put 30 in cell A2
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 30;

            // Calculate the Sum of A1 and A2
            const results = worksheet.calculateFormula("=Sum(A1:A2)");

            // Prepare output text
            const outputHtml = [
                `<p>Value of A1: ${cellA1.stringValue}</p>`,
                `<p>Value of A2: ${cellA2.stringValue}</p>`,
                `<p>Result of Sum(A1:A2): ${results.toString()}</p>`
            ].join("");

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<div style="color: green;">Operation completed successfully!</div>${outputHtml}`;
        });
    </script>
    </body>
</html>
```

Der obige Code erzeugt die folgende Ausgabe:
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Wie man Formeln wiederholt berechnet**

Wenn es viele Formeln im Arbeitsbuch gibt und der Benutzer sie mehrfach berechnen muss, während er nur einen kleinen Teil verändert, kann es performancefördernd sein, die Formelberechnungskette zu aktivieren: [**formulaSettings.enableCalculationChain**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Calculate Formulas</title>
    </head>
    <body>
        <h1>Calculate Formulas Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Print the time before formula calculation
            console.log(new Date());

            // Set the CreateCalcChain as true
            workbook.settings.formulaSettings.enableCalculationChain = true;

            // Calculate the workbook formulas
            workbook.calculateFormula();

            // Print the time after formula calculation
            console.log(new Date());

            // Change the value of one cell (A1 in first worksheet)
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");
            cell.value = "newvalue";

            // Re-calculate those formulas which depend on cell A1
            workbook.calculateFormula();

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Formulas calculated and cell updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Wichtig zu wissen**

{{% alert color="primary" %}}

Standardmäßig ist die Berechnungskette deaktiviert. Da das Erstellen der Kette zusätzliche Zeit benötigt, kann die erste Berechnung der Formeln ([**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)) mehr CPU-Verarbeitungszeit und Speicher benötigen im Vergleich zur Berechnung ohne Kette. Wenn der Benutzer Formeln nicht wiederholt berechnen muss, ist das Standardverhalten (Direkte Berechnung ohne Kettenbildung) wahrscheinlich die bessere Wahl.

{{% /alert %}}

## **Erweiterte Themen**
- [Zellen zur Microsoft Excel-Formelüberwachung hinzufügen](/cells/de/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Berechnung der IFNA-Funktion mit Aspose.Cells](/cells/de/javascript-cpp/calculating-ifna-function-using-aspose-cells/)
- [Berechnung der Arrayformel von Datenblättern](/cells/de/javascript-cpp/calculation-of-array-formula-of-data-tables/)
- [Berechnung der Excel 2016 MINIFS- und MAXIFS-Funktionen](/cells/de/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Berechnungszeit der Cell.calculate-Methode reduzieren](/cells/de/javascript-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Erkennen von zirkulären Verweisen](/cells/de/javascript-cpp/detecting-circular-reference/)
- [Direkte Berechnung einer benutzerdefinierten Funktion ohne Eintragung in ein Arbeitsblatt](/cells/de/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementieren eines benutzerdefinierten Berechnungsmotors zur Erweiterung des Standard-Berechnungsmotors von Aspose.Cells](/cells/de/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Unterbrechen oder Abbrechen der Formelberechnung des Arbeitsbuchs](/cells/de/javascript-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Rückgabe eines Bereichs von Werten unter Verwendung von AbstractCalculationEngine](/cells/de/javascript-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Festlegen des Formelberechnungsmodus des Arbeitsbuchs](/cells/de/javascript-cpp/setting-formula-calculation-mode-of-workbook/)
- [Verwendung der FormulaText-Funktion in Aspose.Cells](/cells/de/javascript-cpp/using-formulatext-function-in-aspose-cells/)
