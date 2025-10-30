---
title: Implementera 1904 datumssystem med JavaScript via C++
description: Aspose.Cells är ett JavaScript bibliotek för att arbeta med kalkylbladsfiler. Det stöder implementeringen av 1904 datumssystemet, vilket tillåter användare att beräkna och formatera baserat på datumssystemet från 1 januari 1904. Denna artikel beskriver hur man implementerar 1904 datumssystemet med Aspose.Cells biblioteket.
keywords: Aspose.Cells, 1904 datumssystemet, kalkylblad, beräkning, formatering, JavaScript via C++
type: docs
weight: 7000
url: /sv/javascript-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel stöder två datumsystem: 1900-datumssystem (standarddatumssystem som implementeras i Excel för Windows) och 1904-datumssystem. 1904-datumssystemet används normalt för att ge kompatibilitet med Macintosh Excel-filer och är det förvalda systemet om du använder Excel för Macintosh. Du kan ställa in 1904-datumssystemet för Excel-filer med hjälp av Aspose.Cells for JavaScript via C++. 

{{% /alert %}} 

För att implementera 1904-datumssystemet i Microsoft Excel (t.ex. Microsoft Excel 2003):

1. Från menyn **Verktyg** väljer du **Alternativ** och väljer fliken **Beräkning**.
1. Välj alternativet **1904 datumssystem**.
1. Klicka på **OK**.

|**Välja 1904-datumssystem i Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

Se följande kodexempel om hur du uppnår detta med Aspose.Cells API:erna.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Enable 1904 Date System</h1>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement 1904 date system
            workbook.settings.date1904 = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">1904 date system enabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
