---
title: Drehen Sie Text mit Shape innerhalb des Arbeitsblatts mit JavaScript via C++
linktitle: Text mit Shape innerhalb des Arbeitsblatts drehen
type: docs
weight: 1300
url: /de/javascript-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Lernen Sie, wie man Text mit Shape innerhalb eines Excel Arbeitsblatts mit Aspose.Cells for JavaScript via C++ dreht.
---

## **Mögliche Verwendungsszenarien**

Sie können Text in jeder Form mit Microsoft Excel hinzufügen. Wenn Sie eine Form mit sehr altem Microsoft Excel 2003 hinzufügen, wird der Text nicht mit der Form rotiert. Wenn Sie jedoch eine Form mit neueren Versionen von Microsoft Excel hinzufügen, z.B. 2007, 2010, 2013 oder 2016 etc., wird der Text mit der Form rotiert. Sie können steuern, ob der Text mit der Form rotiert werden soll oder nicht, indem Sie die [**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--)-Eigenschaft verwenden. Der Standardwert ist **true**, was bedeutet, dass der Text mit der Form rotiert. Wird ihn jedoch auf **false** gesetzt, rotiert der Text nicht mit der Form.

## **Text mit Form im Arbeitsblatt drehen**

Das folgende Beispiel lädt die [Beispieldatei Excel](64716896.xlsx), die eine Dreiecksform enthält, und deren Text sich mit der Form dreht. Wenn Sie die Beispiel-Excel-Datei in Microsoft Excel öffnen und die Dreiecksform drehen, wird sich auch der Text mitdrehen. Der Code setzt dann die [**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--)-Eigenschaft auf **false** und speichert die Datei als [Ausgabe-Excel](64716897.xlsx). Wenn Sie jetzt die Ausgabedatei in Microsoft Excel öffnen und die Dreiecksform drehen, dreht sich der Text nicht mehr mit. Bitte sehen Sie sich den folgenden Screenshot an, der die Wirkung des Codes auf die Beispiel-Excel-Datei zeigt.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Rotate Text With Shape</title>
    </head>
    <body>
        <h1>Rotate Text With Shape Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access cell B4 and add message inside it.
            const cellB4 = worksheet.cells.get("B4");
            cellB4.value = "Text is not rotating with shape because RotateTextWithShape is false.";

            // Access first shape.
            const shape = worksheet.shapes.get(0);

            // Access shape text alignment.
            const shapeTextAlignment = shape.textBody.textAlignment;

            // Do not rotate text with shape by setting RotateTextWithShape as false.
            shapeTextAlignment.rotateTextWithShape = false;

            // Saving the modified Excel file and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRotateTextWithShapeInsideWorksheet.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
