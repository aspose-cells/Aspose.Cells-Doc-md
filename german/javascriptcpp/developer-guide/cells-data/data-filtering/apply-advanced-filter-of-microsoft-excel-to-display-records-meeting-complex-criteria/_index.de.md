---
title: Anwendung des erweiterten Filters von Microsoft Excel zur Anzeige von Datensätzen, die komplexe Kriterien erfüllen
type: docs
weight: 280
url: /de/javascript-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Lernen Sie, wie Sie mit dem Aspose.Cells for JavaScript via C++ API die erweiterte Filterfunktion von Microsoft Excel für die Anzeige von Datensätzen mit komplexen Kriterien anwenden.
keywords: Erweiterten Filter JavaScript anwenden via C++, Erweiterten Filter JavaScript setzen via C++, Erweiterten Filter JavaScript hinzufügen via C++, Erweiterten Filter JavaScript erstellen via C++, Wie man einen erweiterten Filter zu einem Bereich JavaScript via C++ hinzufügt
---

## **Mögliche Verwendungsszenarien**  

Microsoft Excel ermöglicht es, *Erweiterte Filter* auf Tabellenblatt-Daten anzuwenden, um Datensätze zu filtern, die komplexen Kriterien entsprechen. Sie können den erweiterten Filter in Excel über den Befehl *Daten > Erweitert* ausführen, wie im Screenshot gezeigt.  

![todo:image_alt_text](1.png)  

Das Aspose.Cells for JavaScript via C++ ermöglicht auch die Anwendung des erweiterten Filters mittels der [**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-)-Methode. Genau wie Microsoft Excel akzeptiert es die folgenden Parameter.  

**isFilter**  

Gibt an, ob die Liste am gleichen Ort gefiltert wird.  

**listRange**  

Der Listenbereich.  

**criteriaRange**  

Der Kriterienbereich.  

**copyTo**  

Der Bereich, in den Daten kopiert werden.  

**uniqueRecordOnly**  

Nur eindeutige Zeilen anzeigen oder kopieren.  

## **Erweiterten Filter von Microsoft Excel anwenden, um Datensätze anhand komplexer Kriterien anzuzeigen**  

Der folgende Beispielcode wendet den erweiterten Filter auf die [Beispiel-Excel-Datei](48496692.xlsx) an und erstellt die [Ausgabe-Excel-Datei](48496691.xlsx). Der Screenshot zeigt beide Dateien zum Vergleich. Wie im Screenshot sichtbar ist, wurden die Daten innerhalb der Ausgabedatei entsprechend komplexer Kriterien gefiltert.  

![todo:image_alt_text](2.png)  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Advanced Filter Example</title>
    </head>
    <body>
        <h1>Advanced Filter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Advanced Filter</button>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (sampleAdvancedFilter.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const wb = new Workbook(new Uint8Array(arrayBuffer));

            const ws = wb.worksheets.get(0);

            // Apply advanced filter on range A5:D19 with criteria A1:D2, filter in place, include all records (not unique)
            ws.advanced_Filter(true, "A5:D19", "A1:D2", "", false);

            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAdvancedFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Advanced filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
