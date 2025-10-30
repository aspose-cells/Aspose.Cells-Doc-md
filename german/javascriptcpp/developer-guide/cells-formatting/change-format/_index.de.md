---
title: Ändern Sie das Format einer Zelle
linktitle: Ändern Sie das Format einer Zelle
description: So verwenden Sie die Aspose.Cells Bibliothek in JavaScript über C++, um die Formatierung von Zellen zu ändern, einschließlich Schriftart, Farbe, Rahmen usw. Durch Anpassen dieser Eigenschaften haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Zellenformatierung, JavaScript über C++, Schriftart, Farbe, Rahmen
type: docs
weight: 20
url: /de/javascript-cpp/how-to-change-format-of-cell/
---

## **Mögliche Verwendungsszenarien**
Wenn Sie bestimmte Daten hervorheben möchten, können Sie den Stil der Zellen ändern.

## **Wie man das Format einer Zelle in Excel ändert**

Um das Format einer einzelnen Zelle in Excel zu ändern, befolgen Sie diese Schritte:

1. Öffnen Sie Excel und öffnen Sie die Arbeitsmappe, die die Zelle enthält, die Sie formatieren möchten.

2. Suchen Sie die Zelle, die Sie formatieren möchten.

3. Klicken Sie mit der rechten Maustaste auf die Zelle und wählen Sie "Zellen formatieren" aus dem Kontextmenü. Alternativ können Sie die Zelle auswählen, zum Register Start in der Excel-Befehlsleiste gehen, auf die Dropdown-Schaltfläche "Format" in der Gruppe "Zellen" klicken und "Zellen formatieren" auswählen.

4. Das Dialogfeld "Zellen formatieren" wird angezeigt. Hier können Sie verschiedene Formatierungsoptionen auswählen, die auf die ausgewählte Zelle angewendet werden sollen. Sie können z.B. die Schriftart, die Schriftgröße, die Schriftfarbe, das Zahlenformat, die Rahmen, die Hintergrundfarbe usw. ändern. Erkunden Sie die verschiedenen Registerkarten im Dialogfeld, um auf verschiedene Formatierungsoptionen zuzugreifen.

5. Klicken Sie nach dem Anwenden der gewünschten Formatierungsänderungen auf die Schaltfläche "OK", um die Formatierung auf die ausgewählte Zelle anzuwenden.


## **So ändern Sie das Format einer Zelle mit JavaScript**

Um das Format einer Zelle mit Aspose.Cells zu ändern, können Sie die folgenden Methoden verwenden:
1. [Zellen.stil(Style)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)
2. [Zellen.stil(Style, explicitFlag)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-boolean-)
3. [Zellen.stil(Style, StyleFlag)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-styleflag-)


## **Beispielcode**
In diesem Beispiel erstellen wir ein Excel-Arbeitsbuch, fügen einige Beispieldaten hinzu, greifen auf das erste Arbeitsblatt zu und holen zwei Zellen («A2» und «B3»). Dann holen wir den Stil der Zelle, setzen verschiedene Formatierungsoptionen (z. B. Schriftfarbe, fett) und ändern das Format der Zelle. Schließlich speichern wir das Arbeitsbuch in eine neue Datei.
![todo:image_alt_text](change-format.png)

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;

            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Access the worksheet
            const worksheet = workbook.worksheets.get(0);

            const a2 = worksheet.cells.get("A2");

            // Get style of A2
            const style = a2.style;

            // Change the format
            style.font.color = AsposeCells.Color.Red;
            style.font.isBold = true;

            const flag = new AsposeCells.StyleFlag();
            flag.fontColor = true;
            // Apply style (assignment per conversion rules)
            a2.style = style;

            const b3 = worksheet.cells.get("B3");
            // Get style of B3
            const style2 = b3.style;

            // Change the format
            style2.font.color = AsposeCells.Color.Blue;
            style2.font.isItalic = true;
            b3.style = style2;

            // Saving the modified workbook and offering it for download
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
