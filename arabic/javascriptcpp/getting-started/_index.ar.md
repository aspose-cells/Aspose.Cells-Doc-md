---
title: البدء
type: docs
weight: 5
url: /ar/javascript-cpp/getting-started/
keywords: "Excel،Browser،Serverless،XLS،XLSX،XLSB،CSV،PDF،JPG،PNG،HTML،ODS،XLSM،Spreadsheet،Markdown،XPS،DOCX،PPTX،MHTML،SVG،JSON،SQL،XML"
description: "إعداد Aspose.Cells للجافاسكريبت عبر C++ وإرشادات التثبيت."
---

## **وصف المنتج**
Aspose.Cells for JavaScript عبر C++ هو مكتبة عالية الأداء ومزايا غنية لمعالجة وتحويل ملفات جداول البيانات، بما في ذلك Excel (XLS، XLSX، XLSB، XLSM)، ODS، CSV، وHTML. يوفر مجموعة كاملة من الميزات لإنشاء وتحرير وتحويل وعرض جداول البيانات في بيئات المتصفح و Node.js. مع دعم كامل لجميع تنسيقات Excel الرئيسية، يضمن Aspose.Cells for JavaScript عبر C++ أقصى توافق ومرونة عبر حالات الاستخدام المختلفة.
مصمم باستخدام WebAssembly لفتح أداء قريب من الأداء الأصلي مباشرة في المتصفح، يتيح Aspose.Cells for JavaScript عبر C++ معالجة جداول البيانات بسرعة وكفاءة بدون الحاجة إلى خادم. يضمن حجمه الخفيف دعم عالي لعمليات تشغيل خفيفة على الويب ويوفر حلاً كاملًا وموثوقًا وأداء عالي. يدعم بشكل رئيسي المتصفحات و Node.js.

## **الميزات الرئيسية**
1. **إنشاء وتحرير الملفات:** إنشاء جداول بيانات جديدة من الصفر أو تحرير الموجودة بسهولة. يتضمن ذلك إضافة أو تعديل البيانات، تنسيق الخلايا، إدارة ورقات العمل، وأكثر.
1. **معالجة البيانات:** إجراء عمليات معالجة معقدة للبيانات مثل الترتيب، التصنيف، والتحقق من الصحة. تدعم المكتبة أيضًا الصيغ والوظائف المتقدمة لتسهيل تحليل البيانات والحسابات.
1. **تحويل الملفات:** تحويل ملفات Excel إلى تنسيقات مختلفة مثل PDF، HTML، ODS، وصيغ الصور مثل PNG و JPEG. تعتبر هذه الميزة مفيدة للمشاركة وتوزيع بيانات جدول البيانات بصيغ مختلفة.
1. **الرسوم البيانية والرسوميات:** إنشاء وتخصيص مجموعة واسعة من الرسوم البيانية والرسوم التوضيحية لتمثيل البيانات بصريًا. تدعم المكتبة مخططات الأعمدة، والخطوط، والدائرية، وأكثر، مع خيارات التخصيص للتصميم والتخطيط.
1. **عرض وطباعة:** عرض أوراق عمل Excel كصور عالية الجودة وملفات PDF، مع ضمان دقة التمثيل البصري. كما توفر مكتبة خيارات لطباعة جداول البيانات مع تحكم دقيق في تخطيط الصفحة وتنسيقها.
1. **الحماية والأمان المتقدم:** حماية جداول البيانات بكلمات مرور، تشفير الملفات، وإدارة أذونات الوصول لضمان أمان البيانات وسلامتها.
1. **الأداء وقابلية التوسع:** مصمم للتعامل مع مجموعات البيانات الكبيرة والجداول المعقدة بكفاءة، يضمن Aspose.Cells for JavaScript عبر C++ أداءً عاليًا وقابلية توسع لتطبيقات المؤسسات.


## **المتطلبات المسبقة**

قبل أن تبدأ، تأكد من أن لديك:
- Node.js مثبت على نظامك (تحميل من https://nodejs.org/ )
- ملف ترخيص Aspose صالح (على سبيل المثال، Aspose.Total.lic، Aspose.Cells.lic، أو aspose.cells.js.lic) للاستخدام الكامل الميزات
- معرفة أساسية بـ HTML و JavaScript

## **الخطوة 1: التثبيت**

### تثبيت Aspose.Cells for JavaScript

إنشاء دليل مشروع جديد وتثبيت الحزمة:

{{< highlight bash >}}
# Create a new project directory
mkdir my-excel-project
cd my-excel-project

# Install Aspose.Cells for JavaScript
npm install aspose.cells.js
{{< /highlight >}}

### تثبيت خادم HTTP (مطلوب لإعداد الترخيص)

تثبيت خادم HTTP بسيط على مستوى العالم:

{{< highlight bash >}}
npm install -g http-server
{{< /highlight >}}

أو استخدم خادم Python المدمج (إذا كانت Python مثبتة):
{{< highlight bash >}}
# Python 3
python -m http.server

# Python 2
python -m SimpleHTTPServer
{{< /highlight >}}

## **الخطوة 2: إعداد الترخيص (مطلوب للميزات الكاملة)**

### تشفير ملف الترخيص الخاص بك

1. **ابدأ خادم HTTP** في دليل مشروعك:
   {{< highlight bash >}}
   http-server -p 8080
   {{< /highlight >}}

2. **افتح أداة تشفير الترخيص** في متصفحك:
   ```
   http://localhost:8080/node_modules/aspose.cells.js/encrypt_lic.html
   ```

3. **قم بتحميل ملف الترخيص الخاص بك**:
   - انقر على "اختيار ملف" واختر ملف الترخيص الخاص بك (مثل `Aspose.Total.lic`، `Aspose.Cells.lic`، أو `aspose.cells.js.lic`)
   - ستكتمل عملية التشفير تلقائيًا (سريع جدًا)

4. **حمّل الترخيص المشفر**:
   - انقر على "تحميل الملف المعالج" لتنزيل `aspose.cells.enc`
   - احفظ هذا الملف في دليل مشروعك

### وضع الترخيص المشفر

نقل ملف `aspose.cells.enc` إلى جذر مشروعك أو مجلد معين حيث يمكن لتطبيقك الوصول إليه.

## **الخطوة 3: أمثلة الاستخدام**

### استخدام المتصفح

أنشئ ملف `index.html` في دليل مشروعك:

{{< highlight html >}}
<!DOCTYPE html>
<html>
<head>
    <title>Aspose.Cells Browser Example</title>
</head>
<body>
    <h1>Excel Processing with Aspose.Cells</h1>
    <button id="createExcel">Create Excel File</button>
    <div id="output"></div>

    <script src="./node_modules/aspose.cells.js/aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FileFormatType, SaveFormat } = AsposeCells;

        // Initialize with license (optional, remove for trial mode)
        AsposeCells.onReady({
            license: "aspose.cells.enc"  // Path to your encrypted license
        }).then(() => {
            console.log("Aspose.Cells is ready!");

            document.getElementById('createExcel').onclick = function() {
                // Create a new workbook
                var workbook = new Workbook(FileFormatType.Xlsx);

                // Get the first worksheet
                var worksheet = workbook.worksheets.get(0);

                // Add some data
                worksheet.cells.get("A1").putValue("Hello World");
                worksheet.cells.get("A2").putValue("Created with Aspose.Cells for JavaScript");
                worksheet.cells.get("B1").putValue(42);

                // Save as Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);

                // Create download link
                const blob = new Blob([outputData]);
                const downloadLink = document.createElement('a');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.textContent = 'Download Excel File';
                downloadLink.download = "my-excel-file.xlsx";
                downloadLink.style.display = 'block';

                const output = document.getElementById('output');
                output.innerHTML = '';
                output.appendChild(downloadLink);
            };
        }).catch(error => {
            console.error("Error initializing Aspose.Cells:", error);
        });
    </script>
</html>
{{< /highlight >}}

**لتشغيل مثال المتصفح:**

{{< highlight bash >}}
# Start HTTP server
http-server -p 8080

# Open browser and visit:
# http://localhost:8080
{{< /highlight >}}

### استخدام Node.js

أنشئ ملف `node-example.js`:

{{< highlight javascript >}}
const { AsposeCells, Workbook, SaveFormat, FileFormatType } = require("aspose.cells.js");
const fs = require('fs');

// Initialize Aspose.Cells with license
AsposeCells.onReady({
    license: "aspose.cells.enc",  // Path to your encrypted license
    fontPath: "./fonts/"         // Optional: path to system fonts
}).then(() => {
    console.log("Aspose.Cells initialized successfully!");

    // Create a new workbook
    const workbook = new Workbook(FileFormatType.Xlsx);

    // Get the first worksheet
    const worksheet = workbook.worksheets.get(0);

    // Add data to cells
    worksheet.cells.get("A1").putValue("Product");
    worksheet.cells.get("B1").putValue("Price");
    worksheet.cells.get("A2").putValue("Apple");
    worksheet.cells.get("B2").putValue(1.99);
    worksheet.cells.get("A3").putValue("Orange");
    worksheet.cells.get("B3").putValue(2.49);

    // Save as Excel file
    const excelData = workbook.save(SaveFormat.Xlsx);
    fs.writeFileSync('output.xlsx', Buffer.from(excelData));
    console.log('Excel file saved as output.xlsx');

    // Save as PDF
    const pdfData = workbook.save(SaveFormat.Pdf);
    fs.writeFileSync('output.pdf', Buffer.from(pdfData));
    console.log('PDF file saved as output.pdf');

}).catch(error => {
    console.error("Error:", error);
});
{{< /highlight >}}

**لتشغيل مثال Node.js:**

{{< highlight bash >}}
node node-example.js
{{< /highlight >}}

## **عمليات الملفات الشائعة**

### قراءة ملف إكسل موجود بالفعل

{{< highlight javascript >}}
// Browser (using File input)
const fileInput = document.getElementById('fileInput');
fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    reader.onload = (e) => {
        const arrayBuffer = e.target.result;
        const workbook = new Workbook(new Uint8Array(arrayBuffer));
        // Process the workbook...
    };
    reader.readAsArrayBuffer(file);
});

// Node.js
const fs = require('fs');
const fileBuffer = fs.readFileSync('input.xlsx');
const workbook = new Workbook(fileBuffer);
{{< /highlight >}}

### التحويل بين الصيغ

{{< highlight javascript >}}
// Convert Excel to PDF
const pdfData = workbook.save(SaveFormat.Pdf);

// Convert Excel to HTML
const htmlData = workbook.save(SaveFormat.Html);

// Convert Excel to CSV
const csvData = workbook.save(SaveFormat.Csv);

// Convert Excel to JSON
const jsonData = workbook.save(SaveFormat.Json);
{{< /highlight >}}

## **استكشاف الأخطاء وإصلاحها**

### المشاكل الشائعة والحلول

1. **خطأ "الموديل غير موجود"**
   - تأكد من تشغيل خادم HTTP من الدليل الصحيح
   - تحقق من أن مسار src في السكريبت يشير إلى الموقع الصحيح

2. **الترخيص لا يعمل**
   - تأكد من وجود ملف `aspose.cells.enc` في الموقع الصحيح
   - تحقق من أن ملف الترخيص المشفر تم إنشاؤه بشكل صحيح
   - تحقق من أن ملف الترخيص الأصلي صالح ولم ينتهي تاريخ صلاحيته

3. **مشاكل CORS في المتصفح**
   - استخدم دائمًا خادم HTTP، لا تفتح ملفات HTML مباشرة
   - استخدم `http-server` أو أدوات مماثلة للتطوير المحلي

### الحصول على المساعدة

إذا واجهت مشكلات:
- تحقق من [توثيق Aspose.Cells](https://docs.aspose.com/cells/javascript-cpp/)
- قم بزيارة [منتديات Aspose](https://forum.aspose.com/c/cells/9) للدعم المجتمعي
- اتصل بدعم Aspose مع معلومات الترخيص الخاصة بك

## **الخطوات التالية**

- استعرض [مرجع API](https://reference.aspose.com/cells/javascript-cpp/) للتوثيق المفصل
- تعرف على الميزات المتقدمة مثل الرسوم البيانية والصيغ والتنسيق
- اطلع على مزيد من الأمثلة والدروس في التوثيق
- فكر في الدمج مع تطبيقات الويب الحالية أو أدوات البناء الخاصة بك
