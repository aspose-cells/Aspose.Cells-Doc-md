---
title: تحويل ملف XLSX إلى صيغة PDF باستخدام JavaScript عبر C++
linktitle: تحويل ملف XLSX إلى تنسيق PDF
type: docs
weight: 30
url: /ar/javascript-cpp/convert-xlsx-file-to-pdf-format/
description: توضح هذه الدليل كيفية تحويل ملف Excel (XLSX) إلى صيغة PDF باستخدام Aspose.Cells for Java سكربت عبر C++. 
---

{{% alert color="primary" %}}

يمثّل ملف PDF (تنسيق المستندات المحمول) المستندات بشكل مستقل عن البرمجيات والأجهزة ونظام التشغيل المستخدمة في إنشاء تلك المستندات. يمكن أن يكون ملف PDF مستندات تحتوي على أي تجميع من النصوص والرسومات والصور بطريقة مستقلة عن الجهاز ومستقلة عن الدقة. غالبًا ما تكون ملفات PDF مضغوطة، حيث يستغرق حجمها مساحة أقل من الملف الأصلي.

في بعض الأحيان، تحتاج إلى تحويل ملف Microsoft Excel إلى PDF. لذلك، تحتاج إلى حل سريع وآمن ودقيق وموثوق يتيح لك توزيع مستندات PDF حول العالم. هناك العديد من أدوات التحويل التي يمكنها أداء المهمة، لكن عليك التأكد من أن تخطيط المستند الأصلي في Excel يُحتفظ به بدقة في ملف PDF الناتج. يجب أن يتم عرض الصور والرسوم البيانية والأشكال وتنسيقات البيانات والخطوط والميزات وألوان إعدادات الصفحة واتجاه النص والحدود والرسوم البيانية بدقة وبدقة. يضمن [Aspose.Cells](https://products.aspose.com/cells/javascript-cpp/) التحويل بدقة عالية.

تم تصميم هذا المستند لتوفير فهم شامل لكيفية تحويل مستند Microsoft Excel (يحتوي على صور، رسوم بيانية، تنسيقات إلخ) إلى PDF. للقيام بذلك، يوضح كيفية إنشاء تطبيق وحدة التحكم بسيط في JavaScript عبر C++ يحول ملف Excel إلى PDF باستخدام API الخاص بـ Aspose.Cells. يتم إجراء التحويل بدقة وبدقة عالية.

{{% /alert %}}

## **تحويل Excel إلى PDF**

يستخدم هذا المثال ملف Excel (SampleInput.xlsx) كنموذج. يحتوي دفتر العمل على أوراق عمل مع مخططات وصور. كل ورقة تحتوي على أنواع مختلفة من التنسيقات باستخدام الخطوط والصفات والألوان وتأثيرات التظليل والحدود. توجد مخطط عمود على الورقة الأولى وصورة في الأخيرة.

### **ملف Excel القالب**

ملف النموذج يحتوي على ثلاث أوراق عمل، بما في ذلك الرسوم البيانية والصور كوسائط. تحتوي الورقة الأولى على رسوم بيانية، والورقة الأخيرة تحتوي على صورة كما هو موضح في لقطات الشاشة أدناه.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|الورقة العمل الأولى **(توقعات المبيعات)**|الورقة العمل الثانية **(تقرير المبيعات)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|الصفحة العملية الثالثة **(ادخال البيانات)**|الصفحة العملية الأخيرة **(الصورة)**|

### **عملية التحويل**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Excel to PDF</title>
    </head>
    <body>
        <h1>Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;"></a>
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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the PDF file
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

إذا كان جدول البيانات يحتوي على صيغ، فمن الأفضل استدعاء طريقة [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) قبل تحويل الجدول إلى PDF. يضمن ذلك إعادة حساب القيم المعتمدة على الصيغ، وعرض القيم الصحيحة في ملف PDF.

{{% /alert %}}

### **النتيجة**

عند تشغيل الرمز أعلاه، يتم إنشاء ملف PDF في مجلد Files في دليل التطبيق الخاص بك.
توضح اللقطات الشاشة التالية صفحات ملف PDF. يرجى ملاحظة أن الهوامش العلوية والسفلية محتفظ بها أيضًا في ملف PDF الناتج.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|الورقة العمل الأولى **(توقعات المبيعات)**|الورقة العمل الثانية **(تقرير المبيعات)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|الصفحة العملية الثالثة **(ادخال البيانات)**|الصفحة العملية الأخيرة **(الصورة)**|
