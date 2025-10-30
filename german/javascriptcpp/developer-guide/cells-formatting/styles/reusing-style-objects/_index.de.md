---
title: Wiederverwendung von Style Objekten
linktitle: Wiederverwendung von Style Objekten
description: In Aspose.Cells for JavaScript via C++, durch Erstellung und Verwendung wiederverwendbarer Stilobjekte, können Sie die Stilverwaltung vereinfachen und die Code Effizienz verbessern. Unser Leitfaden hilft Ihnen, die Vorteile wiederverwendbarer Stilobjekte zu nutzen und sie in Ihrer Anwendung umzusetzen.
keywords: Aspose.Cells for JavaScript via C++, Wiederverwendung von Stilobjekten, Stilverwaltung, Code Effizienz, Wiederverwendbare Stile, Anwendungsentwicklung, API Referenz, Beispielcode, Download, Support.
type: docs
weight: 3000
url: /de/javascript-cpp/reusing-style-objects/
---

{{% alert color="primary" %}}  
Die Wiederverwendung von Style-Objekten kann Speicherplatz sparen und ein Programm schneller machen.  
{{% /alert %}}  

Um einige Formatierungen auf einen großen Zellenbereich in einem Arbeitsblatt anzuwenden:

1. Erstellen Sie ein Style-Objekt.
1. Geben Sie die Attribute an.
1. Wenden Sie den Style auf die Zellen im Bereich an.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Font</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            // Creating a new workbook (empty)
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            const styleObject = workbook.createStyle();
            styleObject.font.color = Color.Red;
            styleObject.font.name = "Times New Roman";
            cell1.style = styleObject;
            cell2.style = styleObject;

            // Put the values inside the cell
            cell1.value = "Hello World!";
            cell2.value = "Hello World!!";

            // Save to XLSX
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleOutput_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}  
Da der Ansatz [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) / [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) viel weniger Speicher benötigt und effizient ist, wurde die ältere Eigenschaft Cell.style mit der Freigabe von Aspose.Cells 7.1.0 entfernt.  
{{% /alert %}}
