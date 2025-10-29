---
title: تطبيق التظليل على الصفوف والأعمدة البديلة باستخدام التنسيق الشرطي
linktitle: تطبيق التظليل على الصفوف والأعمدة البديلة باستخدام التنسيق الشرطي
description: كيفية استخدام مكتبة Aspose.Cells في جافا سكريبت عبر C++ لتطبيق ظلال تنسيق شرطي للصفوف والأعمدة المتناوبة. من خلال ضبط هذه المعايير، لديك تحكم أكبر في مظهر الخلايا.
keywords: Aspose.Cells، التنسيق الشرطي، جافا سكريبت عبر C++، صفوف متناوبة، أعمدة متناوبة، ظلال
type: docs
weight: 30
url: /ar/javascript-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

توفر واجهات برمجة التطبيقات لAspose.Cells الوسائل لإضافة وتعديل قواعد التنسيق الشرطي لكائن [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). يمكن تخصيص هذه القواعد بعدة طرق للحصول على التنسيق المطلوب بناءً على الشروط أو القواعد. ستوضح هذه المقالة استخدام واجهات برمجة تطبيقات Aspose.Cells for JavaScript عبر C++ لتطبيق التظليل على الصفوف والأعمدة المتناوبة بمساعدة قواعد التنسيق الشرطي ووظائف إكسل المدمجة.

{{% /alert %}}

تستخدم هذه المقالة وظائف Excel المدمجة مثل ROW، COLUMN و MOD. فيما يلي بعض التفاصيل حول هذه الوظائف لفهم أفضل لمقتطف الكود المقدم فيما بعد.

- تتضمن دالة **ROW()** إرجاع رقم الصف لمرجع خلية. إذا تم الاستغناء عن معلمة المرجع، فهي تفترض أن المرجع هو عنوان الخلية التي تم إدخال دالة ROW فيها.
- تتضمن دالة **COLUMN()** إرجاع رقم العمود لمرجع خلية. إذا تم الاستغناء عن معلمة المرجع، فهي تفترض أن المرجع هو عنوان الخلية التي تم إدخال دالة COLUMN فيها.
- تقوم وظيفة **MOD()** بإرجاع الباقي بعد قسمة العدد على المقسوم، حيث يكون العدد الأول للوظيفة هو القيمة العددية التي ترغب في العثور على باقيها والمعامل الثاني هو العدد المستخدم للقسمة في المعامل الأول للوظيفة. إذا كان المقسوم هو 0، فسيعيد الخطأ #DIV/0!.

لنبدأ بكتابة بعض الرموز لتحقيق هذا الهدف بمساعدة Aspose.Cells for JavaScript عبر API C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Conditional Formatting</title>
    </head>
    <body>
        <h1>Conditional Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, Utils } = AsposeCells;

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
            // Create an instance of Workbook
            const book = new Workbook();

            // Access the first worksheet
            const sheet = book.worksheets.get(0);

            // Add FormatConditions to the instance of Worksheet
            let idx = sheet.conditionalFormattings.add();

            // Access the newly added FormatConditions via its index
            const conditionCollection = sheet.conditionalFormattings.get(idx);

            // Define a CellsArea on which conditional formatting will be applicable (A1 to I20)
            const area = CellArea.createCellArea("A1", "I20");

            // Add area to the instance of FormatConditions
            conditionCollection.addArea(area);

            // Add a condition to the instance of FormatConditions (Expression type)
            idx = conditionCollection.addCondition(AsposeCells.FormatConditionType.Expression);

            // Access the newly added FormatCondition via its index
            const formatCondition = conditionCollection.get(idx);

            // Set the formula for the FormatCondition
            formatCondition.formula1 = "=MOD(ROW(),2)=0";

            // Set the background color and pattern for the FormatCondition's Style
            formatCondition.style.backgroundColor = AsposeCells.Color.Blue;
            formatCondition.style.pattern = AsposeCells.BackgroundType.Solid;

            // Save the result and provide a download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


يوضح المثال التالي لقطة للجدول النهائي المحمّل في تطبيق Excel.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

من أجل تطبيق التظليل على الأعمدة البديلة، كل ما عليك فعله هو تغيير الصيغة **=MOD(ROW(),2)=0** إلى **=MOD(COLUMN(),2)=0**، أي؛ بدلاً من الحصول على فهرس الصف، قم بتعديل الصيغة لاسترجاع فهرس العمود.  
جدول البيانات الناتج، في هذه الحالة، سيظهر كما يلي.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
