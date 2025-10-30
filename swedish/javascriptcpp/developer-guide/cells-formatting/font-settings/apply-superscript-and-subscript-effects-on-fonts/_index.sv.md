---
title: Tillämpa överstruken och understreckande effekter på typsnitt
linktitle: Tillämpa överstruken och understreckande effekter på typsnitt
type: docs
weight: 80
url: /sv/javascript-cpp/apply-superscript-and-subscript-effects-on-fonts/
description: JavaScript koden för att tillämpa exponent och subscript effekter på text i Excel med hjälp av Aspose.Cells for JavaScript via C++.
keywords: excel exponent JavaScript via C++, excel subscript JavaScript via C++, excel exponent och subscript JavaScript via C++, infoga subscript och exponent i excel JavaScript via C++, lägg till subscript och exponent i excel JavaScript via C++, lägg till exponent och subscript i excel JavaScript via C++, lägg till exponent JavaScript via C++, lägg till subscript JavaScript via C++
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller funktionalitet för att tillämpa överstruken (text ovanför baslinjen) och understreckande (text under baslinjen) effekter på text.

{{% /alert %}}

## **Arbeta med överstruken och understreck**

Tillämpa exponenteffekten genom att sätta [**Font**](https://reference.aspose.com/cells/javascript-cpp/font)-objektets [**isSuperscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSuperscript-boolean-)-egenskap till **true**. För att tillämpa subscript, ställ in [**Font**](https://reference.aspose.com/cells/javascript-cpp/font)-objektets [**isSubscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSubscript-boolean-)-egenskap till **true**.

Följande kodexempel visar hur man tillämpar över- och understreck på text.

### JavaScript-kod för att tillämpa exponenteffekt på text

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


### JavaScript-kod för att tillämpa subscript-effekt på text

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
