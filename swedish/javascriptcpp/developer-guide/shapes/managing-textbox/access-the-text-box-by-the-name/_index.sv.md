---
title: Åtkomst till Textruta via Namn med JavaScript via C++
linktitle: Tillgång till textfältet genom namnet
type: docs
weight: 230
url: /sv/javascript-cpp/access-the-text-box-by-the-name/
description: Lär dig hur man får åtkomst till en textruta efter namn från samlingen i Aspose.Cells for JavaScript via C++. 
---

## Åtkomst till textlådan med namnet

Tidigare kunde textlådor nås via index från [**Worksheet.textBoxes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#textBoxes--)-samlingen, men nu kan du också få åtkomst till textlådan via dess namn i denna samling. Det är ett bekvämt och snabbt sätt att få åtkomst till din textlåda om du redan känner till dess namn.

Följande provkod skapar först en textruta och tilldelar den någon text och namn. Sedan i de följande raderna får vi åtkomst till samma textruta genom dess namn och skriver ut dess text.

### JavaScript-kod för att komma åt textrutan efter namn

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

### Konsoloutput som genereras av provkoden



{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
