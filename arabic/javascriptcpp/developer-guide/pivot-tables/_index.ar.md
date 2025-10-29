---
title: إدراج جدول محوري
linktitle: جداول الدوران
type: docs
weight: 160
url: /ar/javascript-cpp/create-pivot-table/
description: إنشاء وتنسيق جداول الدوران في ملفات جداول البيانات في Excel.
---

## **إنشاء جدول محوري**

من الممكن استخدام Aspose.Cells for JavaScript عبر C++ لإضافة جداول محورية إلى جداول البيانات بشكل برمجي.

### **نموذج كائن جدول الدوران**

يوفر Aspose.Cells for JavaScript عبر C++ مجموعة خاصة من الفئات التي تُستخدم لإنشاء والتحكم في الجداول المحورية. تُستخدم هذه الفئات لإنشاء وتعيين [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) كائنات، وهي اللبنات الأساسية للجدول المحوري. الكائنات هي:

- [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield) يمثل حقل في [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection) يمثل مجموعة من جميع كائنات [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield) في [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) يمثل جدول دوران على ورقة العمل.
- [**PivotTableCollection**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) يمثل مجموعة من جميع كائنات [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) على ورقة العمل.

### **إنشاء جدول دوران بسيط باستخدام Aspose.Cells**

1. إضافة بيانات إلى ورقة العمل باستخدام طريقة [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) لكائن [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).
   سيتم استخدام هذه البيانات كمصدر بيانات جدول الدوران.
1. إضافة جدول دوران إلى ورقة العمل عن طريق استدعاء طريقة [**add**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#add-string-string-string-) للمجموعة [**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection)، التي تم تقنينها في كائن ورقة العمل.
1. الوصول إلى كائن [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) الجديد من مجمع [**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) عن طريق تمرير فهرس PivotTable.
1. استخدام أي من كائنات [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) (المشرحة أعلاه) لإدارة جدول الدوران.

بعد تنفيذ رمز المثال، يتم إضافة جدول دوران إلى ورقة العمل.

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

                // Unshowing grand totals for rows.
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

عند تعيين مجموعة من الخلايا كمصدر بيانات، يجب أن تكون المجموعة من الزاوية العلوية اليسرى إلى الزاوية السفلى اليمنى. على سبيل المثال، "A1:C3" صالح ولكن "C3:A1" غير صالح.

{{% /alert %}}
