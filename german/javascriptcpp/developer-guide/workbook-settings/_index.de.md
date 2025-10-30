---
title: Verwalten Sie die Einstellungen von Excel Tabellendateien mit JavaScript über C++
linktitle: Arbeitsmappeneinstellungen
type: docs
weight: 185
url: /de/javascript-cpp/workbook-settings/
description: Verwalten Sie die Einstellungen von Excel Dateien mit Aspose.Cells for JavaScript über C++.
---

## **Überblick über Arbeitsmappen-Einstellungen**
Die Arbeit mit Excel-Dateien umfasst verschiedene Einstellungen, die programmatisch mit Aspose.Cells for JavaScript über C++ manipuliert werden können. Dieses Dokument beschreibt, wie diese Einstellungen effektiv verwaltet werden können.

## **Mögliche Verwendungsszenarien**
Die folgenden Szenarien zeigen, wann es erforderlich sein könnte, Arbeitsmappen-Einstellungen zu verwalten:
- Anzeigeoptionen anpassen
- Berechnungsmodus einstellen
- Parameter für die Seitenkonfiguration festlegen

## **Verwaltung der Arbeitsmappeneinstellungen mit Aspose.Cells for JavaScript über C++**
Dieses Beispiel zeigt, wie man Arbeitsmappen-Einstellungen wie Berechnungsoptionen und Anzeigeeinstellungen verwaltet.

1. Erstellen Sie eine neue Arbeitsmappe oder laden Sie eine bestehende.
2. Ändern Sie die Arbeitsmappen-Einstellungen entsprechend Ihren Anforderungen.
3. Speichern Sie die Arbeitsmappe, um die Änderungen zu sichern.

### **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Workbook Settings Example</h1>
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
            // Create a new workbook
            const workbook = new Workbook();

            // Access the settings of the workbook
            const settings = workbook.settings;
            settings.calculationMode = 1; // Manual calculation

            // Display options
            settings.showGridLines = false; // Disable gridlines

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkbookSettingsExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Wichtige Eigenschaften und Methoden der Arbeitsmappen-Einstellungen**
Aspose.Cells for JavaScript über C++ bietet eine Reihe von Eigenschaften und Methoden, um Arbeitsmappeneinstellungen anzupassen:
- **Workbook.settings**: Greift auf die Einstellungen der Arbeitsmappe zu.
- **Settings.calculationMode**: Setzt den Berechnungsmodus für die Arbeitsmappe.
- **Settings.showGridLines**: Aktiviert oder deaktiviert die Gitternetzlinien auf der Anzeige.

## **Fazit**
Die Verwaltung der Arbeitseinstellungen in Aspose.Cells for JavaScript über C++ ist unkompliziert und bietet zahlreiche Optionen, um das Verhalten von Excel-Dateien anzupassen. Durch die Nutzung der verfügbaren Einstellungen können Sie die Arbeitsmappe an Ihre spezifischen Anforderungen anpassen.
