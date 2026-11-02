---
title: إدراج صورة في خلية
linktitle: إدراج صورة في خلية
description: Aspose.Cells for JavaScript via C++ هي مكتبة للعمل مع ملفات جداول البيانات. يوضح هذا المقال كيفية ضبط صورة لتلائم خلية واحدة بدقة، إما بوضع صورة عائمة فوق الخلية أو بتضمين الصورة مباشرةً داخلها.
keywords: Aspose.Cells, مكتبة JavaScript عبر C++, جدول بيانات, إدراج صورة, تضمين صورة, صورة في خلية, ملاءمة صورة للخلية, Pictures, EmbeddedImage
type: docs
weight: 80
url: /ar/javascript-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
توفر Aspose.Cells طريقتين متميزتين لربط صورة بخلية واحدة. الصورة العائمة شكل في طبقة رسم ورقة العمل يتراكب بصريًا فوق نطاق من الخلايا، بينما تُخزَّن الصورة المضمَّنة داخل الخلية نفسها وتُحجَّم تلقائيًا لتلائم منطقة العرض الخاصة بالخلية. اختر الأسلوب الأنسب لمتطلبات تخطيطك.
{{% /alert %}}

## **مقدمة**
تُعد ملاءمة صورة بدقة مع خلية واحدة متطلبًا شائعًا عند تصميم جداول بيانات تؤدي دور تقارير بصرية أو فهارس منتجات أو أدلة موظفين أو لوحات معلومات أو قوائم مخزون. بدلاً من تمديد صورة عبر خلايا متعددة أو وضعها على ورقة العمل دون ربطها بدقة، قد ترغب في صورة مرتبطة بالخلية ونظيفة تحافظ على محاذاتها مع الخلية التي تنتمي إليها.
تدعم Aspose.Cells هذا السيناريو بطريقتين متكاملتين:
- **الأسلوب 1 — وضع صورة عائمة فوق خلية.** أضف `Picture` إلى ورقة العمل، وحدِّد موضعه باستخدام `picture.setPlacement(PlacementType.MoveAndSize)`، واضبط خلايا ارتساء الصورة من خلال `picture.setUpperLeftRow()` و`picture.setUpperLeftColumn()` و`picture.setLowerRightRow()` و`picture.setLowerRightColumn()` بحيث تغطي الصورة خلية واحدة بالضبط.
- **الأسلوب 2 — تضمين صورة مباشرة في خلية.** أسند `Buffer` يحتوي على بيانات الصورة إلى الخلية باستخدام `cell.setEmbeddedImage(imageBuffer)`. تُحجَّم الصورة تلقائيًا لتلائم منطقة عرض الخلية وتنتقل مع الخلية.
يتناول بقية هذا المقال الأسلوبين، ويشرح واجهات برمجة التطبيقات (API) ذات الصلة، ويوضح كيفية استخدامها في التعليمات البرمجية.

## **الأسلوب 1: وضع صورة عائمة فوق خلية**
الصورة العائمة هي كائن `Picture` موجود في طبقة رسم ورقة العمل. وهي ليست جزءًا من أي خلية مفردة، لكنها مرتبطة بنطاق من الخلايا. خلايا ارتساء الصورة — أي ركنها الأيسر العلوي وركنها الأيمن السفلي — تحدد امتدادها المرئي على ورقة العمل. افتراضيًا، تمتد الصورة المضافة حديثًا عبر عدة خلايا.
لجعل صورة عائمة تغطي **خلية واحدة بالضبط**، عليك:
1. أضف الصورة باستخدام `worksheet.getPictures().add(row, column, imageBuffer)`، حيث يكون `imageBuffer` من نوع `Buffer` ويحتوي على بيانات الصورة. يربط هذا الاستدعاء الصورة الجديدة بالخلية المحددة.
2. اضبط قيم الارتساء الأربع بحيث يتطابق المستطيل المحيط بالصورة مع الخلية الهدف.
3. استدعِ `picture.setPlacement(PlacementType.MoveAndSize)` حتى تتحرك الصورة وتُغيّر حجمها مع الخلية المرتبطة بها عندما يغيّر المستخدم عرض العمود أو ارتفاع الصف.

### **ارتساء الصورة بخلية واحدة**
تُحدَّد إحداثيات ارتساء الصورة بواسطة أربع دوال وصول ذات فهارس تبدأ من الصفر:
- `picture.getUpperLeftRow()` و`picture.setUpperLeftRow(value)` — فهرس الصف للحافة العلوية للصورة.
- `picture.getUpperLeftColumn()` و`picture.setUpperLeftColumn(value)` — فهرس العمود للحافة اليسرى للصورة.
- `picture.getLowerRightRow()` و`picture.setLowerRightRow(value)` — فهرس الصف للحافة السفلية للصورة. لجعل الحافة السفلية للصورة تقع عند أسفل الصف `r`، اضبط هذه القيمة على `r + 1`.
- `picture.getLowerRightColumn()` و`picture.setLowerRightColumn(value)` — فهرس العمود للحافة اليمنى للصورة. لجعل الحافة اليمنى للصورة تقع عند الحد الأيمن للعمود `c`، اضبط هذه القيمة على `c + 1`.

{{% alert color="primary" %}}
تبدأ ترقيم فهارس الصفوف والأعمدة في Aspose.Cells من الصفر. يكون للخلية C6 فهرس صف قدره 5 وفهرس عمود قدره 2. وتُعد أخطاء الزيادة أو النقص بمقدار واحد في ارتساء الزاوية السفلية اليمنى أكثر الأخطاء شيوعًا التي تجعل الصور تبدو وكأنها تتداخل مع خلية مجاورة.
{{% /alert %}}

### **التحكم في سلوك الموضع**
يستخدم كل من `picture.getPlacement()` و`picture.setPlacement(value)` تعداد `PlacementType` للتحكم في سلوك الصورة عندما يغيّر المستخدم حجم الصف أو العمود الواقع تحتها. القيمة الموصى بها لصورة مرتبطة بخلية واحدة هي `PlacementType.MoveAndSize`، ما يجعل الصورة تتحرك وتُغيّر حجمها مع الخلية المرتبطة بها، مع الحفاظ على الملاءمة الدقيقة.

### **تعليمات خطوة بخطوة**
1. أنشئ مصنفًا جديدًا باستخدام `Workbook` أو افتح مصنفًا موجودًا.
2. احصل على ورقة العمل `Worksheet` الهدف من خلال `workbook.getWorksheets().getAt(0)`.
3. اقرأ ملف الصورة من القرص وأحمِّله في `Buffer`، على سبيل المثال باستخدام `fs.readFileSync` في Node.js.
4. استدعِ `worksheet.getPictures().add(5, 2, imageBuffer)` لإضافة صورة مرتبطة بالخلية C6. تُرجع الطريقة فهرس الصورة الجديدة في مجموعة `Pictures`؛ استخدمه لاسترجاع `Picture` المقابلة.
5. اضبط إحداثيات الارتساء الأربع بحيث تغطي الصورة خلية C6 فقط: `picture.setUpperLeftRow(5)` و`picture.setUpperLeftColumn(2)` و`picture.setLowerRightRow(6)` و`picture.setLowerRightColumn(3)`.
6. استدعِ `picture.setPlacement(PlacementType.MoveAndSize)` للحفاظ على محاذاة الصورة مع C6 عند تغيير عرض العمود أو ارتفاع الصف.
7. اختياريًا، أضف نصًا توضيحيًا إلى الخلايا المجاورة لإظهار أن خلية C6 فقط هي التي تحتوي على الصورة.
8. احفظ المصنف على القرص كملف `.xlsx`.
يوضح الكود التالي هذا الأسلوب بالكامل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,image/png" />
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
            const fileInput = document.getElementById('fileInput');
            const file = fileInput.files[0];
            if (!file) {
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Please select a PNG image.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const imageData = new Uint8Array(await file.arrayBuffer());
            const picIndex = worksheet.pictures.add(5, 2, imageData);
            const picture = worksheet.pictures.get(picIndex);
            picture.upperLeftRow = 5;
            picture.upperLeftColumn = 2;
            picture.lowerRightRow = 6;
            picture.lowerRightColumn = 3;
            picture.placement = AsposeCells.Drawing.PlacementType.MoveAndSize;
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **الأسلوب 2: تضمين صورة مباشرة في خلية**
تتيح Aspose.Cells أيضًا آلية أبسط للصور المرتبطة بالخلايا: طريقة `cell.setEmbeddedImage(imageBuffer)`. وعند إسناد بيانات الصورة بهذه الطريقة، تُرفق الصورة بالخلية نفسها، كما لو كانت عنصرًا مضمَّنًا داخلها.

### **كيف تعمل الصور المضمَّنة**
- تُخزَّن الصورة كجزء من محتوى الخلية بدلاً من تخزينها كشكل في طبقة الرسم.
- تُحجَّم الصورة تلقائيًا لتلائم الحدود المعروضة داخل الخلية. ولا يلزم استخدام إحداثيات ارتساء أو إعدادات موضع.
- تظل الخلية خلية فعلية ذات عنوان فعلي يمكن الإشارة إليها في الصيغ أو فرزها ضمن صف أو استخدامها في عمليات أخرى على مستوى الخلية.
يجعل ذلك `cell.setEmbeddedImage(imageBuffer)` الخيار الأكثر إيجازًا عندما يكون هدفك ببساطة «صورة توجد داخل هذه الخلية».

### **تعليمات خطوة بخطوة**
1. أنشئ مصنفًا جديدًا باستخدام `Workbook` أو افتح مصنفًا موجودًا.
2. احصل على ورقة العمل `Worksheet` الهدف من خلال `workbook.getWorksheets().getAt(0)`.
3. اقرأ ملف الصورة من القرص وأحمِّله في `Buffer`، على سبيل المثال باستخدام `fs.readFileSync` في Node.js.
4. احصل على مرجع للخلية الهدف، إما من خلال `worksheet.getCells().get("C6")` أو `worksheet.getCells().get(5, 2)`.
5. مرّر `Buffer` إلى الخلية باستخدام `cell.setEmbeddedImage(imageBuffer)`.
6. اختياريًا، عدّل ارتفاع الصف المستهدف وعرض العمود المستهدف لجعل الصورة المضمَّنة أكثر وضوحًا.
7. احفظ المصنف على القرص كملف `.xlsx`.
يوضح الكود التالي هذا الأسلوب بالكامل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,.jpg,.jpeg" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const asposeReady = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files || fileInput.files.length === 0) {
                result.innerHTML = '<p style="color: red;">Please select an image file.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // الحصول على الخلية الهدف C6
            const cell = worksheet.cells.get("C6");
            // قراءة ملف الصورة إلى مصفوفة بايتات
            const imageData = new Uint8Array(await fileInput.files[0].arrayBuffer());
            // تضمين الصورة مباشرة في الخلية
            cell.embeddedImage = imageData;
            // اختياريًا، اضبط ارتفاع الصف وعرض العمود لتكون الصورة المضمّنة أكثر وضوحًا
            worksheet.cells.setColumnWidth(2, 30); // العمود C (الفهرس 2)
            worksheet.cells.setRowHeight(5, 100); // الصف 6 (الفهرس 5)
            // حفظ المصنف الناتج كملف ‎.xlsx
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **اختيار الأسلوب المناسب**
ينتج كلا الأسلوبين صورة تناسب خلية واحدة، لكنهما يختلفان في طريقة تخزين الصورة وسلوكها:
- **استخدم صورة عائمة (الأسلوب 1) عندما:**
  - تحتاج إلى تحكم أدق في الموضع أو ترتيب الطبقات أو المحاذاة مع كائنات الرسم الأخرى.
  - تريد أن تتصرف الصورة كشكل يمكن تحديده أو إعادة ترتيبه أو تجميعه مع أشكال أخرى.
  - تحتاج إلى التوافق مع التعليمات البرمجية القديمة التي تعمل بالفعل مع مجموعة `Pictures` التي يتم الوصول إليها عبر `worksheet.getPictures()`.
  - تحتاج إلى حساب إحداثيات الارتساء ديناميكيًا استنادًا إلى تخطيط ورقة العمل.
- **استخدم صورة مضمَّنة (الأسلوب 2) عندما:**
  - تريد أبسط طريقة ممكنة لإدراج صورة في خلية.
  - ينبغي أن تنتقل الصورة مع الخلية مثل أي محتوى آخر في الخلية.

## مقالات ذات صلة
- [كاميرا Excel في Aspose.Cells for JavaScript via C++](/cells/ar/javascript-cpp/excel-camera/)
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for JavaScript via C++](/cells/ar/javascript-cpp/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for JavaScript via C++](/cells/ar/javascript-cpp/apply-style-to-pivot-table/)
- [تحويل Sparkline إلى صورة وHTML في Aspose.Cells for JavaScript via C++](/cells/ar/javascript-cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="javascript-cpp" >}}