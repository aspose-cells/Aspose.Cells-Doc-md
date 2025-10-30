---
title: Sprid formel i tabell eller listobjekt automatiskt vid inmatning av data i nya rader med JavaScript via C++
linktitle: Ställer in tabellformel
type: docs
weight: 260
url: /sv/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Lär dig hur du automatiskt sprider formler i tabeller eller listobjekt vid inmatning av data i nya rader med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**
Ibland vill du att en formel i din tabell eller lista automatiskt ska spridas till nya rader vid inmatning av ny data. Detta är standardbeteendet i Microsoft Excel. För att uppnå samma funktionalitet med Aspose.Cells for JavaScript via C++, använd [ListColumn.formula](https://reference.aspose.com/cells/javascript-cpp/listcolumn/#formula--) egenskapen.

## **Sprid formel automatiskt i tabell eller listobjekt medan du matar in data i nya rader**
Följande exempel på kod skapar en tabell eller listobjekt så att formeln i kolumn B automatiskt sprids till nya rader när du matar in ny data. Kontrollera den [utdataexcel-fil](5115469.xlsx) som genereras med denna kod. Om du skriver in ett tal i cell A3, kommer du att se att formeln i cell B2 automatiskt sprids till cell B3.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells ListObject Example</h1>
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
            // Create workbook object
            const book = new Workbook();

            // Access first worksheet
            const sheet = book.worksheets.get(0);

            // Add column headings in cell A1 and B1
            sheet.cells.get(0, 0).value = "Column A";
            sheet.cells.get(0, 1).value = "Column B";

            // Add list object, set its name and style
            const listObject = sheet.listObjects.get(
                sheet.listObjects.add(0, 0, 1, sheet.cells.maxColumn, true)
            );
            listObject.tableStyleType = AsposeCells.TableStyleType.TableStyleMedium2;
            listObject.displayName = "Table";

            // Set the formula of second column so that it propagates to new rows automatically while entering data
            listObject.listColumns.get(1).formula = "=[Column A] + 1";

            // Save the workbook in xlsx format
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
