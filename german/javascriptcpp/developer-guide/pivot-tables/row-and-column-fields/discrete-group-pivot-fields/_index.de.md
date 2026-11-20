---
title: Diskrete Gruppierung von Pivot-Feldelementen
linktitle: Diskrete Gruppierung
description: Erfahren Sie, wie Sie mithilfe der Klasse DiscreteGroupItem und der Eigenschaft PivotFieldGroupOptions.discreteGroupItems in Aspose.Cells for JavaScript via C++ Pivot-Feldelemente in benutzerdefinierte Gruppen wie Obst und Gemüse gruppieren.
keywords: Aspose.Cells, PivotTable, diskrete Gruppierung, DiscreteGroupItem, PivotFieldGroupOptions, Pivot-Feldelemente gruppieren, benutzerdefinierte Gruppen, PivotField.group, Aspose.Cells for JavaScript via C++, Excel-PivotTable
type: docs
weight: 90
url: /de/javascript-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
- Die automatische Gruppierung fasst Elemente nach Datentyp zusammen, beispielsweise Datumswerte in Monate und Quartale oder Zahlen in Bereiche. Die diskrete Gruppierung löst das entgegengesetzte Problem: Sie fasst bestimmte, nicht zusammengehörige Elemente in benutzerdefinierte Gruppen mit Namen zusammen, etwa Produkte in Obst und Gemüse, Geschäfte in Regionen oder Konten in Zonen. Aspose.Cells bietet die diskrete Gruppierung mithilfe der Klasse `DiscreteGroupItem` und der Eigenschaft `PivotFieldGroupOptions.discreteGroupItems` an.
- Ein `DiscreteGroupItem` ist ein Gruppenname plus die Elemente, die ihm angehören. Die Elemente können auf zwei Arten identifiziert werden: durch ihre Namen (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) oder durch ihre nullbasierten Positionen in den Quelldaten (`new DiscreteGroupItem("fruit", [0, 3])`). Beide Formen führen zum selben Ergebnis.
- Für ein Feld im Zeilen- oder Spaltenbereich der PivotTable werden die Optionen an `PivotField.group(PivotFieldGroupOptions)` übergeben, um die diskrete Gruppierung anzuwenden.

## **Pivot-Feldelemente nach Elementnamen gruppieren**
Das folgende Beispiel erstellt eine kleine Verkaufsliste (Produkt, Datum und Betrag), erzeugt daraus eine PivotTable mit `product` im Zeilenbereich, `date` im Spaltenbereich und `amount` im Datenbereich und definiert anschließend zwei benutzerdefinierte Gruppen anhand der Elementnamen: Obst (Traube, Kirsche) und Gemüse (Karotte, Kartoffel). Das Ergebnis zeigt ein zweistufiges Zeilenlayout, wobei der Gruppenname die äußere Ebene bildet und die ursprünglichen Elemente darunter verschachtelt sind. So lassen sich Trends je benutzerdefinierter Gruppe und je Element ablesen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            const { Workbook, DiscreteGroupItem, PivotFieldGroupOptions } = AsposeCells;
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType =
                    AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // Group specific items into custom groups by item names
                const fruit = new DiscreteGroupItem("fruit", ["grape", "cherry"]);
                const vegetable = new DiscreteGroupItem("vegetable", ["carrot", "potato"]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

Nach `calculateData()` zeigt der Zeilenbereich der PivotTable Obst (Traube 50, Kirsche 80) und Gemüse (Karotte 60, Kartoffel 70) mit der Gesamtsumme 260, während die Spaltenbeschriftungen die vier Datumswerte (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024) beibehalten.

## **Pivot-Feldelemente nach Elementindizes gruppieren**
Wenn die Elementnamen lang oder lokalisiert sind, identifiziert der zweite Konstruktor von `DiscreteGroupItem` die Elemente über ihren Index. Die Indizes sind nullbasierte Positionen der Elemente in der Reihenfolge, in der sie in den Quelldaten erscheinen, nicht in alphabetischer Reihenfolge. In den obigen Beispieldaten ist Traube Element 0, Karotte Element 1, Kartoffel Element 2 und Kirsche Element 3; daher ist Obst `{ 0, 3 }` und Gemüse `{ 1, 2 }`. Das Ergebnis ist identisch mit dem namensbasierten Beispiel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            const {
                Workbook,
                SaveFormat,
                DiscreteGroupItem,
                PivotFieldGroupOptions
            } = AsposeCells;
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
                // (zero-based positions in the order the items appear in the source data)
                const fruit = new DiscreteGroupItem("fruit", [0, 3]);
                const vegetable = new DiscreteGroupItem("vegetable", [1, 2]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotFieldByIndex.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

## **Hinweis**

{{% alert color="primary" %}}
- Elemente, die keiner benutzerdefinierten Gruppe zugeordnet sind, gehen nicht verloren. Sie bleiben in der PivotTable auf derselben Ebene wie die benutzerdefinierten Gruppen, jeweils als eigener Eintrag mit einem Element. Im obigen Beispiel bleiben Karotte und Kartoffel, wenn nur die Gruppe Obst definiert wird, im Zeilenbereich als eigenständige Einträge neben der Gruppe Obst.
- Die Eigenschaft `PivotFieldGroupOptions.newPivotField` steuert das Layout der diskreten Gruppierung. Der Standardwert ist `true`. Dadurch wird das gruppierte Feld als neues äußeres Feld neben dem ursprünglichen Feld hinzugefügt, wodurch das oben gezeigte zweistufige Layout entsteht (`rowFields` wird auf 2 erweitert). Setzen Sie den Wert auf `false`, um das ursprüngliche Feld zu ersetzen. Der Zeilenbereich zeigt dann eine einzige Ebene, die nur die Gruppennamen mit ihren aggregierten Werten enthält: Obst 130 (50 + 80) und Gemüse 130 (60 + 70).
- Die namens- und indexbasierten Konstruktoren von `DiscreteGroupItem` können innerhalb desselben `discreteGroupItems`-Arrays kombiniert werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Pivot-Felder in der PivotTable gruppieren](/cells/de/javascript-cpp/group-pivot-fields-in-the-pivot-table/)
- [Zeilen- und Spaltenfelder zur PivotTable hinzufügen](/cells/de/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [PivotTables nach Bezeichnung oder Wert filtern](/cells/de/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [Formatierung auf eine PivotTable anwenden](/cells/de/javascript-cpp/apply-style-to-pivot-table/)
- [PivotTable aktualisieren](/cells/de/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}