---
title: Anzeige von Aufzählungszeichen durch Setzen des Zellenwerts mit HTML
type: docs
weight: 130
url: /de/javascript-cpp/display-bullets-by-setting-cell-value-using/
description: Bullets in Excel Zellen mit HTML hinzufügen, einfach zu verwendendes Aspose.Cells for JavaScript via C++ API.
keywords: Aufzählungszeichen in Excel mit JavaScript via C++ hinzufügen, Aufzählungszeichen in Excel mit JavaScript via C++ anzeigen, Aufzählungszeichen in Excel mit HTML in JavaScript hinzufügen, Aufzählungszeichen in Excel mit HTML in JavaScript anzeigen, Aufzählungszeichen in Excel mit HTML in JavaScript hinzufügen via C++
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Anzeige von Punkten mit HTML-Code. Dieser Artikel erklärt, wie man Punkte durch Setzen des Zellwerts mit HTML anzeigt. Wir verwenden die Methode [**Cell.htmlString(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-), um den Zellwert mit unserem HTML festzulegen.

{{% /alert %}}

## JavaScript-Code zur Anzeige von Aufzählungszeichen durch Setzen des Zellwerts mit HTML

Der folgende Code verwendet den HTML-Code, um den Zellwert festzulegen. Sobald Sie diesen Code ausführen, erhalten Sie die Ausgabe wie im Bild unten.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Bullets In Cells</title>
    </head>
    <body>
        <h1>Bullets In Cells Example</h1>
        <p>Select an existing Excel file to modify or leave empty to create a new workbook.</p>
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

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set the HTML string (converted from setHtmlString -> htmlString property)
            cell.htmlString = "<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'>Text 1 </font><font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font><font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 2 </font><font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font><font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 3 </font><font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font><font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 4 </font>";

            // Auto fit the Columns
            worksheet.autoFitColumns();

            // Save the workbook to a Blob and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'BulletsInCells_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File: BulletsInCells_out.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## Ausgabe, die vom Beispielcode generiert wurde

Der folgende Screenshot zeigt die Ausgabe des obigen Beispielcodes.

![todo:image_alt_text](display-bullets-by-setting-cell-value-using-html_1.png)
