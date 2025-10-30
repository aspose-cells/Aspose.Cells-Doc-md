---
title: Überlagerungs und Indizierungseffekte auf Schriftarten anwenden
linktitle: Überlagerungs und Indizierungseffekte auf Schriftarten anwenden
type: docs
weight: 80
url: /de/javascript-cpp/apply-superscript-and-subscript-effects-on-fonts/
description: Der JavaScript Code, um in Excel mithilfe von Aspose.Cells for JavaScript über C++ Superscript und Subscript Effekte auf Text anzuwenden.
keywords: Excel Superskript JavaScript via C++, Excel Unterstrich JavaScript via C++, Excel Superskript und Unterstrich JavaScript via C++, Unterstrich und Superskript in Excel JavaScript via C++ einfügen, Subscript und Superscript in Excel JavaScript via C++ hinzufügen, Superskript und Subscript in Excel JavaScript via C++ hinzufügen, Superskript in Excel JavaScript via C++ hinzufügen, Subscript in Excel JavaScript via C++ hinzufügen
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Funktionalität, Überlagerungs- (Text über der Grundlinie) und Indizierungseffekte (Text unterhalb der Grundlinie) auf Text anzuwenden.

{{% /alert %}}

## **Arbeiten mit Überlagerungs- und Indizierungseffekten**

Wenden Sie den Superskript-Effekt an, indem Sie die [**Font**](https://reference.aspose.com/cells/javascript-cpp/font)-Objektesteigenschaft [**isSuperscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSuperscript-boolean-) auf **true** setzen. Um Subscript anzuwenden, setzen Sie die [**Font**](https://reference.aspose.com/cells/javascript-cpp/font)-Objektesteigenschaft [**isSubscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSubscript-boolean-) auf **true**.

Die folgenden Codebeispiele zeigen, wie man Über- und Indizierung auf Text anwendet.

### JavaScript-Code, um den Superskript-Effekt auf Text anzuwenden

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Superscript Example</title>
    </head>
    <body>
        <h1>Superscript Example</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello";

            // Setting the font Superscript
            const style = cell.style;
            style.font.isSuperscript = true;
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Superscript.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### JavaScript-Code, um den Subscript-Effekt auf Text anzuwenden

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Subscript Example</h1>
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
            // Instantiate a Workbook object
            const workbook = new Workbook();

            // Add a new worksheet to the Excel object
            workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Access the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello";

            // Setting the font Subscript
            const style = cell.style;
            style.font.isSubscript = true;
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Subscript.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created with subscript formatting. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
