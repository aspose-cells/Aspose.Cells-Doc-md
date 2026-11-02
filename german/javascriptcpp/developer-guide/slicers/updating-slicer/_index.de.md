---
title: Slicer mit JavaScript via C++ aktualisieren
linktitle: Slicer aktualisieren
type: docs
weight: 50
url: /de/javascript-cpp/updating-slicer/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: Dieser Artikel zeigt, wie Sie einen Slicer aktualisieren, um die Daten der verknüpften Pivot-Tabelle oder Tabelle mit Aspose.Cells for JavaScript via C++ zu filtern.
keywords: Aspose.Cells JavaScript via C++, Slicer in JavaScript aktualisieren, wie man den Slicer in JavaScript ändert, wie man eine Pivot-Tabelle über einen Slicer in JavaScript filtert, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
---

## **Mögliche Verwendungsszenarien**
Das Aktualisieren eines Slicers bedeutet, die Daten der Pivot-Tabelle oder Tabelle zu filtern, mit der der Slicer verbunden ist. Wenn Sie Slicer-Elemente in Microsoft Excel auswählen oder abwählen, wird die verknüpfte Pivot-Tabelle oder Tabelle entsprechend neu berechnet. Mit Aspose.Cells for JavaScript via C++ müssen Sie die Slicer-Cache-Elemente nicht durchlaufen und den Slicer nicht manuell aktualisieren — die Methode [**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/javascript-cpp/slicer/) aktualisiert den Slicer und berechnet die verknüpfte Pivot-Tabelle oder Tabelle direkt anhand der Filterelemente neu:
- `Slicer.selectItems(labels, append)` — wählt die angegebenen Bezeichnungen aus und berechnet die verknüpfte Pivot-Tabelle oder Tabelle neu. Wenn `append` `true` ist, werden die ursprünglich ausgewählten Bezeichnungen beibehalten und die angegebenen Bezeichnungen zur Auswahl hinzugefügt; wenn `append` `false` ist, werden alle ursprünglichen Auswahlen gelöscht und nur die angegebenen Bezeichnungen bleiben ausgewählt.
- `Slicer.unselectItems(labels)` — wählt einen Teil der aktuell ausgewählten Elemente ab.
- `Slicer.clearFilter()` — entfernt den Filter und wählt alle Elemente aus.

{{% alert color="primary" %}}
Ab Aspose.Cells for JavaScript via C++ 26.10 wird die Eigenschaft `SlicerCacheItem.selected` schreibgeschützt, und ihr Setter wird nicht mehr unterstützt. Verwenden Sie die Methoden `Slicer.selectItems`, `Slicer.unselectItems` und `Slicer.clearFilter` anstelle des elementweisen Setzens von `SlicerCacheItem.selected`.
{{% /alert %}}

## **Wie man den Slicer aktualisiert**
Der folgende Beispielscode lädt die [Beispiel-Excel-Datei](67338475.xlsx), die einen vorhandenen, mit einer Pivot-Tabelle verbundenen Slicer enthält. Er wählt mit `Slicer.selectItems(labels, false)` nur die Elemente „Blue“ und „Pink“ des Slicers aus — die Pivot-Tabelle wird direkt anhand der Filterelemente neu berechnet, ohne einen manuellen `Slicer.refresh()`-Aufruf. Anschließend speichert er die Arbeitsmappe als [Ausgabe-Excel-Datei](67338476.xlsx). Der folgende Screenshot zeigt die Auswirkung des Beispielscodes auf die Beispiel-Excel-Datei. Wie Sie im Screenshot sehen können, zeigt die Pivot-Tabelle nur die gefilterten Elemente.
![todo:image_alt_text](updating-slicer_1.png)

## **Beispielcode**
Ersetzt die aktuelle Auswahl (nur die angegebenen Bezeichnungen bleiben ausgewählt) und berechnet die verknüpfte Pivot-Tabelle oder Tabelle neu:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Update Slicer</title>
    </head>
    <body>
        <h1>Update Slicer Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Select only "Blue" and "Pink"; the linked pivot table or table
            // is recalculated directly from the filter items
            slicer.selectItems(["Blue", "Pink"], false);

            // Save modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Behält die aktuell ausgewählten Bezeichnungen bei und wählt zusätzlich weitere Elemente aus:

```javascript
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

Wählt einen Teil der ausgewählten Elemente ab:

```javascript
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

Entfernt den Filter (wählt alle Elemente aus):

```javascript
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="javascript-cpp" >}}