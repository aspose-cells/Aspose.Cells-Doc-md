---
title: Arbeiten mit ContentTypeProperties mit JavaScript über C++
linktitle: Arbeiten mit ContentTypeProperties
type: docs
weight: 150
url: /de/javascript-cpp/working-with-contenttypeproperties/
description: Erfahren Sie, wie Sie mit benutzerdefinierten ContentTypeProperties in Excel Dateien mit Aspose.Cells for JavaScript über C++ arbeiten.
---

Aspose.Cells bietet die [**Workbook.contentTypeProperties**](https://reference.aspose.com/cells/javascript-cpp/workbook/#contentTypeProperties--)-Methode zum Hinzufügen benutzerdefinierter ContentTypeProperties zu einer Excel-Datei. Sie können die Eigenschaft auch optional machen, indem Sie die [**ContentTypeProperty.isNillable()**](https://reference.aspose.com/cells/javascript-cpp/contenttypeproperty/#isNillable--)-Eigenschaft auf **true** setzen. Das folgende Codebeispiel demonstriert das Hinzufügen optionaler benutzerdefinierter ContentTypeProperties zu einer Excel-Datei. Das folgende Bild zeigt beide Eigenschaften, die durch den Beispielcode hinzugefügt wurden.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

Die durch den Beispielcode generierte Ausgabedatei ist als Referenz angehängt.

[Ausgabedatei](95584314.xlsx)

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Working With Content Type Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FileFormatType } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').disabled = false;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');

            // Creating a new Workbook with Xlsx format
            const workbook = new Workbook(FileFormatType.Xlsx);

            // Adding content type properties
            let index = workbook.contentTypeProperties.add("MK31", "Simple Data");
            workbook.contentTypeProperties.get(index).isNillable = false;

            index = workbook.contentTypeProperties.add("MK32", new Date().toISOString(), "DateTime");
            workbook.contentTypeProperties.get(index).isNillable = true;

            // Saving the workbook and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkingWithContentTypeProperties_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
