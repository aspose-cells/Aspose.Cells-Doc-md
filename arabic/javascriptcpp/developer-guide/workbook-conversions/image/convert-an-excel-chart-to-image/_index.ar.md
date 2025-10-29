---
title: تحويل مخطط Excel إلى صورة باستخدام JavaScript عبر C++
linktitle: تحويل مخطط Excel إلى صورة
type: docs
weight: 20
url: /ar/javascript-cpp/convert-an-excel-chart-to-image/
description: تعلم كيفية تحويل مخططات Excel إلى صور باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}  

الرسوم البيانية ملفتة للنظر من الناحية البصرية وتجعل من السهل على المستخدمين رؤية المقارنات والأنماط والاتجاهات في البيانات. على سبيل المثال، بدلاً من تحليل أعمدة الأرقام في ورقة العمل، يُظهر المخطط في لمحة ما إذا كانت المبيعات في انخفاض أم في ارتفاع، أو كيف تقارن المبيعات الفعلية بالمبيعات المتوقعة. يُطلب من الأشخاص كثيرًا تقديم المعلومات الإحصائية والرسومية بطريقة سهلة الفهم وسهلة الصيانة. تُساعد الصورة في ذلك.  

في بعض الأحيان، تكون المخططات ضرورية في تطبيق أو صفحات ويب. أو قد يكون من الضروري لملف Word، أو ملف PDF، أو عرض PowerPoint أو تطبيق آخر. في كل حالة، ترغب في عرض المخطط كصورة لاستخدامه في مكان آخر.  

{{% /alert %}}  

## **تحويل الرسوم البيانية إلى صور**  

في الأمثلة هنا، يتم تحويل مخطط دائري ومخطط عمود إلى صور.  

### **تحويل مخطط دائري إلى ملف صورة**  

أولاً، أنشئ مخطط دائري في Microsoft Excel ثم قم بتحويله إلى ملف صورة باستخدام Aspose.Cells for JavaScript عبر C++. ينشئ هذا المثال صورة EMF استنادًا إلى المخطط الدائري في ملف Excel النموذجي.  

|**الإخراج: صورة مخطط دائري**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|  

1. أنشئ مخطط دائري في Microsoft Excel:  
   1. افتح برنامج Excel الجديد في Microsoft Excel.  
   1. إدخال بعض البيانات في ورقة العمل.  
   1. أنشئ مخطط دائري بناءً على البيانات.  
   4. حفظ الملف.  

|**الملف المدخل.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|  

1. قم بتنزيل وتثبيت Aspose.Cells:  
   1. [تحميل Aspose.Cells for JavaScript عبر C++](https://downloads.aspose.com/cells/javascript-cpp).  
   1. قم بتثبيته على كمبيوتر التطوير الخاص بك.  

جميع مكونات [Aspose](http://www.aspose.com/) تعمل في وضع التقييم عند التثبيت الأول. وضع التقييم ليس له حد زمني ويضيف فقط علامات مائية إلى مستندات الإخراج.  

1. أنشئ مشروعًا:  
   1. ابدأ بيئة التطوير المتكاملة المفضلة لديك.  
   1. أنشئ تطبيق وحدة تحكم جديد. يستخدم هذا المثال تطبيق JavaScript، ولكن يمكنك إنشاؤه باستخدام أي بيئة تشغيل JavaScript.  
   1. أضف مرجعًا. يستخدم هذا المشروع Aspose.Cells لذلك أضف مرجعًا إلى Aspose.Cells for JavaScript عبر C++.  
   1. كتابة الكود الذي يجد الرسم البياني ويحوله. أدناه الكود المستخدم من قِبَل المكون لإنجاز المهمة. يتم استخدام عدد قليل جدًا من السطور من الكود.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Chart to Image Example</h1>
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

            // Get the designer chart (first chart) in the first worksheet of the workbook.
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Convert the chart to an image (EMF) and prepare download link
            const imageData = chart.toImage(AsposeCells.ImageType.Emf);
            const blob = new Blob([imageData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PieChart.out.emf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to EMF successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```  

### **تحويل رسم بياني الأعمدة إلى ملف صورة**  

أولاً، أنشئ مخطط عمودي في Microsoft Excel وقم بتحويله إلى ملف صورة، كما هو موضح أعلاه. بعد تنفيذ الشفرة النموذجية، يتم إنشاء ملف JPEG بناءً على المخطط العمودي في ملف Excel النموذجي.  

|**ملف الإخراج: صورة رسم بياني للأعمدة.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|  

1. إنشاء رسم بياني للأعمدة في Microsoft Excel:  
   1. افتح برنامج Excel الجديد في Microsoft Excel.  
   1. إدخال بعض البيانات في ورقة العمل.  
   1. إنشاء رسم بياني للأعمدة بناءً على البيانات.  
   4. حفظ الملف.  

|**ملف الإدخال.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|  

1. إعداد مشروع، بالمراجع كما هو موضح أعلاه.  
1. تحويل الرسم البياني إلى صورة ديناميكياً. يلي الكود المستخدم من قِبَل المكون لإنجاز المهمة. الكود مماثل للكود السابق:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Chart to Image</title>
    </head>
    <body>
        <h1>Convert Chart to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageType, Utils } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart (first chart) in the first worksheet of the workbook.
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Convert the chart to an image (JPEG)
            const imageData = await chart.toImage(ImageType.Jpeg);

            // Create a Blob and provide a download link
            const blob = new Blob([imageData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ColumnChart.out.jpeg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to image successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
