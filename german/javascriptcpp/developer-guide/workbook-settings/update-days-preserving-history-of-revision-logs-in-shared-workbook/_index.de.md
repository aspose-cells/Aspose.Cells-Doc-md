---
title: Daten in freigegebenen Arbeitsmappen unter Beibehaltung der Änderungshistorie mit JavaScript via C++ aktualisieren
linktitle: Aktualisieren von Tagen unter Beibehaltung des Verlaufprotokolls in einer freigegebenen Arbeitsmappe
type: docs
weight: 80
url: /de/javascript-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Erfahren Sie, wie Sie die Tage zum Beibehalten der Änderungsprotokolle in freigegebenen Arbeitsmappen mit Aspose.Cells for JavaScript via C++ aktualisieren.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie eine Arbeitsmappe freigeben, erscheint die Option ***Änderungshistorie für N Tage aufbewahren***, wie im folgenden Screenshot gezeigt. Sie können die Anzahl der Tage zur Beibehaltung der Historie mit Aspose.Cells for JavaScript via C++ mit der Eigenschaft [**WorksheetCollection.daysPreservingHistory**](https://reference.aspose.com/cells/javascript-cpp/revisionlogcollection/#daysPreservingHistory--) aktualisieren.

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Aktualisieren von Tagen unter Beibehaltung des Verlaufprotokolls in einer freigegebenen Arbeitsmappe**

Der folgende Beispielcode erstellt eine leere Arbeitsmappe, teilt sie dann und aktualisiert die Revisionsprotokolle, um den Verlauf 7 Tage lang zu speichern, was normalerweise 30 Tage beträgt. Bitte sehen Sie die [Ausgabedatei Excel](60489773.xlsx), die vom Code erstellt wurde, als Referenz an.

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Shared Workbook</title>
    </head>
    <body>
        <h1>Shared Workbook - DaysPreservingHistory Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Shared Workbook</button>
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
            // Create empty workbook
            const workbook = new Workbook();

            // Share the workbook
            workbook.settings.shared = true;

            // Update DaysPreservingHistory of RevisionLogs
            workbook.worksheets.revisionLogs.daysPreservingHistory = 7;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputShared_DaysPreservingHistory.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and configured. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
