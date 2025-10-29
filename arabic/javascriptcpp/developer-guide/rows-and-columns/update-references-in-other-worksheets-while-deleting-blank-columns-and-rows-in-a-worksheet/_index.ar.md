---
title: تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل
linktitle: تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل
type: docs
weight: 5000
url: /ar/javascript-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: تعلم كيفية الحفاظ على المراجع في أوراق عمل أخرى عند حذف الأعمدة والصفوف الفارغة باستخدام سكريبت Aspose.Cells for Java عبر ++C.
---

{{% alert color="primary" %}}

عند حذف الأعمدة والصفوف الفارغة في ورقة العمل، تصبح مراجعها في ورقات العمل الأخرى غير صالحة. إذا كنت ترغب في تجنب هذا السلوك وتريد تحديث تلك المراجع لورقة العمل الحالية في ورقات العمل الأخرى أيضًا، يرجى استخدام الخاصية [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) وتعيينها على **صحيح**.

{{% /alert %}}

## **تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل**

 يرجى الاطلاع على رمز العينة التالي وإخراجه في وحدة التحكم. تتضمن الخلية E3 في ورقة العمل الثانية صيغة =Sheet1!C3 والتي تشير إلى الخلية C3 في ورقة العمل الأولى. إذا قمت بضبط خاصية [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) على **صحيح**، سيتم تحديث هذه الصيغة وتحويلها إلى =Sheet1!A1 عند حذف الأعمدة والصفوف الفارغة في ورقة العمل الأولى. ومع ذلك، إذا قمت بضبط خاصية [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) على **خطأ**، فستظل الصيغة في الخلية E3 في ورقة العمل الثانية =Sheet1!C3 وتصبح غير صالحة.

### **نموذج برمجة**

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

### **مخرجات الوحدة**

هذه هي مخرجات وحدة التحكم للرمز النموذجي أعلاه عند تعيين خاصية [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) على **صحيح**.

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

هذه هي مخرجات وحدة التحكم للرمز النموذجي أعلاه عند تعيين خاصية [**DeleteOptions.updateReference**](https://reference.aspose.com/cells/javascript-cpp/deleteoptions/#updateReference--) على **خطأ**. كما ترى، فإن الصيغة في الخلية E3 في ورقة العمل الثانية لم يتم تحديثها، وأصبح قيمة خليةها الآن 0 بدلاً من 4، وهذا غير صالح.

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
