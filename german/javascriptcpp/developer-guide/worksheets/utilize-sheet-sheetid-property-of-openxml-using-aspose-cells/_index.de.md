---
title: Verwenden Sie die Sheet.SheetId Eigenschaft von OpenXml mit Aspose.Cells for JavaScript über C++
linktitle: Verwenden Sie die Sheet.SheetId Eigenschaft von OpenXml mit Aspose.Cells
type: docs
weight: 200
url: /de/javascript-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Dieser Artikel zeigt, wie man die Sheet.SheetId Eigenschaft von OpenXml mit Excel Manipulation und Aspose.Cells for JavaScript programmatisch über C++ nutzt.
keywords: Tabellenblatt ID Eigenschaft von OpenXML JavaScript via C++, Tabellenblatt ID Excel Arbeitsblatt JavaScript via C++
---

## **Mögliche Verwendungsszenarien**

*Sheet.SheetId*-Eigenschaft ist im *DocumentFormat.OpenXml.Spreadsheet*-Modul enthalten und Teil von OpenXml. Diese Eigenschaft und ihr Wert sind in *workbook.xml* sichtbar, wie im folgenden Screenshot gezeigt. Aspose.Cells bietet die entsprechende Eigenschaft als [**Worksheet.tabId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#tabId--).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Nutzen Sie die Sheet.SheetId-Eigenschaft von OpenXml mit Aspose.Cells for JavaScript via C++**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](51740716.xlsx), liest ihre Tabellen- oder Registerkarten-ID, weist ihr dann eine neue Registerkarten-ID zu und speichert sie als [Ausgabe-Excel-Datei](51740717.xlsx). Bitte sehen Sie sich auch die Konsolenausgabe des untenstehenden Codes als Referenz an.

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sheet Id Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Print its Sheet or Tab Id on console and show in page
            console.log("Sheet or Tab Id: " + ws.tabId);
            resultDiv.innerHTML = `<p>Original Sheet or Tab Id: ${ws.tabId}</p>`;

            // Change Sheet or Tab Id
            ws.tabId = 358;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSheetId.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += `<p style="color: green;">Sheet Id changed to ${ws.tabId}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

## **Konsolenausgabe**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
