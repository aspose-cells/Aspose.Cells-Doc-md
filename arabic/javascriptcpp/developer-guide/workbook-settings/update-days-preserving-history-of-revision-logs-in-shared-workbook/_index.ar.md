---
title: تحديث عدد الأيام مع الحفاظ على سجل التعديلات في المصنف المشارك باستخدام جافا سكريبت عبر C++
linktitle: تحديث الأيام الحفظ تاريخ سجلات المراجعة في الورقة المشتركة
type: docs
weight: 80
url: /ar/javascript-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: تعلم كيفية تحديث أيام حفظ سجل التعديلات في المصنفات المشتركة باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

 عند مشاركة مصنف، تحصل على خيار يقول ***حفظ سجل التغييرات لمدة N أيام*** كما هو موضح في لقطة الشاشة التالية. يمكنك تحديث عدد الأيام للحفاظ على السجل باستخدام Aspose.Cells for JavaScript عبر C++ مع الخاصية [**WorksheetCollection.daysPreservingHistory**](https://reference.aspose.com/cells/javascript-cpp/revisionlogcollection/#daysPreservingHistory--). 

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **تحديث أيام الاحتفاظ بتاريخ سجل المراجعة في دفتر العمل المشترك**

الكود المثالي التالي يقوم بإنشاء دفتر عمل فارغ، ثم يشاركه ويحدّث أيام سجلات المراجعة للحفاظ على التاريخ لـ 7 أيام والتي تكون عادة 30 يومًا. يُرجى الرجوع إلى [ملف الإكسل الناتج](60489773.xlsx) الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Shared Workbook</title>
    </head>
    <body>
        <h1>Shared Workbook - DaysPreservingHistory Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Shared Workbook</button>
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
            // Create empty workbook
            const workbook = new Workbook();

            // Share the workbook
            workbook.settings.shared = true;

            // Update DaysPreservingHistory of RevisionLogs
            workbook.worksheets.revisionLogs.daysPreservingHistory = 7;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputShared_DaysPreservingHistory.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and configured. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
