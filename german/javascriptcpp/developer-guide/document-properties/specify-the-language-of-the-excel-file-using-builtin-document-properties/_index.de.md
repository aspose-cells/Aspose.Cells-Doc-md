---
title: Sprache der Excel Datei mit BuiltIn Document Properties in JavaScript via C++ angeben
linktitle: Festlegen der Sprache der Excel Datei unter Verwendung eingebauter Dokumenteigenschaften
type: docs
weight: 30
url: /de/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **Mögliche Verwendungsszenarien**

Sie können die Sprache einer Excel-Datei ändern, indem Sie mit der rechten Maustaste auf die Datei klicken, dann Eigenschaften > Details auswählen und das Feld Sprache bearbeiten. Verwenden Sie die Eigenschaft [**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--), um sie programmatisch mit Aspose.Cells for JavaScript via C++ APIs zu ändern.

## **Festlegen der Sprache der Excel-Datei unter Verwendung eingebauter Dokumenteigenschaften**

Der folgende Beispielcode erstellt eine Arbeitsmappe und ändert die eingebaute Dokumenteigenschaft namens Sprache. Bitte sehen Sie sich die [Ausgabedatei](64716891.xlsx) und den Screenshot an, der das geänderte Sprachfeld mit der [**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--)-Eigenschaft zeigt.

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Language Using BuiltInDocumentProperties</h1>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Create workbook object.
            const wb = new Workbook();

            // Access built-in document property collection.
            const bdpc = wb.builtInDocumentProperties;

            // Set the language of the Excel file.
            bdpc.language = "German, French";

            // Save the workbook in xlsx format.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Language set successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
