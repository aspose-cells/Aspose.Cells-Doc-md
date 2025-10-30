---
title: Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle
linktitle: Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle
type: docs
weight: 5000
url: /tr/javascript-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Boş sütunlar ve satırlar silerken diğer çalışma sayfalarındaki referansların korunmasını öğrenin, Aspose.Cells for JavaScript ile C++ kullanarak.
---

{{% alert color="primary" %}}

Çalışma sayfasında boş sütunları ve satırları sildiğinizde, diğer çalışma sayfalarındaki bu sütunların referansları geçersiz hale gelir. Bu davranışı önlemek ve diğer çalışma sayfalarındaki bu çalışma sayfasının referanslarının güncellenmesini istiyorsanız, lütfen [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) özelliğini kullanın ve bunu **true** olarak ayarlayın.

{{% /alert %}}

## **Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle**

Aşağıdaki örnek kod ve konsol çıktısına bakın. İkinci çalışma sayfasındaki E3 hücresinde =Sheet1!C3 formülü var, bu da ilk çalışma sayfasındaki C3 hücresine referans verir. [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) özelliğini **true** olarak ayarlarsanız, bu formül güncellenerek =Sheet1!A1 olur, ilk çalışma sayfasında boş sütunlar ve satırları sildikten sonra. Ancak, [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) özelliğini **false** yaparsanız, ikinci çalışma sayfasındaki E3 hücresindeki formül değişmeden kalır ve geçersiz olur.

### **Programlama Örneği**

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

### **Konsol Çıktısı**

Yukarıdaki örnek kodun, [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) özelliği **true** olarak ayarlandığında çıkan konsol çıktısı.

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

Yukarıdaki örnek kodun, [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) özelliği **false** olarak ayarlandığında çıkan konsol çıktısı. Gördüğünüz gibi, ikinci çalışma sayfasındaki E3 hücresindeki formül güncellenmedi ve hücre değeri artık 4 yerine 0 oldu, bu da geçersiz.

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
