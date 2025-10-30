---
title: Slicer mit JavaScript über C++ aktualisieren
linktitle: Slicer aktualisieren
type: docs
weight: 50
url: /de/javascript-cpp/updating-slicer/
description: Dieser Artikel zeigt, wie man verbundene Pivot Tabellen durch Aktualisieren des Slicers mit Aspose.Cells for JavaScript über C++ aktualisiert.
keywords: Aspose.Cells JavaScript über C++, Slicer aktualisieren JavaScript, wie man den Slicer JavaScript ändert, wie man den Slicer in JavaScript anpasst, wie man Slicer Items per JavaScript auswählt oder abwählt über C++.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie einen Slicer in Microsoft Excel aktualisieren möchten, wählen oder abwählen Sie die Artikel, und der Slicer-Tabellen oder Pivot-Tabellen werden entsprechend aktualisiert. Bitte verwenden Sie [**Slicer.slicerCacheItems**](https://reference.aspose.com/cells/javascript-cpp/slicercache/#slicerCacheItems--), um Slicer-Artikel mit Aspose.Cells auszuwählen oder abzuwählen, und rufen dann die Methode [**Slicer.refresh()**](https://reference.aspose.com/cells/javascript-cpp/slicer/#refresh--) auf, um den Slicer-Tabellen oder Pivot-Tabellen zu aktualisieren.

## **Wie man den Slicer aktualisiert**

Der folgende Beispielscode lädt die [Beispiel-Excel-Datei](67338475.xlsx), die einen vorhandenen Slicer enthält. Es entwählt die 2. und 3. Elemente des Slicers und aktualisiert den Slicer. Anschließend speichert es die Arbeitsmappe unter [Ausgabe-Excel-Datei](67338476.xlsx). Der folgende Screenshot zeigt die Auswirkung des Beispielscodes auf die Beispiel-Excel-Datei. Wie Sie auf dem Screenshot sehen können, wurde durch das Aktualisieren des Slicers mit ausgewählten Elementen auch die Pivot-Tabelle entsprechend aktualisiert.

![todo:image_alt_text](updating-slicer_1.png)

## **Beispielcode**

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Access the slicer items via slicer cache
            const items = slicer.slicerCache.slicerCacheItems;

            // Iterate items and deselect "Pink" and "Green"
            for (let i = 0; i < items.count; i++) {
                const item = items.get(i);
                if (item.value === "Pink" || item.value === "Green") {
                    item.selected = false;
                }
            }

            // Refresh slicer to apply changes
            slicer.refresh();

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
