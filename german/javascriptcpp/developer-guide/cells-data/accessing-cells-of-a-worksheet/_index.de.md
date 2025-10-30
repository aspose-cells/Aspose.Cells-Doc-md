---
title: Zugriff auf Zellen eines Arbeitsblatts
type: docs
weight: 10
url: /de/javascript-cpp/accessing-cells-of-a-worksheet/
description: Dieser Artikel zeigt, wie man den maximalen Anzeigebereich eines Arbeitsblatts erhält und Zellen über die Aspose.Cells for JavaScript via C++ API zugreift.
keywords: Hol Cell Objekt, Zugriff auf Zellen, Holen Sie sich den maximalen Anzeigebereich des Arbeitsblatts. 
---

{{% alert color="primary" %}}

Wir wissen, dass alle Arbeitsblätter Daten enthalten können, die im Wesentlichen in Zellen gespeichert sind (aus denen ein Arbeitsblatt besteht). Eine Zelle ist ein grundlegender Teil eines Arbeitsblatts, der verwendet wird, um das gesamte Arbeitsblatt als Folge von Zeilen und Spalten aufzubauen. Bevor wir versuchen, Daten aus einem Arbeitsblatt zuzugreifen, müssen wir Zugriff auf seine Zellen erhalten. In diesem Thema besprechen wir einige grundlegende Ansätze, um auf Arbeitsblattzellen zur Laufzeit mit Aspose.Cells for JavaScript via C++ zuzugreifen.

{{% /alert %}}

## **Wie man auf Zellen zugreift**

Aspose.Cells for JavaScript via C++ stellt eine Klasse bereit, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) enthält eine [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection), die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung, die alle Zellen im Arbeitsblatt repräsentiert.

Wir können die [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung verwenden, um auf Zellen in einem Arbeitsblatt zuzugreifen. Aspose.Cells for JavaScript via C++ bietet drei grundlegende Ansätze, um Zellen in einem Arbeitsblatt zu erreichen:

1. Verwenden des Zellnamens
2. Verwendung von Zeilen- und Spaltenindex einer Zelle.
1. Verwendung eines Zellindex in der [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung

 Wir haben erwähnt, dass der 3. Ansatz der schnellste und der 1. Ansatz der langsamste ist. Der Leistungsunterschied zwischen den Ansätzen ist sehr gering, daher müssen Sie sich keine Sorgen um Leistungsverschlechterung machen, welchen Ansatz Sie auch wählen.

### **So erhalten Sie ein Zellenobjekt anhand des Zellnamens**

Entwickler können auf eine bestimmte Zelle zugreifen, indem sie den Zellnamen an die [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung der [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse als Index übergeben.

Wenn Sie zu Beginn ein leeres Arbeitsblatt erstellen, ist die Anzahl der [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung null. Wenn Sie diesen Ansatz zum Zugriff auf eine Zelle verwenden, prüft er, ob diese Zelle in der Sammlung existiert. Falls ja, gibt er das Zellobjekt aus der Sammlung zurück, andernfalls erstellt er ein neues [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Objekt, fügt es der [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung hinzu und gibt es zurück. Dieser Ansatz ist der einfachste, wenn Sie mit Microsoft Excel vertraut sind, aber im Vergleich zu anderen Ansätzen der langsamste.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Read Cell Example</h1>
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

            // Using the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its name
            const cell = worksheet.cells.get("A1");

            // Output the cell's string value to the page
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.stringValue}</p>`;
        });
    </script>
</html>
```

### **So erhalten Sie ein Zellenobjekt anhand des Zeilen- und Spaltenindexes der Zelle**

Entwickler können auf eine bestimmte Zelle zugreifen, indem sie die Zeilen- und Spaltenindizes an die [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung der [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse übergeben.

Dieser Ansatz funktioniert genauso wie der erste Ansatz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell Value</h1>
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

            // Using the first worksheet in workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column (A1 -> 0,0)
            const cell = worksheet.cells.get(0, 0);

            // Printing the string value of the cell
            const value = cell.stringValue;
            console.log(value);
            resultDiv.innerHTML = `<p>Cell A1 value: ${value}</p>`;
        });
    </script>
</html>
```

### **So erhalten Sie ein Zellenobjekt anhand des Zellindexes in der Zellensammlung**

Eine Zelle kann auch durch Übergeben ihres numerischen Index an die [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung erreicht werden.

Wenn Sie diese Methode zum Zugriff auf Zellen verwenden, kann eine Ausnahme geworfen werden, wenn der numerische Index der Zelle außerhalb des Bereichs liegt. Dieser Ansatz ist der schnellste, um Zellen zu erreichen, aber wichtig zu wissen ist, dass sich der numerische Index nach dem Hinzufügen neuer Zellen zur [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung ändern kann. Die Zellobjekte in der [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung sind intern nach Zeilen- und Spaltenindizes sortiert.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell String Value</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the Sheet 1 in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column.
            const cell = worksheet.cells.get(0, 0);

            // Output the string value of the cell
            console.log(cell.stringValue);
            resultDiv.innerHTML = `<p>Cell (0,0) string value: <strong>${cell.stringValue}</strong></p>`;
        });
    </script>
</html>
```

## **So erhalten Sie die maximale Anzeigebereich des Arbeitsblatts**

Aspose.Cells for JavaScript via C++ ermöglicht es Entwicklern, den maximalen Anzeigebereich eines Arbeitsblatts zuzugreifen. Der maximale Anzeigebereich – der Bereich der Zellen zwischen der ersten und der letzten Zelle mit Inhalt – ist nützlich, wenn Sie den gesamten Inhalt eines Arbeitsblatts kopieren, auswählen oder als Bild anzeigen möchten.

Sie können den maximalen Anzeigebereich eines Arbeitsblatts mit [**Cells.maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--) zugreifen. Der folgende Beispielcode zeigt, wie die Eigenschaft [**maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--) aufgerufen wird.

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Ensure Aspose.Cells is initialized
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the Maximum Display Range
            const range = worksheet.cells.maxDisplayRange;

            // Print / display the Maximum Display Range RefersTo property
            const refersTo = range.refersTo;
            resultDiv.innerHTML = `<p style="color: green;">Maximum Display Range: ${refersTo}</p>`;
        });
    </script>
</html>
```
