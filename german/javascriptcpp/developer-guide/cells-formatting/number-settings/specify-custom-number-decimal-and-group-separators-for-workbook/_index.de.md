---
title: Benutzerdefinierte Dezimal und Gruppentrennzeichen für Arbeitsmappe festlegen
linktitle: Benutzerdefinierte Dezimal und Gruppentrennzeichen für Arbeitsmappe festlegen
type: docs
weight: 110
url: /de/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Ändern Sie Dezimal und Gruppentrennzeichen in Excel mit Aspose.Cells for JavaScript via C++.
keywords: Geben Sie benutzerdefinierte Dezimal und Gruppentrennzeichen in Excel JavaScript via C++ an, ändern Sie Dezimal und Gruppentrennzeichen in Excel JavaScript via C++, ändern Sie Dezimal und Gruppentrennzeichen in Excel JavaScript via C++
---

{{% alert color="primary" %}}

In Microsoft Excel können Sie die benutzerdefinierten Dezimal- und Tausendertrennzeichen festlegen, anstatt die Systemtrennzeichen aus den **Erweiterten Excel-Optionen** zu verwenden, wie im untenstehenden Screenshot gezeigt.

Aspose.Cells stellt die Methoden [**WorkbookSettings.numberDecimalSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberDecimalSeparator-string-) und [**WorkbookSettings.numberGroupSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberGroupSeparator-string-) zum Festlegen der benutzerdefinierten Trennzeichen für die Formatierung/Analyse von Zahlen bereit.

{{% /alert %}}

## **Benutzerdefinierte Trennzeichen mit Microsoft Excel festlegen**

Der folgende Screenshot zeigt die **Erweiterten Excel-Optionen** und hebt den Abschnitt hervor, um die **Benutzerdefinierten Trennzeichen** festzulegen.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Benutzerdefinierte Trennzeichen mit Aspose.Cells for JavaScript via C++ spezifizieren**

Der folgende Beispielcode verdeutlicht, wie die benutzerdefinierten Trennzeichen mithilfe der Aspose.Cells-API festgelegt werden. Es legt die benutzerdefinierten Dezimal- und Gruppentrennzeichen als Punkt und Leerzeichen fest.

### JavaScript-Code zum Festlegen benutzerdefinierter Dezimal- und Gruppentrennzeichen bei Nummern

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Custom Number Separator Example</h1>
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

            // Load workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify custom separators
            workbook.settings.numberDecimalSeparator = '.';
            workbook.settings.numberGroupSeparator = ' ';

            const worksheet = workbook.worksheets.get(0);

            // Set cell value
            const cell = worksheet.cells.get("A1");
            cell.value = 123456.789;

            // Set custom cell style
            const style = cell.style;
            style.custom = "#,##0.000;[Red]#,##0.000";
            cell.style = style;

            worksheet.autoFitColumns();

            // Save workbook as pdf
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomSeparator_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
