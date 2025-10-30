---
title: Zugriff auf das Textfeld nach Namen mit JavaScript via C++
linktitle: Greifen Sie auf die Textbox über den Namen zu
type: docs
weight: 230
url: /de/javascript-cpp/access-the-text-box-by-the-name/
description: Lernen Sie, wie Sie mit Aspose.Cells for JavaScript via C++ auf ein Textfeld nach Name aus der Sammlung zugreifen. 
---

##Greifen Sie über den Namen auf die Textbox zu

 Früher wurden Textfelder anhand ihres Index aus der [**Worksheet.textBoxes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#textBoxes--)-Sammlung zugegriffen, jetzt können Sie auch auf das Textfeld nach Name aus dieser Sammlung zugreifen. Dies ist eine bequeme und schnelle Methode, um auf Ihr Textfeld zuzugreifen, wenn Sie bereits seinen Namen kennen.

Der folgende Beispielcode erstellt zunächst eine Textbox und weist ihr einen Text und einen Namen zu. Anschließend greifen wir in den nächsten Zeilen auf dieselbe Textbox anhand ihres Namens zu und drucken ihren Text aus.

### JavaScript-Code zum Zugriff auf das Textfeld nach Name

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TextBox Example</title>
    </head>
    <body>
        <h1>TextBox Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const sheet = workbook.worksheets.get(0);

            const idx = sheet.textBoxes.add(10, 10, 10, 10);

            const tb1 = sheet.textBoxes.get(idx);
            tb1.name = "MyTextBox";
            tb1.text = "This is MyTextBox";

            const tb2 = sheet.textBoxes.get("MyTextBox");

            console.log(tb2.text);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">TextBox added. Text from named TextBox: ${tb2.text}</p>`;
        });
    </script>
</html>
```

### Von der Beispiellösung generierte Konsolenausgabe



{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
