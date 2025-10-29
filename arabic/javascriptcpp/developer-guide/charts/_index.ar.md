---
title: إنشاء وإدارة مخطط باستخدام JavaScript عبر C++
linktitle: رسوم بيانية
description: تعلم كيفية استخدام 8667720447سكربت عبر C++ لإنشاء مخططات في مايكروسوفت إكسل. سيعرض دليلنا أنواع المخططات المختلفة وكيفية تخصيص مظهرها وتنسيقها.
keywords: 8667720447سكربت عبر C++، إنشاء مخططات، مايكروسوفت إكسل، أنواع المخططات، التخصيص، المظهر، التنسيق.
type: docs
weight: 130
url: /ar/javascript-cpp/creating-charts/
---

{{% alert color="primary" %}}

من الممكن إضافة مجموعة متنوعة من الرسوم البيانية إلى جداول البيانات باستخدام Aspose.Cells. توفر Aspose.Cells العديد من كائنات الرسم البياني المرنة. يتناول هذا الموضوع كائنات الرسم البياني في Aspose.Cells.

{{% /alert %}}

## **إنشاء الرسوم البيانية**

### **ببساطة إنشاء رسم بياني**
إنشاء مخطط بسيط باستخدام Aspose.Cells يمكن تحقيقه باستخدام أكواد الأمثلة التالية:
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
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding sample values to cells
            worksheet.cells.get("A2").value = "Category1";
            worksheet.cells.get("A3").value = "Category2";
            worksheet.cells.get("A4").value = "Category3";

            worksheet.cells.get("B1").value = "Column1";
            worksheet.cells.get("B2").value = 4;
            worksheet.cells.get("B3").value = 20;
            worksheet.cells.get("B4").value = 50;

            worksheet.cells.get("C1").value = "Column2";
            worksheet.cells.get("C2").value = 50;
            worksheet.cells.get("C3").value = 100;
            worksheet.cells.get("C4").value = 150;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Setting chart data source as the range "A1:C4"
            chart.chartDataRange = { range: "A1:C4", isSeriesInRows: true };

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **الأشياء التي يجب معرفتها لإنشاء مخطط**

قبل إنشاء المخططات، من المهم فهم بعض المفاهيم الأساسية التي تساعد عند إنشاء المخططات باستخدام Aspose.Cells.

#### **كائنات المخطط**

المبالغ الخاصة بالمخططات مذكورة أدناه:

- Series، سلسلة بيانات واحدة في المخطط.
- Axis، محور المخطط.
- Chart، مخطط Excel واحد.
- ChartArea، منطقة المخطط في ورقة العمل.
- ChartDataTable، جدول بيانات المخطط.
- ChartFrame، كائن الإطار في المخطط.
- ChartPoint، نقطة واحدة في سلسلة في المخطط.
- ChartPointCollection، مجموعة تحتوي على جميع النقاط في سلسلة واحدة.
- Charts، مجموعة من كائنات المخطط.
- DataLabels، مجموعة من جميع كائنات DataLabel للسلسلة المحددة.
- FillFormat، تنسيق الملء للشكل.
- Floor، الطابق لمخطط ثلاثي الأبعاد.
- Legend، وسام المخطط.
- Line، خط المخطط.
- SeriesCollection، مجموعة من كائنات Series.
- تسميات العلامات، علامات العلامة المرتبطة بعلامات ضبط على محور الرسم البياني.
- العنوان، عنوان الرسم البياني أو المحور.
- خط الاتجاه، خط اتجاه في الرسم البياني.
- مجموعة خطوط الاتجاه، مجموعة من جميع كائنات خط الاتجاه لسلسلة البيانات المحددة.
- الجدران، الجدران في رسم بياني ثلاثي الأبعاد.

#### **استخدام كائنات الرسم البياني**

كما ذكر أعلاه، جميع كائنات الرسم البياني هي حالات من فئاتها الخاصة وتوفر خصائص وأساليب محددة لأداء مهام محددة. استخدم كائنات الرسم البياني لإنشاء رسوم بيانية.

أضف أي نوع من المخططات إلى ورقة العمل باستخدام مجموعة [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--). يمثل كل عنصر في مجموعة [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--) كائن [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/). ي encapsulate كائن [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) كل كائنات المخطط الأخرى اللازمة لتخصيص مظهر المخطط. يوضح القسم التالي كيفية استخدام بعض الكائنات الأساسية للمخطط لإنشاء مخطط بسيط.

### **إنشاء رسم بياني باستخدام Aspose.Cells**



1. أضف بعض البيانات إلى خلايا ورقة العمل باستخدام طريقة [**putValue(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-string-) الخاصّة بكائن [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/).
   سيتم استخدام هذا كمصدر بيانات للرسم البياني.
2. أضف مخططًا إلى ورقة العمل من خلال استدعاء طريقة [**add**](https://reference.aspose.com/cells/javascript-cpp/chartcollection/#add-charttype-number-number-number-number-) من مجموعة [**ChartCollection**](https://reference.aspose.com/cells/javascript-cpp/chartcollection)، الملفوفة في كائن [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/).
3. حدد نوع المخطط باستخدام تعداد [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/).
   على سبيل المثال، يستخدم المثال أدناه قيمة [**ChartType.Pyramid**](https://reference.aspose.com/cells/javascript-cpp/charttype) كنمط للمخطط.
4. الوصول إلى كائن [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) الجديد من مجموعة [**Charts**](https://reference.aspose.com/cells/javascript-cpp/chartcollection) عن طريق تمرير فهرسه.
5. استخدم أي من كائنات المخططات الم encapsulated في كائن [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) لإدارة المخطط.
   يستخدم المثال أدناه كائن [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection/) للمخطط لتحديد مصدر بيانات المخطط.

عند إضافة بيانات المصدر إلى الرسم البياني، يمكن أن يكون مصدر البيانات مجال خلايا (مثل "A1:C3")، أو تسلسل خلايا غير متجاورة (مثل "A1، A3، A5")، أو تسلسل من القيم (مثل "1،2،3").

تتيح لك هذه الخطوات العامة إنشاء أي نوع من الرسم البياني. استخدم كائنات الرسم البياني المختلفة لإنشاء رسوم بيانية مختلفة.

من الممكن إنشاء العديد من أنواع الرسوم البيانية المختلفة باستخدام Aspose.Cells. جميع الرسوم البيانية القياسية المدعومة بواسطة Aspose.Cells محددة مسبقًا في تعداد يسمى [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/).

تخطيطات الرسوم البيانية المحددة مسبقًا هي:

|**أنواع الرسوم البيانية**|**الوصف**|
| :- | :- |
|Column| يمثل مخطط الأعمدة المتجانبة
|ColumnStacked| يمثل مخطط الأعمدة المكدسة
|Column100PercentStacked| يمثل مخطط الأعمدة المكدسة بنسبة 100%
|Column3DClustered| يمثل مخطط الأعمدة المتجانبة ثلاثي الأبعاد
|Column3DStacked| يمثل مخطط الأعمدة المكدسة ثلاثي الأبعاد
|Column3D100PercentStacked| يمثل مخطط الأعمدة المكدسة بنسبة 100% ثلاثي الأبعاد
|Column3D| يمثل مخطط الأعمدة ثلاثي الأبعاد
|Bar| يمثل مخطط الأعمدة المتجانبة الأفقية
|BarStacked| يمثل مخطط الأعمدة المكدسة الأفقية
|Bar100PercentStacked| يمثل مخطط الأعمدة المكدسة بنسبة 100% الأفقية
|Bar3DClustered| يمثل مخطط الأعمدة المتجانبة ثلاثي الأبعاد الأفقية
|Bar3DStacked| يمثل مخطط الأعمدة المكدسة ثلاثي الأبعاد الأفقية
|Bar3D100PercentStacked| يمثل مخطط الأعمدة المكدسة بنسبة 100% ثلاثي الأبعاد الأفقية
|Line| يمثل مخطط الخطوط
|LineStacked| يمثل مخطط الخطوط المكدسة
|Line100PercentStacked| يمثل مخطط الخطوط المكدسة بنسبة 100%
|LineWithDataMarkers| يمثل مخطط الخط مع علامات البيانات
|LineStackedWithDataMarkers|تمثل مخطط خطوط مكدسة مع علامات البيانات|
|Line100PercentStackedWithDataMarkers|تمثل مخطط خطوط مكدسة 100% مع علامات البيانات|
|Line3D|تمثل مخطط خطوط ثلاثي الأبعاد|
|Pie|تمثل مخطط دائري|
|Pie3D|تمثل مخطط دائري ثلاثي الأبعاد|
|PiePie|تمثل مخطط دائري فوق الدائرة|
|PieExploded|تمثل مخطط دائري منفجر|
|Pie3DExploded|تمثل مخطط دائري منفجر ثلاثي الأبعاد|
|PieBar|تمثل مخطط بارز فوق القطعة من البيتزا|
|Scatter|تمثل مخطط النقاط|
|ScatterConnectedByCurvesWithDataMarker|تمثل مخطط النقاط متصلة بالخطوط المنحنية، مع علامات البيانات|
|ScatterConnectedByCurvesWithoutDataMarker|تمثل مخطط النقاط متصلة بالخطوط المنحنية، بدون علامات البيانات|
|ScatterConnectedByLinesWithDataMarker|تمثل مخطط النقاط متصلة بخطوط، مع علامات البيانات|
|ScatterConnectedByLinesWithoutDataMarker|تمثل مخطط النقاط متصلة بخطوط، بدون علامات البيانات|
|Area|تمثل مخطط المساحة|
|AreaStacked|تمثل مخطط المساحة المكدسة|
|Area100PercentStacked|تمثل مخطط المساحة المكدسة 100%|
|Area3D|تمثل مخطط المساحة ثلاثي الأبعاد|
|Area3DStacked|تمثل مخطط المساحة المكدسة ثلاثي الأبعاد|
|Area3D100PercentStacked|تمثل مخطط المساحة المكدسة 100% ثلاثي الأبعاد|
|Doughnut|يمثل مخطط الدونات|
|DoughnutExploded|يمثل مخطط الدونات المتفجر|
|Radar|يمثل مخطط الرادار|
|RadarWithDataMarkers|يمثل مخطط الرادار مع علامات البيانات|
|RadarFilled|يمثل مخطط الرادار المملوء|
|Surface3D|يمثل مخطط السطح ثلاثي الأبعاد|
|SurfaceWireframe3D|يمثل مخطط سطح ثلاثي الأبعاد بالأسلاك|
|SurfaceContour|يمثل مخطط التكهف|
|SurfaceContourWireframe|يمثل مخطط التكهف بالأسلاك|
|Bubble|يمثل مخطط الفقاعات|
|Bubble3D|يمثل مخطط الفقاعات ثلاثي الأبعاد|
|Cylinder|يمثل مخطط الأسطوانة|
|CylinderStacked|يمثل مخطط الأسطوانة المكدسة|
|Cylinder100PercentStacked|يمثل المخطط الأسطواني المكدس بنسبة 100٪|
|CylindericalBar|يمثل مخطط الأعمدة الأسطوانية|
|CylindericalBarStacked|يمثل مخطط الأعمدة الأسطوانية المكدسة|
|CylindericalBar100PercentStacked|يمثل المخطط الأسطواني المكدس بنسبة 100٪|
|CylindericalColumn3D|يمثل مخطط الأعمدة الأسطوانية ثلاثي الأبعاد|
|Cone|يمثل مخطط المخروط|
|ConeStacked|يمثل مخطط المخروط المكدس|
|Cone100PercentStacked|يمثل 100% حجم الرسم البياني المكدس المخروطي|
|ConicalBar|يمثل رسم بياني شريطي مخروطي|
|ConicalBarStacked|يمثل رسم بياني شريطي مكدس مخروطي|
|ConicalBar100PercentStacked|يمثل رسم بياني شريطي مخروطي مكدس بنسبة 100%|
|ConicalColumn3D|يمثل رسم بياني أعمدة مخروطي ثلاثي الأبعاد|
|Pyramid|يمثل رسم بياني الهرم|
|PyramidStacked|يمثل رسم بياني الهرم المكدس|
|Pyramid100PercentStacked|يمثل رسم بياني الهرم المكدس بنسبة 100%|
|PyramidBar|يمثل رسم بياني شريطي هرمي|
|PyramidBarStacked|يمثل رسم بياني شريطي هرمي مكدس|
|PyramidBar100PercentStacked|يمثل رسم بياني شريطي هرمي مكدس بنسبة 100%|
|PyramidColumn3D|يمثل رسم بياني أعمدة هرمي ثلاثي الأبعاد|

{{% alert color="primary" %}}

عندما تُسند نطاقًا من الخلايا كمصدر للبيانات، يمكنك تعيين النطاق فقط من الزاوية العلوية اليسرى إلى الزاوية السفلى اليمنى. على سبيل المثال، "A1:C3" صالح بينما "C3:A1" غير صالح.

{{% /alert %}}

#### **رسم بياني الهرم**

عند تنفيذ الشيفرة المرجعية، يتم إضافة رسم بياني للهرم إلى ورقة العمل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Chart and Download</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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

            // If a file is provided, load it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Pyramid, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and chart added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **رسم بياني خطي**

في المثال أعلاه، ببساطة تغيير [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) إلى *Line* ينشئ مخطط خطي. المصدر الكامل موفر أدناه. عند تنفيذ الكود، يتم إضافة مخطط خطي إلى ورقة العمل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Chart</title>
    </head>
    <body>
        <h1>Add Chart Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **رسم بياني فقاعي**

لإنشاء مخطط فقاعه، يجب إعداد [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) إلى [**ChartType.Bubble**](https://reference.aspose.com/cells/javascript-cpp/charttype) وبعض الخصائص الإضافية مثل BubbleSizes و Values و XValues وفقًا لذلك. عند تنفيذ الكود التالي، يتم إضافة مخطط فقاعه إلى ورقة العمل.

#### **رسم بياني خطي بمؤشرات البيانات**

لإنشاء مخطط بخط مع علامة البيانات، يجب إعداد [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) إلى *ChartType.LineWithDataMarkers* وبعض الخصائص الإضافية مثل المنطقة الخلفية، علامات السلسلة، القيم و XValues وفقًا لذلك. عند تنفيذ الكود التالي، يتم إضافة مخطط بخط مع علامة البيانات إلى ورقة العمل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Line With Data Marker Chart</title>
    </head>
    <body>
        <h1>Line With Data Marker Chart Example</h1>
        <p>You may optionally select an existing Excel file to modify, or leave empty to create a new workbook.</p>
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
            if (fileInput.files.length === 0) {
                // Proceed with a new workbook if no file selected
            }

            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set columns title 
            worksheet.cells.get(0, 0).putValue("X");
            worksheet.cells.get(0, 1).putValue("Y");

            // Random data shall be used for generating the chart
            // Create random data and save in the cells
            for (let i = 1; i < 21; i++) {
                worksheet.cells.get(i, 0).putValue(i);
                worksheet.cells.get(i, 1).putValue(0.8);
            }

            for (let i = 21; i < 41; i++) {
                worksheet.cells.get(i, 0).putValue(i - 20);
                worksheet.cells.get(i, 1).putValue(0.9);
            }

            // Add a chart to the worksheet
            const idx = worksheet.charts.add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

            // Access the newly created chart
            const chart = worksheet.charts.get(idx);

            // Set chart style
            chart.style = 3;

            // Set autoscaling value to true
            chart.autoScaling = true;

            // Set foreground color white
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;

            // Set Properties of chart title
            chart.title.text = "Sample Chart";

            // Set chart type
            chart.type = AsposeCells.ChartType.LineWithDataMarkers;

            // Set Properties of categoryaxis title
            chart.categoryAxis.title.text = "Units";

            //Set Properties of nseries
            const s2_idx = chart.nSeries.add("A2:A2", true);
            const s3_idx = chart.nSeries.add("A22:A22", true);

            // Set IsColorVaried to true for varied points color
            chart.nSeries.isColorVaried = true;

            // Set properties of background area and series markers
            const series2 = chart.nSeries.get(s2_idx);
            series2.area.formatting = AsposeCells.FormattingType.Custom;
            series2.marker.area.foregroundColor = AsposeCells.Color.Yellow;
            series2.marker.border.isVisible = false;

            // Set X and Y values of series chart
            series2.xValues = "A2:A21";
            series2.values = "B2:B21";

            // Set properties of background area and series markers for series3
            const series3 = chart.nSeries.get(s3_idx);
            series3.area.formatting = AsposeCells.FormattingType.Custom;
            series3.marker.area.foregroundColor = AsposeCells.Color.Green;
            series3.marker.border.isVisible = false;

            // Set X and Y values of series chart
            series3.xValues = "A22:A41";
            series3.values = "B22:B41";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'LineWithDataMarkerChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [قراءة وتلاعب شكل بيانات Excel 2016](/cells/ar/javascript-cpp/read-and-manipulate-excel-2016-charts/)
- [إدارة محاور مخططات Excel](/cells/ar/javascript-cpp/chart-axes/)
- [ضبط مظهر الرسم البياني](/cells/ar/javascript-cpp/setting-chart-appearance/)
- [أنواع المخططات](/cells/ar/javascript-cpp/chart-types/)
- [تخصيص المخططات](/cells/ar/javascript-cpp/customizing-charts/)
- [تعيين مصدر البيانات للمخطط](/cells/ar/javascript-cpp/data-formatting-in-charts/)
- [إدارة تسميات البيانات في مخططات Excel](/cells/ar/javascript-cpp/insert-datalabels-to-chart/)
- [الحصول على ورقة العمل من المخطط](/cells/ar/javascript-cpp/get-worksheet-of-the-chart/)
- [إدارة الأسطورة في مخططات Excel](/cells/ar/javascript-cpp/chart-legend/)
- [تلاعب بموقع وحجم وتصميم المخطط](/cells/ar/javascript-cpp/manipulate-position-size-and-designer-chart/)
- [إنشاء مخطط دائري مع خطوط قيادة](/cells/ar/javascript-cpp/creating-pie-chart-with-leader-lines/)
- [الأشكال في المخططات](/cells/ar/javascript-cpp/controls-in-charts/)
- [إدارة عناوين مخططات Excel](/cells/ar/javascript-cpp/chart-and-axis-titles/)
- [عرض الرسم البياني](/cells/ar/javascript-cpp/chart-rendering/)
- [الحصول على نص المعادلة لخط اتجاه المخطط](/cells/ar/javascript-cpp/get-equation-text-of-chart-trendline/)
