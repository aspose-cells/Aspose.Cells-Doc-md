---  
title: Insert Pivot Table  
linktitle: Pivot Tables  
type: docs  
weight: 160  
url: /javascript-cpp/create-pivot-table/  
description: Create and format pivot tables of Excel spreadsheet files.  
---  

## **Create Pivot Table**  

It is possible to use Aspose.Cells for JavaScript via C++ to add pivot tables to spreadsheets programmatically.  

### **Pivot Table Object Model**  

Aspose.Cells for JavaScript via C++ provides a special set of classes that are used to create and control pivot tables. These classes are used to create and set [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) objects, the building blocks of a pivot table. The objects are:

- [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield) represents a field in a [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable).  
- [**PivotFieldCollection**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection) represents a collection of all the [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield) objects in the [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable).  
- [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) represents a PivotTable on a worksheet.  
- [**PivotTableCollection**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) represents a collection of all the [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) objects on a worksheet.  

### **Creating a Simple Pivot Table Using Aspose.Cells**  

1. Add data to a worksheet using the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) object's [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) method. This data will be used as the pivot table's data source.  
2. Add a pivot table to the worksheet by calling the [**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) collection's [**add**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#add-string-string-string-) method, which is encapsulated in the Worksheet object.  
3. Access the new [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) object from the [**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) collection by passing the PivotTable's index.  
4. Use any of the [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) objects (explained above) to manage the pivot table.  

After executing the example code, a pivot table is added to the worksheet.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Pivot Table Example</h1>
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
            
            document.getElementById('runExample').addEventListener('click', async () => {
                // Instantiate a new Workbook object
                const workbook = new Workbook();

                // Obtaining the reference of the newly added worksheet
                const sheetIndex = workbook.worksheets.add();
                const sheet = workbook.worksheets.get(sheetIndex);
                const cells = sheet.cells;

                // Setting the value to the cells
                let cell = cells.get("A1");
                cell.value = "Sport";
                cell = cells.get("B1");
                cell.value = "Quarter";
                cell = cells.get("C1");
                cell.value = "Sales";

                cell = cells.get("A2");
                cell.value = "Golf";
                cell = cells.get("A3");
                cell.value = "Golf";
                cell = cells.get("A4");
                cell.value = "Tennis";
                cell = cells.get("A5");
                cell.value = "Tennis";
                cell = cells.get("A6");
                cell.value = "Tennis";
                cell = cells.get("A7");
                cell.value = "Tennis";
                cell = cells.get("A8");
                cell.value = "Golf";

                cell = cells.get("B2");
                cell.value = "Qtr3";
                cell = cells.get("B3");
                cell.value = "Qtr4";
                cell = cells.get("B4");
                cell.value = "Qtr3";
                cell = cells.get("B5");
                cell.value = "Qtr4";
                cell = cells.get("B6");
                cell.value = "Qtr3";
                cell = cells.get("B7");
                cell.value = "Qtr4";
                cell = cells.get("B8");
                cell.value = "Qtr3";

                cell = cells.get("C2");
                cell.value = 1500;
                cell = cells.get("C3");
                cell.value = 2000;
                cell = cells.get("C4");
                cell.value = 600;
                cell = cells.get("C5");
                cell.value = 1500;
                cell = cells.get("C6");
                cell.value = 4070;
                cell = cells.get("C7");
                cell.value = 5000;
                cell = cells.get("C8");
                cell.value = 6430;

                const pivotTables = sheet.pivotTables;

                // Adding a PivotTable to the worksheet
                const index = pivotTables.add("=A1:C8", "E3", "PivotTable2");

                // Accessing the instance of the newly added PivotTable
                const pivotTable = pivotTables.get(index);

                // Hiding grand totals for rows.
                pivotTable.rowGrand = false;

                // Dragging the first field to the row area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);

                // Dragging the second field to the column area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, 1);

                // Dragging the third field to the data area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 2);

                // Saving the Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'CreatePivotTable_out.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table created successfully! Click the download link to get the file.</p>';
            });
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  

When assigning a range of cells as the data source, the range must go from top left to bottom right. For example, "A1:C3" is valid but "C3:A1" is not.  

{{% /alert %}}