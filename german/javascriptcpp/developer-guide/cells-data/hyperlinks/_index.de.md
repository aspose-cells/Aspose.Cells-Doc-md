---
title: Hyperlinks in Excel oder OpenOffice einfügen
linktitle: Hyperlinks verwalten
type: docs
weight: 45
url: /de/javascript-cpp/insert-hyperlinks-to-excel/
description: Wie man Hyperlinks ohne MS Excel mit der Aspose.Cells Bibliothek in eine Excel Datei in JavaScript via C++ einfügt.
keywords: Hyperlinks in Excel in JavaScript via C++ einfügen, Hyperlinks in JavaScript via C++ hinzufügen oder einfügen, Link zu einer URL in JavaScript via C++ hinzufügen oder einfügen, Link zu einer Zelle in JavaScript via C++ hinzufügen oder einfügen, Link zu einer externen Datei in JavaScript via C++ hinzufügen
---

{{% alert color="primary" %}} 

Ein Hyperlink wird verwendet, um eine Verknüpfung zwischen zwei Entitäten herzustellen. Jeder kennt die Verwendung von Hyperlinks, insbesondere auf Websites.
Mithilfe von Aspose.Cells können Entwickler verschiedene Arten von Hyperlinks in Microsoft Excel-Dateien erstellen. Dieses Thema erläutert, welche Arten von Hyperlinks von Aspose.Cells unterstützt werden und wie sie in unseren Excel-Dateien verwendet werden können.

{{% /alert %}} 

## **Hinzufügen von Hyperlinks**
Aspose.Cells ermöglicht es Entwicklern, Hyperlinks entweder über die API oder Designer-Tabellen (Tabellen, in denen Hyperlinks manuell erstellt und mit Aspose.Cells in andere Tabellen importiert werden) hinzuzufügen.

Aspose.Cells bietet die Klasse [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook) enthält eine [WorksheetCollection](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection), die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet) dargestellt. Die Klasse [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet) bietet verschiedene Methoden zum Hinzufügen unterschiedlicher Hyperlinks in Excel-Dateien.
## **Hinzufügen eines Links zu einer URL**
Die [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse enthält eine Sammlung [hyperlinks](https://reference.aspose.com/cells/javascript-cpp/worksheet/#hyperlinks-). Jedes Element in der Sammlung [hyperlinks](https://reference.aspose.com/cells/javascript-cpp/worksheet/#hyperlinks-) repräsentiert einen [Hyperlink](https://reference.aspose.com/cells/javascript-cpp/hyperlink). Fügen Sie Hyperlinks zu URLs hinzu, indem Sie die Methode [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) der Sammlung [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection) aufrufen. Die Methode [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) akzeptiert folgende Parameter:

- Zellname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Hyperlink-Bereich.
- URL, die URL-Adresse.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Hyperlink Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example (Create Workbook & Add Hyperlink)</button>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a hyperlink to a URL at "A1" cell
            worksheet.hyperlinks.add("A1", 1, 1, "http://www.aspose.com");

            // Save the Excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}} 

Im obigen Beispiel wird einem leeren Zellfeld **A1** ein Hyperlink zu einer URL hinzugefügt. In solchen Fällen, wenn eine Zelle leer ist, wird auch die URL-Adresse zu dieser leeren Zelle als ihr Wert hinzugefügt. Wenn die Zelle nicht leer ist und ein Hyperlink hinzugefügt wird, sieht der Wert der Zelle wie normaler Text aus. Um ihn wie einen Hyperlink aussehen zu lassen, wenden Sie die entsprechenden Formatierungseinstellungen auf diese Zelle an.

{{% /alert %}} 
## **Hinzufügen eines Links zu einer Zelle in derselben Datei**
Es ist möglich, Hyperlinks in die gleichen Excel-Dateien zu Zellen hinzuzufügen, indem Sie die Methode [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) der Sammlung [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection) aufrufen. Die Methode [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) funktioniert sowohl für interne als auch für externe Hyperlinks. Eine Version der Überladungsmethode nimmt die folgenden Parameter:

- Zellname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Hyperlink-Bereich.
- URL, die Adresse der Zielzelle.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Internal Hyperlink Example</h1>
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
            // Create a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            workbook.worksheets.add();

            // Obtaining the reference of the first (default) worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding an internal hyperlink to the "B3" cell of the other worksheet "Sheet2" in the same Excel file
            worksheet.hyperlinks.add("B3", 1, 1, "Sheet2!B9");

            // Saving the Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Excel file created successfully. Click the download link to save it.</p>';
        });
    </script>
</html>
```


## **Hinzufügen eines Links zu einer externen Datei**
Es ist möglich, Hyperlinks zu externen Excel-Dateien hinzuzufügen, indem Sie die Methode [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) der Sammlung [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection) aufrufen. Die Methode [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) akzeptiert folgende Parameter:

- Zellname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Hyperlink-Bereich.
- URL, die Adresse des Ziels, externen Excel-Datei.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <p>Select an optional Excel file to use its filename as the hyperlink target (or leave empty to use "book1.xls"):</p>
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
            let targetFileName = 'book1.xls';
            if (fileInput.files.length) {
                targetFileName = fileInput.files[0].name;
            }

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Adding an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
            worksheet.hyperlinks.add("A5", 1, 1, targetFileName);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **Erweiterte Themen**
- [Bild-Hyperlinks hinzufügen](/cells/de/javascript-cpp/add-image-hyperlinks/)
- [Hyperlink-Typ erkennen](/cells/de/javascript-cpp/detect-hyperlink-type/)
- [Hyperlinks im Arbeitsblatt bearbeiten](/cells/de/javascript-cpp/editing-hyperlinks-of-worksheet/)
- [Hyperlinks im Bereich abrufen](/cells/de/javascript-cpp/get-hyperlinks-in-range/)
