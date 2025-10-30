---
title: Optimierung des Speicherverbrauchs beim Arbeiten mit großen Dateien und großen Datensätzen
type: docs
weight: 110
url: /de/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Beim Erstellen eines Arbeitsmappen mit großen Datensätzen oder beim Lesen einer großen Microsoft Excel-Datei ist die Gesamtmenge an RAM, die der Prozess benötigt, immer ein Anliegen. Es gibt Maßnahmen, die zur Bewältigung der Herausforderung angepasst werden können. Aspose.Cells bietet einige relevante Optionen und API-Aufrufe, um den Speicherverbrauch zu verringern, zu reduzieren und zu optimieren. Außerdem kann es dem Prozess helfen, effizienter zu arbeiten und schneller zu laufen.

Verwenden Sie die [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)-Option, um den Speicherplatz für Zellendaten zu optimieren und die Gesamtspeicherkosten zu senken. Beim Erstellen großer Datensätze für Zellen kann dies im Vergleich zur Verwendung der Standardeinstellung [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) eine bestimmte Menge an Speicherplatz sparen.

{{% /alert %}}

## **Speicheroptimierung**

 Das folgende Beispiel zeigt, wie man bei der Arbeit mit großen Daten in Aspose.Cells for JavaScript über C++ den Speicherverbrauch optimieren kann.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Optimize Memory Usage Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, MemorySetting } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file or leave empty to create a new one.</p>';
                // Allow creating a new workbook even if no file selected; return only if user explicitly requires file.
            }

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // apply the setting to existing "Sheet1"
            workbook.worksheets.get(0).cells.memorySetting = MemorySetting.MemoryPreference;

            // apply the setting globally
            workbook.settings.memorySetting = MemorySetting.MemoryPreference;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Memory settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Vorsicht**

Die Standardeinstellung [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) wird für alle Versionen angewendet. Für einige Situationen, wie das Erstellen einer Arbeitsmappe mit einem großen Datensatz für Zellen, kann die Option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) den Speicherplatz optimieren und die Speicherkosten für die Anwendung senken. Diese Option kann jedoch die Leistung in einigen speziellen Fällen wie folgt beeinträchtigen.

1. **Zufälliger und wiederholter Zugriff auf Zellen**: Die effizienteste Sequenz für den Zugriff auf die Zellensammlung ist Zelle für Zelle in einer Zeile und dann Zeile für Zeile. Insbesondere wenn Sie Zeilen/Zellen über den Enumerator, der von [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection) und [**Row**](https://reference.aspose.com/cells/javascript-cpp/row) erworben wurde, abrufen, wird die Leistung mit [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) maximiert.
1. **Einfügen & Löschen von Zellen & Zeilen**: Bitte beachten Sie, dass bei vielen Einfüge-/Löschvorgängen für Zellen/Zeilen die Leistungseinbußen für den [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)-Modus im Vergleich zum [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)-Modus spürbar sein werden.
1. **Arbeiten mit verschiedenen Zellentypen**: Wenn die meisten Zellen Zeichenfolgenwerte oder Formeln enthalten, wird der Speicherverbrauch dem des [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)-Modus entsprechen. Wenn jedoch viele leere Zellen vorhanden sind oder Zellwerte numerisch, boolesch usw. sind, wird die Option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) eine bessere Leistung bieten.
