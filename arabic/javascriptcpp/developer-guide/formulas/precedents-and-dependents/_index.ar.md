---
title: المراجع والاعتمادات مع جافا سكريبت عبر C++
linktitle: الدوائر والتبعيات
type: docs
weight: 230
url: /ar/javascript-cpp/precedents-and-dependents/
description: تعلم كيفية تتبع الخلايا المسبقة والمعتمدة في الجداول باستخدام Aspose.Cells for JavaScript عبر C++. فهم كيفية تحديد الخلايا المرتبطة في أوراق مالية معقدة.
---

{{% alert color="primary" %}} 

ورق العمل المالي المعقد، خصوصًا تلك التي تم تطويرها بالتعاون، يمكن أن تخفي الأخطاء الأكثر إحراجًا. فحص الصيغ لضمان الدقة والعثور على مصدر الخطأ يمكن أن يكون صعبًا عندما تستخدم الصيغ خلايا سابقة وخلايا معولة.

{{% /alert %}} 
## **مقدمة**
- **الخلايا المسبقة** هي الخلايا التي يشير إليها صيغة في خلية أخرى. على سبيل المثال، إذا كانت الخلية D10 تحتوي على الصيغة =B5، فإن الخلية B5 هي مسبقة للخلية D10.
- **الخلايا المعتمدة** تحتوي على صيغ تشير إلى خلايا أخرى. على سبيل المثال، إذا كانت الخلية D10 تحتوي على الصيغة =B5، فإن D10 تعتمد على B5.

لجعل ورق العمل سهل القراءة، قد ترغب في إظهار بشكل واضح الخلايا المستخدمة في صيغة. بالمثل، قد ترغب في استخراج الخلايا المعولة لخلايا أخرى.

تتيح Aspose.Cells لك تتبع الخلايا ومعرفة الخلايا المرتبطة.
## **تتبع خلايا السابقة والتابعة: مايكروسوفت إكسل**
قد تتغير الصيغ استنادًا إلى التعديلات التي قام بها العميل. على سبيل المثال ، إذا كانت الخلية C1 معتمدة على C3 و C4 التي تحتوي على صيغة ، وتم تغيير C1 (بحيث يتم تجاوز الصيغة) ، فيجب تغيير C3 و C4 ، أو غيرها من الخلايا ، لتوازن الجدول الخماسي استنادًا إلى قواعد الأعمال.

بالمثل ، فلنفترض أن C1 تحتوي على الصيغة "=(B1*22)/(M2*N32)". أريد أن أجد الخلايا التي يعتمد C1 عليها ، أي الخلايا السابقة B1 و M2 و N32.

قد تحتاج إلى تتبع التبعية لخلية معينة إلى خلايا أخرى. إذا تم تضمين قواعد الأعمال في الصيغ ، نود معرفة التبعيات وتنفيذ بعض القواعد استنادًا إليها. بالمثل ، إذا تم تعديل قيمة خلية معينة ، فأي الخلايا في ورقة العمل يتأثر بتلك التغيير؟

تسمح مايكروسوفت إكسل للمستخدمين بتتبع الخلايا السابقة والتابعة.

1. في شريط الأدوات **View Toolbar** ، حدد **Formula Auditing**. سيتم عرض مربع حوار Formula Auditing.
1. تتبع السابقين:
   1. حدد الخلية التي تحتوي الصيغة التي تريد العثور على الخلايا السابقة لها.
   1. لعرض السهم التتبع إلى كل خلية توفر بيانات مباشرة للخلية النشطة، انقر على **تتبع السابقين** على شريط أدوات **تدقيق الصيغ**.
1. تتبع الصيغ التي تشير إلى خلية معينة (التوابع)
   1. حدد الخلية التي تريد تحديد الخلايا التابعة لها.
   1. لعرض سهم التتبع لكل خلية تعتمد على الخلية النشطة، انقر على **تتبع المعتمدين** على شريط أدوات تدقيق الصيغ.
## **تتبع خلايا السابقة والتابعة: Aspose.Cells**
### **تتبع السابقين**
يسهل Aspose.Cells الحصول على الخلايا المسبقة. يمكن لها ألا تسترد الخلايا التي تقدم البيانات للسلف المبسط فحسب بل تجد أيضًا الخلايا التي تقدم البيانات للسلف المعقد مع النطاقات المسماة.

في المثال أدناه، يتم استخدام ملف إكسل نموذجي، Book1.xls. يحتوي جدول البيانات على بيانات وصيغ على ورقة العمل الأولى.

توفر Aspose.Cells طريقة [Cell.precedents()](https://reference.aspose.com/cells/javascript-cpp/cell/#precedents--) لتتبع المراجع المسبقة لخلية معينة. تعود بمجموعة من المناطق المشار إليها. كما هو موضح أعلاه، في ملف Book1.xls، تحتوي الخلية B7 على صيغة "=SUM(A1:A3)". لذا، فإن الخلايا A1:A3 تعتبر خلايا سابقة للخلية B7. يوضح المثال التالي ميزة تتبع المراجع المسبقة باستخدام قالب الملف Book1.xls.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Precedents Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet's cells
            const cells = workbook.worksheets.get(0).cells;

            // Get cell B4
            const cell = cells.get("B4");

            if (cell) {
                // Get precedents (converted from getPrecedents)
                const ret = cell.precedents;

                if (!ret.isNull() && ret.count > 0) {
                    const area = ret.get(0);

                    const sheetName = area.sheetName;
                    const startAddress = AsposeCells.CellsHelper.cellIndexToName(area.startRow, area.startColumn);
                    const endAddress = AsposeCells.CellsHelper.cellIndexToName(area.endRow, area.endColumn);

                    console.log(sheetName);
                    console.log(startAddress);
                    console.log(endAddress);

                    document.getElementById('result').innerHTML = `<pre>Sheet: ${sheetName}\nStart: ${startAddress}\nEnd: ${endAddress}</pre>`;
                } else {
                    document.getElementById('result').innerHTML = '<p style="color: red;">No precedents found for the cell.</p>';
                }
            } else {
                document.getElementById('result').innerHTML = '<p style="color: red;">Cell B4 is null.</p>';
            }
        });
    </script>
</html>
```
### **تتبع المعتمدين**
تتيح لك Aspose.Cells الحصول على الخلايا المعتمدة في جداول البيانات. لا تقتصر على استرجاع الخلايا التي توفر البيانات لصيغة بسيطة فحسب، بل أيضًا العثور على الخلايا التي توفر البيانات للمعتمدين على صيغة معقدة مع النطاقات المسماة.

توفر Aspose.Cells طريقة [Cell.dependents(boolean)]](https://reference.aspose.com/cells/javascript-cpp/cell/#dependents-boolean-) لتتبع الخلايا المعتمدة. على سبيل المثال، في ملف Book1.xlsx تحتوي خلايا B2 و C2 على الصيغ "=A1+20" و "=A1+30" على التوالي. يوضح المثال التالي كيفية تتبع المعتمدين لخلية A1 باستخدام القالب الخاص بـ Book1.xlsx.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Get Cell Dependents Example</h1>
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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("B2");
            // Ensure dependents is accessed as a property (converted from getDependents)
            const dependents = cell.dependents;

            if (Array.isArray(dependents)) {
                let out = '<p>Dependents found:</p><ul>';
                for (const c of dependents) {
                    console.log(c.name);
                    out += `<li>${c.name}</li>`;
                }
                out += '</ul>';
                resultDiv.innerHTML = out;
            } else {
                console.error("Dependents is not an array");
                resultDiv.innerHTML = '<p style="color: red;">Dependents is not an array</p>';
            }
        });
    </script>
</html>
```
### **تتبع الخلايا المسبقة والمعتمدة وفقًا لسلسلة الحساب**
واجهات برمجة التطبيقات أعلاه لتتبع المراجع والمعتمدين تعتمد على تعبير الصيغة نفسه. فهي توفر طريقة مريحة للمستخدمين لتتبع الاعتمادات المتبادلة لعدد قليل من الصيغ. إذا كان هناك عدد كبير من الصيغ في المصنف ويحتاج المستخدم إلى تتبع المراجع والمعتمدين لكل خلية، فإن الأداء سيضعف. لمثل هذا الوضع، ينبغي للمستخدم النظر في استخدام الطريقتين [Cell.precedentsInCalculation()](https://reference.aspose.com/cells/javascript-cpp/cell/#precedentsInCalculation--) و [Cell.dependentsInCalculation(boolean)]](https://reference.aspose.com/cells/javascript-cpp/cell/#dependentsInCalculation-boolean-) اللتان تتبعان الاعتمادات وفقاً لسلسلة الحساب. لذا، لاستخدامهما، يجب أولاً تمكين سلسلة الحساب من خلال [FormulaSettings.enableCalculationChain()](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--). ثم، يجب إجراء حساب كامل للمصنف باستخدام [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--). بعد ذلك، يمكنك تتبع المراجع أو الاعتمادات لجميع تلك الخلايا التي تحتاجها.

بالنسبة لبعض الصيغ، قد تكون المراجع الناتجة مختلفة بين المراجع و precedentsInCalculation، ويكون المعتمدون النهائيون مختلفين بين dependents و dependentsInCalculation. على سبيل المثال، إذا كانت صيغة الخلية A1 هي "=IF(TRUE,B2,C3)", ستوفر المراجع B2 و C3 كمراجع مسبقة لـ A1. ووفقًا لذلك، تحتوي الخلايا B2 و C3 على الاعتماد A1 عند التحقق بواسطة dependents. ومع ذلك، بالنسبة لحساب هذه الصيغة، فمن الواضح أن B2 فقط يمكن أن تؤثر على النتيجة المحسوبة. لذا، لن توفر precedentsInCalculation C3 ل A1، ولن توفر dependentsInCalculation A1 لـ C3. أحيانًا، يحتاج المستخدم فقط إلى تتبع تلك الاعتمادات المتبادلة التي تؤثر فعليًا على النتيجة المحسوبة للصيغ استنادًا إلى البيانات الحالية للمصنف، لذا يجب عليهم استخدام dependentsInCalculation/precedentsInCalculation بدلاً من dependents/precedents.

المثال التالي يوضح كيفية تتبع السابقين والمعتمدين وفقًا لسلسلة الحساب للخلايا:


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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;

            // Setting formulas
            cells.get("A1").formula = "=B1+SUM(B1:B10)+[Book1.xls]Sheet1!B2";
            cells.get("A2").formula = "=IF(TRUE,B2,B1)";

            // Enable calculation chain
            workbook.settings.formulaSettings.enableCalculationChain = true;

            // Calculate formulas
            workbook.calculateFormula();

            // Collect output
            let output = '';

            let en = cells.get("B1").dependentsInCalculation;
            output += "B1's calculation dependents:\n";
            if (en && en.length !== undefined) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            } else if (en) {
                // If it's an iterable but doesn't have length
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            }
            output += "\n";

            en = cells.get("B2").dependentsInCalculation;
            output += "B2's calculation dependents:\n";
            if (en && en.length !== undefined) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            } else if (en) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            }
            output += "\n";

            en = cells.get("A1").precedentsInCalculation;
            output += "A1's calculation precedents:\n";
            if (en && en.length !== undefined) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            } else if (en) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            }
            output += "\n";

            en = cells.get("A2").precedentsInCalculation;
            output += "A2's calculation precedents:\n";
            if (en && en.length !== undefined) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            } else if (en) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            }

            resultDiv.innerHTML = '<pre>' + output.replace(/</g, '&lt;') + '</pre>';

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
        });
    </script>
</html>
```
