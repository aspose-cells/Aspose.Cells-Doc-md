---
title: الأشكال في المخططات باستخدام JavaScript عبر C++
linktitle: الأشكال في الرسوم البيانية
description: تعلم كيفية استخدام Aspose.Cells for JavaScript عبر C++ لإضافة عناصر تحكم وتخصيص المخططات في Microsoft Excel. يوضح هذا الدليل كيفية التلاعب بعناصر المخطط، وضبط التنسيق، وتحسين المظهر العام وسهولة استخدام المخططات الخاصة بك.
keywords: Aspose.Cells for JavaScript عبر C++، عناصر التحكم في المخطط، تخصيص المخططات، Microsoft Excel، عناصر المخطط، التنسيق.
type: docs
weight: 70
url: /ar/javascript-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
أحيانًا تحتاج إلى إدراج كائنات الرسم مثل التسميات وصناديق النص والصور وما إلى ذلك في رسم بياني. يمكن لـ Aspose.Cells إضافة عناصر التحكم إلى رسم بياني في وقت التشغيل.
{{% /alert %}}

## **إضافة عنصر تحكم التسمية إلى الرسم البياني.**

توفر التسميات وسيلة لتقديم معلومات للمستخدمين حول محتوى جدول بيانات. تسمح Aspose.Cells لك بإضافة وتلاعب التسميات حتى في الرسوم البيانية.

توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) طريقة تسمى [**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLabelInChart-number-number-number-number-) تُستخدَم لإضافة عنصر تحكم تسمية إلى رسم بياني. فيما يلي قائمة بالمعلمات المستخدمة للطريقة:

- الأعلى - الإزاحة الرأسية للتسمية عن الزاوية اليسرى العلوية بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- اليسار - الإزاحة الرأسية للتسمية عن الزاوية اليسرى العلوية بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- الارتفاع - ارتفاع التسمية، بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- العرض - عرض التسمية، بوحدات تمثل 1/4000 من منطقة الرسم البياني.

تعيد الطريقة كائن [**Label**](https://reference.aspose.com/cells/javascript-cpp/label/). فئة [**Label**](https://reference.aspose.com/cells/javascript-cpp/label/) تمثل تسمية في الرسم البياني. لديها بعض الأعضاء المهمة.

- [**text**](https://reference.aspose.com/cells/javascript-cpp/shape/#text--) (خاصية) - تحدد سلسلة تسمية التسمية.
- [**fill**](https://reference.aspose.com/cells/javascript-cpp/shape/#fill--) (خاصية) - تحدد سمات لون التعبئة.

المثال التالي يوضح كيفية إضافة تسمية إلى الرسم البياني. يستخدم المثال ملف مصمم (**exp_piechart.xls**) الذي يحتوي على رسم بياني فيه. نستخدم هذا الملف لإدراج تسمية في الرسم البياني. وفيما يلي الشفرة الأصلية لإضافة تسمية إلى الرسم البياني. يتم إنشاء الناتج التالي عند تنفيذ الشفرة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add Label In Chart Example</title>
    </head>
    <body>
        <h1>Add Label In Chart Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the second sheet.
            const sheet = workbook.worksheets.get(1);
            const chart = sheet.charts.get(0);

            // Add a new label to the chart.
            const label = chart.shapes.addLabelInChart(100, 100, 350, 900);

            // Set the caption of the label.
            label.text = "A Label In Chart";

            // Set the Placement Type, the way the Label is attached to the cells.
            label.placement = AsposeCells.PlacementType.FreeFloating;

            // Save the excel file and provide a download link.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Label added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **إضافة عنصر تحكم مربع نص إلى الرسم البياني**

أحد الطرق لتسليط الضوء على معلومات مهمة في تقرير هو استخدام مربع نص. على سبيل المثال ، أدخل نصًا لتسليط الضوء على اسم الشركة أو للإشارة إلى المنطقة الجغرافية ذات أعلى مبيعات. توفر صف الفصل [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) طريقة تسمى [**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-) ، التي تُستخدم لإضافة عنصر تحكم مربع نص إلى رسم بياني. وفيما يلي قائمة المعلمات المستخدمة للطريقة:

- **top** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **left** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **height** - ارتفاع مربع النص ، بوحدات 1/4000 من منطقة الرسم البياني.
- **width** - عرض مربع النص ، بوحدات 1/4000 من منطقة الرسم البياني.

تُرجع الطريقة كائنًا [**TextBox**](https://reference.aspose.com/cells/javascript-cpp/textbox/). صف الفصل [**TextBox**](https://reference.aspose.com/cells/javascript-cpp/textbox/) يمثل عنصر تحكم مربع نص في الرسم البياني.

المثال التالي يوضح كيفية إضافة مربع نص إلى رسم بياني. يستخدم المثال الملف المصمم السابق (**exp_piechart.xls**) الذي يحتوي على رسم بياني فيه. نستخدم هذا الملف لإدراج مربع نص في الرسم البياني لعرض عنوان الرسم البياني. يتم إنشاء الشفرة الأصلية لإضافة مربع نص إلى الرسم البياني أدناه.

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the second sheet.
            const sheet = workbook.worksheets.get(1);
            const chart = sheet.charts.get(0);

            // Add a new textbox to the chart.
            const textbox0 = chart.shapes.addTextBoxInChart(100, 1100, 350, 2550);

            // Fill the text.
            textbox0.text = "Sales By Region";

            // Get the textbox text frame.
            // const textframe0 = textbox0.textFrame;

            // Set the textbox to adjust it according to its contents.
            // textframe0.autoSize = true;

            // Set the font color.
            textbox0.font.color = AsposeCells.Color.Maroon;

            // Set the font to bold.
            textbox0.font.isBold = true;

            // Set the font size.
            textbox0.font.size = 14;

            // Set font attribute to italic.
            textbox0.font.isItalic = true;

            // Get the fill format of the textbox.
            const fillformat = textbox0.fill;

            // Get the line format type of the textbox.
            const lineformat = textbox0.line;

            // Set the line weight.
            lineformat.weight = 2;

            // Set the dash style to solid.
            lineformat.dashStyle = AsposeCells.MsoLineDashStyle.Solid;

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **إضافة صورة إلى الرسم البياني**

تسمح Aspose.Cells لك بإدراج الصور في الرسم البياني. على سبيل المثال ، أضف صورة لتسليط الضوء على الرسم البياني أو محتوياته بمعنى أكبر ، أو قم بإدراج ملف صورة العلامة التجارية.

يوفر صف الفصل [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) طريقة تسمى [**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-) ، والتي تُستخدم لإضافة كائن صورة إلى الرسم البياني. وفيما يلي قائمة المعلمات المستخدمة للطريقة:

- **top** - الإزاحة الرأسية للصورة من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **left** - الإزاحة الرأسية للصورة من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **stream** - كائن تدفق يحتوي على بيانات الصورة.
- **widthScale** - مقياس عرض الصورة ، قيمة نسبية.
- **heightScale** - مقياس ارتفاع الصورة ، قيمة نسبية.

تُرجع الطريقة كائنًا [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/). صف الفصل [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/) يمثل كائن صورة في الرسم البياني.

المثال التالي يوضح كيفية إضافة صورة إلى الرسم البياني. يستخدم المثال الملف التصميمي السابق (**exp_piechart.xls**) الذي يحتوي على رسم بياني فيه. نحن نستخدم هذا الملف لإدراج صورة في الرسم البياني. أدناه هو الكود الأصلي لإضافة صورة إلى الرسم البياني.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Picture to Chart</title>
    </head>
    <body>
        <h1>Add Picture to Chart Example</h1>
        <p>Select an Excel file and an image to add to the first chart in the first worksheet.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="imageInput" accept="image/*" />
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
            const fileInput = document.getElementById('fileInput');
            const imageInput = document.getElementById('imageInput');
            if (!fileInput.files.length || !imageInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file and an image file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const imageFile = imageInput.files[0];

            const arrayBuffer = await file.arrayBuffer();
            const imageBuffer = await imageFile.arrayBuffer();

            // Instantiating a Workbook object from the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the first sheet.
            const sheet = workbook.worksheets.get(0);
            const chart = sheet.charts.get(0);

            // Add a new picture to the chart.
            const pic0 = chart.shapes.addPictureInChart(50, 50, new Uint8Array(imageBuffer), 40, 40);

            // Get the lineformat type of the picture.
            const lineformat = pic0.line;

            // Set the dash style.
            lineformat.dashStyle = AsposeCells.MsoLineDashStyle.Solid;

            // Set the line weight.
            lineformat.weight = 4;

            // Save the modified Excel file and provide a download link.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Picture added to chart successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **إضافة خانة اختيار في الرسم البياني**

تسمح Aspose.Cells بإدراج خانات الاختيار في ورقة الرسم البياني باستخدام تعداد [**MsoDrawingType**](https://reference.aspose.com/cells/javascript-cpp/msodrawingtype/). يوضح المثال التالي إضافة خانة اختيار إلى ورقة الرسم البياني.

الصورة التالية تظهر ورقة الرسم البياني مع خانة الاختيار في ملف الإخراج.

![todo:image_alt_text](controls-in-charts_1.jpg)

الملف الناتج (101089316.xlsx) الذي تم إنشاؤه بواسطة مقتطف الكود التالي مرفق للرجوع إليه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Checkbox in Chart Sheet Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadLink { display: none; margin-top: 10px; display: inline-block; }
            #result p { margin: 8px 0; }
        </style>
    </head>
    <body>
        <h1>Insert Checkbox in Chart Sheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';
            // This example creates a new workbook and inserts a chart sheet with a checkbox in the chart.
            // The file input is optional for this example (a new workbook is created regardless).

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a chart sheet to the workbook
            const index = workbook.worksheets.add(AsposeCells.SheetType.Chart);

            // Access the newly added chart sheet
            const sheet = workbook.worksheets.get(index);

            // Add a floating column chart to the chart sheet
            sheet.charts.addFloatingChart(AsposeCells.ChartType.Column, 0, 0, 1024, 960);

            // Add nSeries to the chart (single series with values 1,2,3)
            sheet.charts.get(0).nSeries.add("{1,2,3}", false);

            // Add checkbox to the chart
            sheet.charts.get(0).shapes.addShapeInChart(AsposeCells.MsoDrawingType.CheckBox, AsposeCells.PlacementType.Move, 400, 400, 1000, 600);

            // Set text of the checkbox shape
            sheet.charts.get(0).shapes.get(0).text = "CheckBox 1";

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertCheckboxInChartSheet_out.xlsx';
            downloadLink.style.display = 'inline-block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Chart sheet with checkbox created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [إضافة علامة مائية WordArt إلى الرسم البياني](/cells/ar/javascript-cpp/add-wordart-watermark-to-chart/)
