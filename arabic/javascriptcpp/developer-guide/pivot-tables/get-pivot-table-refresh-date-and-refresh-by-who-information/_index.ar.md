---
title: الحصول على تاريخ تحديث جدول الدوران ومعلومات من يقوم بالتحديث
type: docs
weight: 100
url: /ar/javascript-cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: كيفية الحصول على تاريخ تحديث الجدول المحوري ومعلومات من قام بالتحديث باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: Aspose.Cells for JavaScript مكتبة Excel، JavaScript لـ Excel، الحصول على تاريخ تحديث الجدول المحوري ومعلومات من قام بالتحديث باستخدام Aspose.Cells for JavaScript عبر مكتبة Excel لـ C++.
---

{{% alert color="primary" %}}

يدعم Aspose.Cells for JavaScript عبر C++ الآن استرجاع تاريخ التحديث والمعلومات من قام بالتحديث من ملف العمل.

{{% /alert %}}

## **كيفية الحصول على تاريخ تحديث جدول البيانات المحوري ومن قام بتحديثه**
تعيد [**PivotTable.refreshDate**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshDate--) التاريخ الذي تم فيه تحديث تقرير PivotTable لآخر مرة. بالمثل، تعيد الخاصية [**PivotTable.refreshedByWho**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshedByWho--) اسم المستخدم الذي قام بتحديث التقرير في المرة الأخيرة. يوضح المثال التالي هذه الميزة ويمكن تنزيل ملف العينة من الرابط التالي.

[SourcePivotTable.xlsx](77496335.xlsx)

**كود عينة**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Info</title>
    </head>
    <body>
        <h1>Pivot Table Information</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            const pivotTable = worksheet.pivotTables.get(0);

            const refreshedByWho = pivotTable.refreshedByWho;
            const refreshDate = pivotTable.refreshDate;

            console.log("Pivot table refresh by who = " + refreshedByWho);
            console.log("Pivot table refresh date = " + refreshDate);

            document.getElementById('result').innerHTML = `
                <p>Pivot table refresh by who = ${refreshedByWho}</p>
                <p>Pivot table refresh date = ${refreshDate}</p>
            `;
        });
    </script>
</html>
```
