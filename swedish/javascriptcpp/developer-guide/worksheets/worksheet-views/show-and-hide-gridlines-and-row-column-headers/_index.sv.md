---
title: Visa och Dölj Rutnätslinjer och Rad Kolumnrubriker med JavaScript via C++
linktitle: Visa och dölj rutnät och radkolumnhuvuden
type: docs
weight: 30
url: /sv/javascript-cpp/show-and-hide-gridlines-and-row-column-headers/
description: Denna artikel ger exempel på kod för att använda JavaScript API via C++ för att programmässigt dölja eller visa rutnätslinjer, radrubriker och kolumnrubriker i ett Excel ark.
---

{{% alert color="primary" %}}  
Aspose.Cells stödjer döljning och visning av kalkylbladets rutnät som är synliga som standard. Den ger också kontroll över synligheten av radkolumnhuvuden på kalkylbladet.  
{{% /alert %}}  

## **Visa och dölj rutnät**  

Alla Excel-kalkylblad har rutnät som standard. De hjälper till att avgränsa celler så att det är lätt att ange data i specifika celler. Rutnät gör det möjligt för oss att se ett kalkylblad som en samling av celler, där varje cell är lätt identifierbar.  

### **Kontrollera synligheten av rutnäten**  

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) klassen innehåller en [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) samling som tillåter utvecklare att komma åt varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett arbetsblad. För att kontrollera synligheten för rutnät, använd egenskapen [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--). [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) är en boolesk egenskap, vilket betyder att den endast kan lagra ett **true** eller **false** värde.  

#### **Gör rutnätslinjer synliga**  

Gör rutnät synliga genom att ställa in egenskapen [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) till **true**.  

#### **Gömmer rutnätslinjer**  

Dölj rutnät genom att ställa in egenskapen [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) till **false**.  

Ett komplett exempel visas nedan som demonstrerar användningen av egenskapen [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) genom att öppna en Excel-fil (book1.xls), dölja rutnäten på det första arbetsbladet och spara den modifierade filen som output.xls.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hide Gridlines Example</title>
    </head>
    <body>
        <h1>Hide Gridlines Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object
            // Opening the Excel file through the file data
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the grid lines of the first worksheet of the Excel file
            worksheet.isGridlinesVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Gridlines hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Visa och dölj radkolumnhuvuden**  

Alla kalkylblad i en Excel-fil består av celler som är ordnade i rader och kolumner. Alla rader och kolumner har unika värden som används för att identifiera dem och individuella celler. Till exempel har rader nummer - 1, 2, 3, 4, osv.- och kolumner är ordnade alfabetiskt - A, B, C, D, osv. Rad- och kolumnvärdena visas i huvudena. Med Aspose.Cells kan utvecklare kontrollera synligheten av dessa rad- och kolumnhuvuden.  

### **Kontrollera synligheten av arbetsbladen**  

 Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) klassen innehåller en [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) samling som tillåter utvecklare att komma åt varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett arbetsblad. För att kontrollera synligheten av rad- och kolumnhuvuden, använd egenskapen [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--). [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) är en boolesk egenskap, vilket betyder att den endast kan lagra ett **true** eller **false** värde.  

#### **Göra rad-/kolumnrubriker synliga**  

Gör rad- och kolumnhuvuden synliga genom att ställa in egenskapen [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) till **true**.  

#### **Gömma rad-/kolumnrubriker**  

Dölj rad- och kolumnhuvuden genom att ställa in egenskapen [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) till **false**.  

Ett komplett exempel visas nedan som visar hur man använder egenskapen [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) genom att öppna en Excel-fil (book1.xls), dölja rad- och kolumnhuvuden på det första arbetsbladet och spara den modifierade filen som output.xls.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Row/Column Headers</title>
    </head>
    <body>
        <h1>Hide Row and Column Headers Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the headers of rows and columns
            worksheet.isRowColumnHeadersVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Headers hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Det är också möjligt att använda metoderna [**Cells.unhideRows(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRows-number-number-number-) och [**Cells.unhideColumns(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumns-number-number-number-) av [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-klassen för att göra flera rader och kolumner synliga.  
{{% /alert %}}
