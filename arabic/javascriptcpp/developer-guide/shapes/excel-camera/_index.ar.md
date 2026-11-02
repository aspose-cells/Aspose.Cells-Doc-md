---
title: كاميرا Excel في Aspose.Cells for JavaScript via C++
linktitle: كاميرا Excel في Aspose.Cells for JavaScript via C++
description: تعلّم كيفية استخدام كاميرا Excel في Aspose.Cells for JavaScript via C++ لإنشاء صورة ديناميكية مرتبطة بنطاق من الخلايا تتحدث تلقائيًا عند تغير بيانات المصدر وتحافظ على جميع تنسيقات المصدر.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, كاميرا Excel, صورة ديناميكية, صورة مرتبطة, picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /ar/javascript-cpp/excel-camera/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

تمثّل كاميرا Excel كائنًا مخصصًا لورقة العمل يعرض صورة حيّة لنطاق من الخلايا ويطفو على طبقة الرسم، تمامًا مثل صورة عادية. يدعم Aspose.Cells وضعين للإنشاء: صورة ديناميكية تتحدث تلقائيًا كلما تغيرت بيانات المصدر، وصورة ثابتة تلتقط لقطة واحدة لنطاق. يوضح هذا المقال كلا النهجين لتتمكن من اختيار النهج الذي يناسب تخطيطك.

## ما هي كاميرا Excel؟
كاميرا Excel هي في الأساس كائن `Picture` مثبت عند صف وعمود محددين في طبقة الرسم الخاصة بورقة العمل. وبخلاف الصورة العادية المدرجة، ترتبط الكاميرا بنطاق مصدر من خلال صيغة بنمط A1 مثل `"A1:F10"`. كلما تغيرت أي خلية داخل هذا النطاق، تتحدث صورة الكاميرا تلقائيًا لتعرض المحتوى الجديد. تحافظ الكاميرا على كامل تنسيق منطقة المصدر — الحدود وألوان الخلفية والخطوط وتنسيقات الأرقام — بحيث يظهر كل ما يمكن رؤيته داخل الخلايا داخل صورة الكاميرا أيضًا. وهذا يجعل الكاميرا مفيدة بشكل خاص للوحات المعلومات والملخصات والألواح الجانبية وتخطيطات التقارير، حيث تريد معاينة مرئية لمنطقة أخرى في ورقة العمل دون الحاجة إلى التمرير أو تكرار البيانات. هناك أمران يجب مراعاتهما: يجب استدعاء `updateSelectedValue()` قبل حفظ المصنف، ويجب تصدير الملف إلى HTML أو PDF، لأن تنسيقَي HTML وPDF يعتمدان على بيانات الصورة المضمّنة بدلاً من إعادة الحساب مباشرة.

## الطريقة 1 — إضافة صورة كاميرا ديناميكية
الكاميرا الديناميكية هي النهج الأكثر شيوعًا والأقرب إلى أداة الكاميرا المدمجة في Excel. تعمل عن طريق إضافة صورة بلا محتوى أولي، ثم تعيين خاصية `formula` بحيث تشير إلى نطاق المصدر. بعد تعيين الصيغة، يحدّث استدعاء `updateSelectedValue()` بيانات الصورة المضمّنة حتى تتزامن مع الخلايا التي تعكسها. لا تُوفر الكاميرا فئة مخصصة، بل تُبنى بالكامل على النوع القياسي `Picture`.
أهم واجهات API المستخدمة هي:
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, null)` — يضيف صورة مثبتة عند الصف والعمود المحددين. يؤدي تمرير `null` لمعامل الصورة إلى إنشاء صورة فارغة تعمل كعنصر نائب لكاميرا ديناميكية. ويُعيد الطريقة فهرس الصورة الجديدة.
- `worksheet.getPictures().get(index)` — يسترجع كائن `Picture` محددًا من المجموعة.
- `picture.formula` — خاصية من نوع سلسلة نصية تحتوي على مرجع بنمط A1 لنطاق المصدر الذي تعكسه الكاميرا، مثل `"A1:F10"`.
- `picture.updateSelectedValue()` — طريقة لا تُرجع قيمة، وتحدّث بيانات الصورة المضمّنة من الخلايا التي تشير إليها `formula`.

{{% alert color="primary" %}}
يجب استدعاء `updateSelectedValue()` قبل الحفظ عندما يكون الإخراج بصيغة HTML أو PDF؛ وإلا فلن يحتوي الملف المُصدَّر على بيانات الصورة، وستظهر الكاميرا فارغة في الإخراج المعروض.
ينشئ الكود التالي مصنفًا، ويضيف صورة فارغة مثبتة عند الصف 10 والعمود 6، ويربطها بنطاق المصدر `A1:F10` من خلال الخاصية `formula`، ويحدّث بيانات الصورة المضمّنة، ويحفظ المصنف.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // الكاميرا الديناميكية: أضف صورة فارغة، واربطها عبر الصيغة إلى A1:F10، ثم حدّثها
            const pictures = worksheet.pictures;
            const index = pictures.add(10, 6, null);
            const picture = pictures.get(0);
            picture.formula = "A1:F10";
            picture.updateSelectedValue();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_dynamic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## الطريقة 2 — إضافة صورة كاميرا ثابتة
الكاميرا الثابتة هي في الأساس معاينة مصوّرة لمرة واحدة لنطاق من الخلايا. وبدلاً من الحفاظ على ارتباط مباشر، يُصيَّر النطاق إلى بايتات صورة مرة واحدة، وتُغلَّف هذه البايتات في `Buffer`، ثم تُضاف كصورة عادية. يُثبَّت محتوى الصورة عند لحظة الإنشاء ولا يتحدث تلقائيًا عند تغير خلايا المصدر.
أهم واجهات API المستخدمة هي:
- `cells.createRange(address)` — ينشئ كائن `Range` من عنوان بنمط A1 مثل `"A1:F10"`.
- `range.toImage(options)` — يُصيّر النطاق إلى بايتات صورة. يؤدي تمرير `null` إلى استخدام خيارات التصيير الافتراضية؛ وتتوفر تحميلات متعددة للدالة تتيح تحكمًا أدق في الإخراج.
- `Buffer.from(imageBytes)` — يغلّف بايتات الصورة المصوّرة في كائن `Buffer` يمكن تمريره إلى `worksheet.getPictures().add`.
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, imageBuffer)` — يضيف الصورة المثبتة عند الصف والعمود المحددين، مع تمرير `Buffer` الناتج عن التصيير هذه المرة.
ينشئ الكود التالي مصنفًا، ويبني كائن `Range` لـ `A1:F10`، ويصيّره إلى بايتات صورة عبر `range.toImage(null)`، ويغلّف البايتات في `Buffer`، ويضيف الصورة المثبتة عند الصف 10 والعمود 6، ويحفظ المصنف.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // كاميرا ثابتة: إنشاء النطاق، وعرضه إلى بايتات، ولفه في MemoryStream، وإضافته كصورة
            const range = worksheet.cells.createRange("A1:F10");
            const imageData = range.toImage();
            const pictures = worksheet.pictures;
            pictures.add(10, 6, imageData);
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_static.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## الاختيار بين الكاميرا الديناميكية والثابتة
- **الكاميرا الديناميكية:** تتحدث عند كل إعادة حساب، وتتيح تصدير الملف إلى HTML وPDF بعد `updateSelectedValue()`، وتحافظ على سلوك الارتباط المباشر طوال دورة حياة الملف.
- **الكاميرا الثابتة:** نتيجة تصيير واحدة لا تتحدث أبدًا، وهي مفيدة عندما تريد لقطة بصرية ثابتة مضمّمة وقت البناء بدلًا من مرآة حية للبيانات.
يدعم Aspose.Cells كلا من كاميرا ديناميكية تتحدث تلقائيًا، مبنية على `picture.formula` مع `updateSelectedValue()`، وكاميرا ثابتة ذات تصيير واحد، مبنية على `range.toImage` مع `Buffer`. اختر النهج الديناميكي عندما يحتاج إخراجك إلى البقاء متزامنًا مع خلايا المصدر، واختر النهج الثابت عندما تحتاج فقط إلى لقطة بصرية ثابتة وقت البناء.

## مقالات ذات صلة
- [تحويل Sparkline إلى صورة وHTML في Aspose.Cells for JavaScript via C++](/cells/ar/javascript-cpp/convert-sparkline-to-image-and-html/)
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for JavaScript via C++](/cells/ar/javascript-cpp/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for JavaScript via C++](/cells/ar/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}