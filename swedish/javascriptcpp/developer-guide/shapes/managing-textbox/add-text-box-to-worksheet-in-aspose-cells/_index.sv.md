---
title: Hur man lägger till/infogar TextBox i Arbetsblad med JavaScript via C++
linktitle: Lägg till textfält i arbetsbladet
type: docs
weight: 10
url: /sv/javascript-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Hur man lägger till/infogar TextBox i Arbetsblad i Aspose.Cells for JavaScript via C++.
keywords: lägg till/infoga Text Box TextBox Arbetsblad Excel Aspose JavaScript via C++
---

## Lägg till textfält i arbetsbladet i Excel

I Excel-programmet (version 07 och senare) finns två platser där du kan infoga text lådor. En i "infoga-former", den andra är på högra sidan av toppmenyn för "Infoga"-alternativet.

### metod ett:

![1](1.png)

### metod två:

![2](2.png)

## Hur man skapar

Du kan skapa textfält med horisontell eller vertikal text.

- Välj motsvarande alternativ (horisontell eller vertikal)
- Vänsterklicka på sidan
- Håll ner vänsterknappen och dra en distans på sidan
- Släpp vänsterknappen

Nu har du ett textfält.

## Lägg till Text Box i Arbetsblad i Aspose.Cells for JavaScript via C++

När du behöver massinlägga TextBox i kalkbladet är den manuella insättningsmetoden självklart ett katastrof. Om detta stör dig tror jag att detta dokument hjälper dig. [Aspose.Cells](https://products.aspose.com/cells/) ger dig ett API för att enkelt göra bulkinsättningar i din kod.

Följande provkod skapar en textruta.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add TextBox</title>
    </head>
    <body>
        <h1>Add TextBox to Workbook</h1>
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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the TextBox to the worksheet
            sheet.textBoxes.add(6, 10, 100, 200);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">TextBox added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Du kommer att få en fil som liknar [resultatfilen](result.xlsx). I filen kommer du se följande:

![](52449.png)
