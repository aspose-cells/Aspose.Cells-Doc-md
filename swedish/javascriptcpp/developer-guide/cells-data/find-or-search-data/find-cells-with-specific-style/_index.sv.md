---
title: Hitta celler med specifik stil
type: docs
weight: 190
url: /sv/javascript-cpp/find-cells-with-specific-style/
description: Lär dig hur du hittar eller söker celler med en särskild stil tillämpad med hjälp av API t Aspose.Cells for JavaScript via C++.
keywords: Hitta celler med en särskild stil tillämpad JavaScript via C++, Sök celler med en särskild stil tillämpad JavaScript via C++
---

{{% alert color="primary" %}}

 Ibland behöver du hitta celler med en särskild stil tillämpad. Du kan använda Aspose.Cells for JavaScript via C++ för att hitta alla celler med en gemensam stil. Aspose.Cells tillhandahåller metoden [**FindOptions.style(Style)**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#style-style-) som du kan använda för att ange den stil du vill söka celler för.

{{% /alert %}}

Koden i detta exempel hittar alla celler som har samma stil som cell A1. Efter att koden har utförts innehåller alla celler som har samma stil som A1 texten "Hittad".

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Cells by Style</title>
    </head>
    <body>
        <h1>Find Cells by Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FindOptions } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the style of cell A1
            const style = worksheet.cells.get("A1").style;

            // Specify the style for searching
            const options = new FindOptions();
            options.style = style;

            let nextCell = null;

            do {
                // Find the cell that has a style of cell A1
                nextCell = worksheet.cells.find(null, nextCell, options);
                if (nextCell === null) break;
                // Change the text of the cell
                nextCell.value = "Found";
            } while (true);

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
