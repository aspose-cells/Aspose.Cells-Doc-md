---
title: Uppdatera referenser i andra arbetsblad samtidigt som tomma kolumner och rader tas bort i ett arbetsblad
linktitle: Uppdatera referenser i andra arbetsblad samtidigt som tomma kolumner och rader tas bort i ett arbetsblad
type: docs
weight: 5000
url: /sv/javascript-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Lär dig hur du behåller referenser i andra kalkylblad vid radering av tomma kolumner och rader i ett kalkylblad med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

När du tar bort tomma kolumner och rader i en arbetsbok blir dess hänvisningar i andra arbetsblad ogiltiga. Om du vill undvika detta beteende och vill att hänvisningarna från det nuvarande arbetsbladet i andra arbetsblad också uppdateras, använd sedan egenskapen [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) och sätt den till **true**.

{{% /alert %}}

## **Uppdatera referenser i andra arbetsblad samtidigt som tomma kolumner och rader tas bort i ett arbetsblad**

 Se följande exempel på kod och dess konsolutdata. Cellen E3 i det andra bladet har en formel =Sheet1!C3 som refererar till cell C3 i det första bladet. Om du ställer in [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) egenskapen till **true**, kommer denna formel att uppdateras och bli =Sheet1!A1 vid borttagning av tomma kolumner och rader i det första bladet. Men om du ställer in [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) egenskapen till **false**, förblir formeln i cell E3 i det andra bladet =Sheet1!C3 och blir ogiltig.

### **Programmeringsexempel**

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

            // If you comment DeleteOptions.UpdateReference property below, then the formula in cell E3 in second sheet will not be updated
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

### **Konsoloutput**

Detta är konsolutdata för ovanstående kod när [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) egenskapen har ställts in till **true**.

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

Detta är konsolutdata för ovanstående kod när [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) egenskapen har ställts in till **false**. Som du kan se är formeln i cell E3 i det andra bladet inte uppdaterad och dess cellvärde är nu 0 istället för 4, vilket är ogiltigt.

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
