---
title: كيفية تنسيق الرقم كتاريخ
type: docs
weight: 10
url: /ar/javascript-cpp/format-number-to-date/
description: سيقدم هذا المقال كيف يمكن تنسيق رقم إلى تاريخ باستخدام API Script عبر C++.
keywords: تنسيق الرقم كتاريخ، إعدادات رقم الخلية، تنسيق الرقم إلى تاريخ، إعدادات التاريخ، تنسيق التاريخ.
---

## **سيناريوهات الاستخدام المحتملة**
إن تنسيق الأرقام كتاريخ في Excel (أو أي برنامج جدول بيانات آخر) مهم لعدة أسباب، خاصة عندما تعمل مع بيانات تتضمن وقتًا أو معلومات جدولة. إليك أسباب فائدة تنسيق الأرقام إلى تواريخ:

1. التفسير الصحيح لقيم التاريخ: في Excel، تُخزن التواريخ كأرقام تسلسلية (مثلاً، 1 يمثل 1 يناير 1900، و44210 يمثل 6 سبتمبر 2021). إذا لم يتم تنسيق هذه الأرقام كتاريخ، قد يرى المستخدمون أرقامًا لا معنى لها بدلاً من تواريخ قابلة للتعرف عليها. يتيح تنسيقها بشكل صحيح لـ Excel عرضها كتاريخ فعلي (مثلاً، 06/09/2021 بدلاً من 44210).
1. يبسط العمليات الحسابية المتعلقة بالوقت: يمكن لـ Excel إجراء العديد من العمليات باستخدام التواريخ، مثل حساب عدد الأيام بين تاريخين، إضافة أو طرح أيام، أو تحديد يوم الأسبوع. إذا لم يتم تنسيق الأرقام كتاريخ، فلن يتمكن Excel من أداء هذه العمليات بفعالية. على سبيل المثال، إذا كنت تريد معرفة عدد الأيام بين 01/09/2023 و01/10/2023، يمكن لـ Excel حساب ذلك بسهولة إذا كانت الأرقام بتنسيق التاريخ.
1. يضمن التناسق: عندما يتم تنسيق جميع القيم المتعلقة بالتاريخ بشكل صحيح، فإن ذلك يضمن ظهور جميع التواريخ بأسلوب موحد وسهل القراءة. هذا التناسق مهم في التقارير الأعمال، جداول المشاريع، وقواعد البيانات التي يكون فيها التناسق ضروريًا للتواريخ.
تستخدم مناطق مختلفة صيغ تواريخ مختلفة (مثل MM/DD/YYYY في الولايات المتحدة مقابل DD/MM/YYYY في العديد من الدول الأخرى)، لذلك يساعد التنسيق على ضمان تفسير التواريخ بشكل صحيح.
1. يحسن قابلية القراءة: التواريخ المعروضة بصيغة قياسية (مثل 01/01/2024) أسهل في القراءة من الأرقام التسلسلية الخام مثل 45000. يجعل التنسيق الصحيح للتواريخ جدول البيانات أكثر ودية للمستخدم ويجنب الالتباس. هذا مهم بشكل خاص في سيناريوهات مثل الجدولة، الجداول الزمنية، تخطيط الأحداث، أو البيانات التاريخية.
1. يساعد في الفرز والتصفية: عند تنسيق التواريخ بشكل صحيح، يتعرف Excel عليها كتاريخ فعلي، مما يسهل فرز البيانات أو تصفيتها زمنياً. على سبيل المثال، يمكنك فرز قائمة الأحداث حسب التاريخ أو تصفية نطاق البيانات لإظهار سجلات بين تاريخين معينين. بدون تنسيق التاريخ الصحيح، قد يتم الفرز بناءً على الرقم الخام بدلاً من التواريخ الفعلية على التقويم.
1. يمكّن من استخدام وظائف التاريخ: يوفر Excel مجموعة من وظائف التاريخ القوية، مثل: TODAY()، DATEDIF()، WORKDAY()، YEAR()، MONTH()، DAY(). تتطلب هذه الوظائف تنسيق التواريخ بشكل صحيح للحصول على حسابات دقيقة.
1. يدعم التصور (الرسوم البيانية/الجداول الزمنية): يمكن استخدام التواريخ المنسقة بشكل صحيح لإنشاء رسوم بيانية ومخططات حيث يكون الوقت محورًا رئيسيًا. على سبيل المثال، في مخطط الجدول الزمني، يحتاج Excel إلى وجود تواريخ بتنسيق معترف به لرسم الأحداث بدقة على مدار الزمن. الأرقام غير المنسقة أو غير المنسقة قد تؤدي إلى رسوم بيانية لا معنى لها أو تعكس معلومات غير صحيحة.
1. يمنع سوء التفسير: يمكن أن يُساء فهم الأرقام الخام بسهولة. على سبيل المثال، قد يُقرأ 44210 كقيمة رقمية عامة، لكن عند تنسيقه كتاريخ، يتضح أنه يمثل 6 سبتمبر 2021. تساعد التواريخ المنسقة بشكل صحيح على تجنب سوء تفسير البيانات.
1. يسهل إدخال البيانات: عندما يتم تنسيق الخلايا كتاريخ، يُطلب من المستخدمين إدخال البيانات بصيغة تاريخ صحيحة، مما يمنع أخطاء إدخال البيانات ويضمن تسجيل قيم التاريخ بشكل صحيح.
1. ضروري للجدولة والمتابعة: في أي موقف يتطلب جدول، تتبع، أو مواعيد نهائية (مثل إدارة المشاريع، التوقعات المالية، أو التقارير الحساسة للوقت)، يُعد تنسيق الأرقام كتاريخ أمرًا حيويًا للدقة والفهم. يسمح بالتخطيط والتنفيذ بشكل أفضل.


## **كيفية تنسيق الرقم إلى تاريخ في Excel**
لتنسيق رقم كتاريخ في Excel، اتبع هذه الخطوات:

### **باستخدام الشريط (علامة التبويب الصفحة الرئيسية)**
1. حدد الخلايا التي تحتوي على الأرقام التي تريد تنسيقها كتاريخ.
1. انتقل إلى علامة التبويب الصفحة الرئيسية في الشريط.
1. في مجموعة الرقم، انقر على السهم المنسدل في مربع تنسيق الرقم (الذي قد يظهر كـ "عام" أو "رقم" بشكل افتراضي).
1. اختر التاريخ القصير أو التاريخ الطويل من القائمة المنسدلة. التاريخ القصير: يعرض التاريخ بصيغة موجزة، مثل MM/DD/YYYY (التنسيق الأمريكي) أو DD/MM/YYYY (التنسيق الدولي). التاريخ الطويل: يعرض التاريخ بشكل أكثر تفصيلًا، مثل الاثنين، 1 يناير 2024.
<br>
<img src="1.png" width=60% />

### **استخدام مربع حوار تنسيق الخلايا**
1. حدد الخلايا التي تريد تنسيقها.
1. انقر بزر الماوس الأيمن على الخلايا المحددة واختر تنسيق الخلايا، أو اضغط Ctrl + 1 (Windows) أو Cmd + 1 (Mac).
1. في مربع حوار تنسيق الخلايا، انتقل إلى علامة التبويب الأرقام.
1. من القائمة على اليسار، اختر التاريخ.
1. اختر تنسيق التاريخ المرغوب من القائمة على اليمين (مثلاً، MM/DD/YYYY، DD/MM/YYYY، أو تنسيقات مخصصة).
<br>
<img src="2.png" width=60% />
1. انقر فوق موافق لتطبيق تنسيق التاريخ.

## **كيفية تنسيق الرقم كتاريخ في Aspose.Cells**

لتنسيق الأرقام كتاريخ في مكتبة Script عبر C++ للعمل مع ملفات إكسل، يمكنك تطبيق تنسيق التاريخ على الخلايا برمجياً. إليك كيفية القيام بذلك باستخدام Script عبر C++:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Date & Custom Format Example</h1>
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
            // Create a new workbook
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell you want to format
            const a1 = worksheet.cells.get("A1");

            // Set a numeric value that represents a date (e.g., 44210 represents 09/06/2021 in Excel)
            a1.value = 44210;

            // Create a style object to apply the date format
            const a1Style = a1.style;

            // "14" represents a standard date format in Excel (MM/DD/YYYY)
            a1Style.number = 14;

            // Apply the style to the cell
            a1.style = a1Style;

            // Access the cell where you want to apply the currency format
            const a2 = worksheet.cells.get("A2");

            // Set a numeric value to the cell
            a2.value = 44210;

            // Create a style object to apply the date format
            const a2Style = a2.style;
            // Custom format for YYYY-MM-DD
            a2Style.custom = "YYYY-MM-DD";

            // Apply the style to the cell
            a2.style = a2Style;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DateFormatted.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and formatted successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
