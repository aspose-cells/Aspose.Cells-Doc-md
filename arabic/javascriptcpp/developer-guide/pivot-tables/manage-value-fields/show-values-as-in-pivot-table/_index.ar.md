---
title: إظهار القيم كـ في جدول محوري
description: عرض قيم حقول بيانات جدول محوري كنسبة مئوية من الإجمالي، أو فرقًا عن عنصر أساسي، أو مجموعات تراكمية، أو ترتيبات، وأكثر باستخدام Aspose.Cells for JavaScript via C++.
linktitle: Show Values As
keywords: Aspose.Cells, JavaScript via C++, جدول محوري, إظهار القيم كـ, تنسيق عرض البيانات, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /ar/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
عادةً ما يجمع جدول محوري كل حقل بيانات باستخدام دالة تجميع مثل `Sum` أو `Count`. ميزة **Show Values As** في Excel تستبدل كل نتيجة معروضة بحساب ثانوي مستمد من ذلك التجميع — على سبيل المثال، نسبة من الإجمالي الكلي، أو مجموع متراكم، أو فرق عن عنصر أساسي مختار، أو ترتيب — بحيث يمكنك إجراء تحليل مقارن دون الحاجة إلى صيغ مساعدة أو أعمدة محسوبة.  
تشمل الاستخدامات الشائعة تحليل الحصة من الإجمالي، بما في ذلك النسب المئوية للصف أو العمود أو الإجمالي الكلي؛ والتقارير التراكمية باستخدام مجموع متتابع في حقل زمني؛ وتحليل الانحراف مقابل عنصر مرجعي باستخدام الفرق أو الفرق بالنسبة المئوية؛ وترتيب القيم من الأصغر إلى الأكبر أو العكس.  
في Aspose.Cells for JavaScript via C++، يحدد `PivotFieldDataDisplayFormat` الحساب الثانوي. الخاصية للقراءة فقط `PivotField.showValuesSetting` تُعيد كائن `PivotShowValuesSetting`، ويمكن تعديل الخصائص القابلة للكتابة `calculationType` و `baseFieldIndex` و `baseItemPositionType` و `baseItemIndex` لتكوين السلوك؛ كما تُطبق الطريقة المريحة `PivotField.showValuesAs(...)` نفس الإعدادات الأربع في استدعاء واحد. يُطبق هذا التكوين على حقل بيانات أو قيمة يتم الحصول عليه من `PivotTable.dataFields`.

## **أعضاء تعداد PivotFieldDataDisplayFormat**
يظل حقل البيانات يحتفظ بدالة التجميع الخاصة به، مثل Sum أو Count، بينما يقوم Show Values As بتحويل طريقة عرض القيمة المجمعة فقط. بالإضافة إلى كتابة خصائص `PivotShowValuesSetting` مباشرة (انظر القسم الأخير)، تُطبق طريقة المساعدة ذات الاستدعاء الواحد نفس التكوين:

```html
dataField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
```

| المعامل | المعنى | متى يكون مطلوبًا |
| --- | --- | --- |
| `displayFormat` | حساب ثانوي من نوع `PivotFieldDataDisplayFormat` يُراد تطبيقه. | دائمًا. |
| `baseField` | الفهرس الصفري للحقول الأساسية بين الحقول الأساسية لجدول محوري (على سبيل المثال، فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي). | فقط تنسيقات المرجع الستة أدناه (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `baseItemPositionType` | طريقة اختيار العنصر الأساسي بالنسبة للعنصر الحالي: `PivotItemPositionType.Previous`، `.Next`، أو `.Custom`. | فقط تنسيقات العنصر الأساسي الثلاثة (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `baseItem` | الفهرس الصفري للعنصر الأساسي. | فقط عندما يكون `baseItemPositionType` هو `Custom` (يُحدّد الفهرس العنصر الأساسي بدقة); تُهمل لـ `Previous` / `Next` ولكل الصيغ غير القائمة على العنصر الأساسي — يُمرّر `0`. |

| نوع الحساب | السلوك | معاملات العنصر الأساسي |
| --- | --- | --- |
| `Normal` | لا يوجد حساب ثانوي؛ تُعرض القيمة المجمعة كما هي (الافتراضي). | — |
| `DifferenceFrom` | تُظهر القيمة كفرق عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` فقط مع `Custom`) |
| `PercentageOf` | تُظهر القيمة كنسبة مئوية من قيمة عنصر أساسي في حقل أساسي. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` فقط مع `Custom`) |
| `PercentageDifferenceFrom` | تُظهر القيمة كنسبة مئوية للفرق عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` فقط مع `Custom`) |
| `RunningTotalIn` | تُظهر القيمة كمجموع متراكم للعناصر المتتابعة في حقل أساسي. | `baseField` (الحقل الذي يتحكم بترتيب التجميع) |
| `PercentageOfRow` | تُظهر القيمة كنسبة مئوية لإجمالي الصف. | — |
| `PercentageOfColumn` | تُظهر القيمة كنسبة مئوية لإجمالي العمود. | — |
| `PercentageOfTotal` | تُظهر القيمة كنسبة مئوية للإجمالي الكلي. | — |
| `Index` | تُظهر القيمة باستخدام صيغة الفهرس في Excel ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | تُظهر القيمة كنسبة مئوية لإجمالي الصف الأصلي (للحقول الصفية المتداخلة). | — |
| `PercentageOfParentColumnTotal` | تُظهر القيمة كنسبة مئوية لإجمالي العمود الأصلي (للحقول العمودية المتداخلة). | — |
| `PercentageOfParentTotal` | تُظهر القيمة كنسبة مئوية لإجمالي الأصل. | `baseField` (الحقل الأصل المرجعي) |
| `PercentageOfRunningTotalIn` | تُظهر القيمة كنسبة مئوية لمجموع متراكم في حقل أساسي. | `baseField` (حقل التجميع) |
| `RankSmallestToLargest` | ترتّب القيم من الأصغر (1) إلى الأكبر. | — |
| `RankLargestToSmallest` | ترتّب القيم من الأكبر (1) إلى الأصغر. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` يكتب الخصائص لـ `PivotShowValuesSetting` (`calculationType`, `baseFieldIndex`, `baseItemPositionType`, `baseItemIndex`) — تُعَدُّ الطريقة وكائن الخاصية طريقتين لتكوين الحالة نفسها، مماثلة لمحددات الحقل الأساسي والعنصر الأساسي في مربع حوار Show Values As في Excel.
{{% /alert %}}

## **إظهار القيم كنسبة مئوية من الإجمالي**
استدعِ الطريقة `PivotField.showValuesAs` مع `PivotFieldDataDisplayFormat.PercentageOfTotal` لتحويل كل خلية حقل بيانات، بما فيها الإجمالي الكلي، إلى نصيبها من الإجمالي الكلي. لذلك تُعرض الأرقام كنسب من مجموعة النتائج الكاملة. هذه الصيغة تقيس كل قيمة مقابل الإجمالي الكلي فقط، لذلك لا تحتاج إلى حقل أساسي أو عنصر أساسي — الوسائط الأخيرة (`0`, `PivotItemPositionType.Previous`, `0`) هي مجرد نائبات يتجاهلها التنسيق كما هو موضح في جدول المعاملات أعلاه.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                // Load or create a workbook with source data
                const workbook = new Workbook();
                const dataSheet = workbook.worksheets.get(0);
                const cells = dataSheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Amount";
                const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
                const amounts = [10, 20, 30, 40, 50, 60];
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = amounts[i];
                }
                // Add a pivot table on a new worksheet
                const pivotSheetIndex = workbook.worksheets.add();
                const pivotSheet = workbook.worksheets.get(pivotSheetIndex);
                const pivotTable = pivotSheet.pivotTables.add("=Sheet1!A1:B7", 2, 2);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                // Show the Amount data field as a percentage of the grand total with the
                // one-call method; PercentageOfTotal takes no base item, so the trailing
                // base arguments (0, Previous, 0) are placeholders the format ignores
                const dataField = pivotTable.dataFields.get(0);
                dataField.showValuesAs(
                    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
                    0,
                    AsposeCells.PivotItemPositionType.Previous,
                    0
                );
                pivotTable.calculateData();
                // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "ShowValuesAsPercentageOfTotal.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **قراءة وتكوين PivotField.showValuesSetting**
اقرأ التكوين الحالي عبر `PivotField.showValuesSetting`: الخاصية للقراءة فقط تُعيد كائن `PivotShowValuesSetting` الخاص بالحقل، والذي تصف خصائصه الأربعة الحساب الثانوي النشط. لتغيير التكوين، استدعِ الطريقة `PivotField.showValuesAs` — فهي تكتب جميع الإعدادات الأربع في استدعاء واحد، لذا لن تحتاج أبدًا إلى تعيين الخصائص واحدة تلو الأخرى.  
يعرض كائن `PivotShowValuesSetting` الخصائص الأربعة التي تُكتبها `showValuesAs`:
- `calculationType` يُحدد الحساب الثانوي من نوع `PivotFieldDataDisplayFormat`.
- `baseFieldIndex` يحدّد الفهرس الصفري للحقول الأساسية داخل حقول المحوري. يُستعمل في تنسيقات المرجع.
- `baseItemPositionType` يحدد طريقة تموضع العنصر الأساسي بالنسبة للعنصر الحالي ويقبل القيم `PivotItemPositionType.Next`, `PivotItemPositionType.Previous`, أو `PivotItemPositionType.Custom`.
- `baseItemIndex` يحدّد الفهرس الصفري للعنصر الأساسي ويُستعمل عندما يكون `baseItemPositionType` هو `Custom`.  
بعد استدعاء `showValuesAs`، استدعِ `PivotTable.calculateData()` مرة أخرى بحيث يتم إعادة حساب جسم الجدول المحوري وإعادة عرضه بالإعدادات المحدثة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const ready = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await ready;
                const file = document.getElementById('fileInput').files[0];
                if (!file) {
                    throw new Error("Please select ShowValuesAsPercentageOfTotal.xlsx.");
                }
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(1);
                const pivotTable = worksheet.pivotTables.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Read the current show-values settings
                const settings = dataField.showValuesSetting;
                const messages = [
                    `CalculationType: ${settings.calculationType}`,
                    `BaseFieldIndex: ${settings.baseFieldIndex}`,
                    `BaseItemPositionType: ${settings.baseItemPositionType}`,
                    `BaseItemIndex: ${settings.baseItemIndex}`
                ];
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                // Switch to a base-item calculation with the one-call method: difference
                // from the value of the previous item in the row field
                dataField.showValuesAs(
                    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
                    pivotTable.rowFields.get(0).baseIndex,
                    AsposeCells.PivotItemPositionType.Previous,
                    0
                );
                pivotTable.calculateData();
                // Note: the percentage number format saved by the previous example still
                // clings to the data field cells; the underlying values are now differences
                // Re-read the applied configuration
                messages.push(`CalculationType now: ${dataField.showValuesSetting.calculationType}`);
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "ShowValuesAsDifferenceFrom.xlsx";
                downloadLink.style.display = "block";
            } catch (error) {
                document.getElementById('result').innerHTML =
                    `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **مقالات ذات صلة**
- [إدارة حقول القيم في جدول محوري](/cells/ar/javascript-cpp/manage-value-fields/)
- [تحديث جدول محوري](/cells/ar/javascript-cpp/refresh-pivot-table/)
- [تطبيق نمط على جدول محوري](/cells/ar/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}