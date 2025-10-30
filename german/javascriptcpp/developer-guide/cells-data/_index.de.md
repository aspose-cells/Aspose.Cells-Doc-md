---
title: Verwalten von Daten von Excel Dateien
linktitle: Zellendaten
type: docs
weight: 110
url: /de/javascript-cpp/view-and-edit-excel-data/
description: Dieser Artikel beschreibt, wie Sie mit Aspose.Cells für JavaScript über C++ Daten in Excel Dateien anzeigen und bearbeiten können.
keywords: Aspose.Cells JavaScript über C++, Daten von Excel Dateien verwalten, Daten zu Excel Dateien hinzufügen, Daten aus Excel Dateien abfragen, Effizienz beim Hinzufügen von Daten verbessern, Zellen verwalten, Zellen aktualisieren, Zellen abfragen, Zellen einfügen
---

{{% alert color="primary" %}}

In [Zellen eines Arbeitsblatts zugreifen](/cells/de/javascript-cpp/accessing-cells-of-a-worksheet/) haben wir grundlegende Ansätze zum Zugriff auf Zellen in einem Arbeitsblatt diskutiert. Dieser Artikel verwendet einen dieser Ansätze, um unterschiedliche Datentypen zu Zellen hinzuzufügen.

{{% /alert %}}

## **Wie man Daten zu Zellen hinzufügt**

Aspose.Cells for JavaScript über C++ stellt die Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) vor, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) bietet eine [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-Sammlung. Jedes Element in der [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-Sammlung repräsentiert ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Aspose.Cells erlaubt es Entwicklern, Daten durch Aufruf der [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Klasse-Methode [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) zu Zellen in Arbeitsblättern hinzuzufügen. Aspose.Cells bietet überladene Versionen der [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)-Methode, die Entwicklern erlauben, unterschiedliche Datentypen zu Zellen hinzuzufügen. Mit diesen überladenen Versionen der [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)-Methode können Boolean-, String-, Double-, Integer- oder Date-/Uhrzeitwerte in die Zelle eingefügt werden.

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

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding values to cells
            const cells = worksheet.cells;
            const cellA1 = cells.get("A1");
            cellA1.value = "Hello World";

            const cellA2 = cells.get("A2");
            cellA2.value = 20.5;

            const cellA3 = cells.get("A3");
            cellA3.value = 15;

            const cellA4 = cells.get("A4");
            cellA4.value = true;

            const cellA5 = cells.get("A5");
            cellA5.value = new Date();

            // Setting the display format of the date
            let style = cellA5.style;
            style.number = 15;
            cellA5.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


## **Wie man die Effizienz verbessert**

Wenn Sie die [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)-Methode verwenden, um eine große Datenmenge in ein Arbeitsblatt einzufügen, sollten Sie zuerst Werte zeilenweise und dann spaltenweise hinzufügen. Dieser Ansatz verbessert die Effizienz Ihrer Anwendungen erheblich.

## **Wie man Daten von Zellen abruft**

Aspose.Cells for JavaScript via C++ bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse enthält eine [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-Sammlung, die Zugriff auf die Arbeitsblätter in der Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse bietet eine [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-Sammlung. Jedes Element in der [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-Sammlung repräsentiert ein Objekt der [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Klasse.

Die [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Klasse bietet mehrere Eigenschaften, mit denen Entwickler Werte aus Zellen entsprechend ihrem Datentyp abrufen können. Diese Eigenschaften umfassen:

- [**stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--): gibt den String-Wert der Zelle zurück.
- [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--): Gibt den doppelten Wert der Zelle zurück.
- [**boolValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#boolValue--): Gibt den booleschen Wert der Zelle zurück.
- [**dateTimeValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#dateTimeValue--): Gibt den Datum/Uhrzeit-Wert der Zelle zurück.
- [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--): Gibt den Fließkomma-Wert der Zelle zurück.
- [**intValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#intValue--): Gibt den Ganzzahlwert der Zelle zurück.

Wenn ein Feld nicht ausgefüllt ist, werfen Zellen mit [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--) oder [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--) eine Ausnahme.

Der Typ der in einer Zelle enthaltenen Daten kann auch durch Verwendung der [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Klasse' [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--)-Methode überprüft werden. Tatsächlich basiert die [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Klasse' [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--)-Methode auf der [**CellValueType**](https://reference.aspose.com/cells/javascript-cpp/cellvaluetype)-Aufzählung, deren vordefinierte Werte unten aufgelistet sind:

|**Zellwerttypen**|**Beschreibung**|
| :- | :- |
|IsBool| Gibt an, dass der Zellenwert Boolean ist.|
|IsDateTime| Gibt an, dass der Zellenwert Datum/Uhrzeit ist.|
|IsNull| Stellt eine leere Zelle dar.|
|IsNumeric| Gibt an, dass der Zellenwert numerisch ist.|
|IsString| Gibt an, dass der Zellenwert eine Zeichenfolge ist.|
|IsUnknown| Gibt an, dass der Zellenwert unbekannt ist.|

Sie können auch die oben definierten Standard-Zellwerttypen verwenden, um sie mit dem Datentyp in jeder Zelle zu vergleichen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Cell Values Example</h1>
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

            // Opening an existing workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing first worksheet
            const worksheet = workbook.worksheets.get(0);

            var cells = worksheet.cells;
            var maxRow = cells.maxRow;
            var maxColumn = cells.maxColumn;
            let logs = [];
            for (let i = 0; i <= maxRow; i++) {
                for (let j = 0; j <= maxColumn; j++) 
                {
                    const cell1 = cells.get(i, j);
                    if (!cell1) {
                        continue;
                    }
                    // Variables to store values of different data types
                    let stringValue;
                    let doubleValue;
                    let boolValue;
                    let dateTimeValue;

                    // Passing the type of the data contained in the cell for evaluation
                    switch (cell1.type) {
                        // Evaluating the data type of the cell data for string value
                        case AsposeCells.CellValueType.IsString:
                            stringValue = cell1.stringValue;
                            console.log("String Value: " + stringValue);
                            logs.push("String Value: " + stringValue);
                            break;

                        // Evaluating the data type of the cell data for double value
                        case AsposeCells.CellValueType.IsNumeric:
                            doubleValue = cell1.doubleValue;
                            console.log("Double Value: " + doubleValue);
                            logs.push("Double Value: " + doubleValue);
                            break;

                        // Evaluating the data type of the cell data for boolean value
                        case AsposeCells.CellValueType.IsBool:
                            boolValue = cell1.boolValue;
                            console.log("Bool Value: " + boolValue);
                            logs.push("Bool Value: " + boolValue);
                            break;

                        // Evaluating the data type of the cell data for date/time value
                        case AsposeCells.CellValueType.IsDateTime:
                            dateTimeValue = cell1.dateTimeValue;
                            console.log("DateTime Value: " + dateTimeValue);
                            logs.push("DateTime Value: " + dateTimeValue);
                            break;

                        // Evaluating the unknown data type of the cell data
                        case AsposeCells.CellValueType.IsUnknown:
                            stringValue = cell1.stringValue;
                            console.log("Unknown Value: " + stringValue);
                            logs.push("Unknown Value: " + stringValue);
                            break;

                        // Terminating the type checking of type of the cell data is null
                        case AsposeCells.CellValueType.IsNull:
                            break;
                    }
                }
            }

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! See console for detailed cell values.</p><pre>${logs.join("\n")}</pre>`;
        });
    </script>
</html>
```


{{% alert color="primary" %}}

Beim Arbeiten an Tabellenblättern können Benutzer verschiedene Datentypen in den Zellen hinzufügen. Diese Datentypen können Boolean, Ganzzahlen, Fließkommazahlen, Text oder Datum/Uhrzeit-Werte einschließen. Mit Aspose.Cells können Sie die entsprechenden Werte aus den Zellen entsprechend ihrer Datentypen abrufen.

{{% /alert %}}

## **Erweiterte Themen**
- [Zellen eines Arbeitsblatts zugreifen](/cells/de/javascript-cpp/accessing-cells-of-a-worksheet/)
- [Text numerische Daten in Nummer konvertieren](/cells/de/javascript-cpp/convert-text-numeric-data-to-number/)
- [Teilergebnisse erstellen](/cells/de/javascript-cpp/creating-subtotals/)
- [Daten filtern](/cells/de/javascript-cpp/data-filtering/)
- [Daten sortieren](/cells/de/javascript-cpp/sort-data-of-excel/)
- [Datenüberprüfung](/cells/de/javascript-cpp/data-validation/)
- [Daten suchen oder suchen](/cells/de/javascript-cpp/find-or-search-data/)
- [Zellzeichenfolgenwert mit und ohne Formatierung abrufen](/cells/de/javascript-cpp/get-cell-string-value-with-and-without-formatting/)
- [Hinzufügen von HTML-Rich-Text in die Zelle](/cells/de/javascript-cpp/adding-html-rich-text-inside-the-cell/)
- [Hyperlinks in Excel oder OpenOffice einfügen](/cells/de/javascript-cpp/insert-hyperlinks-to-excel/)
- [Verwendung und Platzierung von Enumeratoren](/cells/de/javascript-cpp/how-and-where-to-use-enumerators/)
- [Breite und Höhe des Zellenwerts in Pixeln messen](/cells/de/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lesen von Zellenwerten in mehreren Threads gleichzeitig](/cells/de/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Umwandlung zwischen Zellnamen und Zeilen-/Spaltenindex](/cells/de/javascript-cpp/names-and-indices/)
- [Daten erst nach Zeile und dann nach Spalte ausfüllen](/cells/de/javascript-cpp/populate-data-first-by-row-then-by-column/)
- [Einzelnes Anführungszeichen-Prefix des Zellenwerts oder -bereichs beibehalten](/cells/de/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Teile des Rich-Texts der Zelle zugreifen und aktualisieren](/cells/de/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
