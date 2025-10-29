---
title: إعداد الصفحة وخيارات الطباعة مع JavaScript عبر C++
linktitle: إعدادات الصفحة وخيارات الطباعة
type: docs
weight: 60
url: /ar/javascript-cpp/page-setup-and-printing-options/
---

{{% alert color="primary" %}}  
أحيانًا، يحتاج المطورون إلى تكوين إعدادات الصفحة وخيارات الطباعة للتحكم في عملية الطباعة. تقدم إعدادات الصفحة وخيارات الطباعة خيارات متنوعة ومعتمدة بشكل كامل في Aspose.Cells.  

توضح هذه المقالة كيف تنشئ تطبيق وحدة التحكم باستخدام JavaScript عبر C++، وتطبق إعداد الصفحة وخيارات الطباعة على ورقة عمل ببضع خطوط بسيطة من الكود باستخدام واجهة برمجة التطبيقات Aspose.Cells.  
{{% /alert %}}  

## **العمل مع إعدادات الصفحة والطباعة**  

للتحقق من هذا المثال، قمنا بإنشاء دفتر عمل في Microsoft Excel واستخدمنا Aspose.Cells لضبط إعدادات الصفحة وخيارات الطباعة.  

### **استخدام Aspose.Cells لضبط خيارات إعداد الصفحة**  

ابدأ أولا بإنشاء ورقة عمل بسيطة في Microsoft Excel. ثم قم بتطبيق خيارات إعداد الصفحة عليها. سيقوم تنفيذ الكود بتغيير خيارات إعداد الصفحة كما هو موضح في صورة الشاشة أدناه.  

|**ملف الإخراج.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|  

1. إنشاء ورقة عمل ببعض البيانات في Microsoft Excel:  
   1. افتح برنامج Excel الجديد في Microsoft Excel.  
   1. أضف بعض البيانات.  
1. ضبط خيارات إعداد الصفحة:  
   قم بتطبيق خيارات إعداد الصفحة على الملف. وفيما يلي صورة للخيارات الافتراضية، قبل تطبيق الخيارات الجديدة.  

|**خيارات إعداد الصفحة الافتراضية.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|  

1. قم بتنزيل وتثبيت Aspose.Cells:  
   1. [تحميل](https://downloads.aspose.com/cells/javascript-cpp) Aspose.Cells for JavaScript عبر C++.  
   1. قم بتثبيته على كمبيوتر التطوير الخاص بك.  
      جميع مكونات Aspose، عند التثبيت، تعمل في وضع التقييم. وضع التقييم لا يحتوي على حد زمني ويقوم فقط بحقن العلامات المائية إلى الوثائق المنتجة.  
1. أنشئ مشروعًا:  
   1. ابدأ بيئة JavaScript الخاصة بك.  
   1. أنشئ تطبيقًا جديدًا على الكونسول.  
      سيعرض هذا المثال تطبيق وحدة تحكم JavaScript، ولكن يمكنك أيضًا استخدام الربط مع C++.  
1. أضف مراجع:  
   1. يستخدم هذا المثال Aspose.Cells لذا أضف مرجعًا إلى تلك المكونة للمشروع. على سبيل المثال:  
      …\Program Files\Aspose\Aspose.Cells\Bin\JavaScript-Cpp\Aspose.Cells.node  
1. اكتب التطبيق الذي يستدعي واجهة برمجة التطبيق:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PageOrientationType, PaperSizeType } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Access page setup as a property
            const pageSetup = worksheet.pageSetup;

            // Setting the orientation to Portrait
            pageSetup.orientation = PageOrientationType.Portrait;

            // Setting the number of pages to which the length of the worksheet will be spanned
            pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            pageSetup.fitToPagesWide = 1;

            // Setting the paper size to A4
            pageSetup.paperSize = PaperSizeType.PaperA4;

            // Setting the print quality of the worksheet to 1200 dpi
            pageSetup.printQuality = 1200;

            // Setting the first page number of the worksheet pages
            pageSetup.firstPageNumber = 2;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetup_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **ضبط خيارات الطباعة**  

إعدادات إعداد الصفحة توفر أيضًا العديد من خيارات الطباعة (المسمى أيضًا خيارات الورقة) التي تسمح للمستخدمين بالتحكم في كيفية طباعة صفحات ورق العمل. تسمح للمستخدمين ب:  

- تحديد منطقة طباعة معينة من ورقة عمل.
- طباعة العناوين.
- طباعة خطوط الشبكة.
- طباعة عناوين الصفوف/الأعمدة.
- تحقيق جودة مسودة.
- طباعة التعليقات.
- طباعة أخطاء الخلية.
- تعريف ترتيب الصفحات.  

المثال التالي يطبق خيارات الطباعة على الملف الذي تم إنشاؤه في المثال أعلاه (PageSetup.xls). يظهر اللقطة الشاشية أدناه الخيارات الافتراضية للطباعة قبل تطبيق الخيارات الجديدة.  

|**مستند الإدخال**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|  
تغيير خيارات الطباعة ينفذ الشيفرة.  

|**ملف الإخراج**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Setup Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
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

            // Open the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            const pageSetup = worksheet.pageSetup;

            // Specifying the cells range (from A1 cell to E30 cell) of the print area
            pageSetup.printArea = "A1:E30";

            // Defining column numbers A & E as title columns
            pageSetup.printTitleColumns = "$A:$E";

            // Defining row numbers 1 as title rows
            pageSetup.printTitleRows = "$1:$2";

            // Allowing to print gridlines
            pageSetup.printGridlines = true;

            // Allowing to print row/column headings
            pageSetup.printHeadings = true;

            // Allowing to print worksheet in black & white mode
            pageSetup.blackAndWhite = true;

            // Allowing to print comments as displayed on worksheet
            pageSetup.printComments = AsposeCells.PrintCommentsType.PrintInPlace;

            // Allowing to print worksheet with draft quality
            pageSetup.printDraft = true;

            // Allowing to print cell errors as N/A
            pageSetup.printErrors = AsposeCells.PrintErrorsType.PrintErrorsNA;

            // Setting the printing order of the pages to over then down
            pageSetup.order = AsposeCells.PrintOrderType.OverThenDown;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetup_Print_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
