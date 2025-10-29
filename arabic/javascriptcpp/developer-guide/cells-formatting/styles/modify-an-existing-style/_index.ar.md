---
title: تعديل نمط موجود
linktitle: تعديل نمط موجود
description: Aspose.Cells هي مكتبة لجافا سكريبت عبر C++ للعمل مع ملفات الجدول التي تتيح للمستخدمين تعديل أنماط الخلايا الموجودة. ستقدم هذه المقالة كيفية تعديل نمط خلية موجود باستخدام مكتبة Aspose.Cells بحيث يمكن للمستخدمين تغيير مظهر الخلايا حسب الحاجة.
keywords: تعديل الأنماط الموجودة، تخصيص مظهر وشكل تطبيقك، دليل، تعليمات، مساعدة، وثائق التطوير، مستندات واجهة برمجة التطبيقات، رمز عينة، تنزيلات، الدعم.
type: docs
weight: 90
url: /ar/javascript-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

لتطبيق نفس الخيارات التنسيق على الخلايا، قم بإنشاء كائن نمط التنسيق جديد. كائن نمط التنسيق هو مزيج من الخصائص التنسيقية مثل الخط، حجم الخط، البدء، الرقم، الحدود، الأنماط الخطية وما إلى ذلك، مسمى ومخزن كمجموعة. عند التطبيق، يتم تطبيق كل من التنسيق في ذلك النمط.

يمكنك أيضًا استخدام نمط موجود، حفظه مع الدفتر واستخدامه لتنسيق المعلومات بنفس السمات.

عندما لا تتم تنسيق الخلايا بشكل صريح، يتم تطبيق النمط العادي (نمط الافتراضي للدفتر). Microsoft Excel يعرف مسبقا العديد من الأنماط بالإضافة إلى النمط العادي بما في ذلك Comma و Currency و Percent.

تسمح Aspose.Cells بتعديل أي من هذه الأنماط أو أي نمط آخر تعرفه بالسمات المرغوبة.

{{% /alert %}}

## **استخدام Microsoft Excel**

لتحديث نمط في Microsoft Excel 97-2003:

1. في قائمة **تنسيق**، انقر على **نمط**.
1. حدد النمط الذي تريد تعديله من قائمة **اسم النمط**.
1. انقر على **تعديل**.
1. اختر خيارات النمط التي تريدها باستخدام علامات التبويب في مربع حوار تنسيق الخلايا.
1. انقر على **موافق**.
1. في **يتضمن النمط**, حدد ميزات النمط التي تريدها.
1. انقر **موافق** لحفظ النمط وتطبيقه على النطاق المحدد.

## **باستخدام Aspose.Cells for JavaScript عبر C++**

 توضح الأمثلة التالية كيفية استخدام طريقة [**Style.update()**](https://reference.aspose.com/cells/javascript-cpp/style/#update--).

### **إنشاء وتعديل نمط**

 ينشئ هذا المثال كائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)، يطبقه على مجموعة خلايا، ويعدّل كائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). تُطبّق التعديلات تلقائيًا على الخلية والنطاق الذي تم تطبيق النمط عليه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Style Example</h1>
        <p>Select an existing Excel file to modify or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiate workbook from uploaded file or create a new one
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a new style object.
            const style = workbook.createStyle();

            // Set the number format.
            style.number = 14;

            // Set the font color to red color.
            style.font.color = AsposeCells.Color.Red;

            // Name the style.
            style.name = "Date1";

            // Get the first worksheet cells.
            const cells = workbook.worksheets.get(0).cells;

            // Specify the style (described above) to A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.style = style;

            // Create a range (B1:D1).
            const range = cells.createRange("B1", "D1");

            // Initialize styleflag object.
            const flag = new AsposeCells.StyleFlag();

            // Set all formatting attributes on.
            flag.all = true;

            // Apply the style (described above) to the range.
            range.applyStyle(style, flag);

            // Modify the style (described above) and change the font color from red to black.
            style.font.color = AsposeCells.Color.Black;

            // Done! Since the named style (described above) has been set to a cell and range, 
            // The change would be reflected(new modification is implemented) to cell(A1) and 
            // Range (B1:D1).
            style.update();

            // Save the excel file. 
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book_styles.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **تعديل نمط موجود**

يستخدم هذا المثال ملف Excel قالبي بسيط تم تطبيق نمط يُسمى النسبة على نطاق معين بالفعل. المثال:

1. يستلم النمط,
1. ينشئ كائن نمط و
1. يعدل تنسيق النمط.

يتم تطبيق التعديلات تلقائيًا على النطاق الذي تم تطبيق النمط عليه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Named Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, Utils } = AsposeCells;

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

            // Create a workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the named style "Percent" via the styles collection
            const style = workbook.styles.get("Percent");

            // Change the number format to "0.00%".
            style.number = 11;

            // Set the font color.
            style.font.color = Color.Red;

            // Update the style so ranges using this named style are updated.
            style.update();

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book2.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Style updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
