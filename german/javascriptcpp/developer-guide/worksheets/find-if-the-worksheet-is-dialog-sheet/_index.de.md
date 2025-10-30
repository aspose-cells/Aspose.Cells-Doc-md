---
title: Ermitteln, ob das Arbeitsblatt ein Dialogblatt ist, mit JavaScript über C++
linktitle: Feststellen, ob das Arbeitsblatt ein Dialogblatt ist
type: docs
weight: 90
url: /de/javascript-cpp/find-if-the-worksheet-is-dialog-sheet/
description: Dieser Artikel enthält Anweisungen und Beispielcode, um programmgesteuert festzustellen, ob ein Excel Arbeitsblatt ein Dialogblatt ist, unter Verwendung von Aspose.Cells for JavaScript über C++.
keywords: Finden Sie den Excel Arbeitsblatt Dialogtyp mit JavaScript über C++, Arbeitsblatt Dialog JavaScript über C++
---

## **Mögliche Verwendungsszenarien**

Dialogblatt ist ein altes Format eines Blatts, das eine Dialogbox enthält. Ein solches Blatt kann von einer älteren Version von Microsoft Excel, z. B. 2003, eingefügt werden, wie in diesem Screenshot gezeigt. Es kann auch in neueren Versionen, z. B. Microsoft Excel 2016, mit VBA eingefügt werden.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Sie können feststellen, ob das Blatt ein Dialogblatt ist oder einen anderen Typ hat, mit der Eigenschaft [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--), bereitgestellt durch Aspose.Cells for JavaScript via C++. Wenn sie den Enumerationswert [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype) zurückgibt, bedeutet dies, dass Sie es mit einem Dialogblatt zu tun haben.

## **Feststellen, ob das Arbeitsblatt ein Dialogblatt ist**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716820.xlsx), die ein Dialogblatt enthält. Er prüft die Eigenschaft [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--), vergleicht sie mit [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype) und gibt dann die Nachricht aus. Für weitere Hilfe siehe die Konsolenausgabe des Beispielcodes unten.

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Detect Dialog Sheet</title>
    </head>
    <body>
        <h1>Detect if Worksheet Is a Dialog Sheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Find if the sheet type is dialog and print the message
            if (ws.type === AsposeCells.SheetType.Dialog) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet is a Dialog Sheet.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is NOT a Dialog Sheet.</p>';
            }
        });
    </script>
</html>
```

## **Konsolenausgabe**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
