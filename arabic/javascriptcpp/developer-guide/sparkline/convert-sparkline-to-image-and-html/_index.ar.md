---
title: تحويل الخط المصغّر إلى صورة وHTML في Aspose.Cells for JavaScript via C++
linktitle: تحويل الخط المصغّر إلى صورة وHTML في Aspose.Cells for JavaScript via C++
description: تعلم كيفية عرض الخطوط المصغرة في Aspose.Cells كصور مستقلة لتضمينها في الخلايا، وتصدير أوراق العمل التي تحتوي على الخطوط المصغرة إلى HTML باستخدام HtmlSaveOptions.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, الخطوط المصغرة, sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, عرض الخطوط المصغرة, تحويل الخط المصغّر إلى صورة, تصدير الخط المصغّر إلى HTML
type: docs
weight: 120
url: /ar/javascript-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
الخطوط المصغرة هي رسوم بيانية مصغرة تُوضع داخل خلايا أوراق العمل. يتيح لك Aspose.Cells استخراج كل خط مصغّر كصورة مستقلة (للتضمين في خلية أخرى أو تقرير خارجي)، كما يتيح لك تصدير ورقة العمل التي تحتوي على الخطوط المصغرة إلى HTML للتوزيع عبر المتصفح. تتوفر خاصية `cell.embeddedImage` المستخدمة في هذه المقالة في **Aspose.Cells 26.5 والإصدارات الأحدث**.
{{% /alert %}}

## **مقدمة**
تُعد الخطوط المصغرة طريقة مضغوطة لتصور الاتجاهات مباشرة داخل ورقة العمل. ورغم أن مستخدمي Excel يرونها في مواضعها، تتطلب كثير من السيناريوهات الواقعية أن ينتقل الخط المصغّر خارج الخلية — على سبيل المثال، ليُضمَّن في خلية أخرى كصورة ثابتة، أو يُرفق برسالة بريد إلكتروني آلية، أو يُعرض كجزء من تقرير HTML يُنشر على الويب.
يدعم Aspose.Cells هاتين العمليتين. تُعرض طريقة `sparkline.toImage` الخط المصغّر الفردي في هيئة `Buffer`، ويمكن تعيين البايتات الناتجة إلى `cell.embeddedImage` ليُخزَّن الصورة داخل خلية واحدة في المصنف. وبالإضافة إلى ذلك، تتيح لك `HtmlSaveOptions` تحويل المصنف بأكمله — بما في ذلك الخطوط المصغرة — إلى ملف HTML مستقل بذاته. يشرح هذا المقال كلا سيرَي العمل من البداية إلى النهاية.

## **سير العمل 1 — تحويل الخطوط المصغرة إلى صور وتضمينها في الخلايا**
في هذا سير العمل، ستنشئ ورقة عمل تحتوي على نطاق صغير من القيم المصدرية، وتضيف ثلاث مجموعات من الخطوط المصغرة بأنواع مختلفة (Line وColumn وStacked/Win-Loss) إلى هذا النطاق، وتحوّل كل مجموعة إلى صورة PNG، ثم تكتب بايتات PNG في الخلايا المجاورة كصور مضمَّنة. والنتيجة ملف `.xlsx` واحد يحتوي على الخطوط المصغرة الحية، إلى جانب الصور الثابتة المقابلة لها.

### **تعليمات خطوة بخطوة**
1. أنشئ `Workbook` جديدًا واحصل على مرجع إلى أول `Worksheet`.
2. املأ الخلايا `A1` إلى `E1` بخمس قيم رقمية نموذجية (على سبيل المثال، المبيعات اليومية أو قراءات الحرارة).
3. أضف ثلاثة كائنات من نوع `SparklineGroup` إلى ورقة العمل من خلال استدعاء `worksheet.getSparklineGroups().add(...)`:
   - مجموعة من نوع `SparklineType.Line` مرتبطة بالخلية `F1`، باستخدام نطاق البيانات `A1:E1`.
   - مجموعة من نوع `SparklineType.Column` مرتبطة بالخلية `G1`، باستخدام نطاق البيانات `A1:E1`.
   - مجموعة من نوع `SparklineType.Stacked` (فوز/خسارة) مرتبطة بالخلية `H1`، باستخدام نطاق البيانات `A1:E1`.
4. أنشئ كائن `ImageOrPrintOptions` واضبط الخاصية `imageType` على `ImageType.Png` حتى يُعرض كل خط مصغّر في صورة PNG.
6. احفظ المصنف باسم `output_with_sparklines.xlsx`.

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
        const { Workbook, CellArea, ImageOrPrintOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // ملء بيانات العينة في الخلايا A1:E1
            cells.get("A1").value = 5;
            cells.get("B1").value = -3;
            cells.get("C1").value = 8;
            cells.get("D1").value = -2;
            cells.get("E1").value = 6;
            // إضافة مجموعة Sparkline من النوع Line مثبتة عند F1 (العمود 5، الصف 0)
            const lineArea = new CellArea();
            lineArea.startColumn = 5;
            lineArea.endColumn = 5;
            lineArea.startRow = 0;
            lineArea.endRow = 0;
            const lineIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Line,
                "A1:E1",
                false,
                lineArea
            );
            // إضافة مجموعة Sparkline من النوع Column مثبتة عند G1 (العمود 6، الصف 0)
            const columnArea = new CellArea();
            columnArea.startColumn = 6;
            columnArea.endColumn = 6;
            columnArea.startRow = 0;
            columnArea.endRow = 0;
            const columnIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Column,
                "A1:E1",
                false,
                columnArea
            );
            // إضافة مجموعة Sparkline من النوع Win/Loss (Stacked) مثبتة عند H1 (العمود 7، الصف 0)
            const stackedArea = new CellArea();
            stackedArea.startColumn = 7;
            stackedArea.endColumn = 7;
            stackedArea.startRow = 0;
            stackedArea.endRow = 0;
            const stackedIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Stacked,
                "A1:E1",
                false,
                stackedArea
            );
            // configuring image options for PNG output
            const imageOptions = new ImageOrPrintOptions();
            imageOptions.imageType = AsposeCells.ImageType.Png;
            // Convert the Line sparkline to image and embed it in cell F2
            const lineSp = worksheet.sparklineGroups.get(lineIdx).sparklines.get(0);
            cells.get("F2").embeddedImage = lineSp.toImage(imageOptions);
            // Convert the Column sparkline to image and embed it in cell G2
            const columnSp = worksheet.sparklineGroups.get(columnIdx).sparklines.get(0);
            cells.get("G2").embeddedImage = columnSp.toImage(imageOptions);
            // Convert the Win/Loss sparkline to image and embed it in cell H2
            const stackedSp = worksheet.sparklineGroups.get(stackedIdx).sparklines.get(0);
            cells.get("H2").embeddedImage = stackedSp.toImage(imageOptions);
            // Save the workbook to disk
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_with_sparklines.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

يُنتج الكود أعلاه مصنفًا يحتوي كل تمثيل بصري للخط المصغّر في شكلين: الخط المصغّر الحي المرتبط بخلية في الصف 1، وصورة PNG ثابتة مضمَّنة مباشرةً في خلية مجاورة في الصف 2. ولأن الصور مخزنة داخل الملف نفسه، يظل المصنف ملفًا واحدًا مستقلًا يمكن إرساله بالبريد الإلكتروني أو أرشفته من دون أن تتعطل مراجع الصور المضمَّنة.

{{% alert color="primary" %}}
لأن كل مجموعة من الخطوط المصغرة مرتبطة بخلية واحدة، يمكنك الوصول إلى الخط المصغّر الخاص بها عبر المفهرس `group.getSparklines()[0]` بدلًا من المرور على عناصر المجموعة. ويُبقي هذا كود العرض قصيرًا ويتوافق مع النمط المعتاد «خط مصغّر واحد لكل خلية تثبيت». ويتطلب تخزين بايتات الصورة عبر `cell.embeddedImage` إصدار Aspose.Cells 26.5 أو أحدث.
{{% /alert %}}

## **سير العمل 2 — تصدير ورقة العمل التي تحتوي على خطوط مصغرة إلى HTML**
بمجرد أن يحتوي المصنف على خطوط مصغرة حية (واختياريًا صور ثابتة مقابلة لها)، يمكن نشر ورقة العمل بالكامل على الويب بحفظها بتنسيق HTML. تتيح لك فئة `HtmlSaveOptions` الخصائص اللازمة للتحكم في هذا التصدير؛ وفي هذا سير العمل، ستعيد استخدام الملف `output_with_sparklines.xlsx` الذي أنشأه سير العمل 1 وتحوّله إلى مستند HTML نظيف من صفحة واحدة.

### **تعليمات خطوة بخطوة**
1. تأكد من توفّر الملف `output_with_sparklines.xlsx` الذي أنشأه سير العمل 1 على القرص في دليل العمل الخاص بك.
2. حمّل هذا الملف في نسخة جديدة من `Workbook`.
3. أنشئ كائن `HtmlSaveOptions` واضبط الخاصية `exportActiveWorksheetOnly` على `true` بحيث يحتوي ملف HTML الناتج على ورقة العمل النشطة فقط بدلًا من المصنف بأكمله.
4. استدعِ `workbook.save("sparklines.html", htmlOptions)` لكتابة مخرجات HTML على القرص.

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
        const { Workbook, HtmlSaveOptions } = AsposeCells;
        AsposeCells.onReady({
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
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const htmlOptions = new HtmlSaveOptions();
                htmlOptions.exportActiveWorksheetOnly = true;
                const outputData = workbook.save(AsposeCells.SaveFormat.Html, htmlOptions);
                const blob = new Blob([outputData], { type: "text/html" });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "sparklines.html";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

يحوّل الكود أعلاه مصنف الخطوط المصغرة الذي أنشأه سير العمل 1 إلى ملف HTML قابل للنقل. وتُعرض مجموعات الخطوط المصغرة كصور مُضمَّنة داخل جدول HTML المُنشأ، مما يتيح للمستخدمين النهائيين عرض الاتجاهات في أي متصفح حديث دون الحاجة إلى تثبيت Excel. وبضبط `exportActiveWorksheetOnly` على `true`، تتجنب عن طريق الخطأ نشر الأوراق المخفية أو البيانات المساعدة؛ إذ تُصدَّر ورقة العمل الظاهرة للمستخدم حاليًا فقط.

{{% alert color="primary" %}}
تقدّم فئة `HtmlSaveOptions` خصائص إضافية لضبط المخرجات، مثل `exportHiddenWorksheet` و`exportImagesAsBase64` و`encoding`. اضبطها حسب متطلبات بيئة النشر.
{{% /alert %}}

## **ملخص API**
تعتمد إجراءات سير العمل أعلاه على مجموعة صغيرة من واجهات API في Aspose.Cells تعمل معًا.
- تُستخدم `SparklineGroup` وواجهة الوصول إلى المجموعة `worksheet.getSparklineGroups()` لتعريف نوع كل مجموعة (Line وColumn وStacked)، ونطاق البيانات، وخلية التثبيت الخاصة بها. في هذه المقالة، ترتبط كل مجموعة بخلية واحدة، لذا يتم الوصول إليها عبر `worksheet.getSparklineGroups()[i]`.
- يمثل `Sparkline` الخط المصغّر داخل المجموعة، ويمكن الوصول إليه عبر المفهرس `group.getSparklines()[0]`. ولأن كل مجموعة في المثال تحتوي على خط مصغّر واحد بالضبط، لا يلزم استخدام حلقة تكرار.
- تُعد `sparkline.toImage(imageOrPrintOptions)` طريقة العرض التي تُعيد صورة الخط المصغّر في هيئة `Buffer`. ويمكن تعيين البايتات المعادة مباشرةً إلى `cell.embeddedImage`.
- يقصر `HtmlSaveOptions.exportActiveWorksheetOnly` (قيمة منطقية) تصدير HTML على ورقة العمل النشطة. وهو إحدى الخصائص الأكثر استخدامًا في `HtmlSaveOptions` عند إنشاء تقارير من صفحة واحدة.
- يحدد `ImageOrPrintOptions.imageType` تنسيق الصورة (على سبيل المثال، `ImageType.Png`) المستخدم عند العرض عبر `toImage` وعند طباعة أوراق العمل كصور.

{{< app/cells/assistant language="javascript-cpp" >}}