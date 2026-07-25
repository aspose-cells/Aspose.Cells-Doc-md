---
title: تعطيل شريط جدول الدوران
type: docs
weight: 90
url: /ar/javascript-cpp/disable-pivot-table-ribbons/
description: كيفية تعطيل أشرطة القوائم للجدول المحوري باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: Aspose.Cells for JavaScript عبر C++ مكتبة Excel، JavaScript لـ Excel عبر مكتبة C++، تعطيل أشرطة القوائم للجدول المحوري باستخدام Aspose.Cells for JavaScript عبر مكتبة Excel لـ C++.
---

{{% alert color="primary" %}}

تحليلات التقرير المبنية على الجداول المحورية مفيدة ولكنها عرضة للأخطاء إذا لم يكن لدى المستخدمين المستهدفين معرفة تفصيلية بـ Excel لضبط هذه التقارير. في هذه الحالات، سترغب المؤسسات في تقييد قدرة المستخدمين على تعديل تقارير الجدول المحوري. الميزات الشائعة للجدول المحوري مثل إضافة مرشحات إضافية، المقاطع، الحقول، أو تغيير ترتيب أشياء معينة في التقرير غير موصى بها في الغالب لكل المستخدمين. من ناحية أخرى، يجب أن يكون بمقدور هؤلاء المستخدمين تحديث التقرير واستخدام المرشحات أو المقاطع الحالية. وفرت Aspose.Cells for JavaScript عبر C++ هذه القدرة للمطورين لتقييد المستخدمين من تعديل هذه التقارير أثناء إنشائها. ولهذه الغاية، توفر Excel ميزة لتعطيل شريط القوائم الخاص بالجدول المحوري، وتوفرها أيضًا Aspose.Cells for JavaScript عبر C++، أي يمكن للمطور تعطيل الشريط الذي يحتوي على أدوات تعديل هذه التقارير.

{{% /alert %}}

## **كيفية تعطيل شريط القوائم للجدول المحوري باستخدام Aspose.Cells for JavaScript عبر C++**

يوضح الكود التالي هذه الميزة عن طريق الوصول إلى جدول دوران من ورقة ومن ثم ضبط [**enableWizard**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#enableWizard-boolean-) إلى **false**. يمكن تنزيل ملف جدول الدوران المثالي من هذا [الرابط](pivot_table_test.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Pivot Table Wizard Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the pivot table in the first sheet
            const pt = workbook.worksheets.get(0).pivotTables.get(0);

            // Disable ribbon for this pivot table
            pt.enableWizard = false;

            // Save output file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table wizard disabled successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
