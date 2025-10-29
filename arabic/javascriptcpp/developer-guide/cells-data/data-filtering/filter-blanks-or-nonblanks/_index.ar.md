---
title: كيفية تصفية الخانات الفارغة أو غير الفارغة
type: docs
weight: 85
url: /ar/javascript-cpp/how-to-filter-blanks-and-non-blanks/
description: تعلم كيفية تصفية الخلايا الفارغة وغير الفارغة باستخدام Aspose.Cells for JavaScript عبر C++ API.
keywords: تصفية الخانات الفارغة، تصفية الخانات غير الفارغة، تصفية الخانات الفارغة في ورق العمل، تصفية الخانات غير الفارغة في ورق العمل، تصفية الخانات الفارغة في إكسل، تصفية الخانات غير الفارغة في إكسل، تصفية الخانات الفارغة وغير الفارغة في إكسل
---

## **سيناريوهات الاستخدام المحتملة**
تصفية البيانات في إكسل هي أداة قيمة تعزز تحليل البيانات واستكشافها وعرضها عن طريق تمكين المستخدمين من التركيز على مجموعات محددة من البيانات استنادًا إلى معاييرهم، مما يجعل عملية تلاعب البيانات الشاملة وعملية التفسير أكثر كفاءة وفعالية.

## **كيفية تصفية الخانات الفارغة أو غير الفارغة في إكسل**
في إكسل، يمكنك بسهولة تصفية الخانات الفارغة أو غير الفارغة باستخدام خيارات التصفية. إليك كيف يمكنك القيام بذلك:

### **كيفية تصفية الخانات الفارغة في إكسل**
1. تحديد النطاق: انقر على حرف رأس العمود لتحديد العمود بأكمله أو حدد النطاق الذي تريد تصفية الخانات الفارغة فيه.
1. فتح قائمة التصفية: انتقل إلى علامة "البيانات" في شريط الأدوات.
<br>
<image src="1.png" width="70%" />
1. خيارات التصفية: انقر على زر "تصفية". سيتم إضافة أسهم تصفية إلى النطاق المحدد.
1. تصفية الخانات الفارغة: انقر على سهم التصفية في العمود الذي تريد تصفية الخانات الفارغة فيه. قم بإلغاء تحديد جميع الخيارات باستثناء "فارغة" وانقر على موافق. ستقوم هذه الخطوة بعرض الخانات الفارغة فقط في ذلك العمود.
<br>
<image src="2.png" width="70%" />
1. النتيجة كما يلي:
<br>
<image src="3.png" width="70%" />

### **كيفية تصفية الخلايا الغير فارغة في اكسل**
1. حدد النطاق: انقر على حرف رأس العمود لتحديد العمود بأكمله أو حدد النطاق الذي ترغب في تصفية الخلايا الغير فارغة فيه.
1. فتح قائمة التصفية: انتقل إلى علامة "البيانات" في شريط الأدوات.
<br>
<image src="1.png" width="70%" />
1. خيارات التصفية: انقر على زر "تصفية". سيتم إضافة أسهم تصفية إلى النطاق المحدد.
1. تصفية الخلايا الغير فارغة: انقر على سهم التصفية في العمود الذي ترغب في تصفية الخلايا الغير فارغة فيه. قم بإلغاء تحديد جميع الخيارات ما عدا "الغير فارغة" أو "مخصص" وقم بتعيين الشروط وفقًا لذلك. انقر على موافق. سيتم عرض الخلايا المحتوية على قيم في تلك العمود فقط.
<br>
<image src="4.png" width="70%" />
1. النتيجة كما يلي:
<br>
<image src="5.png" width="70%" />

## **كيفية تصفية الخلايا الفارغة باستخدام Aspose.Cells for JavaScript عبر C++**
إذا كانت العمود يحتوي على نص بحيث بعض الخلايا فارغة، وتُطلب عملية تصفية لاختيار تلك الصفوف فقط حيث توجد خلايا فارغة، يمكن استخدام الدالتين [**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#matchBlanks-number-) و [**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#addFilter-number-string-) كما هو موضح أدناه. 

يرجى الاطلاع على الكود النموذجي التالي الذي يحمل [ملف اكسل عينة](sample.xlsx) الذي يحتوي على بيانات وهمية. يستخدم الكود النموذجي ثلاثة أساليب لتصفية الخانات الفارغة. ثم يقوم بحفظ الدفتر كملف اكسل [ملف الانتاج](FilteredBlanks.xlsx). 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Filter for Blank Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.autoFilter.addFilter(1, null);
            worksheet.autoFilter.refresh();

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download FilteredBlanks.xlsx';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied and file ready for download.</p>';
        });
    </script>
</html>
```


## **كيفية تصفية غير الفارغة باستخدام Aspose.Cells for JavaScript عبر C++**

يرجى الاطلاع على مثال الكود التالي الذي يحمل [ملف إكسل العينة](sample.xlsx) والذي يحتوي على بعض البيانات الوهمية. بعد تحميل الملف، استدعِ وظيفة [AutoFilter.matchNonBlanks(number)](https://reference.aspose.com/cells/javascript-cpp/autofilter/#matchNonBlanks-number-) لتصفية البيانات غير الفارغة، وأخيرًا احفظ دفتر العمل كـ [ملف إكسل الناتج](FilteredNonBlanks.xlsx). 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter NonBlanks Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call MatchNonBlanks function to apply the filter
            worksheet.autoFilter.matchNonBlanks(1);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNonBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
