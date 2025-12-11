---  
title: Find Cells with Specific Style  
type: docs  
weight: 190  
url: /javascript-cpp/find-cells-with-specific-style/  
description: Learn how to find or search cells with a particular style applied through the Aspose.Cells for JavaScript via C++ API.  
keywords: Find cells with a particular style applied JavaScript via C++, Search cells with a particular style applied JavaScript via C++  
---  

{{% alert color="primary" %}}  

Sometimes, you need to find cells with a particular style applied. You can use Aspose.Cells for JavaScript via C++ to find all cells with a common style. Aspose.Cells provides the [**FindOptions.style(Style)**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#style-style-) method which you can use to specify the style to search cells for.  

{{% /alert %}}  

The code in this example finds all cells that have the same style as that of cell A1. After the code has been executed, all the cells that have the same style as A1 contain the text "Found".  

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
                // Find the cell that has the same style as cell A1
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