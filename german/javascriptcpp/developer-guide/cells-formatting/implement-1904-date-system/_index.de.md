---
title: Implementieren Sie das 1904 Datumsystem mit JavaScript über C++
description: Aspose.Cells ist eine JavaScript Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Sie unterstützt die Implementierung des 1904 Datumsystems, das es Benutzern ermöglicht, auf der Grundlage des Datums 1. Januar 1904 zu berechnen und zu formatieren. Dieser Artikel beschreibt, wie man das 1904 Datumsystem mit der Aspose.Cells Bibliothek implementiert.
keywords: Aspose.Cells, 1904 Datumsystem, Tabellenkalkulation, Berechnung, Formatierung, JavaScript über C++
type: docs
weight: 7000
url: /de/javascript-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel unterstützt zwei Datumsysteme: das 1900-Datumsystem (das Standard-Datumsystem, das in Excel für Windows implementiert ist) und das 1904-Datumsystem. Das 1904-Datumsystem wird normalerweise verwendet, um die Kompatibilität mit Macintosh-Excel-Dateien herzustellen und ist das Standard-System, wenn Sie Excel für Macintosh verwenden. Sie können das 1904-Datumsystem für Excel-Dateien mithilfe von Aspose.Cells for JavaScript über C++ einstellen. 

{{% /alert %}} 

Um das 1904-Datensystem in Microsoft Excel zu implementieren (zum Beispiel in Microsoft Excel 2003):

1. Wählen Sie im **Extras**-Menü die Option **Optionen** und wählen Sie den Tab **Berechnung**.
1. Wählen Sie die Option **1904-Datensystem** aus.
1. Klicken Sie auf **OK**.

|**Auswählen des 1904-Datensystems in Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

Sehen Sie sich den folgenden Beispielcode an, wie Sie dies mit Aspose.Cells-APIs erreichen können.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Enable 1904 Date System</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement 1904 date system
            workbook.settings.date1904 = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">1904 date system enabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
