---
title: Gemeinsame Arbeitsmappe mit Aspose.Cells for JavaScript via C++ erstellen
linktitle: Freigegebene Arbeitsmappe mit Aspose.Cells erstellen
type: docs
weight: 40
url: /de/javascript-cpp/create-shared-workbook-with-aspose-cells/
description: Erfahren Sie, wie Sie eine gemeinsame Arbeitsmappe mit Aspose.Cells for JavaScript via C++ erstellen.
---

## **Mögliche Verwendungsszenarien**  

Microsoft Excel ermöglicht es, die Arbeitsmappe wie im folgenden Screenshot zu teilen. Wenn Sie die Arbeitsmappe teilen, können mehr als ein Benutzer die Arbeitsmappe im Netzwerk bearbeiten. Aspose.Cells for JavaScript via C++ ermöglicht die Erstellung einer geteilten Arbeitsmappe mit der [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--) Eigenschaft.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Gemeinsame Arbeitsmappe mit Aspose.Cells erstellen**  

Der folgende Beispielcode erstellt ein geteiltes Arbeitsbuch, indem er die [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--)-Eigenschaft auf **true** setzt. Wenn Sie die [Ausgabedatei](55541786.xlsx) in Microsoft Excel öffnen, sehen Sie **Shared** mit dem Namen der Arbeitsmappe, wie in diesem Screenshot gezeigt.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Shared Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="createShared" disabled>Create Shared Workbook</button>
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
            document.getElementById('createShared').disabled = false;
        });

        document.getElementById('createShared').addEventListener('click', async () => {
            const wb = new Workbook();

            // Share the Workbook (converted getter/setter to property)
            wb.settings.shared = true;

            // Save the Shared Workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Shared Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared workbook created successfully! Click the download link to save the file.</p>';
        });
    </script>
</html>
```
