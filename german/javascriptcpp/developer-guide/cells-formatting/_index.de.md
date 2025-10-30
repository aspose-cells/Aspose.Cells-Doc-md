---
title: Zellen mit JavaScript via C++ formatieren
description: Erfahren Sie, wie Sie Zellen in Aspose.Cells for JavaScript via C++ formatieren und stylen, einschließlich Zahlenformatierung, Datumsformatierung, Schriftarten und anderen Zellstiloptionen. Unser Leitfaden hilft Ihnen, ansprechende und professionell aussehende Tabellen zu erstellen.
keywords: Aspose.Cells for JavaScript via C++, Zellformatierung, Styling, Zahlenformatierung, Datumsformatierung, Schriftstil, Zellstiloptionen, Tabellen, erstellen, professionelles Aussehen, Zeilen und Spalten formatieren.
linktitle: Zellen formatieren
type: docs
weight: 120
url: /de/javascript-cpp/cells-formatting/
---

## **Einführung**

{{% alert color="primary" %}}

Aspose.Cells bietet die [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)- und [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)-Methoden der [Cell](https://reference.aspose.com/cells/javascript-cpp/cell)-Klasse, mit denen Sie den Formatierungsstil einer Zelle abrufen/setzen können. Aspose.Cells stellt auch eine [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Klasse bereit.

{{% /alert %}}

## **So formatieren Sie Zellen mit Style-Methoden**

Auf Zellen verschiedene Arten von Formatierungsstilen anwenden, um Hintergrund- oder Vordergrundfarben, Rahmen, Schriftarten, horizontale und vertikale Ausrichtungen, Einrückungsebene, Textausrichtung, Drehwinkel und vieles mehr festzulegen.

### **So verwenden Sie die Style-Methoden**

Wenn Entwickler unterschiedliche Formatierungsstile auf verschiedene Zellen anwenden müssen, ist es besser, das [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) der Zelle mit der [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)-Methode zu erhalten, die Stil-Attribute zu spezifizieren und dann die Formatierung mit der [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)-Methode anzuwenden. Ein Beispiel zeigt, wie dieser Ansatz angewendet wird, um verschiedene Formatierungen auf eine Zelle anzuwenden.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Styling Example</h1>
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

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Defining a Style object
            let style;

            // Get the style from A1 cell
            style = cell.style;

            // Setting the vertical alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text
            style.font.color = AsposeCells.Color.Green;

            // Setting to shrink according to the text contained in it
            style.shrinkToFit = true;

            // Setting the bottom border color to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Applying the style to A1 cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Wie man das Style-Objekt verwendet, um verschiedene Zellen zu formatieren**

Wenn Entwickler denselben Formatierungsstil auf verschiedene Zellen anwenden möchten, können sie das [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekt verwenden. Folgen Sie den untenstehenden Schritten, um das [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekt zu verwenden:

1. Fügen Sie ein [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekt hinzu, indem Sie die [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--)-Methode der [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse aufrufen
2. Greifen Sie auf das neu hinzugefügte [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekt zu
3. Legen Sie die gewünschten Eigenschaften/Attribute des [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekts fest, um die gewünschten Formatierungseinstellungen anzuwenden
4. Weisen Sie das konfigurierte [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekt Ihren gewünschten Zellen zu

Dieser Ansatz kann die Effizienz Ihrer Anwendungen erheblich verbessern und auch Speicherplatz sparen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Style Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, Color, BorderType, CellBorderType } = AsposeCells;

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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Add a new worksheet to the workbook
            const i = workbook.worksheets.add();

            // Obtain the newly added worksheet by index
            const worksheet = workbook.worksheets.get(i);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set value of A1
            cell.value = "Hello Aspose!";

            // Create a new style
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = TextAlignmentType.Center;
            style.horizontalAlignment = TextAlignmentType.Center;

            // Set font color
            style.font.color = Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(BorderType.BottomBorder).color = Color.Red;
            style.borders.get(BorderType.BottomBorder).lineStyle = CellBorderType.Medium;

            // Apply style to A1
            cell.style = style;

            // Apply same style to B1, C1, D1
            worksheet.cells.get("B1").style = style;
            worksheet.cells.get("C1").style = style;
            worksheet.cells.get("D1").style = style;

            // Save workbook to XLS format and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Wie man die Microsoft Excel 2007 vordefinierten Stile verwendet**

Wenn Sie unterschiedliche Formatierungsstile für Microsoft Excel 2007 anwenden müssen, wenden Sie Stile mithilfe der Aspose.Cells API an. Ein Beispiel unten zeigt diesen Ansatz zur Anwendung eines vordefinierten Stils auf einer Zelle.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Workbook and Set Cell Style Example</h1>
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
            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Create a style object.
            const style = workbook.createStyle();

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Input a value to A1 cell.
            cell.putValue("Test");

            // Apply the style to the cell.
            cell.style = style;

            // Saving the Excel 2007 file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```



## **Wie man ausgewählte Zeichen in einer Zelle formatiert**

Der Umgang mit Schriftart-Einstellungen erklärt, wie Text in Zellen formatiert wird, aber es erklärt nur, wie der gesamte Zellinhalt formatiert wird. Was ist, wenn Sie nur bestimmte Zeichen formatieren möchten?

Aspose.Cells unterstützt diese Funktion ebenfalls. Dieser Artikel erklärt, wie diese Funktion effektiv genutzt werden kann.

### **Wie man ausgewählte Zeichen formatiert**

Aspose.Cells stellt die Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) bereit, die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse enthält eine [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-Sammlung, die den Zugriff auf jedes Tabellenblatt in einer Excel-Datei ermöglicht. Ein Tabellenblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse bietet eine [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-Sammlung. Jedes Element in der [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-Sammlung repräsentiert ein Objekt der [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Klasse.

Die [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Klasse bietet die [**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-)-Methode, die die folgenden Parameter akzeptiert, um einen Zeichenbereich in einer Zelle auszuwählen:

- **Startindex**: Der Index des Zeichens, von dem die Auswahl beginnt.
- **Anzahl der Zeichen**: Die Anzahl der ausgewählten Zeichen.

Die [**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-)-Methode gibt eine Instanz der [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting)-Klasse zurück, die es Entwicklern ermöglicht, die Charaktere auf die gleiche Weise zu formatieren wie eine Zelle, wie im folgenden Codebeispiel gezeigt. Im Ausgabedokument wird im A1-Feld das Wort 'Visit' mit der Standardschriftart formatiert, aber 'Aspose!' ist fett und blau.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
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
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the font of selected characters to bold and color to blue
            const charRange = cell.characters(6, 7);
            charRange.font.isBold = true;
            charRange.font.color = AsposeCells.Color.Blue;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Wenn Sie daran interessiert sind, einen Teil des Rich Texts in einer Zelle zu formatieren, können Sie die [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) & [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-)-Methoden verwenden. Die [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--)-Methode dient dazu, auf die Textabschnitte zuzugreifen, und Änderungen können mit der [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-)-Methode vorgenommen werden, während die **Get**-Methode ein Array [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting)-Objekte zurückgibt, die manipuliert werden können, um verschiedene Eigenschaften wie Schriftart, Schriftfarbe, Fettdruck usw. festzulegen. Die **Set**-Methode kann verwendet werden, um die Änderungen anzuwenden.

{{% /alert %}}

## **Wie man Zeilen und Spalten formatiert**

Manchmal müssen Entwickler dieselbe Formatierung auf Zeilen oder Spalten anwenden. Die Formatierung einzelner Zellen nacheinander dauert oft länger und ist keine gute Lösung.
Um dieses Problem zu lösen, bietet Aspose.Cells einen einfachen, schnellen Weg, der in diesem Artikel ausführlich erörtert wird.

### **Formatierung von Zeilen & Spalten**

Aspose.Cells bietet die Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse enthält eine [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-Sammlung, die den Zugriff auf jedes Tabellenblatt in der Excel-Datei ermöglicht. Ein Tabellenblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse bietet eine [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-Sammlung. Die [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-Sammlung bietet eine [**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--)-Sammlung.

### **Wie man eine Zeile formatiert**

Jeder Eintrag in der [**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--)-Sammlung repräsentiert ein [**Row**](https://reference.aspose.com/cells/javascript-cpp/row)-Objekt. Das [**Row**](https://reference.aspose.com/cells/javascript-cpp/row)-Objekt bietet die [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-)-Methode, die verwendet wird, um die Zeilenformatierung festzulegen. Um eine gleiche Formatierung auf eine Zeile anzuwenden, verwenden Sie das [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekt. Die unten dargestellten Schritte zeigen, wie es verwendet wird.

1. Fügen Sie ein [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekt der [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse hinzu, indem Sie seine [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--)-Methode aufrufen.
2. Legen Sie die Eigenschaften des [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekts fest, um die Formatierungseinstellungen anzuwenden.
3. Schalten Sie die relevanten Attribute für das [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag)-Objekt ein.
4. Weisen Sie das konfigurierte [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekt dem [**Row**](https://reference.aspose.com/cells/javascript-cpp/row)-Objekt zu.

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Adding a new Style to the styles
            const style = workbook.createStyle();

            // Setting the vertical alignment of the text in the "A1" cell
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment of the text in the "A1" cell
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text in the "A1" cell
            style.font.color = AsposeCells.Color.Green;

            // Shrinking the text to fit in the cell
            style.shrinkToFit = true;

            // Setting the bottom border color of the cell to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type of the cell to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Creating StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Accessing a row from the Rows collection
            const row = worksheet.cells.rows.get(0);

            // Assigning the Style object to the Style property of the row
            row.applyStyle(style, styleFlag);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Wie man eine Spalte formatiert**

Die [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-Sammlung bietet auch eine [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--)-Sammlung. Jedes Element in der [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--)-Sammlung repräsentiert ein [**Column**](https://reference.aspose.com/cells/javascript-cpp/column)-Objekt. Ähnlich wie bei einem [**Row**](https://reference.aspose.com/cells/javascript-cpp/row)-Objekt bietet auch das [**Column**](https://reference.aspose.com/cells/javascript-cpp/column)-Objekt die [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-)-Methode zum Formatieren einer Spalte.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Style and Column Apply Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a new Style to the styles
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Set font color
            style.font.color = AsposeCells.Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Create and configure StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Access first column and apply style
            const column = worksheet.cells.getColumns().get(0);
            column.applyStyle(style, styleFlag);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Style applied to column successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Erweiterte Themen**
- [Ausrichtungseinstellungen](/cells/de/javascript-cpp/cells-alignment-settings/)
- [Rahmeneinstellungen](/cells/de/javascript-cpp/cells-border-settings/)
- [Bedingte Formate von Excel- und ODS-Dateien festlegen.](/cells/de/javascript-cpp/conditional-formatting/)
- [Excel-Themen und Farben](/cells/de/javascript-cpp/excel-themes-and-colors/)
- [Fülleinstellungen](/cells/de/javascript-cpp/cells-fill-settings/)
- [Schriftarteinstellungen](/cells/de/javascript-cpp/cells-font-settings/)
- [Zellenformat in einer Arbeitsmappe](/cells/de/javascript-cpp/format-worksheet-cells-in-a-workbook/)
- [Implementieren des 1904-Datumsformats](/cells/de/javascript-cpp/implement-1904-date-system/)
- [Zusammenführen und Aufheben der Zellenzusammenführung](/cells/de/javascript-cpp/merging-and-unmerging-cells/)
- [Nummern-Einstellungen](/cells/de/javascript-cpp/cells-number-settings/)
- [Stil für Zellen abrufen und festlegen](/cells/de/javascript-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)
