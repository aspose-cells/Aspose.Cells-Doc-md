---
title: Excel TextBox veya Shape in Karakter Boşluğunu JavaScript ve C++ kullanarak değiştirme
linktitle: Excel Metin Kutusu veya Şeklin Karakter Boşluğunu Değiştirme
type: docs
weight: 280
url: /tr/javascript-cpp/change-character-spacing-of-excel-textbox-or-shape/
description: C++ kullanarak Aspose.Cells for JavaScript ile Excel metin kutuları veya şekillerinin karakter boşluğunu değiştirin. 
---

{{% alert color="primary" %}}

Bir Excel metin kutusu veya şeklin karakter aralığını [**TextOptions.spacing**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#spacing--) özelliği kullanarak değiştirebilirsiniz.

{{% /alert %}}

Aşağıdaki örnek kod, Excel dosyasındaki metin kutusunun karakter boşluğunu 4 nokta olarak değiştirir ve sonra kaydeder.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access your text box which is also a shape object from shapes collection
            const shape = workbook.worksheets.get(0).shapes.get(0);

            // Access the first font setting object via richFormattings property
            const fontSetting = shape.richFormattings[0];

            // Set the character spacing to point 4
            fontSetting.textOptions.spacing = 4;

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeTextBoxOrShapeCharacterSpacing.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Character spacing updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // Creating a workbook
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a textbox to the worksheet
            const shape = worksheet.shapes.addTextBox(5, 5, 100, 50);
            shape.textBody.text = "Hello World!";

            // Change character spacing
            shape.textBody.paragraphs.get(0).portions.get(0).fontSetting.textOptions.spacing = 4;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ChangedCharacterSpacing.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
