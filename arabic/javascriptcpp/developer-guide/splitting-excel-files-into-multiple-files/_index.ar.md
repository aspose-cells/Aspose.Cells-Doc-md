---
title: تقسيم ملفات Excel إلى ملفات متعددة
linktitle: تقسيم ملفات Excel إلى ملفات متعددة
description: Aspose.Cells for JavaScript via C++ هي مكتبة جافا سكريبت عبر C++ للعمل مع ملفات جداول البيانات، وتدعم تقسيم ملف Excel واحد إلى ملفات متعددة. ستُظهر هذه المقالة كيفية تقسيم ملفات Excel بنسخ كل ورقة عمل إلى مصنف منفصل ومن خلال نسخ نطاقات خلايا محددة إلى مصنفات أخرى.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++ library, جدول بيانات, تقسيم ملف Excel, نسخ ورقة عمل, نسخ نطاق, مصنفات متعددة, حفظ كملفات منفصلة
type: docs
weight: 195
url: /ar/javascript-cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ يدعم تقسيم ملف Excel واحد إلى ملفات متعددة. هناك طريقتان رئيسيتان للقيام بذلك: (1) بنسخ كل ورقة عمل من المصنف المصدر إلى مصنف جديد وحفظ كل منها كملف منفصل، و(2) بنسخ نطاق خلايا محدد من ورقة عمل إلى مصنف جديد. كلا النهجين مفيدان عندما تحتاج إلى توزيع أجزاء من البيانات، إنشاء تقارير أصغر لجهات مختلفة، أو عزل البيانات للمعالجة الفردية.
{{% /alert %}}

## **مقدمة**
هناك العديد من السيناريوهات الواقعية حيث يحتاج المطور إلى تقسيم ملف Excel واحد إلى عدة ملفات أصغر. على سبيل المثال، قد يحتوي المصنف على ورقة عمل واحدة لكل قسم، ويحتاج كل رئيس قسم إلى استلام ورقته فقط. في حالات أخرى، قد ترغب في استخراج جدول أو كتلة بيانات معينة من ورقة عمل وإرسالها كملف مستقل عبر البريد الإلكتروني دون الكشف عن باقي المصنف. قد تحتاج المصنفات الكبيرة المجمعة أيضًا إلى تقسيم إلى أجزاء أصغر لتسهيل المعالجة، تسريع التحميل، أو المعالجة اللاحقة بواسطة أنظمة أخرى.
Aspose.Cells for JavaScript via C++ يوفر طريقتين مرنتين لهذه المهمة. الطريقة الأولى تقوم بالتكرار عبر كل ورقة عمل في المصنف المصدر وتنسخ محتواها إلى نسخة جديدة تمامًا من فئة `Workbook`، مع حفظ كل واحدة كملف منفصل. الطريقة الثانية تركز على نطاق خلايا محدد داخل ورقة عمل وتنسخ ذلك النطاق فقط إلى مصنف جديد. في الحالتين، سير العمل العام هو نفسه: تحميل المصنف المصدر باستخدام فئة `Workbook`، الوصول إلى البيانات ذات الصلة عبر كائنات `Worksheet` و`Cells`، نقل المحتوى إلى مصنف الوجهة `Workbook`، ثم حفظ الوجهة على القرص.

## **تقسيم ملف Excel بنسخ كل ورقة عمل إلى مصنف جديد**

### **نظرة عامة على النهج**
في هذا النهج، يتم فتح المصنف المصدر مرة واحدة، ثم لكل `Worksheet` في مجموعة `Worksheets` الخاصة به، يتم إنشاء `Workbook` وجهة جديد. يتم بعد ذلك نسخ محتوى ورقة العمل المصدر إلى ورقة العمل الأولى في المصنف الوجهة، ويُحفظ المصنف الوجهة كملف يُستمد اسمه من اسم ورقة العمل المصدر. النتيجة هي ملف إخراج واحد لكل ورقة عمل، بحيث يحتوي كل ملف على بيانات ورقة المصدر الواحدة.
هذه الطريقة هي الاختيار المناسب عندما تمثل كل ورقة عمل في المصنف المصدر وحدة معلومات مستقلة منطقياً (مثل قسم، منطقة، شهر، أو خط إنتاج) وتريد تسليم أو معالجة كل وحدة على حدة.

### **الخطوات**
1. فتح ملف Excel المصدر بإنشاء كائن `Workbook` وتمرير مسار الملف إلى المُنشئ الخاص به.  
2. التكرار عبر مجموعة `Workbook.Worksheets` باستخدام حلقة `for` أو `for...of` بحيث يتم معالجة كل `Worksheet` في الملف المصدر.  
3. داخل الحلقة، إنشاء كائن `Workbook` جديد للوجهة (مصنف فارغ) للورقة الحالية.  
4. نسخ محتوى ورقة العمل المصدر إلى ورقة العمل الوجهة. يمكن القيام بذلك عبر تكرار خلايا مجموعة `Cells` الخاصة بورقة العمل المصدر وكتابة قيمها في الخلايا المقابلة في ورقة العمل الوجهة، أو باستخدام طريقة `Cells.Copy` لنقل نطاق كامل مرة واحدة.  
5. إنشاء مسار ملف إخراج يدمج اسم ورقة العمل المصدر (مثال: `dataDir + worksheet.Name + ".xls"` ) لضمان أن يكون لكل ملف مُولد اسم فريد.  
6. استدعاء طريقة `Workbook.Save` للمصنف الوجهة لكتابة الملف إلى القرص.  
7. تكرار الخطوات 3 إلى 6 للورقة التالية حتى يتم معالجة جميع أوراق العمل.

### **Code Example**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls" />
        <button id="runExample">Run Example</button>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                const result = document.getElementById('result');
                try {
                    const fileInput = document.getElementById('fileInput');
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an .xls file.</p>';
                        return;
                    }
                    result.innerHTML = '<p>Processing...</p>';
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    const downloadLinks = document.createElement('div');
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const sourceSheet = workbook.worksheets.get(i);
                        const sheetName = sourceSheet.name;
                        const destWorkbook = new Workbook();
                        const destIndex = destWorkbook.worksheets.add();
                        const destSheet = destWorkbook.worksheets.get(destIndex);
                        destSheet.name = sheetName;
                        destSheet.copy(sourceSheet);
                        const outputData = destWorkbook.save(AsposeCells.SaveFormat.Excel97To2003);
                        const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
                        const downloadLink = document.createElement('a');
                        downloadLink.href = URL.createObjectURL(blob);
                        downloadLink.download = `${sheetName}.xls`;
                        downloadLink.textContent = `Download ${sheetName}.xls`;
                        downloadLink.style.display = 'block';
                        downloadLink.style.marginTop = '8px';
                        downloadLinks.appendChild(downloadLink);
                    }
                    result.innerHTML = '<p style="color: green;">Done! Click a download link to get the result file.</p>';
                    result.appendChild(downloadLinks);
                } catch (error) {
                    console.error(error);
                    const errorMessage = document.createElement('p');
                    errorMessage.style.color = 'red';
                    errorMessage.textContent = `Error: ${error instanceof Error ? error.message : error}`;
                    result.replaceChildren(errorMessage);
                }
            });
        </script>
    </body>
</html>
```

النتيجة المتوقعة هي مجموعة من الملفات الجديدة في دليل البيانات، ملف واحد لكل ورقة عمل من المصنف المصدر. كل ملف يُسمّى باسم ورقة المصدر المقابلة، ويحتوي على البيانات (وبإمكانك إضافة التنسيق إذا رغبت) لتلك الورقة الوحيدة.

## **تقسيم ملف Excel بنسخ نطاق إلى مصنف جديد**

### **نظرة عامة على النهج**
في بعض الأحيان لا يتطابق البيانات التي تحتاج إلى تقسيمها مع ورقة عمل كاملة، بل مع منطقة مستطيلة محددة داخل ورقة العمل، مثل `A1:D10` أو نطاق مسمى يمثل جدولًا معينًا. في هذه الحالات، يكون نسخ أوراق العمل بالكامل إهدارًا، ويتطلب نهجًا أكثر دقة: تحديد النطاق المصدر، نسخ ذلك النطاق فقط إلى مصنف جديد، وحفظ الملف الجديد.
هذا النهج مثالي عندما تريد استخراج جدول واحد، أو كتلة تقرير، أو منطقة بيانات من ورقة عمل أكبر مع حذف كل المحتوى غير المتعلق. كما أنه مفيد لتصدير المناطق التي يحددها المستخدم من ورقة كملفات مستقلة.

### **الخطوات**
1. فتح ملف Excel المصدر بإنشاء كائن `Workbook` مع مسار الملف.  
2. استرجاع `Worksheet` المستهدف الذي يحتوي على النطاق الذي تريد نسخه، إما عبر الفهرس (مثال: الورقة الأولى) أو عبر الاسم من مجموعة `Worksheets`.  
3. تحديد النطاق المراد نسخه. ويمكن أن يكون نطاقًا ثابتًا مثل `A1:C10`، أو نطاقًا مسمى يتم الحصول عليه عبر مجموعة `Worksheet.Cells`، أو نطاقًا تم إنشاؤه عبر `Worksheet.Cells.CreateRange`.  
4. إنشاء كائن `Workbook` جديد للوجهة.  
5. الوصول إلى أول `Worksheet` في المصنف الوجهة (الورقة الافتراضية).  
6. نسخ النطاق المصدر إلى ورقة العمل الوجهة، عادةً بدءًا من الخلية `A1`. يمكن استخدام طريقة `Cells.Copy` على مجموعة `Cells` الخاصة بالوجهة لنسخ نطاق كامل، أو يمكنك تكرار خلايا النطاق المصدر وكتابة قيمها في خلايا الوجهة باستخدام `PutValue`. يمكن توفير `CopyOptions` اختيارية للتحكم فيما يتم نقله (قيم فقط، قيم وتنسيقات، صيغ، وما إلى ذلك).  
7. حفظ المصنف الوجهة إلى مسار ملف جديد على القرص باستخدام طريقة `Workbook.Save`.

### **Code Example**
النتيجة المتوقعة هي ملف جديد واحد في دليل البيانات يحتوي فقط على القيم (وبإمكانك إضافة التنسيق إذا رغبت) للنطاق المحدد المستخرج من المصنف المصدر. لا يرتبط ملف الوجهة بأي بيانات أخرى في الملف المصدر؛ فهو يحتوي فقط على النطاق المستخرج، بدءًا من الخلية `A1` في أول ورقة عمل له.

## **المقالات ذات الصلة**
- [إضافة حقول الفلتر إلى جدول محوري في Aspose.Cells for JavaScript via C++](/cells/ar/javascript-cpp/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for JavaScript via C++](/cells/ar/javascript-cpp/apply-style-to-pivot-table/)
- [تعديل تخطيط حقل الصفحة في جدول محوري](/cells/ar/javascript-cpp/change-page-field-layout/)
- [تحويل Sparkline إلى صورة وHTML في Aspose.Cells for JavaScript via C++](/cells/ar/javascript-cpp/convert-sparkline-to-image-and-html/)
- [تحويل Excel إلى صيغة OFD](/cells/ar/javascript-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="javascript-cpp" >}}