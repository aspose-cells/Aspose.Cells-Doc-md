---
title: Update references in other worksheets while deleting blank columns and rows in a worksheet
linktitle: Update references in other worksheets while deleting blank columns and rows in a worksheet
type: docs
weight: 5000
url: /javascript-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Learn how to maintain references in other worksheets when deleting blank columns and rows in a worksheet using Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

When you delete blank columns and rows in a worksheet, its references in other worksheets become invalid. If you want to avoid this behavior and have those references of the current worksheet in other worksheets also updated, please use the [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) property and set it to **true**.

{{% /alert %}}

## **Update references in other worksheets while deleting blank columns and rows in a worksheet**

Please see the following sample code and its console output. The cell E3 in the second worksheet has a formula `=Sheet1!C3` which refers to cell C3 in the first worksheet. If you set the [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) property to **true**, this formula will be updated and become `=Sheet1!A1` when deleting blank columns and rows in the first worksheet. However, if you set the property to **false**, the formula in cell E3 of the second worksheet will remain `=Sheet1!C3` and become invalid.

### **Programming Sample**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Delete Blank Rows/Columns and Update References Example</h1>
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
            let wb;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create workbook
                wb = new Workbook();
            }

            // Add second sheet with name Sheet2
            wb.worksheets.add("Sheet2");

            // Access first sheet and add some integer value in cell C1
            // Also add some value in any cell to increase the number of blank rows and columns
            const sht1 = wb.worksheets.get(0);
            sht1.cells.get("C1").putValue(4);
            sht1.cells.get("K30").putValue(4);

            // Access second sheet and add formula in cell E3 which refers to cell C1 in first sheet
            const sht2 = wb.worksheets.get(1);
            sht2.cells.get("E3").formula = "'Sheet1'!C1";

            // Calculate formulas of workbook
            wb.calculateFormula();

            // Print the formula and value of cell E3 in second sheet before deleting blank columns and rows in Sheet1.
            let outputHtml = "";
            outputHtml += "<p>Cell E3 before deleting blank columns and rows in Sheet1.</p>";
            outputHtml += "<pre>--------------------------------------------------------</pre>";
            outputHtml += "<p>Cell Formula: " + sht2.cells.get("E3").formula + "</p>";
            outputHtml += "<p>Cell Value: " + sht2.cells.get("E3").stringValue + "</p>";

            // If you comment out DeleteOptions.updateReference property below, the formula in cell E3 on the second sheet will not be updated
            const opts = new AsposeCells.DeleteOptions();
            opts.updateReference = true;

            // Delete all blank rows and columns with delete options
            sht1.cells.deleteBlankColumns(opts);
            sht1.cells.deleteBlankRows(opts);

            // Calculate formulas of workbook
            wb.calculateFormula();

            // Print the formula and value of cell E3 in second sheet after deleting blank columns and rows in Sheet1.
            outputHtml += "<br/><br/>";
            outputHtml += "<p>Cell E3 after deleting blank columns and rows in Sheet1.</p>";
            outputHtml += "<pre>--------------------------------------------------------</pre>";
            outputHtml += "<p>Cell Formula: " + sht2.cells.get("E3").formula + "</p>";
            outputHtml += "<p>Cell Value: " + sht2.cells.get("E3").stringValue + "</p>";

            document.getElementById('result').innerHTML = outputHtml;

            // Save the modified workbook to download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
        });
    </script>
</html>
```

### **Console Output**

This is the console output of the above sample code when the [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) property has been set to **true**.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

This is the console output of the above sample code when the [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) property has been set to **false**. As you can see, the formula in cell E3 of the second worksheet is not updated and its cell value is now 0 instead of 4, which is invalid.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}