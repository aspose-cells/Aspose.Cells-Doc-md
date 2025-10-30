---
title: Erweiterte Sicherheitseinstellungen seit Excel XP mit JavaScript über C++
linktitle: Erweiterte Schutzeinstellungen seit Excel XP
type: docs
weight: 30
url: /de/javascript-cpp/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

Seit der Veröffentlichung von Excel 2002 oder XP hat Microsoft viele erweiterte Schutzeinstellungen hinzugefügt.

{{% /alert %}}


## **Einführung**

Diese Schutzeinstellungen beschränken oder erlauben Benutzern:

- Zeilen oder Spalten löschen.
- Inhalte, Objekte oder Szenarien bearbeiten.
- Zellen, Reihen oder Spalten formatieren.
- Zeilen, Spalten oder Hyperlinks einfügen.
- Gesperrte oder ungesperrte Zellen auswählen.
- Pivot-Tabellen verwenden und vieles mehr.

Aspose.Cells for JavaScript über C++ unterstützt alle erweiterten Sicherheitseinstellungen, die von Excel XP oder späteren Versionen angeboten werden.

### **Erweiterte Schutzeinstellungen mit Excel XP und späteren Versionen verwenden**

Um die Schutzeinstellungen in Excel XP anzuzeigen:

1. Wählen Sie im **Extras**-Menü **Schutz** und danach **Arbeitsblatt schützen** aus. Es wird ein Dialogfeld angezeigt.

Um die verfügbaren Schutzeinstellungen in Excel 2016 anzuzeigen:

1. Wählen Sie im **Datei**-Menü **Arbeitsmappe schützen** und danach **Aktuelles Blatt schützen** aus.
1. Wählen Sie **Arbeitsblatt schützen** im **Überprüfen**-Menü aus.

Die oben genannten Schritte zeigen ein Dialogfeld, in dem Sie Arbeitsblattfunktionen zulassen, einschränken oder ein Passwort für das Arbeitsblatt festlegen können.

### **Erweiterte Sicherheitseinstellungen mit Aspose.Cells for JavaScript über C++**

Aspose.Cells for JavaScript über C++ unterstützt alle erweiterten Sicherheitseinstellungen.

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), bereit, die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) repräsentiert.

Die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) stellt die Eigenschaft [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) bereit, die verwendet wird, um diese erweiterten Schutzeinstellungen anzuwenden. Die Eigenschaft [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) ist tatsächlich ein Objekt der Klasse [**Protection**](https://reference.aspose.com/cells/javascript-cpp/protection), das mehrere boolesche Eigenschaften zum Deaktivieren oder Aktivieren von Beschränkungen umschließt.

Unten finden Sie eine kleine Beispielanwendung. Es öffnet eine Excel-Datei und verwendet die meisten von Excel XP und späteren Versionen unterstützten erweiterten Schutzeinstellungen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Worksheet Protection Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const protection = worksheet.protection;

            // Restricting users to delete columns of the worksheet
            protection.allowDeletingColumn = false;

            // Restricting users to delete row of the worksheet
            protection.allowDeletingRow = false;

            // Restricting users to edit contents of the worksheet
            protection.allowEditingContent = false;

            // Restricting users to edit objects of the worksheet
            protection.allowEditingObject = false;

            // Restricting users to edit scenarios of the worksheet
            protection.allowEditingScenario = false;

            // Restricting users to filter
            protection.allowFiltering = false;

            // Allowing users to format cells of the worksheet
            protection.allowFormattingCell = true;

            // Allowing users to format rows of the worksheet
            protection.allowFormattingRow = true;

            // Allowing users to insert columns in the worksheet
            protection.allowFormattingColumn = true;

            // Allowing users to insert hyperlinks in the worksheet
            protection.allowInsertingHyperlink = true;

            // Allowing users to insert rows in the worksheet
            protection.allowInsertingRow = true;

            // Allowing users to select locked cells of the worksheet
            protection.allowSelectingLockedCell = true;

            // Allowing users to select unlocked cells of the worksheet
            protection.allowSelectingUnlockedCell = true;

            // Allowing users to sort
            protection.allowSorting = true;

            // Allowing users to use pivot tables in the worksheet
            protection.allowUsingPivotTable = true;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protection settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Bitte rufen Sie beim Verwenden der [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--)-Eigenschaft die [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-)-Methode der [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse nicht auf. Speichern Sie die Datei außerdem im Excel97To2003- oder Xlsx-Format, da die erweiterten Schutzeinstellungen nur von Excel XP und späteren Versionen unterstützt werden.

{{% /alert %}}

### **Problem mit Zellsperre**

Wenn Sie Nutzer daran hindern möchten, Zellen zu bearbeiten, müssen die Zellen vor der Anwendung der Schutz-Einstellungen gesperrt werden. Andernfalls können die Zellen auch bei aktiviertem Schutz bearbeitet werden. In Microsoft Excel XP können Zellen über den folgenden Dialog gesperrt werden:

|**Dialog zum Sperren von Zellen in Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Es ist auch möglich, Zellen mit der Aspose.Cells-API zu sperren. Jede Zelle kann eine [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Formatierung erhalten, die eine boolesche Eigenschaft [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) enthält. Setzen Sie die [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--)-Eigenschaft auf **true** oder **false**, um die Zelle zu sperren oder zu entsperren.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Lock cell A1 by setting the style property
            const cell = worksheet.cells.get("A1");
            cell.style.isLocked = true;

            // Protect the sheet now.
            worksheet.protect(ProtectionType.All);

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
