---
title: Erstellen Sie ein berechnetes Feld im Pivot Table
type: docs
weight: 130
url: /de/javascript-cpp/add-calculated-field-in-pivot-table/
description: Wie man ein berechnetes Feld in Pivot Tabellen mit Aspose.Cells for JavaScript über C++ hinzufügt.
keywords: Aspose.Cells for JavaScript über C++ Excel, JavaScript Bibliothek für Excel, Hinzufügen eines berechneten Feldes in Pivot Tabellen mit JavaScript Excel Library.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie eine Pivot-Tabelle basierend auf bekannten Daten erstellen, stellen Sie fest, dass die Daten darin nicht das sind, was Sie wollen. Die Daten, die Sie wollen, sind die Kombination dieser Originaldaten. Zum Beispiel müssen Sie die ursprünglichen Daten addieren, subtrahieren, multiplizieren und dividieren, bevor Sie die Daten wollen. Zu diesem Zeitpunkt müssen Sie ein berechnetes Feld erstellen und die entsprechende Formel für die Berechnung festlegen. Führen Sie dann einige Statistiken und andere Operationen auf dem berechneten Feld durch. 

## **Wie man ein berechnetes Feld in einer Pivot-Tabelle in Excel hinzufügt**
Fügen Sie ein berechnetes Feld in eine Pivot-Tabelle in Excel ein, befolgen Sie diese Schritte:

1. Wählen Sie die Pivot-Tabelle aus, zu der Sie ein berechnetes Feld hinzufügen möchten. 
2. Gehen Sie zum Register PivotTable Analyse in der Menüleiste.
3. Klicken Sie auf "Felder, Elemente und Sets" und wählen Sie dann "Berechnetes Feld" im Dropdown-Menü aus.
4. Geben Sie im Feld "Name" einen Namen für das berechnete Feld ein.
5. Geben Sie im Feld "Formel" die Formel für die Berechnung ein, die Sie unter Verwendung der entsprechenden Feldnamen und mathematischen Operatoren in der Pivot-Tabelle durchführen möchten. 
<br>
<img src="1.png" width=80% />
6. Klicken Sie auf "OK", um das berechnete Feld zu erstellen.
7. Das neue berechnete Feld wird im Bereich Wertliste der Pivot-Tabelle unter den Werten angezeigt.
8. Ziehen Sie das berechnete Feld in den Wertebereich der Pivot-Tabelle, um die berechneten Werte anzuzeigen.
<br>
<img src="2.png" width=80% />

## ** Wie man ein berechnetes Feld in Pivot-Tabellen mit der Aspose.Cells for JavaScript über C++ Bibliothek hinzufügt**
Berechnen Sie ein berechnetes Feld in der Excel-Datei mit Aspose.Cells for JavaScript über C++. Bitte sehen Sie sich den folgenden Beispielcode an. Nach Ausführung des Beispielcodes wird eine Pivot-Tabelle mit berechnetem Feld zum Arbeitsblatt hinzugefügt.
1. Legen Sie die Originaldaten fest und erstellen Sie eine Pivot-Tabelle. 
2. Erstellen Sie das berechnete Feld gemäß dem vorhandenen PivotField in der Pivot-Tabelle.
3. Fügen Sie das berechnete Feld in den Datenbereich ein. 
4. Schließlich wird die Arbeitsmappe im [XLSX-Ausgabeformat](out.xlsx) gespeichert. 

## **Beispielcode**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotFieldType, Utils } = AsposeCells;

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

            // Obtain the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value)
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

            // Adding a PivotTable to the worksheet (converted getPivotTables -> pivotTables)
            const i = ws.pivotTables.add("=A1:C5", "D10", "PivotTable1");
            // Accessing the instance of the newly added PivotTable
            const pivotTable = ws.pivotTables.get(i);
            pivotTable.addFieldToArea(PivotFieldType.Row, 0);
            // Adding a calculated field to PivotTable and drag it to data area.
            pivotTable.addCalculatedField("total", "=Count*Price", true);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
