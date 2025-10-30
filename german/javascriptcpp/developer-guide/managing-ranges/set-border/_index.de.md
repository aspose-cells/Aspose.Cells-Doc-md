---
title: Bereichsrand mit JavaScript über C++ setzen
linktitle: Bereichsgrenze festlegen
type: docs
weight: 600
url: /de/javascript-cpp/set-range-border/
---

## **Mögliche Verwendungsszenarien**  
Wenn Sie den Rand für einen Bereich festlegen möchten, müssen Sie nicht jede Zelle einzeln einstellen. Sie können den Rand für den gesamten Bereich setzen. Aspose.Cells for JavaScript über C++ bietet diese Funktion.  
Dieses Artikel enthält einen Beispielcode, der Aspose.Cells for JavaScript via C++ verwendet, um den Rand eines Bereichs zu setzen.  

## **Bereichsgrenze in Excel festlegen**  
Um die Grenze eines Bereichs in Excel festzulegen, befolgen Sie diese Schritte:  
1. Wählen Sie den Zellenbereich aus, für den Sie die Grenze festlegen möchten.  
2. Suchen Sie im Register „Start“ in der Gruppe „Schriftart“.  
3. Klicken Sie in der Gruppe „Schriftart“ auf die Schaltfläche „Rahmen“.  
<br>  
<img src="border.png" />  
4. Wählen Sie den zu verwendenden Randtyp aus den Optionen im Dropdown-Menü aus. Sie können aus voreingestellten Rahmenstilen wählen oder Ihren eigenen Rahmen anpassen.  
5. Sobald Sie den gewünschten Rahmenstil ausgewählt haben, wird der Rahmen auf den ausgewählten Zellenbereich angewendet.  

## **Setzen Sie den Bereichsrand mit Aspose.Cells for JavaScript via C++**  
Dieses Beispiel zeigt, wie Sie:  

1. Ein Arbeitsbuch erstellen.  
2. Daten in die Zellen des ersten Arbeitsblatts einfügen.  
3. Erstellen Sie ein [**Range**](https://reference.aspose.com/cells/javascript-cpp/range).  
4. Setzen Sie den inneren Rahmen des Bereichs.  
5. Setzen Sie den äußeren Rahmen des Bereichs.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
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
            // Instantiate a new workbook
            const workbook = new Workbook();
            // Obtaining the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.putValue("Fruit");
            cell = cells.get("B1");
            cell.putValue("Count");
            cell = cells.get("C1");
            cell.putValue("Price");

            cell = cells.get("A2");
            cell.putValue("Apple");
            cell = cells.get("A3");
            cell.putValue("Mango");
            cell = cells.get("A4");
            cell.putValue("Blackberry");
            cell = cells.get("A5");
            cell.putValue("Cherry");

            cell = cells.get("B2");
            cell.putValue(5);
            cell = cells.get("B3");
            cell.putValue(3);
            cell = cells.get("B4");
            cell.putValue(6);
            cell = cells.get("B5");
            cell.putValue(4);

            cell = cells.get("C2");
            cell.putValue(5);
            cell = cells.get("C3");
            cell.putValue(20);
            cell = cells.get("C4");
            cell.putValue(30);
            cell = cells.get("C5");
            cell.putValue(60);

            // Create a range (A1:C5).
            const range = cells.createRange("A1", "C5");

            // set inner border of range
            const innerColor = workbook.createCellsColor();
            innerColor.color = AsposeCells.Color.Red;
            range.insideBorders = {
                borderType: AsposeCells.BorderType.Vertical,
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: innerColor
            };
            innerColor.color = AsposeCells.Color.Green;
            range.insideBorders = {
                borderType: AsposeCells.BorderType.Horizontal,
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: innerColor
            };

            // set outer border of range
            const outerColor = workbook.createCellsColor();
            outerColor.color = AsposeCells.Color.Blue;
            range.outlineBorders = {
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: outerColor
            };

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
