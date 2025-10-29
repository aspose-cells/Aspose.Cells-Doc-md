---
title: تحسين استخدام الذاكرة أثناء العمل مع ملفات كبيرة تحتوي على مجموعات بيانات كبيرة
type: docs
weight: 110
url: /ar/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

عند بناء دفتر العمل بمجموعات بيانات كبيرة، أو قراءة ملف إكسل كبير، يكون المبلغ الإجمالي لذاكرة الوصول العشوائي الذي سيتم الاحتفاظ به دائمًا قلقًا. هناك إجراءات يمكن اتخاذها للتكيف مع التحدي. تقدم Aspose.Cells بعض الخيارات والمكالمات واجهة برمجة التطبيقات ذات الصلة لتقليل وخفض وتحسين استخدام الذاكرة. كما يمكن أن تساعد العملية على العمل بشكل أكثر كفاءة وتشغيل أسرع.

استخدم الخيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) لتحسين استخدام الذاكرة المستخدمة لبيانات الخلايا وتقليل التكلفة الإجمالية للذاكرة. عند بناء مجموعة بيانات كبيرة للخلايا، يمكن حفظ مبلغ معين من الذاكرة مقارنة باستخدام الإعداد الافتراضي [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).

{{% /alert %}}

## **تحسين الذاكرة**

يعرض المثال التالي كيفية تحسين استخدام الذاكرة أثناء العمل مع البيانات الكبيرة في Aspose.Cells for JavaScript عبر C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Optimize Memory Usage Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, MemorySetting } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file or leave empty to create a new one.</p>';
                // Allow creating a new workbook even if no file selected; return only if user explicitly requires file.
            }

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // apply the setting to existing "Sheet1"
            workbook.worksheets.get(0).cells.memorySetting = MemorySetting.MemoryPreference;

            // apply the setting globally
            workbook.settings.memorySetting = MemorySetting.MemoryPreference;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Memory settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **احترس**

يتم تطبيق الخيار الافتراضي، [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)، لجميع الإصدارات. بالنسبة لبعض الحالات، مثل بناء دفتر عمل بمجموعة بيانات كبيرة للخلايا، قد يحسن الخيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) استخدام الذاكرة ويقلل من التكلفة الإجمالية للذاكرة للتطبيق. ومع ذلك، قد يؤدي هذا الخيار إلى تدهور الأداء في بعض الحالات الخاصة مثل التالي.

1. **الوصول العشوائي والمتكرر إلى الخلايا**: أكثر تسلسل فعالية للوصول إلى مجموعة الخلايا هو الخلية بالخلية في صف واحد، ثم صف بعد صف. خاصة إذا أمكنك الوصول إلى الصفوف/الخلايا من خلال المدرج المصرف من [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells/)، [**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection) و [**Row**](https://reference.aspose.com/cells/javascript-cpp/row)، سيتم تحقيق أقصى أداء مع [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).
1. **إدراج وحذف الخلايا والصفوف**: يرجى ملاحظة أنه إذا كانت هناك الكثير من عمليات الإدراج/الحذف للخلايا/الصفوف، سيكون هناك تدهور أداء ملحوظ لوضع [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) مقارنة بوضع [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).
1. **العمل على أنواع مختلفة من الخلايا**: إذا كان معظم الخلايا تحتوي على قيم سلسلة أو صيغ، فإن تكلفة الذاكرة ستكون نفسها كوضع [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) ولكن إذا كانت هناك الكثير من الخلايا الفارغة، أو قيم الخلايا هي رقمية، بوليانية وما إلى ذلك، فإن الخيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) سيعطي أداءً أفضل.
