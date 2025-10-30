---
title: Dokumenten Version der Excel Datei mit BuiltIn Document Properties in JavaScript via C++ angeben
linktitle: Festlegen der Dokumentversion der Excel Datei unter Verwendung eingebauter Dokumenteigenschaften
type: docs
weight: 20
url: /de/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Erfahren Sie, wie Sie die Dokumentversion einer Excel Datei programmatisch mit eingebauten Dokumenteigenschaften in JavaScript via C++ angeben.
---

## **Mögliche Verwendungsszenarien**  

Sie können die **Versionsnummer** einer Excel-Datei ändern, indem Sie mit der rechten Maustaste auf die Datei klicken, Eigenschaften > Details auswählen und dann das Feld **Versionsnummer** bearbeiten. Bitte verwenden Sie die [**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--)-Eigenschaft, um sie programmatisch mit Aspose.Cells APIs zu ändern.  

## **Festlegen der Dokumentversion der Excel-Datei unter Verwendung eingebauter Dokumenteigenschaften**  

Der folgende Beispielcode erstellt eine Arbeitsmappe und ändert deren eingebauten Dokumenteigenschaften, einschließlich Titel, Autoren und Versionsnummer. Bitte sehen Sie sich die [Ausgabedatei](64716811.xlsx) und den Screenshot an, der die geänderte Versionsnummer mit der [**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--)-Eigenschaft zeigt.  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Document Version Example</h1>
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
            // Create workbook object
            const wb = new Workbook();

            // Access built-in document property collection
            const bdpc = wb.builtInDocumentProperties;

            // Set the title
            bdpc.title = "Aspose File Format APIs";

            // Set the author
            bdpc.author = "Aspose APIs Developers";

            // Set the document version
            bdpc.documentVersion = "Aspose.Cells Version - 18.3";

            // Save the workbook in xlsx format
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyDocumentVersionOfExcelFile.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and prepared for download. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
