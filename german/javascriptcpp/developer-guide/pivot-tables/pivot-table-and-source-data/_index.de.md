---
title: Pivot Tabelle und Quelldaten
type: docs
weight: 30
url: /de/javascript-cpp/pivot-table-and-source-data/
---

## **Quelldaten der Pivot-Tabelle**

Es gibt Zeiten, in denen Sie Microsoft Excel-Berichte mit Pivot-Tabellen erstellen möchten, die Daten aus verschiedenen Datenquellen (wie einer Datenbank) enthalten, die zur Entwurfszeit nicht bekannt sind. Dieser Artikel stellt einen Ansatz zur Verfügung, um die Datenquelle einer Pivot-Tabelle dynamisch zu ändern.

### **Ändern der Datenquelle einer Pivot-Tabelle**

1. Erstellen einer neuen Designer-Vorlage.
   1. Erstellen Sie eine neue Designer-Vorlagendatei wie im folgenden Screenshot gezeigt.
   1. Definieren Sie dann einen benannten Bereich, **Datenquelle**, der sich auf diesen Zellenbereich bezieht.

      **Erstellen einer Designer-Vorlage & Definieren eines benannten Bereichs, Datenquelle** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Erstellen einer Pivot-Tabelle auf Basis dieses benannten Bereichs.
   1. Wählen Sie in Microsoft Excel **Daten**, dann **PivotTable** und **PivotChart-Bericht** aus.
   1. Erstellen Sie eine Pivot-Tabelle basierend auf dem im ersten Schritt erstellten benannten Bereich.

      **Erstellen einer Pivot-Tabelle basierend auf dem benannten Bereich, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. Ziehen Sie das entsprechende Feld in Zeile und Spalte der Pivot-Tabelle und erstellen Sie dann die resultierende Pivot-Tabelle wie im Screenshot unten.

   **Erstellen einer Pivot-Tabelle basierend auf einem entsprechenden Feld** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Klicken Sie mit der rechten Maustaste auf die Pivot-Tabelle und wählen Sie **Tabellenoptionen**.
   1. Aktivieren Sie **Beim Öffnen aktualisieren** in den **Dateneinstellungen**.

      **Festlegen der Pivot-Tabellenoptionen** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Nun können Sie diese Datei als Ihre Designer-Vorlagendatei speichern.

1. Neue Daten einfügen und die Quelldaten einer Pivot-Tabelle ändern.
   1. Sobald die Designer-Vorlage erstellt ist, verwenden Sie den folgenden Code, um die Quelldaten der Pivot-Tabelle zu ändern.

Die Ausführung des untenstehenden Beispielcodes ändert die Quelldaten der Pivot-Tabelle.

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
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object using uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Populating new data to the worksheet cells
            worksheet.cells.get("A9").value = "Golf";
            worksheet.cells.get("B9").value = "Qtr4";
            worksheet.cells.get("C9").value = 7000;

            // Changing named range "DataSource"
            const range = worksheet.cells.createRange(0, 0, 9, 3);
            range.name = "DataSource";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
