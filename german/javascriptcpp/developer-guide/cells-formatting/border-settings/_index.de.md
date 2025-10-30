---
title: Rahmeneinstellungen
linktitle: Rahmeneinstellungen
description: So verwenden Sie die Aspose.Cells Bibliothek in JavaScript via C++, um den Rahmenstil und die Farbe von Zellen festzulegen. Durch Anpassung der Breite, des Stils und der Farbe des Rahmens haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Zellenrahmen Einstellungen, JavaScript über C++, Rahmenbreite, Rahmenstil, Rahmenfarbe
type: docs
weight: 40
url: /de/javascript-cpp/cells-border-settings/
---

## **Rahmen zu Zellen hinzufügen**

Microsoft Excel ermöglicht es Benutzern, Zellen durch Hinzufügen von Rändern zu formatieren. Der Randtyp hängt davon ab, wo er hinzugefügt wird. Zum Beispiel ist ein oberer Rand einer, der an die obere Position einer Zelle gesetzt wird. Benutzer können auch den Linienstil und die Farbe der Ränder anpassen.

Mit Aspose.Cells for JavaScript über C++ können Entwickler Rahmen hinzufügen und das Aussehen nach gleicher flexibler Art wie in Microsoft Excel anpassen.

### **Rahmen zu Zellen hinzufügen**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse enthält eine [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)–Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse bietet die [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung. Jedes Element in der [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung repräsentiert ein Objekt der [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Klasse.

Aspose.Cells bietet die [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)-Eigenschaft in der [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Klasse. Die [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) wird verwendet, um den Formatierungsstil einer Zelle festzulegen. Die [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Klasse stellt Eigenschaften zum Hinzufügen von Rahmen zu Zellen bereit.

#### **Rahmen zu einer Zelle hinzufügen**

Entwickler können Ränder zu einer Zelle hinzufügen, indem sie die [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Eigenschaftensammlung des [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--)-Objekts verwenden. Der Rahmentyp wird als Index an die [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--)-Sammlung übergeben. Alle Rahmentypen sind in der [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype)-Aufzählung vorab definiert.

**Rahmen-Aufzählung**

|**Rahmentypen**|**Beschreibung**|
| :- | :- |
|BottomBorder|Eine untere Rahmenlinie
|DiagonalDown|Eine diagonale Linie von oben links nach rechts unten
|DiagonalUp|Eine diagonale Linie von unten links nach oben rechts|
|LeftBorder|Eine Linie am linken Rand|
|RightBorder|Eine Linie am rechten Rand|
|TopBorder|Eine Linie am oberen Rand|

Die [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--)-Sammlung speichert alle Ränder. Jeder Rand in der [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--)-Sammlung wird durch ein [**Border**](https://reference.aspose.com/cells/javascript-cpp/border)-Objekt repräsentiert, das zwei Eigenschaften, [**color**](https://reference.aspose.com/cells/javascript-cpp/border/#color-color-) und [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-), zur Festlegung der Linienfarbe und des Stils eines Rands bereitstellt.

Um die Linienfarbe eines Rahmens festzulegen, wählen Sie eine Farbe mit der Color-Aufzählung (Teil von JavaScript) und weisen Sie sie der Farb-Eigenschaft des Rahmenobjekts zu.

Der Linienstil des Rands wird festgelegt, indem ein Linienstil aus der [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype)-Aufzählung ausgewählt wird.

**Zellrahmentyp-Enumeration**

|**Linienstile**|**Beschreibung**|
| :- | :- |
|DashDot|Dünne gestrichelt-punktierte Linie|
|DashDotDot|Dünne gestrichelt-punkt-punktierte Linie|
|Dashed|Gestrichelte Linie|
|Dotted|Gepunktete Linie|
|Double|Doppelte Linie|
|Hair|Haarlinie|
|MediumDashDot|Mittlere gestrichelt-punktierte Linie|
|MediumDashDotDot|Mittlere gestrichelt-punkt-punktierte Linie|
|MediumDashed|Mittlere gestrichelte Linie|
|None|Keine Linie|
|Medium|Mittlere Linie|
|SlantedDashDot|Geneigte mittlere Strichpunktlinie|
|Thick|Dicke Linie|
|Thin|Dünne Linie|
Wählen Sie einen der Linienstile aus und weisen Sie ihn der [**Border**](https://reference.aspose.com/cells/javascript-cpp/border)-Eigenschaft des [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-)-Objekts zu.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Borders to A1 Cell Example</h1>
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
            // This example creates a new workbook and adds borders to cell A1.
            // No try/catch is used so errors propagate for testing.

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Create a style object
            const style = cell.style;

            // Setting the line style and color of the top border
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the bottom border
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the left border
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the right border
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;

            // Apply the border styles to the cell
            cell.style = style;

            // Saving the Excel file
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

{{% alert color="primary" %}}
Sie sollten sowohl den Linienstil als auch die Farbe gleichzeitig festlegen. Die beiden diagonalen Ränder sollten den gleichen Linienstil und die gleiche Farbe haben.
{{% /alert %}}

#### **Hinzufügen von Rahmen zu einem Zellenbereich**

Es ist auch möglich, Ränder an einen Zellbereich statt nur an eine einzelne Zelle hinzuzufügen. Dazu erstellen Sie zunächst einen Zellbereich, indem Sie die [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung mit der [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-)-Methode aufrufen. Diese nimmt die folgenden Parameter:

- Erste Zeile, die erste Zeile des Bereichs.
- Erste Spalte, stellt die erste Spalte des Bereichs dar.
- Anzahl der Zeilen, die Anzahl der Zeilen im Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Bereich.

Die [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-)-Methode gibt ein [**Range**](https://reference.aspose.com/cells/javascript-cpp/range)-Objekt zurück, das den angegebenen Zellbereich enthält. Das [**Range**](https://reference.aspose.com/cells/javascript-cpp/range)-Objekt bietet eine [**outlineBorder**](https://reference.aspose.com/cells/javascript-cpp/range/#outlineBorder-bordertype-cellbordertype-cellscolor-)-Methode, die die folgenden Parameter akzeptiert, um einen Rand zum Zellbereich hinzuzufügen:

- **Ramentyp**, der Randtyp, ausgewählt aus der [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype)-Aufzählung.
- **Linienstil**, der Linienstil des Rands, ausgewählt aus der [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype)-Aufzählung.
- **Farbe**, die aus der Farb-Aufzählung ausgewählte Linienfarbe.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Apply Borders</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color } = AsposeCells;

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
            // This example creates a new workbook, writes to A1, creates a range and applies borders, then offers the file for download.
            const workbook = new Workbook();

            const worksheet = workbook.worksheets.get(0);

            const cell = worksheet.cells.get("A1");

            cell.putValue("Hello World From Aspose");

            const range = worksheet.cells.createRange(0, 0, 1, 3);

            // Applying borders using property assignment conversions for setter methods
            range.outlineBorder = [BorderType.TopBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.BottomBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.LeftBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.RightBorder, CellBorderType.Thick, Color.Blue];

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and borders applied successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
