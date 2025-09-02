---
title: Lock or unlock shapes with JavaScript via C++
linktitle: Lock or unlock shapes
type: docs
weight: 200
url: /javascript-cpp/lock-or-unlock-shapes/
description: This article shows you code explaining how to lock or unlock shapes to protect them using Aspose.Cells library for JavaScript via C++.
keywords: JavaScript via C++ Lock Shapes to Protect Them, How to Lock or unlock shapes using JavaScript via C++, Lock or unlock shapes to Protect Them in JavaScript via C++.
---

## **Possible Usage Scenarios**

Sometimes, you need to protect all shapes in certain worksheets to prevent them from being destroyed by unwanted situations. In this case, you need to lock all shapes in the specified worksheet. 

Locking shapes in a spreadsheet or document can be beneficial for several reasons:
1. Prevent Accidental Changes: Locking shapes ensures that they are not accidentally moved, resized, or deleted by users. This is particularly important in complex documents where shapes may be used for annotations, illustrations, or as part of the document's design.
1. Maintain Layout and Design: Shapes often play a crucial role in the layout and visual design of a document. Locking them preserves the intended appearance, ensuring that the document remains professional and visually appealing.
1. Data Integrity: In spreadsheets, shapes can be used to highlight important data points, add comments, or provide visual explanations. Locking these shapes ensures that the contextual information they provide remains accurate and intact.
1. Consistency in Shared Documents: When collaborating on documents, different users might have varying levels of expertise. Locking shapes helps maintain consistency across the document by preventing unintended alterations.
1. Security: In sensitive documents, locking shapes can be part of a broader strategy to protect information. For example, in financial reports or legal documents, locked shapes can be used to safeguard specific annotations or highlights that provide critical context.

Sometimes, you need to be able to modify certain shapes in certain protected worksheets, in which case, you need to unlock these shapes. This article will introduce in detail how to lock and unlock specified shapes.

## **How to Lock Shapes to Protect Them in Excel**

Here's how you can lock cells in Microsoft Excel:

1. Open Your Excel File: Open the Excel file that contains the shapes you want to lock.

1. Select the Shape: Click on the shape you want to lock. You can also select multiple shapes by holding down the Ctrl key and clicking on each shape.

1. Open the Format Shape Pane: Right-click on the selected shape(s) and choose "Size and Properties." Alternatively, you can go to the "Format" tab on the Ribbon, and in the "Size" group, click on the dialog launcher (a small arrow) to open the "Format Shape" pane.
1. Lock the Shape: In the "Format Shape" pane, go to the "Size & Properties" tab (the icon looks like a square with arrows). Under the "Properties" section, check the box for "Locked."
<br>
<img src="1.png" width=60% />
1. Protect the Worksheet: Go to the "Review" tab on the Ribbon. Click "Protect Sheet." Set a password (optional) and choose the permissions you want to allow (e.g., selecting locked cells, formatting cells, etc.). Click "OK."
<br>
<img src="2.png" width=60% />

## **How to Lock all shapes in a specified worksheet**

To protect all shapes in a specified worksheet, use the `worksheet.protect(ProtectionType.Objects)` method, as shown in the following sample code.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Lock Shapes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;
        
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const text = "This is a test";
            const worksheet = workbook.worksheets.get(0);

            let shape = worksheet.shapes.addTextBox(1, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addRectangle(5, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addButton(9, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addOval(13, 0, 1, 0, 50, 100);
            shape.text = text;

            // Protect all shapes in the specified worksheet
            shape.worksheet.protect(ProtectionType.Objects);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shapes locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **How to Unlock specified shapes in a protected worksheet**

To unlock a specified shape in a protected worksheet, use `shape.isLocked`, as shown in the following sample code.

Note: `shape.isLocked` is meaningful only when the worksheet is protected.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Unlock Shape</title>
    </head>
    <body>
        <h1>Unlock Shape Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get protected worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the specified shape to be unlocked
            const shape = worksheet.shapes.get("TextBox 1");

            if (!shape) {
                resultDiv.innerHTML = '<p style="color: red;">Shape "TextBox 1" not found.</p>';
                return;
            }

            // Unlock the specified shape
            if (!worksheet.protection.allowEditingObject && shape.isLocked) {
                shape.isLocked = false;
            }

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'UnLocked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape unlocked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```