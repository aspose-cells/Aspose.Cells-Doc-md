---
title: ワークシート内の空白の列と行を削除する際に、他のワークシートの参照を更新する
linktitle: ワークシート内の空白の列と行を削除する際に、他のワークシートの参照を更新する
type: docs
weight: 5000
url: /ja/javascript-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: C++を使用してAspose.Cells for JavaScriptでワークシートの空白の列と行を削除した際に他のワークシートの参照を維持する方法を学びます。
---

{{% alert color="primary" %}}

ワークシート内の空白の列と行を削除すると、他のワークシートでの参照が無効になります。この動作を回避し、他のワークシートでの現在のワークシートの参照も更新されるようにするには、[**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--)プロパティを使用して**true**に設定してください。

{{% /alert %}}

## **ワークシート内の空白の列と行を削除する際に、他のワークシートの参照を更新する**

以下のサンプルコードとそのコンソール出力を参照してください。第2のワークシートにあるセルE3には`=Sheet1!C3`の数式が入っています。これは第1シートのセルC3を参照しています。[**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--)プロパティを**true**に設定すると、この数式は更新され、第1シートの空白列と行を削除した後は`=Sheet1!A1`になります。ただし、[**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--)プロパティを**false**に設定すると、セルE3の数式は`=Sheet1!C3`のままで無効になります。

### **プログラミングサンプル**

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

### **コンソール出力**

上記のサンプルコードの[**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--)プロパティを**true**に設定した場合のコンソール出力です。

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

上記のサンプルコードの[**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--)プロパティを**false**に設定した場合のコンソール出力です。ご覧のとおり、2番目のワークシートのセルE3の数式は更新されず、その値は4から0に変わり、不正です。

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
