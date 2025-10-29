---
title: ثيمات وألوان إكسل
linktitle: ثيمات وألوان إكسل  
type: docs  
weight: 100  
url: /ar/javascript-cpp/excel-themes-and-colors/  
description: تعلم كيفية استخدام مخططات ألوان مخصصة مع Aspose.Cells for JavaScript عبر C++.  
keywords: جافاسكريبت إنشاء وتطبيق مخططات ألوان، برمجيًا إنشاء مخطط ألوان مخصص، كيف تطبق مخطط ألوان مخصص جافاسكريبت، كيفية استخدام مخطط الألوان في إكسل باستخدام جافاسكريبت  
---

## **كيفية تطبيق وإنشاء مخطط الألوان في إكسل**  
تجعل مواضيع المستند من السهل تنسيق ألوان وخطوط وتأثيرات تنسيق الرسومات للوثائق وتحديثها بسرعة.  
تقدم السمات مظهر موحد مع أنماط مسماة، تأثيرات رسومية، والكائنات الأخرى المستخدمة في دفتر العمل. على سبيل المثال، يظهر نمط Accent1 بشكل مختلف في سمات Office وApex. غالبًا، تطبق سمة مستند ثم تعدلها حسب رغبتك.  

### **كيفية تطبيق مخطط لون في إكسل**  
1. افتح Excel وانتقل إلى علامة "تخطيط الصفحة" في شريط الأدوات.  
1. انقر على زر "الألوان" في قسم "الثيمات".  
<br>  
<img src="color.png" width=70% />  
1. اختر لوحة ألوان تتناسب مع متطلباتك أو قم بتحويل المؤشر فوق نظام لرؤية معاينة مباشرة.  

### **كيفية إنشاء مجموعة ألوان مخصصة في إكسيل**  
يمكنك إنشاء مجموعة ألوان خاصة بك لإعطاء مستندك مظهرًا جديدًا وفريدًا أو لتلائم معايير علامة تجارية منظمتك.  

1. افتح Excel وانتقل إلى علامة "تخطيط الصفحة" في شريط الأدوات.  
1. انقر على زر "الألوان" في قسم "الثيمات".  
1. انقر على زر "تخصيص الألوان...".  
<br>  
<img src="color2.png" width=70% />  

1. في مربع الحوار "إنشاء ألوان ثيم جديدة"، يمكنك اختيار الألوان لكل عنصر عن طريق النقر على القوائم المنسدلة للألوان بجوارها. يمكنك اختيار الألوان من اللوحة أو تعريف ألوان مخصصة باستخدام خيار "مزيد من الألوان".  
<br>  
<img src="color3.png" width=70% />  
1. بعد اختيار جميع الألوان المطلوبة، قم بتوفير اسم لمجموعة الألوان المخصصة في حقل "الاسم".  

1. انقر على زر "حفظ" لحفظ مجموعة الألوان المخصصة الخاصة بك. ستكون مجموعة الألوان المخصصة الخاصة بك الآن متاحة في قائمة الألوان المنسدلة للاستخدام المستقبلي.  

## **كيفية إنشاء وتطبيق مجموعة ألوان في Aspose.Cells**  
توفر Aspose.Cells ميزات لتخصيص الثيمات والألوان.  

### **كيفية إنشاء موضوع ألوان مخصص في Aspose.Cells**  
إذا تم استخدام ألوان السمة في الملف، فلا حاجة لتعديل كل خلية على حدة؛ فقط نحتاج إلى تعديل الألوان في السمة.  

المثال التالي يوضح كيفية تطبيق ثيمات مخصصة باستخدام الألوان المرغوبة. نحن نستخدم ملف قالب عيني تم إنشاؤه يدويًا في Microsoft Excel 2007.  

يعرض المثال التالي تحميل ملف قالب XLSX، وتحديد ألوان لأنواع ألوان السمة المختلفة، وتطبيق الألوان المخصصة، وحفظ ملف إكسل.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Custom Theme Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Define Color array (of 12 colors) for Theme.
            const carr = [
                new Color("AntiqueWhite"), // Background1
                new Color("Brown"), // Text1
                new Color("AliceBlue"), // Background2
                new Color("Yellow"), // Text2
                new Color("YellowGreen"), // Accent1
                new Color("Red"), // Accent2
                new Color("Pink"), // Accent3
                new Color("Purple"), // Accent4
                new Color("PaleGreen"), // Accent5
                new Color("Orange"), // Accent6
                new Color("Green"), // Hyperlink
                new Color("Gray") // Followed Hyperlink
            ];

            // Set the custom theme with specified colors.
            workbook.customTheme("CustomeTheme1", carr);

            // Save as the excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom theme applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



### **كيفية تطبيق ألوان الثيم في Aspose.Cells**  
يعرض المثال التالي تطبيق لون المقدمة وخط النص لخلية استنادًا إلى أنواع ألوان السمة الافتراضية (دفتر العمل). كما يحفظ ملف إكسل على القرص.  


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
        const { Workbook, SaveFormat } = AsposeCells;

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
            // Instantiate a Workbook.
            const workbook = new Workbook();

            // Get cells collection in the first (default) worksheet.
            const cells = workbook.worksheets.get(0).cells;

            // Get the D3 cell.
            const c = cells.get("D3");

            // Get the style of the cell.
            const s = c.style;

            // Set foreground color for the cell from the default theme Accent2 color.
            s.foregroundThemeColor = new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent2, 0.5);

            // Set the pattern type.
            s.pattern = AsposeCells.BackgroundType.Solid;

            // Get the font for the style.
            const f = s.font;

            // Set the theme color.
            f.themeColor = new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent4, 0.1);

            // Apply style.
            c.style = s;

            // Put a value.
            c.value = "Testing1";

            // Save the excel file and provide download link.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to save the file.</p>';
        });
    </script>
</html>
```


### **كيفية الحصول على وتعيين ألوان الثيم في Aspose.Cells**  
فيما يلي بعض الطرق والخصائص التي تنفذ فيها ألوان الثيم.  

- [**Style.foregroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundThemeColor-themecolor-): يُستخدم لضبط لون المقدمة.  
- [**Style.backgroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundThemeColor-themecolor-): يُستخدم لضبط لون الخلفية.  
- [**Font.themeColor**](https://reference.aspose.com/cells/javascript-cpp/font/#themeColor-themecolor-): يُستخدم لضبط لون الخط.  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-): يُستخدم للحصول على لون السمة.  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-color-): يُستخدم لضبط لون السمة.  

المثال التالي يوضح كيفية الحصول على وتعيين ألوان الثيم.  

يعرض المثال التالي استخدام ملف قالب XLSX، والحصول على ألوان لأنواع ألوان السمة المختلفة، وتغيير الألوان، وحفظ ملف إكسل.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Theme Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, ThemeColorType } = AsposeCells;

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

            // Instantiating a Workbook object and opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Background1 theme color.
            let c = workbook.themeColor(ThemeColorType.Background1);
            console.log("theme color Background1: ", c);

            // Get the Accent2 theme color.
            c = workbook.themeColor(ThemeColorType.Accent2);
            console.log("theme color Accent2: ", c);

            // Change the Background1 theme color.
            workbook.themeColor(ThemeColorType.Background1, Color.Red);

            // Get the updated Background1 theme color.
            c = workbook.themeColor(ThemeColorType.Background1);
            console.log("theme color Background1 changed to: ", c);

            // Change the Accent2 theme color.
            workbook.themeColor(ThemeColorType.Accent2, Color.Blue);

            // Get the updated Accent2 theme color.
            c = workbook.themeColor(ThemeColorType.Accent2);
            console.log("theme color Accent2 changed to: ", c);

            // Saving the updated file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Updated Excel File';

            // Display results
            let resultHtml = '';
            resultHtml += `<p>theme color Background1: ${JSON.stringify(workbook.themeColor(ThemeColorType.Background1))}</p>`;
            resultHtml += `<p>theme color Accent2: ${JSON.stringify(workbook.themeColor(ThemeColorType.Accent2))}</p>`;
            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! See console for detailed logs.</p>' + resultHtml;
        });
    </script>
</html>
```


## **مواضيع متقدمة**  
- [استخراج بيانات الثيم من ملف Excel](/cells/ar/javascript-cpp/extract-theme-data-from-excel-file/)
