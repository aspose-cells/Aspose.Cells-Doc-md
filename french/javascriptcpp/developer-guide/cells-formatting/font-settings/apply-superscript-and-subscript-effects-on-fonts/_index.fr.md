---
title: Appliquer des effets de exposant et d indice sur les polices
linktitle: Appliquer des effets de exposant et d indice sur les polices
type: docs
weight: 80
url: /fr/javascript-cpp/apply-superscript-and-subscript-effects-on-fonts/
description: Le code JavaScript pour appliquer des effets de haut et de bas indices dans Excel en utilisant Aspose.Cells for JavaScript via C++.
keywords: JavaScript pour l exposant et l indice en Excel via C++, JavaScript pour le sous indice en Excel via C++, JavaScript pour exposant et indice en Excel via C++, insertion de sous indice et d’exposant en JavaScript dans Excel via C++, ajout de sous indice et d’exposant en JavaScript dans Excel, ajout d’exposant et d’indice en JavaScript dans Excel, ajout d’exposant en JavaScript dans Excel, ajout de sous indice en JavaScript dans Excel
---

{{% alert color="primary" %}}

Aspose.Cells offre la fonctionnalité d'appliquer les effets d'exposant (texte au-dessus de la ligne de base) et d'indice (texte en dessous de la ligne de base) au texte.

{{% /alert %}}

## **Travailler avec l'effet d'exposant et d'indice**

Appliquez l'effet d'exposant en réglant la propriété [**isSuperscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSuperscript-boolean-) de l’objet [**Font**](https://reference.aspose.com/cells/javascript-cpp/font) à **true**. Pour appliquer le sous-indice, réglez la propriété [**isSubscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSubscript-boolean-) de l’objet [**Font**](https://reference.aspose.com/cells/javascript-cpp/font) à **true**.

Les exemples de code suivants montrent comment appliquer un exposant et un indice au texte.

### Code JavaScript pour appliquer l'effet d'exposant sur le texte

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


### Code JavaScript pour appliquer l'effet de sous-indice sur le texte

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
