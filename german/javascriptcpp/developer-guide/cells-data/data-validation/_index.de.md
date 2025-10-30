---
title: Datenvalidierung
type: docs
weight: 90
url: /de/javascript-cpp/data-validation/
description: Erfahren Sie, wie Sie die Datenvalidierung mit dem Aspose.Cells for JavaScript über C++ API hinzufügen.
keywords: JavaScript zur Datenvalidierung über C++ hinzufügen, JavaScript zum Abrufen des Validation Werts über C++, Ganze Zahl Datenvalidierung JavaScript über C++, Listen Datenvalidierung JavaScript über C++, Datumsdatenvalidierung JavaScript über C++, Zeitdatenvalidierung JavaScript über C++, Textlänge Datenvalidierung JavaScript über C++, Zellbereich zu bestehender Validierung JavaScript über C++, Überprüfung, ob die Validierung in der Zelle ein Dropdown ist JavaScript über C++, Benutzerdefinierte Validierung JavaScript über C++ hinzufügen
---

{{% alert color="primary" %}}
Microsoft Excel bietet einige nützliche Funktionen zum automatischen Filtern oder Validieren von Arbeitsblattdaten. Aspose.Cells unterstützt vollständig die Datenvalidierungs- und Autofilter-Funktionen von Microsoft Excel. Dieser Artikel erklärt, wie man die Funktionen in Microsoft Excel benutzt und sie mit dem Aspose.Cells for JavaScript über C++ programmiert.
{{% /alert %}}

## **Datenvalidierungstypen und Ausführung**

Datenvalidierung ermöglicht das Festlegen von Regeln für auf einem Arbeitsblatt eingegebene Daten. Verwenden Sie beispielsweise Validierungen, um sicherzustellen, dass eine Spalte mit der Bezeichnung DATUM nur Datumsangaben enthält oder dass eine andere Spalte nur Zahlen enthält. Sie könnten sogar sicherstellen, dass eine Spalte mit der Bezeichnung DATUM nur Daten innerhalb eines bestimmten Bereichs enthält. Mit Datenvalidierungen können Sie steuern, was in Zellen im Arbeitsblatt eingegeben wird.

Microsoft Excel unterstützt verschiedene Arten von Datenvalidierungen. Jede Art wird verwendet, um zu steuern, welche Art von Daten in eine Zelle oder Zellbereich eingegeben wird. Nachfolgend werden Codeausschnitte illustriert, wie überprüft wird, dass:

- Zahlen ganzzahlig sind, d.h. keine Dezimalstellen haben.
- Dezimalzahlen die richtige Struktur aufweisen. Das Codebeispiel definiert, dass ein Zellbereich zwei Dezimalstellen haben sollte.
- Werte auf eine Liste von Werten beschränkt sind. Die Listenvalidierung definiert eine separate Liste von Werten, die auf eine Zelle oder einen Zellbereich angewendet werden können.
- Daten innerhalb eines bestimmten Bereichs liegen.
- Eine Uhrzeit innerhalb eines bestimmten Bereichs liegt.
- Ein Text eine bestimmte Zeichenlänge aufweist.

### **Datenvalidierung mit Microsoft Excel**

Um Validierungen mit Microsoft Excel zu erstellen:

1. Wählen Sie in einem Arbeitsblatt die Zellen aus, auf die Sie die Überprüfung anwenden möchten.
1. Wählen Sie im **Daten**-Menü **Validierung** aus. Der Validierungsdialog wird angezeigt.
1. Klicken Sie auf die Registerkarte **Einstellungen** und geben Sie die Einstellungen ein.

### **Datenvalidierung mit Aspose.Cells for JavaScript über C++**

Die Datenvalidierung ist eine leistungsstarke Funktion zur Überprüfung der in Arbeitsblätter eingegebenen Informationen. Mit der Datenvalidierung können Entwickler Benutzern eine Auswahlliste bereitstellen, Daten eingaben auf einen bestimmten Typ oder eine bestimmte Größe beschränken usw.
In Aspose.Cells for JavaScript über C++ verfügt jede [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) Klasse über eine [**validations**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#validations--) Sammlung, die eine Sammlung von [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation) Objekten darstellt. Um die Validierung einzurichten, setzen Sie einige Eigenschaften der [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation) Klasse wie folgt:

- Typ – repräsentiert den Validierungstyp, der durch die Verwendung eines der vordefinierten Werte im [**ValidationType**](https://reference.aspose.com/cells/javascript-cpp/validationtype) Enum festgelegt werden kann.
- Operator – repräsentiert den Operator, der bei der Validierung verwendet wird, der durch eines der vordefinierten Werte im [**OperatorType**](https://reference.aspose.com/cells/javascript-cpp/operatortype) Enum festgelegt werden kann.
- Formel1 – stellt den Wert oder den Ausdruck dar, der mit dem ersten Teil der Datenvalidierung verbunden ist.
- Formel2 – repräsentiert den Wert oder Ausdruck, der mit dem zweiten Teil der Datenvalidierung verbunden ist.

Wenn die Eigenschaften des [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation) Objekts konfiguriert wurden, können Entwickler die [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea) Struktur nutzen, um Informationen über den Zellbereich zu speichern, der mit der erstellten Validierung geprüft werden soll.

#### **Arten der Datenvalidierung**

Das [**ValidationType**](https://reference.aspose.com/cells/javascript-cpp/validationtype) Enum hat die folgenden Mitglieder:

|**Member Name**|**Description**|
| :- | :- |
|AnyValue|Bezeichnet einen Wert jedes Typs.
|WholeNumber|Bezeichnet den Validierungstyp für ganze Zahlen.
|Decimal|Bezeichnet den Validierungstyp für Dezimalzahlen.
|List|Bezeichnet den Validierungstyp für Dropdown-Liste.
|Date|Bezeichnet den Validierungstyp für Datum.
|Time|Bezeichnet den Validierungstyp für Uhrzeit.
|TextLength|Bezeichnet den Validierungstyp für die Länge des Textes.
|Custom|Bezeichnet benutzerdefinierten Validierungstyp.

##### **Ganze Zahl Datenvalidierung**

Mit dieser Art von Validierung können Benutzer nur ganze Zahlen innerhalb eines bestimmten Bereichs in die validierten Zellen eingeben. Die nachfolgenden Codebeispiele zeigen, wie man den WholeNumber-Validierungstyp implementiert. Das Beispiel erstellt die gleiche Datenvalidierung mit dem Aspose.Cells for JavaScript über C++, wie wir sie zuvor mit Microsoft Excel erstellt haben.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Example</h1>
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');

            if (fileInput.files.length > 0) {
                // If a file is provided, we will open it; otherwise create a new workbook
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                // Instantiate workbook from uploaded file
                var workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook
                var workbook = new Workbook();
            }

            // Create a worksheet and get the first worksheet.
            const ExcelWorkSheet = workbook.worksheets.get(0);

            // Accessing the Validations collection of the worksheet
            const validations = workbook.worksheets.get(0).validations;

            // Create Cell Area
            const ca = new AsposeCells.CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Creating a Validation object
            const idx = validations.add(ca);
            const validation = validations.get(idx);

            // Setting the validation type to whole number
            validation.type = AsposeCells.ValidationType.WholeNumber;

            // Setting the operator for validation to Between
            validation.operator = AsposeCells.OperatorType.Between;

            // Setting the minimum value for the validation
            validation.formula1 = "10";

            // Setting the maximum value for the validation
            validation.formula2 = "1000";

            // Applying the validation to a range of cells from A1 to B2 using the CellArea structure
            const area = new AsposeCells.CellArea();
            area.startRow = 0;
            area.endRow = 1;
            area.startColumn = 0;
            area.endColumn = 1;

            // Adding the cell area to Validation
            validation.addArea(area);

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Validation added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Listendatenvalidierung**

Bei dieser Art der Validierung kann der Benutzer Werte aus einer Dropdown-Liste eingeben. Es bietet eine Liste: eine Reihe von Zeilen, die Daten enthalten. Im Beispiel wird ein zweites Arbeitsblatt hinzugefügt, um die Listenquelle zu speichern. Benutzer können nur Werte aus der Liste auswählen. Der Gültigkeitsbereich ist der Zellenbereich A1:A5 im ersten Arbeitsblatt.

Hier ist es wichtig, dass Sie die [**Validation.inCellDropDown(boolean)**](https://reference.aspose.com/cells/javascript-cpp/validation/#inCellDropDown-boolean-)-Eigenschaft auf **true** setzen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation List Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, OperatorType, ValidationAlertType } = AsposeCells;

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
            // This example creates a new workbook in the browser (file input is optional here).
            const workbook = new Workbook();

            // Get the first worksheet.
            const worksheet1 = workbook.worksheets.get(0);

            // Add a new worksheet and access it.
            const i = workbook.worksheets.add();
            const worksheet2 = workbook.worksheets.get(i);

            // Create a range in the second worksheet.
            const range = worksheet2.cells.createRange("E1", "E4");

            // Name the range.
            range.name = "MyRange";

            // Fill different cells with data in the range.
            range.get(0, 0).value = "Blue";
            range.get(1, 0).value = "Red";
            range.get(2, 0).value = "Green";
            range.get(3, 0).value = "Yellow";

            // Get the validations collection.
            const validations = worksheet1.validations;

            // Create Cell Area
            const ca = new CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Create a new validation to the validations list.
            const validation = validations.get(validations.add(ca));

            // Set the validation type.
            validation.type = ValidationType.List;

            // Set the operator.
            validation.operator = OperatorType.None;

            // Set the in cell drop down.
            validation.inCellDropDown = true;

            // Set the formula1.
            validation.formula1 = "=MyRange";

            // Enable it to show error.
            validation.showError = true;

            // Set the alert type severity level.
            validation.alertStyle = ValidationAlertType.Stop;

            // Set the error title.
            validation.errorTitle = "Error";

            // Set the error message.
            validation.errorMessage = "Please select a color from the list";

            // Specify the validation area.
            const area = new CellArea();
            area.startRow = 0;
            area.endRow = 4;
            area.startColumn = 0;
            area.endColumn = 0;

            // Add the validation area.
            validation.addArea(area);

            // Save the Excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Validation list created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


##### **Datum Datenvalidierung**

Bei diesem Validierungstyp gibt der Benutzer Datumswerte innerhalb eines bestimmten Bereichs oder gemäß bestimmten Kriterien in die validierten Zellen ein. Im Beispiel ist der Benutzer darauf beschränkt, Daten zwischen 1970 und 1999 einzugeben. Der Gültigkeitsbereich ist die Zelle B1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Date Validation Example</h1>
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
            // This example creates a new workbook in the browser (no file input required)
            const workbook = new Workbook();

            // Obtain the cells of the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Put a string value into the A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.value = "Please enter Date b/w 1/1/1970 and 12/31/1999";

            // Set row height and column width for the cells by accessing row/column objects
            const row0 = cells.rows.get(0);
            row0.height = 31;
            const col0 = cells.columns.get(0);
            col0.width = 35;

            // Get the validations collection.
            const validations = worksheet.validations;

            // Create Cell Area
            const ca = new AsposeCells.CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Add a new validation.
            const validationIndex = validations.add(ca);
            const validation = validations.get(validationIndex);

            // Set the data validation type.
            validation.type = AsposeCells.ValidationType.Date;

            // Set the operator for the data validation
            validation.operator = AsposeCells.OperatorType.Between;

            // Set the value or expression associated with the data validation.
            validation.formula1 = "1/1/1970";

            // The value or expression associated with the second part of the data validation.
            validation.formula2 = "12/31/1999";

            // Enable the error.
            validation.showError = true;

            // Set the validation alert style.
            validation.alertStyle = AsposeCells.ValidationAlertType.Stop;

            // Set the title of the data-validation error dialog box
            validation.errorTitle = "Date Error";

            // Set the data validation error message.
            validation.errorMessage = "Enter a Valid Date";

            // Set and enable the data validation input message.
            validation.inputMessage = "Date Validation Type";
            validation.ignoreBlank = true;
            validation.showInput = true;

            // Set a collection of CellArea which contains the data validation settings.
            const cellArea = new AsposeCells.CellArea();
            cellArea.startRow = 0;
            cellArea.endRow = 0;
            cellArea.startColumn = 1;
            cellArea.endColumn = 1;

            // Add the validation area.
            validation.addArea(cellArea);

            // Save the Excel file and provide download link.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and validation added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

##### **Zeit Datenvalidierung**

Bei diesem Typ der Validierung können Benutzer Zeiten innerhalb eines bestimmten Bereichs oder gemäß bestimmter Kriterien in die validierten Zellen eingeben. Im Beispiel ist der Benutzer darauf beschränkt, Zeiten zwischen 09:00 und 11:30 Uhr einzugeben. Der Gültigkeitsbereich ist die Zelle B1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Time Validation Example</h1>
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Obtain the cells of the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Put a string value into A1 cell.
            const a1 = cells.get("A1");
            a1.value = "Please enter Time b/w 09:00 and 11:30 'o Clock";

            // Set the row height and column width for the cells using row/column objects.
            cells.rows.get(0).height = 31;
            cells.columns.get(0).width = 35;

            // Get the validations collection.
            const validations = worksheet.validations;

            // Create Cell Area
            const ca = new AsposeCells.CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Add a new validation and obtain it.
            const validationIndex = validations.add(ca);
            const validation = validations.get(validationIndex);

            // Set the data validation type and other properties.
            validation.type = AsposeCells.ValidationType.Time;
            validation.operator = AsposeCells.OperatorType.Between;
            validation.formula1 = "09:00";
            validation.formula2 = "11:30";
            validation.showError = true;
            validation.alertStyle = AsposeCells.ValidationAlertType.Information;
            validation.errorTitle = "Time Error";
            validation.errorMessage = "Enter a Valid Time";
            validation.inputMessage = "Time Validation Type";
            validation.ignoreBlank = true;
            validation.showInput = true;

            // Set a collection of CellArea which contains the data validation settings.
            const cellArea = new AsposeCells.CellArea();
            cellArea.startRow = 0;
            cellArea.endRow = 0;
            cellArea.startColumn = 1;
            cellArea.endColumn = 1;

            // Add the validation area.
            validation.addArea(cellArea);

            // Save the Excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Textlängendatenvalidierung**

Bei diesem Validierungstyp können Benutzer Textwerte einer bestimmten Länge in die validierten Zellen eingeben. Im Beispiel ist der Benutzer darauf beschränkt, Zeichenfolgenwerte mit nicht mehr als 5 Zeichen einzugeben. Der Gültigkeitsbereich ist die Zelle B1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Text Length Validation</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, OperatorType, ValidationAlertType } = AsposeCells;

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
            // Create a new workbook.
            const workbook = new Workbook();

            // Obtain the cells of the first worksheet.
            const cells = workbook.worksheets.get(0).cells;

            // Put a string value into A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.value = "Please enter a string not more than 5 chars";

            // Set row height and column width for the cell.
            cells.rows.get(0).height = 31;
            cells.columns.get(0).width = 35;

            // Get the validations collection.
            const validations = workbook.worksheets.get(0).validations;

            // Create Cell Area
            const ca = new CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Add a new validation.
            const validationIndex = validations.add(ca);
            const validation = validations.get(validationIndex);

            // Set the data validation type.
            validation.type = ValidationType.TextLength;

            // Set the operator for the data validation.
            validation.operator = OperatorType.LessOrEqual;

            // Set the value or expression associated with the data validation.
            validation.formula1 = "5";

            // Enable the error.
            validation.showError = true;

            // Set the validation alert style.
            validation.alertStyle = ValidationAlertType.Warning;

            // Set the title of the data-validation error dialog box.
            validation.errorTitle = "Text Length Error";

            // Set the data validation error message.
            validation.errorMessage = " Enter a Valid String";

            // Set and enable the data validation input message.
            validation.inputMessage = "TextLength Validation Type";
            validation.ignoreBlank = true;
            validation.showInput = true;

            // Set a collection of CellArea which contains the data validation settings.
            const cellArea = new CellArea();
            cellArea.startRow = 0;
            cellArea.endRow = 0;
            cellArea.startColumn = 1;
            cellArea.endColumn = 1;

            // Add the validation area.
            validation.addArea(cellArea);

            // Save the Excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File created successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **Datenvalidierungsregeln**

Wenn Datenvalidierungen implementiert sind, kann die Validierung durch die Zuordnung verschiedener Werte in den Zellen überprüft werden. [**cell.validationValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) kann verwendet werden, um das Validierungsergebnis abzurufen. Das folgende Beispiel zeigt diese Funktion mit unterschiedlichen Werten. Die Beispieldatei kann zum Testen vom folgenden Link heruntergeladen werden:

[sampleDataValidationRules.xlsx](77496339.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Data Validation Check Example</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate the workbook from the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access Cell C1
            // Cell C1 has the Decimal Validation applied on it.
            // It can take only the values Between 10 and 20
            const cell = worksheet.cells.get("C1");

            const messages = [];

            // Enter 3 inside this cell
            // Since it is not between 10 and 20, it should fail the validation
            cell.value = 3;

            // Check if number 3 satisfies the Data Validation rule applied on this cell
            const isValid3 = cell.validationValue;
            messages.push(`Is 3 a Valid Value for this Cell: ${isValid3}`);

            // Enter 15 inside this cell
            // Since it is between 10 and 20, it should succeed the validation
            cell.value = 15;

            // Check if number 15 satisfies the Data Validation rule applied on this cell
            const isValid15 = cell.validationValue;
            messages.push(`Is 15 a Valid Value for this Cell: ${isValid15}`);

            // Enter 30 inside this cell
            // Since it is not between 10 and 20, it should fail the validation again
            cell.value = 30;

            // Check if number 30 satisfies the Data Validation rule applied on this cell
            const isValid30 = cell.validationValue;
            messages.push(`Is 30 a Valid Value for this Cell: ${isValid30}`);

            // Display results
            resultDiv.innerHTML = messages.map(m => `<p>${m}</p>`).join('');

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
        });
    </script>
</html>
```


## **Überprüfen Sie, ob die Validierung in der Zelle ein Dropdown ist**

Wie wir gesehen haben, gibt es viele Arten von Validierungen, die innerhalb einer Zelle implementiert werden können. Wenn Sie überprüfen möchten, ob eine Validierung ein Dropdown ist oder nicht, können Sie die [**validation.inCellDropDown**](https://reference.aspose.com/cells/javascript-cpp/validation/#inCellDropDown--) Methode verwenden, um dies zu testen. Der folgende Beispielcode demonstriert die Verwendung dieser Eigenschaft. Eine Beispieldatei zum Testen kann vom folgenden Link heruntergeladen werden:

[sampleValidation.xlsx](79527947.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Data Validation Drop-downs</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the worksheet named "Sheet1"
            const sheet = workbook.worksheets.get("Sheet1");
            const cells = sheet.cells;

            const appendMessage = (msg, color = 'black') => {
                const p = document.createElement('p');
                p.style.color = color;
                p.textContent = msg;
                resultDiv.appendChild(p);
            };

            const checkDropDown = (cell, cellRef) => {
                const validation = cell.validation;
                if (validation.inCellDropDown) {
                    appendMessage(`${cellRef} is a dropdown`, 'green');
                } else {
                    appendMessage(`${cellRef} is NOT a dropdown`, 'orange');
                }
            };

            checkDropDown(cells.get("A2"), "A2");
            checkDropDown(cells.get("B2"), "B2");
            checkDropDown(cells.get("C2"), "C2");
        });
    </script>
</html>
```


## **CellArea zur vorhandenen Validierung hinzufügen**

Es könnte Situationen geben, in denen Sie [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea) zu bestehenden [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation) hinzufügen möchten. Wenn Sie [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea) mit [**Validation.addArea(CellArea)**](https://reference.aspose.com/cells/javascript-cpp/validation/#addArea-cellarea-) hinzufügen, prüft Aspose.Cells alle bestehenden Bereiche, um zu sehen, ob der neue Bereich bereits existiert. Wenn die Datei viele Validierungen enthält, beeinträchtigt dies die Leistung. Um dies zu vermeiden, bietet die API die [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/javascript-cpp/validation/#addArea-cellarea-boolean-boolean-) Methode. Der *checkIntersection*-Parameter gibt an, ob die Schnittmenge eines Bereichs mit bestehenden Validierungsbereichen geprüft werden soll. Das Setzen auf **false** deaktiviert diese Überprüfung. Der *checkEdge*-Parameter prüft, ob die angewendeten Bereiche überprüft werden. Wenn der neue Bereich die obere/linke Ecke ist, werden interne Einstellungen neu aufgebaut. Wenn Sie sicher sind, dass der neue Bereich nicht die obere/linke Ecke ist, können Sie diesen Parameter auf **false** setzen.

Der folgende Codeausschnitt zeigt, wie die [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/javascript-cpp/validation/#addArea-cellarea-boolean-boolean-) Methode verwendet wird, um eine neue [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea) zu den bestehenden [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation) hinzuzufügen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Validations</title>
    </head>
    <body>
        <h1>Validations Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Accessing the Validations collection of the worksheet
            const validation = worksheet.validations.get(0);

            // Create your cell area.
            const cellArea = AsposeCells.CellArea.createCellArea("D5", "E7");

            // Adding the cell area to Validation
            validation.addArea(cellArea, false, false);

            // Save the output workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ValidationsSample_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Validation area added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Die Quell- und Ausgabedateien sind als Referenz angehängt.

[Quelldatei](96928093.xlsx)

[Ausgabedatei](96928220.xlsx)

## **Erweiterte Themen**
- [Zellvalidierung in ODS-Dateien erhalten](/cells/de/javascript-cpp/get-cell-validation-in-ods-files/)
- [Validierungen auf einer Zelle abrufen](/cells/de/javascript-cpp/get-validation-applied-on-a-cell/)
- [Überprüfen, ob Zellwert Datenvalidierungsregeln erfüllt](/cells/de/javascript-cpp/verify-that-cell-value-satisfies-data-validation-rules/)
