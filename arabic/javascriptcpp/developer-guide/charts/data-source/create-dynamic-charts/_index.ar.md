---
title: إنشاء مخططات ديناميكية باستخدام JavaScript عبر C++
linktitle: إنشاء رسوم بيانية ديناميكية
description: تعلم كيفية إنشاء مخططات ديناميكية في Aspose.Cells for Javaسكريبت عبر C++. سيظهر لك هذا الدليل كيفية تحديث بيانات الرسم البياني ديناميكيًا، السلاسل، والتنسيق بناءً على متطلباتك، مما يسمح لك بعرض البيانات المتغيرة بصريًا في أوراق العمل الخاصة بك.
keywords: Aspose.Cells for Javaسكريبت عبر C++، رسم بياني، مخططات ديناميكية، بيانات، سلاسل، تنسيق، أوراق العمل، التحديث.
type: docs
weight: 240
url: /ar/javascript-cpp/create-dynamic-charts/
---

{{% alert color="primary" %}}  
الرسوم البيانية الديناميكية (أو التفاعلية) لها القدرة على التغيير عند تغيير نطاق البيانات. وبعبارة أخرى، يمكن للرسوم البيانية الديناميكية أن تعكس تلقائيًا التغييرات عند تغيير مصدر البيانات. من أجل تحفيز تغيير مصدر البيانات، يمكن استخدام خيارات التصفية لجداول البيانات في Excel أو استخدام عنصر تحكم مثل مربع القائمة المنسدلة أو قائمة البحث.

يعرض هذا المقال كيفية استخدام واجهات برمجة التطبيقات Aspose.Cells for Javaسكريبت عبر C++ لإنشاء مخططات ديناميكية باستخدام الطريقتين السابقتين.  
{{% /alert %}}  

## **استخدام جداول Excel**  

{{% alert color="primary" %}}  
تُشار إلى جداول إكسل باسم ListObjects من وجهة نظر Aspose.Cells، لذلك سنستخدم مصطلح "ListObject" بدلاً من "جدول" للوضوح. يرجى قراءة المفصل حول [إنشاء ListObjects](/cells/ar/javascript-cpp/create-and-format-table/) باستخدام Aspose.Cells for Javaسكريبت عبر C++.  
{{% /alert %}}  

تحتوي ListObjects على وظيفة مدمجة لفرز وتصفية البيانات عند تفاعل المستخدم. يتم توفير خيارات الفرز والتصفية من خلال القوائم المنسدلة التي تُضاف تلقائيًا إلى صف الرأس في [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject). نظرًا لهذه الميزات (الفرز والتصفية)، يبدو أن [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject) هو المرشح المثالي ليكون مصدر بيانات لمخطط ديناميكي لأنه عند تغيير الفرز أو التصفية، ستتغير صورة البيانات في المخطط لتعكس الحالة الحالية لـ [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject).

لتسهيل الفهم، سوف ننشئ [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) من الصفر ونتقدم خطوة بخطوة كما هو موضح أدناه.

1. إنشاء [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) فارغة.
1. الوصول إلى [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) لأول [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) في [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook).
3. إدراج بعض البيانات في الخلايا.
1. إنشاء [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject) بناءً على البيانات المدخلة.
1. إنشاء [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart) بناءً على نطاق البيانات لـ [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject).
احفظ النتيجة على القرص الصلب.  

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
        const { Workbook, SaveFormat, ChartType, Utils } = AsposeCells;

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
            // Create an instance of Workbook
            const book = new Workbook();
            // Access first worksheet from the collection
            const sheet = book.worksheets.get(0);
            // Access cells collection of the first worksheet
            const cells = sheet.cells;

            // Insert data column-wise
            cells.get("A1").putValue("Category");
            cells.get("A2").putValue("Fruit");
            cells.get("A3").putValue("Fruit");
            cells.get("A4").putValue("Fruit");
            cells.get("A5").putValue("Fruit");
            cells.get("A6").putValue("Vegetables");
            cells.get("A7").putValue("Vegetables");
            cells.get("A8").putValue("Vegetables");
            cells.get("A9").putValue("Vegetables");
            cells.get("A10").putValue("Beverages");
            cells.get("A11").putValue("Beverages");
            cells.get("A12").putValue("Beverages");

            cells.get("B1").putValue("Food");
            cells.get("B2").putValue("Apple");
            cells.get("B3").putValue("Banana");
            cells.get("B4").putValue("Apricot");
            cells.get("B5").putValue("Grapes");
            cells.get("B6").putValue("Carrot");
            cells.get("B7").putValue("Onion");
            cells.get("B8").putValue("Cabbage");
            cells.get("B9").putValue("Potato");
            cells.get("B10").putValue("Coke");
            cells.get("B11").putValue("Coladas");
            cells.get("B12").putValue("Fizz");

            cells.get("C1").putValue("Cost");
            cells.get("C2").putValue(2.2);
            cells.get("C3").putValue(3.1);
            cells.get("C4").putValue(4.1);
            cells.get("C5").putValue(5.1);
            cells.get("C6").putValue(4.4);
            cells.get("C7").putValue(5.4);
            cells.get("C8").putValue(6.5);
            cells.get("C9").putValue(5.3);
            cells.get("C10").putValue(3.2);
            cells.get("C11").putValue(3.6);
            cells.get("C12").putValue(5.2);

            cells.get("D1").putValue("Profit");
            cells.get("D2").putValue(0.1);
            cells.get("D3").putValue(0.4);
            cells.get("D4").putValue(0.5);
            cells.get("D5").putValue(0.6);
            cells.get("D6").putValue(0.7);
            cells.get("D7").putValue(1.3);
            cells.get("D8").putValue(0.8);
            cells.get("D9").putValue(1.3);
            cells.get("D10").putValue(2.2);
            cells.get("D11").putValue(2.4);
            cells.get("D12").putValue(3.3);

            // Create ListObject, Get the List objects collection in the first worksheet
            const listObjects = sheet.listObjects;

            // Add a List based on the data source range with headers on
            let index = listObjects.add(0, 0, 11, 3, true);

            sheet.autoFitColumns();

            // Create chart based on ListObject
            index = sheet.charts.add(ChartType.Column, 21, 1, 35, 18);
            const chart = sheet.charts.get(index);
            chart.chartDataRange = "A1:D12";
            chart.chartDataRangeHasHeaders = true;
            chart.nSeries.categoryData = "A2:B12";

            // Save spreadsheet
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **استخدام الصيغ الديناميكية**  

في حال رغبتك بعدم استخدام [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject) كمصدر بيانات للمخطط الديناميكي، فإن الخيار الآخر هو استخدام وظائف إكسل (أو الصيغ) لإنشاء مجال بيانات ديناميكي، وعنصر تحكم (مثل مربع مركب) لتفعيل التغيير في البيانات. في هذا السيناريو، سنستخدم وظيفة VLOOKUP لاسترجاع القيم الملائمة استنادًا إلى اختيار مربع مركب. عند تغيير الاختيار، ستقوم وظيفة VLOOKUP بتحديث قيمة الخلية. إذا كان مدى الخلايا يستخدم وظيفة VLOOKUP، فيمكن تحديث النطاق بأكمله عند تفاعل المستخدم، وبالتالي يمكن استخدامه كمصدر لمخطط ديناميكي.

من أجل إبقاء العرض التوضيحي بسيطًا للفهم، سنقوم بإنشاء دفتر العمل من البداية والمضي قدمًا خطوة بخطوة كما هو موضح أدناه.

1. إنشاء [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) فارغة.
1. الوصول إلى [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) لأول [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) في [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook).
1. إدراج بعض البيانات في الخلايا عن طريق إنشاء نطاق مسمى. ستكون هذه البيانات مصدرًا للمخطط الديناميكي.
1. إنشاء [**ComboBox**](https://reference.aspose.com/cells/javascript-cpp/combobox) استنادًا إلى النطاق المسمي الذي تم إنشاؤه في الخطوة السابقة.
1. إدراج بعض البيانات الإضافية في الخلايا التي ستعتبر مصدرًا لوظيفة VLOOKUP.
1. إدراج وظيفة VLOOKUP (مع المعلمات المناسبة) لنطاق من الخلايا. سيعمل هذا النطاق كمصدر للمخطط الديناميكي.
1. إنشاء [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart) استنادًا إلى النطاق الذي تم إنشاؤه في الخطوة السابقة.
احفظ النتيجة على القرص الصلب.  

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
        const { Workbook, SaveFormat, ChartType, Color, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                const resultDiv = document.getElementById('result');
                if (!fileInput.files.length) {
                    resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Creating a workbook object from the uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Get the first worksheet
                const worksheet = workbook.worksheets.get(0);

                // Create a range in the worksheet
                const range = worksheet.cells.createRange("C21", "C24");

                // Name the range
                range.name = "MyRange";

                // Fill different cells with data in the range
                range.get(0, 0).putValue("North");
                range.get(1, 0).putValue("South");
                range.get(2, 0).putValue("East");
                range.get(3, 0).putValue("West");

                const comboBox = worksheet.shapes.addComboBox(15, 0, 2, 0, 17, 64);
                comboBox.inputRange = "=MyRange";
                comboBox.linkedCell = "=B16";
                comboBox.selectedIndex = 0;
                const cell = worksheet.cells.get("B16");
                const style = cell.style;
                style.font.color = Color.White;
                cell.style = style;

                worksheet.cells.get("C16").formula = "=INDEX(Sheet1!$C$21:$C$24,$B$16,1)";

                // Put some data for chart source
                // Data Headers
                worksheet.cells.get("D15").putValue("Jan");
                worksheet.cells.get("D20").putValue("Jan");

                worksheet.cells.get("E15").putValue("Feb");
                worksheet.cells.get("E20").putValue("Feb");

                worksheet.cells.get("F15").putValue("Mar");
                worksheet.cells.get("F20").putValue("Mar");

                worksheet.cells.get("G15").putValue("Apr");
                worksheet.cells.get("G20").putValue("Apr");

                worksheet.cells.get("H15").putValue("May");
                worksheet.cells.get("H20").putValue("May");

                worksheet.cells.get("I15").putValue("Jun");
                worksheet.cells.get("I20").putValue("Jun");

                // Data
                worksheet.cells.get("D21").putValue(304);
                worksheet.cells.get("D22").putValue(402);
                worksheet.cells.get("D23").putValue(321);
                worksheet.cells.get("D24").putValue(123);

                worksheet.cells.get("E21").putValue(300);
                worksheet.cells.get("E22").putValue(500);
                worksheet.cells.get("E23").putValue(219);
                worksheet.cells.get("E24").putValue(422);

                worksheet.cells.get("F21").putValue(222);
                worksheet.cells.get("F22").putValue(331);
                worksheet.cells.get("F23").putValue(112);
                worksheet.cells.get("F24").putValue(350);

                worksheet.cells.get("G21").putValue(100);
                worksheet.cells.get("G22").putValue(200);
                worksheet.cells.get("G23").putValue(300);
                worksheet.cells.get("G24").putValue(400);

                worksheet.cells.get("H21").putValue(200);
                worksheet.cells.get("H22").putValue(300);
                worksheet.cells.get("H23").putValue(400);
                worksheet.cells.get("H24").putValue(500);

                worksheet.cells.get("I21").putValue(400);
                worksheet.cells.get("I22").putValue(200);
                worksheet.cells.get("I23").putValue(200);
                worksheet.cells.get("I24").putValue(100);

                // Dynamically load data on selection of Dropdown value
                worksheet.cells.get("D16").formula = "=IFERROR(VLOOKUP($C$16,$C$21:$I$24,2,FALSE),0)";
                worksheet.cells.get("E16").formula = "=IFERROR(VLOOKUP($C$16,$C$21:$I$24,3,FALSE),0)";
                worksheet.cells.get("F16").formula = "=IFERROR(VLOOKUP($C$16,$C$21:$I$24,4,FALSE),0)";
                worksheet.cells.get("G16").formula = "=IFERROR(VLOOKUP($C$16,$C$21:$I$24,5,FALSE),0)";
                worksheet.cells.get("H16").formula = "=IFERROR(VLOOKUP($C$16,$C$21:$I$24,6,FALSE),0)";
                worksheet.cells.get("I16").formula = "=IFERROR(VLOOKUP($C$16,$C$21:$I$24,7,FALSE),0)";

                // Create Chart
                const index = worksheet.charts.add(ChartType.Column, 0, 3, 12, 9);
                const chart = worksheet.charts.get(index);
                chart.nseries.add("='Sheet1'!$D$16:$I$16", false);
                chart.nseries.get(0).name = "=C16";
                chart.nseries.categoryData = "=$D$15:$I$15";

                // Save result and provide download link
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'output_out.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
            });

        });
    </script>
</html>
```
