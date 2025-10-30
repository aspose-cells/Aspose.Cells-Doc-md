---
title: Füllungseinstellungen
linktitle: Füllungseinstellungen
description: Erfahren Sie, wie Sie die Füll Einstellungen, den Hintergrund und den Stil von Zellen mit der Aspose.Cells Bibliothek für JavaScript über C++ anpassen.
keywords: Aspose.Cells, Zellen, Füll Einstellungen, Hintergrund, Stil, JavaScript über C++
type: docs
weight: 50
url: /de/javascript-cpp/cells-fill-settings/
---

## **Farben und Hintergrundmuster**

Microsoft Excel kann die Vordergrund- (Rahmen) und Hintergrundfarben (Fülle) von Zellen sowie Hintergrundmuster festlegen.

Aspose.Cells unterstützt diese Funktionen ebenfalls in flexibler Weise. In diesem Thema lernen wir, diese Funktionen mit Aspose.Cells zu verwenden.

### **Einstellen von Farben und Hintergrundmustern**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse enthält eine [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse bietet eine [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung. Jedes Element in der [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung stellt ein Objekt der [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Klasse dar.

Die [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Eigenschaft verfügt über die [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)-Eigenschaft, mit der der Formatierungszustand einer Zelle abgerufen und festgelegt wird. Die [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Klasse bietet Eigenschaften zum Festlegen der Vordergrund- und Hintergrundfarben der Zellen. Aspose.Cells bietet eine [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype)-Aufzählung, die eine Reihe vordefinierter Hintergrundmusterarten enthält, wie unten angegeben.

|**Hintergrundmuster**|**Beschreibung**|
| :- | :- |
|DiagonalCrosshatch|: Stellt das diagonale Kreuzmuster dar
|DiagonalStripe|: Stellt das diagonale Streifenmuster dar
|Gray6|: Stellt das 6,25%-graue Muster dar
|Gray12|: Stellt das 12,5%-graue Muster dar
|Gray25|: Stellt das 25%-graue Muster dar
|Gray50|: Stellt das 50%-graue Muster dar
|Gray75|: Stellt das 75%-graue Muster dar
|HorizontalStripe|: Stellt das horizontale Streifenmuster dar
|None|: Stellt keinen Hintergrund dar
|ReverseDiagonalStripe|: Stellt das umgekehrte diagonale Streifenmuster dar
|Solid|: Stellt das einfarbige Muster dar
|ThickDiagonalCrosshatch|: Stellt das dicke diagonale Kreuzmuster dar
|ThinDiagonalCrosshatch|: Stellt das dünnere diagonale Kreuzmuster dar
|ThinDiagonalStripe|: Stellt das dünnere diagonale Streifenmuster dar
|ThinHorizontalCrosshatch|: Stellt das dünnere horizontale Kreuzmuster dar
|ThinHorizontalStripe|: Stellt das dünnere horizontale Streifenmuster dar
|ThinReverseDiagonalStripe|Stellt ein dünn umgekehrtes diagonales Streifenmuster dar|
|ThinVerticalStripe|Stellt ein dünn vertikales Streifenmuster dar|
|VerticalStripe|Stellt ein vertikales Streifenmuster dar|

Im folgenden Beispiel ist die Vordergrundfarbe der Zelle A1 festgelegt, aber A2 ist so konfiguriert, dass sowohl Vordergrund- als auch Hintergrundfarben mit einem vertikalen Streifenmuster hinterlegt sind.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

            // Adding a new worksheet to the Workbook object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Define a Style and get the A1 cell style
            let style = worksheet.cells.get("A1").style;

            // Setting the foreground color to yellow
            style.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A1 cell
            worksheet.cells.get("A1").style = style;

            // Get the A2 cell style
            style = worksheet.cells.get("A2").style;

            // Setting the foreground color to blue
            style.foregroundColor = AsposeCells.Color.Blue;

            // Setting the background color to yellow
            style.backgroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A2 cell
            worksheet.cells.get("A2").style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```


### **Wichtig zu wissen**

{{% alert color="primary" %}}

- Um die Vordergrund- oder Hintergrundfarbe einer Zelle festzulegen, verwenden Sie die [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekt [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) oder [**backgroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundColor-color-) Eigenschaften. Beide treten nur in Kraft, wenn die [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Eigenschaft [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) des [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekts entsprechend konfiguriert ist.
- Die [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-)-Eigenschaft legt die Farbnuance der Zelle fest. Die [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-)-Eigenschaft gibt den Typ des Hintergrundmusters an, das für die Vordergrund- oder Hintergrundfarbe verwendet wird. Aspose.Cells bietet eine Enumeration, [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype), die eine Reihe vordefinierter Hintergrundmustertypen enthält.
- Wenn Sie den Wert *BackgroundType.None* aus der [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype)-Enumeration auswählen, wird die Vordergrundfarbe nicht angewendet. Ebenso wird die Hintergrundfarbe nicht angewendet, wenn Sie die Werte *BackgroundType.None* oder *BackgroundType.Solid* wählen.
- Beim Abrufen der Schattierungs-/Füllfarbe der Zelle gibt [**style.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor--) *Color.Empty* zurück, wenn [**style.pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) *BackgroundType.None* ist.

{{% /alert %}}

### **Anwendung von Verlaufsfülleffekten**

Um Ihre gewünschten Verläufeinstellungen auf die Zelle anzuwenden, verwenden Sie die [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Eigenschaft des [**twoColorGradient**](https://reference.aspose.com/cells/javascript-cpp/style/#twoColorGradient-color-color-gradientstyletype-number-)-Objekts entsprechend.

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
        const { Workbook, SaveFormat, Color, GradientStyleType, TextAlignmentType } = AsposeCells;

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

            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.get(2, 1).putValue("test");

            const style = worksheet.cells.get("B3").style;

            style.isGradient = true;
            style.twoColorGradient = [ new Color(255, 255, 255), new Color(79, 129, 189), GradientStyleType.Horizontal, 1 ];
            style.font.color = Color.Red;
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            worksheet.cells.get("B3").style = style;

            worksheet.cells.rowHeightPixel = [2, 53];

            worksheet.cells.merge(2, 1, 1, 2);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Farben und Palette**

Eine Palette ist die Anzahl der verfügbaren Farben zur Erstellung eines Bildes. Die Verwendung einer standardisierten Palette in einer Präsentation ermöglicht es dem Benutzer, ein konsistentes Erscheinungsbild zu erstellen. Jede Microsoft Excel (97-2003)-Datei hat eine Palette von 56 Farben, die auf Zellen, Schriften, Gitterlinien, grafische Objekte, Füllungen und Linien in einem Diagramm angewendet werden können.

Mit Aspose.Cells ist es möglich, nicht nur die vorhandenen Farben der Palette zu verwenden, sondern auch benutzerdefinierte Farben. Bevor Sie eine benutzerdefinierte Farbe verwenden, fügen Sie diese zunächst der Palette hinzu.

In diesem Thema wird erläutert, wie benutzerdefinierte Farben zur Palette hinzugefügt werden.

### **Hinzufügen von benutzerdefinierten Farben zur Palette**

Aspose.Cells unterstützt Microsoft Excels 56-Farben-Palette. Um eine benutzerdefinierte Farbe zu verwenden, die in der Palette nicht definiert ist, fügen Sie die Farbe der Palette hinzu.

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse bietet eine [**changePalette**](https://reference.aspose.com/cells/javascript-cpp/workbook/#changePalette-color-number-)-Methode, die die folgenden Parameter übernimmt, um eine benutzerdefinierte Farbe hinzuzufügen und die Palette zu ändern:

- Benutzerdefinierte Farbe, die benutzerdefinierte Farbe, die hinzugefügt werden soll.
- Index, der Index der Farbe in der Palette, die die benutzerdefinierte Farbe ersetzen wird. Sollte zwischen 0-55 liegen.

Das folgende Beispiel fügt eine benutzerdefinierte Farbe (Orchid) zur Palette hinzu, bevor sie auf eine Schriftart angewendet wird.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Checks if a color is in the palette for the spreadsheet.
            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding Orchid color to the palette at 55th index
            workbook.changePalette(AsposeCells.Color.Orchid, 55);

            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Hello Aspose!");

            // Defining new Style object
            const styleObject = workbook.createStyle();
            // Setting the Orchid (custom) color to the font
            styleObject.font.color = workbook.colors[55];

            // Applying the style to the cell
            cell.style = styleObject;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}

Die Palette bietet Platz für nur 56 Farben. Wenn Sie eine benutzerdefinierte Farbe zur Palette hinzufügen, wird die Palette geändert und jedes Element in der Datei, das zuvor mit der Farbe formatiert wurde, wird geändert. Wenn Sie also die Palette ändern, seien Sie bitte sehr vorsichtig. Außerdem handelt es sich hierbei ausschließlich um eine Einschränkung im XLS (Excel 97 - 2003) Dateiformat, da es für XLSX oder andere fortgeschrittene MS Excel (2007/2010 oder 2013) Dateiformate keine solche Einschränkung gibt.

{{% /alert %}}
