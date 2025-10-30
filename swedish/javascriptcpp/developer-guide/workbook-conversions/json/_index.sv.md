---
title: JSON med JavaScript via C++
linktitle: Json
type: docs
weight: 300
url: /sv/javascript-cpp/convert-workbook-to-json/
description: Lär dig hur man konverterar Excel arbetsbok till JSON med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}
Aspose.Cells stöder konvertering av en arbetsbok till JSON (JavaScript Object Notation) fil.
{{% /alert %}}

## **Konvertera Excel-arbetsbok till JSON**

Aspose.Cells API erbjuder stöd för att konvertera kalkylblad till JSON-format. För att exportera arbetsboken till JSON, ange [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat) som andra parameter i [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) metoden. Du kan också använda [**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions) klassen för att specificera ytterligare inställningar för export av arbetsblad till JSON.

Följande kodexempel demonstrerar export av det aktiva arbetsbladet till JSON med hjälp av [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/#json) enumeration-medlem. Se koden för att konvertera [källfilen](book1.xlsx) till den [utdata JSON-filen](book1.Json) genererad av koden för referens.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Workbook to JSON</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
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

            // Save workbook as JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook converted to JSON successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [Konvertera CSV till JSON](/cells/sv/javascript-cpp/convert-csv-to-json/)
- [Konvertera-Excel-till-JSON](/cells/sv/javascript-cpp/convert-excel-to-json/)
- [Konvertera JSON till CSV](/cells/sv/javascript-cpp/convert-json-to-csv/)
- [Konvertera-JSON-till-Excel](/cells/sv/javascript-cpp/convert-json-to-excel/)
