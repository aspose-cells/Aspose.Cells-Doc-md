---
title: Avskydda ett arbetsblad med JavaScript via C++
linktitle: Avskydda ett kalkylark
type: docs
weight: 20
url: /sv/javascript-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Om en utvecklare behöver ta bort skydd från ett skyddat kalkylark vid körning så att vissa ändringar kan göras i filen? Detta kan enkelt göras med Aspose.Cells.

{{% /alert %}}

## **Avskydda ett kalkylblad**

### **Använda Microsoft Excel**

För att ta bort skydd från ett arbetsblad:

Från **Verktyg**-menyn, välj **Skydd** följt av **Avskärma blad**. Skyddet tas bort om kalkbladet inte är lösenordsskyddat. I så fall visas en dialog för att ange lösenordet. Ange lösenordet så är kalkbladet olåst.

### **Avskydda ett enkelt skyddat kalkylark med hjälp av Aspose.Cells**

Ett kalkblad kan avskärmas genom att anropa [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassens [**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--)-metod. Ett enkelt skyddat kalkblad är ett som inte är lösenordsskyddat. Sådana kalkblad kan avskärmas genom att anropa [**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--)-metoden utan att passera in någon parameter.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Unprotect Worksheet Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Unprotecting the worksheet without a password
            worksheet.unprotect();

            // Saving the Workbook in Excel97To2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Avskydda ett lösenordsskyddat kalkylark med hjälp av Aspose.Cells**

Ett kalkblad som är lösenordsskyddat är ett som är skyddat med ett lösenord. Sådana kalkblad kan avskärmas genom att anropa en överlagrad version av [**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--)-metoden som tar lösenordet som parameter.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unprotect Worksheet Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Unprotecting the worksheet with a password (empty password in original code)
            worksheet.unprotect("");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
