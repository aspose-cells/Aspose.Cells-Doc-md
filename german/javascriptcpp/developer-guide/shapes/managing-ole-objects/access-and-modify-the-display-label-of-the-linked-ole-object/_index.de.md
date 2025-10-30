---
title: Zugriff auf und Änderung des Anzeigenetiketts des verknüpften Ole Objekts mit JavaScript über C++
linktitle: Auf das Anzeigen des verknüpften Ole Objekts zugreifen und es ändern
type: docs
weight: 100
url: /de/javascript-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Lernen Sie, wie Sie das Anzeigeetikett eines verknüpften Ole Objekts mit Aspose.Cells for JavaScript über C++ zugreifen und ändern. 
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel erlaubt es, das Anzeige-Label des Ole-Objekts zu ändern, wie im folgenden Screenshot gezeigt. Sie können auch das Anzeige-Label des Ole-Objekts mit Aspose.Cells APIs über die Eigenschaft [**OleObject.label**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#label--) zugreifen oder modifizieren.

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Auf das Anzeigen des verknüpften Ole-Objekts zugreifen und es ändern**

Bitte sehen Sie sich den folgenden Beispielcode an, der die <a href="64716810.xlsx">Beispieldatei für Excel</a> lädt, die das Ole-Objekt enthält. Der Code greift auf das Ole-Objekt zu und ändert sein Label von Sample APIs zu Aspose APIs. Unten sehen Sie die Konsolen-Ausgabe, die den Effekt des Beispielcodes auf die Beispieldatei zeigt.

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Access and Modify Label of Ole Object Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file 
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access first Ole Object
            let oleObject = ws.oleObjects.get(0);

            // Display the Label of the Ole Object
            const beforeLabel = oleObject.label;
            console.log("Ole Object Label - Before: " + beforeLabel);

            // Modify the Label of the Ole Object
            oleObject.label = "Aspose APIs";

            // Save workbook to memory stream
            const ms = wb.save(SaveFormat.Xlsx);

            // Set the workbook reference to null / dispose
            wb.dispose();

            // Load workbook from memory stream
            const wbFromStream = new Workbook(ms);

            // Access first worksheet
            const wsFromStream = wbFromStream.worksheets.get(0);

            // Access first Ole Object
            oleObject = wsFromStream.oleObjects.get(0);

            // Display the Label of the Ole Object that has been modified earlier
            const afterLabel = oleObject.label;
            console.log("Ole Object Label - After: " + afterLabel);

            // Prepare download
            const blob = new Blob([ms]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = `<p style="color: green;">Operation completed successfully!</p>
                                   <p>Ole Object Label - Before: ${beforeLabel}</p>
                                   <p>Ole Object Label - After: ${afterLabel}</p>`;
        });
    </script>
</html>
```

## **Konsolenausgabe**

{{< highlight javascript >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
