---
title: جدول محوري وبيانات المصدر
type: docs
weight: 30
url: /ar/javascript-cpp/pivot-table-and-source-data/
---

## **بيانات المصدر للجدول المحوري**

هناك أوقات عندما ترغب في إنشاء تقارير Microsoft Excel باستخدام جداول محورية تأخذ البيانات من مصادر بيانات مختلفة (مثل قاعدة بيانات) غير معروفة في وقت التصميم. يوفر هذا المقال نهجًا لتغيير بيانات مصدر الجدول المحوري بشكل ديناميكي.

### **تغيير مصدر بيانات الجدول المحوري**

1. إنشاء قالب مصمم جديد.
   1. إنشاء ملف قالب مصمم جديد كما في لقطة الشاشة أدناه.
   1. ثم تعريف نطاق مسمى، **DataSource**، الذي يشير إلى هذا النطاق من الخلايا.

      **إنشاء قالب مصمم وتعريف نطاق مسمى، DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. إنشاء جدول محوري بناءً على هذا النطاق المسمى.
   1. في Microsoft Excel ، اختر ** البيانات **، ثم ** جدول البيانات المحوري ** و ** تقرير PivotChart **.
   1. إنشاء جدول محوري استنادًا إلى المجموعة المسماة التي تم إنشاؤها في الخطوة الأولى.

      ** إنشاء جدول محوري استنادًا إلى المجموعة المسماة ، مصدر البيانات ** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. اسحب الحقل المقابل إلى صف جدول البيانات المحوري والعمود ، ثم قم بإنشاء جدول البيانات المحوري الناتج كما في اللقطة أدناه.

   ** إنشاء جدول محوري استنادًا إلى حقل مقابل ** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. انقر بزر الماوس الأيمن على الجدول المحوري وحدد **خيارات الجدول**.
   1. تحقق من ** التحديث عند الفتح ** في إعدادات ** خيارات البيانات **.

      ** ضبط خيارات جدول البيانات المحوري ** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


الآن ، يمكنك حفظ هذا الملف باسم ملف القالب الخاص بالمصمم.

1. ملء البيانات الجديدة وتغيير بيانات مصدر جدول البيانات المحوري.
   1. بمجرد إنشاء قالب المصمم ، استخدم الكود التالي لتغيير بيانات مصدر جدول البيانات المحوري.

تنفيذ الكود المثالي أدناه يغير بيانات مصدر الجدول المحوري.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Populating new data to the worksheet cells
            worksheet.cells.get("A9").value = "Golf";
            worksheet.cells.get("B9").value = "Qtr4";
            worksheet.cells.get("C9").value = 7000;

            // Changing named range "DataSource"
            const range = worksheet.cells.createRange(0, 0, 9, 3);
            range.name = "DataSource";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
