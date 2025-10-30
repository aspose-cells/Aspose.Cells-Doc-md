---
title: Tillämpa avancerad filter av Microsoft Excel för att visa poster som uppfyller komplexa kriterier
type: docs
weight: 280
url: /sv/javascript-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Lär dig hur du använder avancerad filter av Microsoft Excel för att visa poster som uppfyller komplexa kriterier med hjälp av Aspose.Cells for JavaScript via C++ API.
keywords: Tillämpa avancerad filter JavaScript via C++, sätt avancerad filter JavaScript via C++, lägg till avancerad filter JavaScript via C++, skapa avancerad filter JavaScript via C++, hur man lägger till avancerad filter till ett område JavaScript via C++
---

## **Möjliga användningsscenario**  

Microsoft Excel tillåter att du tillämpar *Advanced Filter* på arbetsbladets data för att visa poster som möter komplexa kriterier. Du kan tillämpa avancerad filter med Microsoft Excel via dess *Data > Advanced* kommando som visas i denna skärmskärm.  

![todo:image_alt_text](1.png)  

Aspose.Cells for JavaScript via C++ tillåter också att du använder det [**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-) metoden för att applicera avancerad filter. Precis som Microsoft Excel, accepterar det följande parametrar.  

**isFilter**  

Anger om filtreringen av listan på plats.  

**listRange**  

Listan intervall.  

**criteriaRange**  

Kriterieintervallet.  

**copyTo**  

Intervallet där data kopieras till.  

**uniqueRecordOnly**  

Endast visa eller kopiera unika rader.  

## **Tillämpa Avancerat Filter i Microsoft Excel för att Visa Poster som Uppfyller Komplexa Kriterier**  

Följande kodexempel använder det avancerade filtret på [Exempelfilen Excel](48496692.xlsx) och genererar [Utdata Excel-fil](48496691.xlsx). Skärmbilden visar båda filerna för jämförelse. Som du kan se i skärmbilden, har data filtrerats i utdata Excel-filen enligt komplexa kriterier.  

![todo:image_alt_text](2.png)  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Advanced Filter Example</title>
    </head>
    <body>
        <h1>Advanced Filter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Advanced Filter</button>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (sampleAdvancedFilter.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const wb = new Workbook(new Uint8Array(arrayBuffer));

            const ws = wb.worksheets.get(0);

            // Apply advanced filter on range A5:D19 with criteria A1:D2, filter in place, include all records (not unique)
            ws.advanced_Filter(true, "A5:D19", "A1:D2", "", false);

            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAdvancedFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Advanced filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
