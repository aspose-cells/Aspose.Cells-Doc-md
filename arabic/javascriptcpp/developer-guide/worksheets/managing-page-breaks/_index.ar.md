---
title: إدارة فواصل الصفحات باستخدام جافا سكريبت عبر C++
linktitle: إدارة فواصل الصفحات
type: docs
weight: 30
url: /ar/javascript-cpp/managing-page-breaks/
description: يقدم هذا المقال رمزاً نموذجياً ويشرح كيفية إضافة، مسح، أو حذف فواصل صفحات محددة في أوراق عمل إكسل برمجياً باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: فواصل الصفحات جافا سكريبت عبر C++، فواصل صفحات إكسل جافا سكريبت عبر C++، مسح فواصل الصفحات جافا سكريبت عبر C++، حذف فاصل صفحة معين جافا سكريبت عبر C++
---

{{% alert color="primary" %}}

وفقًا للتعريف، فإن فاصل الصفحة هو المكان في تدفق النص حيث تنتهي صفحة وتبدأ الصفحة التالية. يتيح Microsoft Excel للمستخدمين إضافة فواصل صفحات في أي خلية محددة من ورقة العمل.

في الموقع الذي تمت إضافة كسر الصفحة فيه، تنتهي الصفحة ويتم طباعة بقية البيانات بعد كسر الصفحة على الصفحة التالية أثناء الطباعة. ببساطة، كسر الصفحة يقسم ورقة العمل إلى عدة صفحات وفقًا لمواصفاتك. يمكنك أيضًا إضافة كسر الصفحة إلى ورقة العمل الخاصة بك أثناء التشغيل باستخدام Aspose.Cells. تسمح Aspose.Cells للمطورين بإضافة نوعين من كسر الصفحة:

- فاصل صفحات أفقي
- فاصل صفحات عمودي

في بقية النقاش، سنصف كيف يمكنك إضافة فواصل صفحات أفقية أو عمودية إلى أوراق العمل الخاصة بك باستخدام Aspose.Cells.

{{% /alert %}}

## **كسرات الصفحة**

يوفر Aspose.Cells for JavaScript عبر C++ فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) تتيح الوصول إلى كل ورقة عمل في ملف إكسل.

يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة واسعة من الخصائص والأساليب المستخدمة لإدارة ورقة العمل.

لإضافة كسر الصفحة، استخدم خصائص [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) للفئة والخصائص [**worksheet.horizontalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#horizontalPageBreaks--).

الخصائص [**worksheet.horizontalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#horizontalPageBreaks--) و [**worksheet.verticalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#verticalPageBreaks--) هي مجموعات قد تحتوي على العديد من كسر الصفحة. تحتوي كل مجموعة على العديد من الطرق لإدارة كسر الصفحة الأفقي والعمودي.

### **إضافة فواصل الصفحات**

لإضافة فاصل صفحة في ورقة عمل، قم بإدراج فواصل صفحة أفقية وعمودية عند الخلية المحددة باستخدام استدعاء طريقتي [**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/horizontalpagebreakcollection/#add-number-number-number-) و [**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/verticalpagebreakcollection/#add-number-number-number-). كل طريقة **إضافة** تأخذ اسم الخلية التي يجب إضافة الفاصل إليها.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Page Breaks Example</h1>
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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a page break at cell Y30
            worksheet.horizontalPageBreaks.add("Y30");
            worksheet.verticalPageBreaks.add("Y30");

            // Save the Excel file (Excel 97-2003 format .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingPageBreaks_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page breaks added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

في وضع معاينة كسر الصفحة أو معاينة الطباعة، يمكنك رؤية كيف تعمل هذه الكسور.

{{% /alert %}}

### **إزالة كسر صفحة محدد**

لحذف انقطاع صفحة معين، استدعِ الطريقتين [**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/horizontalpagebreakcollection/#removeAt-number-) و [**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/verticalpagebreakcollection/#removeAt-number-). كل طريقة **removeAt** تأخذ فهرس انقطاع الصفحة المراد حذفه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Remove Specific Page Break Example</title>
    </head>
    <body>
        <h1>Remove Specific Page Break Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Removing a specific page break
            worksheet.horizontalPageBreaks.removeAt(0);
            worksheet.verticalPageBreaks.removeAt(0);

            // Saving the Excel file (Excel 97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RemoveSpecificPageBreak_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page breaks removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **مهم معرفته**

عند ضبط خصائص **fitToPages** (وهي [**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--) و [**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--)) في إعدادات الصفحة، تتأثر إعدادات انقطاع الصفحة، لذلك إذا قمت بطباعة ورقة العمل، لن تؤخذ بعين الاعتبار إعدادات انقطاع الصفحة على الرغم من أنها لا تزال مضبوطة.
