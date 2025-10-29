---
title: تحديد الموقع المطلق لعنصر الجدول المحوري
type: docs
weight: 50
url: /ar/javascript-cpp/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

أحيانًا، يحتاج المستخدم إلى تحديد الموقع المطلق لعناصر الجدول المحوري، قدمت API الخاصة بـ Aspose.Cells for JavaScript عبر C++ بعض الخصائص الجديدة وطريقة لتحقيق متطلبات المستخدم.

- تمت إضافة [**PivotItem.position**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#position-number-) الخاصية التي يمكن استخدامها لتحديد مؤشر الموقع في كافة PivotItems بغض النظر عن العقدة الأم. تمت إضافة [**PivotItem.positionInSameParentNode**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#positionInSameParentNode-number-) للخاصية التي يمكن استخدامها لتحديد مؤشر الموقع في PivotItems تحت نفس العقدة الأم.
- تمت إضافة طريقة [**PivotItem.move**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-) لنقل العنصر لأعلى أو لأسفل بناءً على قيمة العدد، حيث يعد العدد هو عدد الموقع الذي سيتم نقل عنصر الجدول المحوري إليه. إذا كانت قيمة العدد أقل من الصفر، سيتم نقل العنصر لأعلى، بينما إذا كانت قيمة العدد أكبر من الصفر، فإن عنصر الجدول المحوري سيتم نقله لأسفل. يقوم المعامل من نوع Boolean، isSameParent، بتحديد ما إذا كانت العملية المتحركة يجب أن تتم في نفس العقد الأصلي أم لا.
- تم إلغاء طريقة *PivotItem.move(int count)*، لذا يُنصح باستخدام الأسلوب [**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-) الذي تمت إضافته حديثًا بدلاً من ذلك.

{{% /alert %}}

الشيفرة التجريبية التالية تقوم بإنشاء جدول محوري ثم تحدد مواقع عناصر الجدول المحوري في نفس العقد الأصلي. يمكنك تنزيل [ملف إكسل المصدر](5112632.xlsx) و[ملف إكسل الناتج](5112619.xlsx) للإشارة إليه. إذا قمت بفتح ملف إكسل الناتج، سترى أن عنصر الجدول المحوري "4H12" عند الموضع 0 في العقد "K11" و"DIF400" في الموضع 3. بالمثل، CA32 في الموضع 1 وAAA3 في الموضع 2.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Example</title>
    </head>
    <body>
        <h1>PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotFieldType, PivotFieldSubtotalType } = AsposeCells;

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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Add pivot worksheet and get data worksheet
            const wsPivot = workbook.worksheets.add("pvtNew Hardware");
            const wsData = workbook.worksheets.get("New Hardware - Yearly");

            // Get the pivottables collection for the pivot sheet
            const pivotTables = wsPivot.pivotTables;

            // Add PivotTable to the worksheet
            const index = pivotTables.add("='New Hardware - Yearly'!A1:D621", "A3", "HWCounts_PivotTable");

            // Get the PivotTable object
            const pvtTable = pivotTables.get(index);

            // Add vendor row field
            pvtTable.addFieldToArea(PivotFieldType.Row, "Vendor");

            // Add item row field
            pvtTable.addFieldToArea(PivotFieldType.Row, "Item");

            // Add data field
            pvtTable.addFieldToArea(PivotFieldType.Data, "2014");

            // Turn off the subtotals for the vendor row field
            const pivotField = pvtTable.rowFields.get("Vendor");
            pivotField.subtotals = PivotFieldSubtotalType.None;

            // Turn off grand total
            pvtTable.columnGrand = false;

            /*
             * Please call the PivotTable.refreshData() and PivotTable.calculateData()
             * before using PivotItem.setPosition,
             * PivotItem.setPositionInSameParentNode and PivotItem.move methods.
            */
            pvtTable.refreshData();
            pvtTable.calculateData();

            pvtTable.rowFields.get("Item").pivotItems.get("4H12").positionInSameParentNode = 0;
            pvtTable.rowFields.get("Item").pivotItems.get("DIF400").positionInSameParentNode = 3;

            /* 
             * As a result of using PivotItem.setPositionInSameParentNode,
             * it will change the original sort sequence.
             * So when you use PivotItem.setPositionInSameParentNode in another parent node.
             * You need call the method named "calculateData" again. 
            */
            pvtTable.calculateData();

            pvtTable.rowFields.get("Item").pivotItems.get("CA32").positionInSameParentNode = 1;
            pvtTable.rowFields.get("Item").pivotItems.get("AAA3").positionInSameParentNode = 2;

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">PivotTable created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

يرجى ملاحظة أنه من الضروري استدعاء طرق PivotTable.RefreshData وPivotTable.CalculateData قبل استخدام الخصائص [**PivotItem.position**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#position-number-)، [**PivotItem.positionInSameParentNode**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#positionInSameParentNode-number-) والطريقة [**PivotItem.move**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-).

{{% /alert %}}
