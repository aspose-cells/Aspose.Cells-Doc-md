---
title: Sök data med hjälp av ursprungliga värden
type: docs
weight: 380
url: /sv/javascript-cpp/search-data-using-original-values/
description: Lär dig hur du söker data med hjälp av ursprungliga värden via Aspose.Cells for JavaScript via C++ API.
keywords: Sök data med ursprungliga värden JavaScript via C++, Hitta data med ursprungliga värden JavaScript via C++, Sök data med ursprungliga värden JavaScript via C++, Hitta data med ursprungliga värden JavaScript via C++
---

{{% alert color="primary" %}}  

Ibland är värdet på datan dolt eftersom det är formaterat på något sätt. Till exempel, anta att cell D4 har formeln = Sum(A1:A2) och dess värde är 20, men det är formaterat som ---, då är värdet 20 dolt och kan inte hittas med hjälp av Microsoft Excels sökalternativ. Du kan dock hitta det med Aspose.Cells genom att använda [**LookInType.OriginalValues**](https://reference.aspose.com/cells/javascript-cpp/lookintype)  

{{% /alert %}}  

Följande exempelkod illustrerar ovanstående. Den hittar cell D4 som inte kan hittas med Microsoft Excels sökalternativ men Aspose.Cells kan hitta den med hjälp av [**LookInType.OriginalValues**](https://reference.aspose.com/cells/javascript-cpp/lookintype). Läs kommentarerna i koden för mer information.  

## JavaScript-kod för att söka data med hjälp av ursprungliga värden  

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


## Konsolutdata som genereras av exempelkoden  



{{< highlight java >}}  

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]  

{{< /highlight >}}
