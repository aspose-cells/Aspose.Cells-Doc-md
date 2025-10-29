---
title: كيفية منع المستخدمين من طباعة ملف إكسل باستخدام JavaScript عبر C++
linktitle: كيفية منع المستخدمين من طباعة ملف Excel
type: docs
weight: 600
url: /ar/javascript-cpp/how-to-prevent-printing-excel/
description: تعلم كيف تمنع المستخدمين من طباعة ملفات إكسل باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: طباعة excel، منع طباعة excel، كيفية منع المستخدمين من طباعة excel، excel منع الطباعة، منع طباعة دفتر العمل، منع المستخدمين من طباعة الدفتر الكامل بـ VBA.
---

## **سيناريوهات الاستخدام المحتملة**  
في عملنا اليومي، قد توجد معلومات هامة في ملف إكسل؛ ومن أجل حماية البيانات الداخلية من الانتشار، لن تسمح الشركة بطباعتها. ستوضح لك هذه الوثيقة كيفية منع الآخرين من طباعة ملفات إكسل.  

## **كيفية منع المستخدمين من طباعة الملف في برنامج MS-Excel**  
يمكنك تطبيق رمز VBA التالي لحماية ملفاتك المحددة من الطباعة.  
1. افتح جدول العمل الذي لا تسمح للآخرين بطباعته.  
1. حدد علامة التبويب "مطور" في شريط إكسل ثم انقر على زر "عرض الكود" في قسم "التحكمات". أو، يمكنك الضغط مع الاستمرار على مفاتيح ALT + F11 لفتح نافذة Microsoft Visual Basic for Applications.  
<br>  
<img src="1.png" width=70% />  
1. ثم في مستكشف المشروع الأيسر، انقر نقرًا مزدوجًا على ThisWorkbook لفتح الوحدة، وأضف بعض رموز VBA.  
<br>  
<img src="2.png" width=70% />  
1. ثم قم بحفظ وإغلاق هذا الكود، وعد إلى المصنف، وعند طباعة الملف النموذجي، لن يُسمح بالطباعة، وستظهر لك رسالة تحذيرية التالية:  
<br>  
<img src="3.png" width=70% />  

## **كيفية منع المستخدمين من طباعة ملف إكسل باستخدام Aspose.Cells for JavaScript عبر C++**  

توضح الشفرة النموذجية التالية كيفية منع المستخدمين من طباعة ملف إكسل:  

1. قم بتحميل [ملف العينة](sample.xlsx).  
1. احصل على كائن VbaModuleCollection من خاصية VbaProject للمصنف.  
1. احصل على كائن VbaModule عبر اسم "ThisWorkbook".  
1. ضبط خاصية الرموز لكائن VbaModule.  
1. حفظ ملف العينة إلى [تنسيق xlsm](out.xlsm).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update VBA Module Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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

            // Accessing VBA project and its modules
            const modules = workbook.vbaProject.modules;
            const module = modules.get("ThisWorkbook");

            // Setting module codes (converted from setCodes -> codes assignment)
            module.codes = "Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n";

            // Saving the modified workbook as macro-enabled workbook
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
