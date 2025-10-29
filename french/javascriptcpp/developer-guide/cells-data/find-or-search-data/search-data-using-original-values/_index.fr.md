---
title: Rechercher des données en utilisant les valeurs d origine
type: docs
weight: 380
url: /fr/javascript-cpp/search-data-using-original-values/
description: Apprenez comment rechercher des données en utilisant les valeurs d origine via l API Aspose.Cells for JavaScript via C++.
keywords: Rechercher des données en utilisant les valeurs d origine JavaScript via C++, Trouver des données en utilisant les valeurs d origine JavaScript via C++, Rechercher des données par valeurs d origine JavaScript via C++, Trouver des données par valeurs d origine JavaScript via C++
---

{{% alert color="primary" %}}  

Parfois, la valeur des données est masquée car elle est formatée d'une certaine manière. Par exemple, supposons que la cellule D4 ait la formule =Somme(A1:A2) et que sa valeur soit 20 mais qu'elle soit formatée comme ---, alors la valeur 20 est masquée et ne peut pas être trouvée en utilisant les options de recherche de Microsoft Excel. Cependant, vous pouvez la trouver en utilisant Aspose.Cells avec [**LookInType.OriginalValues**](https://reference.aspose.com/cells/javascript-cpp/lookintype)  

{{% /alert %}}  

Le code d'exemple suivant illustre le point ci-dessus. Il trouve la cellule D4 qui ne peut pas être trouvée en utilisant les options de recherche de Microsoft Excel mais Aspose.Cells peut la trouver en utilisant [**LookInType.OriginalValues**](https://reference.aspose.com/cells/javascript-cpp/lookintype). Veuillez lire les commentaires à l'intérieur du code pour plus d'informations.  

## Code JavaScript pour rechercher des données en utilisant des valeurs d'origine  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Formatted Value</title>
    </head>
    <body>
        <h1>Find Formatted Value Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FindOptions, Worksheet, Cell, Utils } = AsposeCells;

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

            // Add 10 in cell A1 and A2
            worksheet.cells.get("A1").value = 10;
            worksheet.cells.get("A2").value = 10;

            // Add Sum formula in cell D4 but customize it as ---
            const cell = worksheet.cells.get("D4");

            let style = cell.style;
            style.custom = "---";
            cell.style = style;

            // The result of formula will be 20 but 20 will not be visible because the cell is formatted as ---
            cell.formula = "=Sum(A1:A2)";

            // Calculate the workbook
            workbook.calculateFormula();

            // Create find options, we will search 20 using original values otherwise 20 will never be found because it is formatted as ---
            const options = new FindOptions();
            options.lookInType = AsposeCells.LookInType.OriginalValues;
            options.lookAtType = AsposeCells.LookAtType.EntireContent;

            let foundCell = null;
            const obj = 20;

            // Find 20 which is Sum(A1:A2) and formatted as ---
            foundCell = worksheet.cells.find(obj, foundCell, options);

            // Print the found cell to the page
            const resultDiv = document.getElementById('result');
            if (foundCell) {
                resultDiv.innerHTML = `<p style="color: green;">Found cell: ${foundCell.name}, value: ${foundCell.value}</p>`;
            } else {
                resultDiv.innerHTML = `<p style="color: red;">Cell not found.</p>`;
            }

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';
        });
    </script>
</html>
```


## Sortie console générée par le code d'exemple  



{{< highlight java >}}  

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]  

{{< /highlight >}}
