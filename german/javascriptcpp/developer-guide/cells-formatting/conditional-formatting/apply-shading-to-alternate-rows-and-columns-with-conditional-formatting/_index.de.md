---
title: Schattierung auf abwechselnden Zeilen und Spalten mit bedingter Formatierung anwenden
linktitle: Schattierung auf abwechselnden Zeilen und Spalten mit bedingter Formatierung anwenden
description: Wie man die Aspose.Cells Bibliothek in JavaScript über C++ verwendet, um Schatten für bedingte Formatierungen bei abwechselnden Zeilen und Spalten anzuwenden. Durch Anpassung dieser Kriterien erhalten Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Bedingte Formatierung, JavaScript über C++, Alternierende Zeilen, Alternierende Spalten, Schatten
type: docs
weight: 30
url: /de/javascript-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Die Aspose.Cells-APIs bieten die Möglichkeit, Bedingungen und Regeln für die bedingte Formatierung des [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Objekts hinzuzufügen und zu manipulieren. Diese Regeln können in verschiedener Weise angepasst werden, um die gewünschte Formatierung basierend auf Bedingungen oder Regeln zu erzielen. Dieser Artikel demonstriert die Verwendung der Aspose.Cells for JavaScript über C++ APIs, um mit Hilfe von bedingter Formatierung und den integrierten Funktionen von Excel Schattierungen bei alternierenden Zeilen und Spalten anzuwenden.

{{% /alert %}}

Dieser Artikel verwendet integrierte Funktionen von Excel wie ROW, COLUMN & MOD. Hier sind einige Details zu diesen Funktionen, um das Code-Snippet, das im Folgenden bereitgestellt wird, besser zu verstehen.

- **ROW()** Funktion gibt die Zeilennummer eines Zellbezugs zurück. Wenn der Referenzparameter weggelassen wird, wird angenommen, dass sich die Referenz auf die Zellenadresse bezieht, in die die ROW-Funktion eingegeben wurde.
- **COLUMN()** Funktion gibt die Spaltennummer eines Zellbezugs zurück. Wenn der Referenzparameter weggelassen wird, wird angenommen, dass sich die Referenz auf die Zellenadresse bezieht, in die die COLUMN-Funktion eingegeben wurde.
- Die **MOD()**-Funktion gibt den Rest nach der Division einer Zahl durch einen Divisor zurück, wobei der erste Parameter der numerische Wert ist, von dem Sie den Rest finden möchten, und der zweite Parameter die Zahl ist, durch die die Nummernparameter dividiert werden. Wenn der Divisor 0 ist, wird der Fehler #DIV/0! zurückgegeben.

Beginnen wir mit dem Schreiben von Code, um dieses Ziel mit Hilfe der Aspose.Cells for JavaScript über C++ API zu erreichen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Conditional Formatting</title>
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
        const { Workbook, SaveFormat, CellArea, Utils } = AsposeCells;

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
            // Create an instance of Workbook
            const book = new Workbook();

            // Access the first worksheet
            const sheet = book.worksheets.get(0);

            // Add FormatConditions to the instance of Worksheet
            let idx = sheet.conditionalFormattings.add();

            // Access the newly added FormatConditions via its index
            const conditionCollection = sheet.conditionalFormattings.get(idx);

            // Define a CellsArea on which conditional formatting will be applicable (A1 to I20)
            const area = CellArea.createCellArea("A1", "I20");

            // Add area to the instance of FormatConditions
            conditionCollection.addArea(area);

            // Add a condition to the instance of FormatConditions (Expression type)
            idx = conditionCollection.addCondition(AsposeCells.FormatConditionType.Expression);

            // Access the newly added FormatCondition via its index
            const formatCondition = conditionCollection.get(idx);

            // Set the formula for the FormatCondition
            formatCondition.formula1 = "=MOD(ROW(),2)=0";

            // Set the background color and pattern for the FormatCondition's Style
            formatCondition.style.backgroundColor = AsposeCells.Color.Blue;
            formatCondition.style.pattern = AsposeCells.BackgroundType.Solid;

            // Save the result and provide a download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


Die folgende Momentaufnahme zeigt die resultierende Tabelle, die in der Excel-Anwendung geladen wird.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Um die Schattierung auf alternative Spalten anzuwenden, müssen Sie lediglich die Formel **=MOD(ZEILE(),2)=0** durch **=MOD(SPALTE(),2)=0** ersetzen, d.h. anstatt den Zeilenindex zu erhalten, ändern Sie die Formel, um den Spaltenindex abzurufen.  
Die resultierende Tabelle wird in diesem Fall folgendermaßen aussehen.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
