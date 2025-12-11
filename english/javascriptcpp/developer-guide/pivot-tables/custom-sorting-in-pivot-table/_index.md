---  
title: Custom sorting in Pivot Table  
type: docs  
weight: 130  
url: /javascript-cpp/custom-sorting-in-pivot-table/  
description: How to sort Pivot Tables on field values with Aspose.Cells for JavaScript via C++.  
keywords: Aspose.Cells for JavaScript via C++ Excel, Excel JavaScript library, sort Pivot Tables on field values using Aspose.Cells for JavaScript via C++ Excel Library.  
---  

## **How to Set Custom Sorting in Pivot Table Using Aspose.Cells for JavaScript via C++ Library**  
By using the Aspose.Cells for JavaScript via C++ API, you can sort Pivot Tables on field values. The following code snippet loads the sample Excel file and adds three pivot tables. The first pivot table is without custom sorting, the second pivot table is sorted on "Seafood" row‑field values, and the third pivot table is sorted on "28/07/2000" column‑field values.  

Sample source file and output files can be downloaded from here for testing the sample code:  

[Source Excel File](98107428.xlsx)  

[Output Excel File](98107429.xlsx)  

[Output PDF File](98107430.pdf)  


## **Sample Code**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Sort Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Sort Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadXlsxLink" style="display: none; margin-right: 10px;">Download Excel File</a>
        <a id="downloadPdfLink" style="display: none;">Download PDF File</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;
        
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
            const downloadXlsxLink = document.getElementById('downloadXlsxLink');
            const downloadPdfLink = document.getElementById('downloadPdfLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (SamplePivotSort.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const pivotTables = sheet.pivotTables;

            // source PivotTable
            // Adding a PivotTable to the worksheet
            let index = pivotTables.add("=Sheet1!A1:C10", "E3", "PivotTable2");
            // Accessing the instance of the newly added PivotTable
            let pivotTable = pivotTables.get(index);
            // Hiding grand totals for rows.
            pivotTable.rowGrand = false;
            pivotTable.columnGrand = false;
            // Dragging the first field to the row area.
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 1);
            let rowField = pivotTable.rowFields.get(0);
            rowField.isAutoSort = true;
            rowField.isAscendSort = true;
            // Dragging the second field to the column area.
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, 0);
            let colField = pivotTable.columnFields.get(0);
            colField.numberFormat = "dd/mm/yyyy";
            colField.isAutoSort = true;
            colField.isAscendSort = true;
            // Dragging the third field to the data area.
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 2);
            pivotTable.refreshData();
            pivotTable.calculateData();
            // end of source PivotTable

            // sort the PivotTable on "Seafood" row field values
            index = pivotTables.add("=Sheet1!A1:C10", "E10", "PivotTable2");
            pivotTable = pivotTables.get(index);
            pivotTable.rowGrand = false;
            pivotTable.columnGrand = false;
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 1);
            rowField = pivotTable.rowFields.get(0);
            rowField.isAutoSort = true;
            rowField.isAscendSort = true;
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, 0);
            colField = pivotTable.columnFields.get(0);
            colField.numberFormat = "dd/mm/yyyy";
            colField.isAutoSort = true;
            colField.isAscendSort = true;
            colField.autoSortField = 0;
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 2);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // sort the PivotTable on "28/07/2000" column field values
            index = pivotTables.add("=Sheet1!A1:C10", "E18", "PivotTable2");
            pivotTable = pivotTables.get(index);
            pivotTable.rowGrand = false;
            pivotTable.columnGrand = false;
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 1);
            rowField = pivotTable.rowFields.get(0);
            rowField.isAutoSort = true;
            rowField.isAscendSort = true;
            rowField.autoSortField = 0;
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, 0);
            colField = pivotTable.columnFields.get(0);
            colField.numberFormat = "dd/mm/yyyy";
            colField.isAutoSort = true;
            colField.isAscendSort = true;
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 2);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Saving the Excel file (XLSX)
            const xlsxData = workbook.save(SaveFormat.Xlsx);
            const xlsxBlob = new Blob([xlsxData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            downloadXlsxLink.href = URL.createObjectURL(xlsxBlob);
            downloadXlsxLink.download = 'out_cpp.xlsx';
            downloadXlsxLink.style.display = 'inline-block';
            downloadXlsxLink.textContent = 'Download Modified Excel File';

            // Saving as PDF
            const options = new AsposeCells.PdfSaveOptions();
            options.onePagePerSheet = true;
            const pdfData = workbook.save(SaveFormat.Pdf, options);
            const pdfBlob = new Blob([pdfData], { type: "application/pdf" });
            downloadPdfLink.href = URL.createObjectURL(pdfBlob);
            downloadPdfLink.download = 'out_cpp.pdf';
            downloadPdfLink.style.display = 'inline-block';
            downloadPdfLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Use the links above to download the results.</p>';
        });
    </script>
</html>
```