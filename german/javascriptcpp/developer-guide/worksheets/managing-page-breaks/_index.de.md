---
title: seitenumbrüche mit JavaScript über C++ verwalten
linktitle: Verwalten von Seitenumbrüchen
type: docs
weight: 30
url: /de/javascript-cpp/managing-page-breaks/
description: Dieser Artikel enthält Beispielcode und erklärt, wie Sie Seitenumbrüche in Excel Arbeitsblättern programmatisch mit Aspose.Cells for JavaScript über C++ hinzufügen, löschen oder entfernen können.
keywords: Seitenumbruchfunktionalitäten mit JavaScript über C++, Seitenumbrüche in Excel mit JavaScript über C++, Seitenumbruch löschen mit JavaScript über C++, Bestimmten Seitenumbruch in JavaScript über C++ entfernen
---

{{% alert color="primary" %}}

Nach Definition ist ein Seitenumbruch eine Stelle in einem Textfluss, an der eine Seite endet und die nächste beginnt. Microsoft Excel ermöglicht es Benutzern, Seitenumbrüche in jede ausgewählte Zelle eines Arbeitsblatts einzufügen.

Der Ort der Zelle, an dem der Seitenumbruch hinzugefügt wird, die Seite endet und der Rest der Daten nach dem Seitenumbruch auf der nächsten Seite gedruckt wird, während des Druckens. Einfach ausgedrückt, teilen Seitenumbrüche Ihr Arbeitsblatt gemäß Ihren Spezifikationen in mehrere Seiten auf. Sie können auch zur Laufzeit Seitenumbrüche zu Ihren Arbeitsblättern mit Aspose.Cells hinzufügen. Aspose.Cells ermöglicht Entwicklern, zwei Arten von Seitenumbrüchen hinzuzufügen:

- Horizontaler Seitenumbruch
- Vertikaler Seitenumbruch

Im weiteren Verlauf der Diskussion werden wir beschreiben, wie Sie horizontale oder vertikale Seitenumbrüche in Ihre Arbeitsblätter mit Aspose.Cells einfügen können.

{{% /alert %}}

## **Seitenumbrüche**

Aspose.Cells for JavaScript über C++ bietet eine [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse, die eine Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse enthält eine [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden, die zur Verwaltung eines Arbeitsblatts verwendet werden.

Um die Seitenumbrüche hinzuzufügen, verwenden Sie die Eigenschaften [**worksheet.horizontalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#horizontalPageBreaks--) und [**worksheet.verticalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#verticalPageBreaks--) der Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

Die Eigenschaften [**worksheet.horizontalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#horizontalPageBreaks--) und [**worksheet.verticalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#verticalPageBreaks--) sind Sammlungen, die mehrere Seitenumbrüche enthalten können. Jede Sammlung enthält mehrere Methoden zur Verwaltung von horizontalen und vertikalen Seitenumbrüchen.

### **Seitenumbrüche hinzufügen**

Um einen Seitenumbruch in einem Arbeitsblatt hinzuzufügen, fügen Sie vertikale und horizontale Seitenumbrüche an der angegebenen Zelle ein, indem Sie die Methoden [**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/horizontalpagebreakcollection/#add-number-number-number-) und [**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/verticalpagebreakcollection/#add-number-number-number-) aufrufen. Jede **add**-Methode nimmt den Namen der Zelle, an der die Umbruchsmarkierung gesetzt werden soll.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Page Breaks Example</h1>
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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a page break at cell Y30
            worksheet.horizontalPageBreaks.add("Y30");
            worksheet.verticalPageBreaks.add("Y30");

            // Save the Excel file (Excel 97-2003 format .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingPageBreaks_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page breaks added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Im Vorschau-Modus für Seitenumbrüche oder im Druckvorschau-Modus können Sie sehen, wie diese Seitenumbrüche funktionieren.

{{% /alert %}}

### **Bestimmten Seitenumbruch entfernen**

 Um einen spezifischen Seitenumbruch zu entfernen, rufen Sie die Methoden [**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/horizontalpagebreakcollection/#removeAt-number-) und [**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/verticalpagebreakcollection/#removeAt-number-) auf. Jede **removeAt**-Methode nimmt den Index des zu entfernenden Seitenumbruchs.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Remove Specific Page Break Example</title>
    </head>
    <body>
        <h1>Remove Specific Page Break Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Removing a specific page break
            worksheet.horizontalPageBreaks.removeAt(0);
            worksheet.verticalPageBreaks.removeAt(0);

            // Saving the Excel file (Excel 97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RemoveSpecificPageBreak_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page breaks removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Wichtig zu wissen**

 Wenn Sie die Eigenschaften **fitToPages** (also [**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--) und [**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--)) in den Seiteneinrichtungsoptionen setzen, werden die Seitenumbruch-Einstellungen beeinflusst, sodass beim Drucken des Arbeitsblatts die Seitenumbrüche zwar gesetzt, aber nicht berücksichtigt werden.
