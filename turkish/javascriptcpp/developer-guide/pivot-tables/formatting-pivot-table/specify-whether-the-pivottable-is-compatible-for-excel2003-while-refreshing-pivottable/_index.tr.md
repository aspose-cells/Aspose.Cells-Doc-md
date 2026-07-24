---
title: PivotTable, PivotTable yeniden tazelenirken Excel2003 için uyumlu olup olmadığını belirtin
type: docs
weight: 80
url: /tr/javascript-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells for JavaC++ betiği, PivotTable’ın Excel2003 uyumluluğunu belirlemek için kullanabileceğiniz [**PivotTable.isExcel2003Compatible**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#isExcel2003Compatible-boolean-) özelliği sağlar. Bu özellik true ise, dize 255 karakterden kısa veya eşit olmalıdır; eğer dize 255 karakterden uzunsa, kesilir. **False** ise, dize yukarıdaki sınırlamaya tabi değildir. Varsayılan değer **true**'dur.

{{% /alert %}}

## **PivotTable, PivotTable yeniden tazelenirken Excel2003 için uyumlu olup olmadığını belirtin**

Aşağıdaki örnek kod, [**PivotTable.isExcel2003Compatible**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#isExcel2003Compatible-boolean-) özelliğinin kullanımını açıklar. Orijinal dize 383 karakter uzunluğundadır. Fakat [**PivotTable.isExcel2003Compatible**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#isExcel2003Compatible-boolean-) özelliği **true** olarak ayarlandığında ve pivot tablosu yeniden tazelendiğinde, pivot tablosunun B5 hücresinin verisi kısaltılır ve 255 karakter uzunluğuna gelir. Ancak [**PivotTable.isExcel2003Compatible**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#isExcel2003Compatible-boolean-) özelliği **false** olarak ayarlandığında ve pivot tablosu tekrar tazelendiğinde, pivot tablosunun B5 hücresinin verisi kısaltılmaz ve 383 karakter uzunluğunda kalır. Bu özelliğin daha iyi anlaşılması için kod içindeki yorumları okuyun lütfen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Specify Compatibility</title>
    </head>
    <body>
        <h1>Specify Compatibility Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (e.g., sample-pivot-table.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet that contains pivot table data
            const dataSheet = workbook.worksheets.get(0);

            // Access cell A3 and sets its data
            const cells = dataSheet.cells;
            let cell = cells.get("A3");
            cell.value = "FooBar";

            // Access cell B3, sets its data. We set B3 a very long string which has more than 255 characters
            const longStr = "Very long text 1. very long text 2. very long text 3. very long text 4. very long text 5. very long text 6. very long text 7. very long text 8. very long text 9. very long text 10. very long text 11. very long text 12. very long text 13. very long text 14. very long text 15. very long text 16. very long text 17. very long text 18. very long text 19. very long text 20. End of text.";
            cell = cells.get("B3");
            cell.value = longStr;

            // Print the length of cell B3 string
            console.log("Length of original data string: "  + cell.stringValue.length);

            // Access cell C3 and sets its data
            cell = cells.get("C3");
            cell.value = "closed";

            // Access cell D3 and sets its data
            cell = cells.get("D3");
            cell.value = "2016/07/21";

            // Access the second worksheet that contains pivot table
            const pivotSheet = workbook.worksheets.get(1);

            // Access the pivot table
            const pivotTable = pivotSheet.pivotTables.get(0);

            // IsExcel2003Compatible property tells if PivotTable is compatible for Excel2003 while refreshing PivotTable.
            // If it is true, a string must be less than or equal to 255 characters, so if the string is greater than 255 characters,
            // it will be truncated. If false, a string will not have the aforementioned restriction. The default value is true.
            pivotTable.isExcel2003Compatible = true;
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Check the value of cell B5 of pivot sheet.
            // It will be 255 because we have set IsExcel2003Compatible property to true. All the data after 255 characters has been truncated
            let b5 = pivotSheet.cells.get("B5");
            console.log("Length of cell B5 after setting IsExcel2003Compatible property to True: "  + b5.stringValue.length);

            // Now set IsExcel2003Compatible property to false and again refresh
            pivotTable.isExcel2003Compatible = false;
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Now it will print the original length of cell data. The data has not been truncated now.
            b5 = pivotSheet.cells.get("B5");
            console.log("Length of cell B5 after setting IsExcel2003Compatible property to False: "  + b5.stringValue.length);

            // Set the row height and column width of cell B5 and also wrap its text
            pivotSheet.cells.setRowHeight(b5.row, 100);
            pivotSheet.cells.setColumnWidth(b5.column, 65);

            const st = b5.style;
            st.isTextWrapped = true;
            b5.style = st;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SpecifyCompatibility_out_.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
