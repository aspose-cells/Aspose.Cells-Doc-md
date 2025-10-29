---
title: إعدادات التعبئة
linktitle: إعدادات التعبئة
description: تعلم كيف تقوم بتخصيص إعدادات التعبئة والخلفية ونمط الخلايا باستخدام مكتبة Aspose.Cells لجافاسكريبت عبر C++.
keywords: Aspose.Cells، خلايا، إعدادات التعبئة، الخلفية، النمط، جافاسكريبت عبر C++
type: docs
weight: 50
url: /ar/javascript-cpp/cells-fill-settings/
---

## **الألوان وأنماط الخلفية**

يمكن لبرنامج Microsoft Excel تعيين ألوان الأمام (الإطار) والخلفية (تعبئة) للخلايا وأنماط الخلفية.

تدعم Aspose.Cells أيضًا هذه الميزات بطريقة مرنة. في هذا الموضوع، نتعلم كيفية استخدام هذه الميزات باستخدام Aspose.Cells.

### **تعيين الألوان وأنماط الخلفية**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) تتيح الوصول إلى كل ورقة عمل في ملف الإكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). كل عنصر في مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) يمثل كائنًا من فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

تمتلك [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) الخاصية [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) التي تُستخدم للحصول على وتعيين تنسيق الخلية. توفر فئة [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) خصائص لضبط ألوان المقدمة والخلفية للخلايا. يوفر Aspose.Cells تعداد [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype) الذي يحتوي على مجموعة من أنماط الأنماط الخلفية المعرفة مسبقًا المذكورة أدناه.

|**أنماط الخلفية**|**الوصف**|
| :- | :- |
|DiagonalCrosshatch|تمثل نمط شفة الصليب المائل|
|DiagonalStripe| يمثل نمط خط مائل |
|Gray6| يمثل نمط رمادي بنسبة 6.25٪ |
|Gray12| يمثل نمط رمادي بنسبة 12.5٪ |
|Gray25| يمثل نمط رمادي بنسبة 25٪ |
|Gray50| يمثل نمط رمادي بنسبة 50٪ |
|Gray75| يمثل نمط رمادي بنسبة 75٪ |
|HorizontalStripe| يمثل نمط خط أفقي |
|None| يمثل عدم وجود خلفية |
|ReverseDiagonalStripe| يمثل نمط خط مائل عكسي |
|Solid| يمثل نمط صلب |
|ThickDiagonalCrosshatch| يمثل نمط علامة تقاطع مائلة سميكة |
|ThinDiagonalCrosshatch| يمثل نمط علامة تقاطع مائلة رفيعة |
|ThinDiagonalStripe| يمثل نمط خط مائل رفيع |
|ThinHorizontalCrosshatch| يمثل نمط علامة تقاطع أفقي رفيعة |
|ThinHorizontalStripe| يمثل نمط خط أفقي رفيع |
|ThinReverseDiagonalStripe| يمثل نمط خط مائل عكسي رفيع |
|ThinVerticalStripe| يمثل نمط خط عمودي رفيع |
|VerticalStripe| يمثل نمط خط عمودي |

في المثال أدناه ، تم تعيين لون الخلفية للخلية A1 ولكن تم تكوين A2 ليكون لها كل من لون الخلفية والأمامية مع نمط خلفية خط عمودي.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Define a Style and get the A1 cell style
            let style = worksheet.cells.get("A1").style;

            // Setting the foreground color to yellow
            style.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A1 cell
            worksheet.cells.get("A1").style = style;

            // Get the A2 cell style
            style = worksheet.cells.get("A2").style;

            // Setting the foreground color to blue
            style.foregroundColor = AsposeCells.Color.Blue;

            // Setting the background color to yellow
            style.backgroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A2 cell
            worksheet.cells.get("A2").style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```


### **مهم معرفته**

{{% alert color="primary" %}}

- لتعيين لون المقدمة أو الخلفية لخلية، استخدم [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) كائن [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) أو [**backgroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundColor-color-) الخاصية. لن يكون لكلاهما تأثير إلا إذا تم ضبط الخاصية [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) لكائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style).
- تحدد الخاصية [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) لون ظل الخلية. تحدد الخاصية [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) نوع نمط الخلفية المستخدم للون المقدمة أو الخلفية. توفر Aspose.Cells تعدادًا [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype) يحتوي على مجموعة من أنواع أنماط الخلفية المعرفة مسبقًا.
- إذا حددت قيمة *BackgroundType.None* من تعداد [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype)، فلن يتم تطبيق لون المقدمة. بالمثل، لن يتم تطبيق لون الخلفية إذا حددت قيم *BackgroundType.None* أو *BackgroundType.Solid*.
- عند استرجاع لون السطوع/التعبئة للخلية، إذا كان [**style.pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) يساوي *BackgroundType.None*، سيقوم [**style.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor--) بإرجاع *Color.Empty*.

{{% /alert %}}

### **تطبيق تأثيرات تعبئة التدرج**

لتطبيق التأثيرات التدرجية التي تريدها على الخلية، استخدم خاصية [**twoColorGradient**](https://reference.aspose.com/cells/javascript-cpp/style/#twoColorGradient-color-color-gradientstyletype-number-) لكائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) وفقًا لذلك.

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
        const { Workbook, SaveFormat, Color, GradientStyleType, TextAlignmentType } = AsposeCells;

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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.get(2, 1).putValue("test");

            const style = worksheet.cells.get("B3").style;

            style.isGradient = true;
            style.twoColorGradient = [ new Color(255, 255, 255), new Color(79, 129, 189), GradientStyleType.Horizontal, 1 ];
            style.font.color = Color.Red;
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            worksheet.cells.get("B3").style = style;

            worksheet.cells.rowHeightPixel = [2, 53];

            worksheet.cells.merge(2, 1, 1, 2);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **الألوان واللوحة**

اللوحة هي عدد الألوان المتاحة للاستخدام في إنشاء صورة. يتيح استخدام لوحة معيارية في العرض للمستخدم إنشاء مظهر متسق. كل ملف من ملفات Microsoft Excel (97-2003) لديه لوحة تتكون من 56 لون يمكن تطبيقها على الخلايا، الخطوط، الخطوط الشبكية، الكائنات الرسومية، التعبئات والخطوط في الرسم البياني.

مع Aspose.Cells، يمكن للمستخدم استخدام الألوان الموجودة في اللوحة بالإضافة إلى الألوان المخصصة. قبل استخدام لون مخصص، قم بإضافته إلى اللوحة أولاً.

يناقش هذا الموضوع كيفية إضافة ألوان مخصصة إلى اللوحة.

### **إضافة ألوان مخصصة إلى اللوحة**

تدعم Aspose.Cells لوحة الألوان من Microsoft Excel التي تتكون من 56 لون. لاستخدام لون مخصص غير معرف في اللوحة، أضف اللون إلى اللوحة.

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، التي تمثل ملف إكسل من مايكروسوفت. توفر فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) طريقة [**changePalette**](https://reference.aspose.com/cells/javascript-cpp/workbook/#changePalette-color-number-) التي تأخذ المعلمات التالية لإضافة لون مخصص لتعديل لوحة الألوان:

- لون مخصص، اللون المخصص الذي سيتم إضافته.
- الفهرس، فهرس اللون في اللوحة الذي سيحل محل اللون المخصص. يجب أن يكون بين 0-55.

المثال أدناه يضيف لون مخصص (Orchid) إلى اللوحة قبل تطبيقه على خط النص.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Checks if a color is in the palette for the spreadsheet.
            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding Orchid color to the palette at 55th index
            workbook.changePalette(AsposeCells.Color.Orchid, 55);

            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Hello Aspose!");

            // Defining new Style object
            const styleObject = workbook.createStyle();
            // Setting the Orchid (custom) color to the font
            styleObject.font.color = workbook.colors[55];

            // Applying the style to the cell
            cell.style = styleObject;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}

تحتوي اللوحة فقط على 56 لونًا. عندما تقوم بإضافة لون مخصص إلى اللوحة، يتم تغيير اللوحة ويتم تغيير أي عنصر في الملف المنسق باللون السابق. لذا، عند تغيير اللوحة، يرجى أن تكون حذرًا جدًا. علاوة على ذلك، هذه هي القيود في تنسيق ملف XLS (Excel 97 - 2003) فقط حيث لا يوجد مثل هذا القيد لتنسيق ملف XLSX أو لأنساق ملفات Microsoft Excel (2007/2010 أو 2013) المتقدمة.

{{% /alert %}}
