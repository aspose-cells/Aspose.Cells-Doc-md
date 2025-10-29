---
title: إدارة إعدادات ملفات إكسل باستخدام جافا سكريبت عبر C++
linktitle: إعدادات السجل الإحصائية
type: docs
weight: 185
url: /ar/javascript-cpp/workbook-settings/
description: إدارة إعدادات ملفات إكسل باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **نظرة عامة على إعدادات الوحدة العمل**
يتضمن العمل مع ملفات إكسل إعدادات متنوعة يمكن التلاعب بها برمجياً باستخدام Aspose.Cells for JavaScript عبر C++. توضح هذه الوثيقة كيفية إدارة هذه الإعدادات بشكل فعال.

## **سيناريوهات الاستخدام المحتملة**
السيناريوهات التالية توضح متى قد تحتاج إلى إدارة إعدادات الوحدة العمل:
- تعديل خيارات العرض
- تعيين وضع الحسابات
- تكوين معلمات إعداد الصفحة

## ** إدارة إعدادات دفتر العمل باستخدام Aspose.Cells for JavaScript عبر C++**
يوضح هذا المثال كيفية إدارة إعدادات الوحدة العمل مثل خيارات الحساب والإعدادات العرضية.

1. إنشاء وحدة عمل جديدة أو تحميل واحدة موجودة.
2. تعديل إعدادات الوحدة العمل حسب متطلباتك.
3. حفظ الوحدة للعمل للحفاظ على التغييرات.

### **مثال على الكود**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Workbook Settings Example</h1>
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
            // Create a new workbook
            const workbook = new Workbook();

            // Access the settings of the workbook
            const settings = workbook.settings;
            settings.calculationMode = 1; // Manual calculation

            // Display options
            settings.showGridLines = false; // Disable gridlines

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkbookSettingsExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **خصائص وطرق إعدادات الوحدة العمل الرئيسية**
 يوفر Aspose.Cells for JavaScript عبر C++ مجموعة من الخصائص والطرق لضبط إعدادات دفتر العمل:
- **Workbook.settings**: الوصول إلى إعدادات دفتر العمل.
- **Settings.calculationMode**: تعيين وضع الحساب لدفتر العمل.
- **Settings.showGridLines**: تفعيل أو تعطيل خطوط الشبكة على العرض.

## **الاستنتاج**
إدارة إعدادات دفتر العمل في Aspose.Cells for JavaScript عبر C++ بسيطة وتوفر العديد من الخيارات لتخصيص سلوكيات ملف إكسل. باستخدام الإعدادات المتاحة، يمكنك تخصيص دفتر العمل ليتناسب مع متطلباتك الخاصة.
