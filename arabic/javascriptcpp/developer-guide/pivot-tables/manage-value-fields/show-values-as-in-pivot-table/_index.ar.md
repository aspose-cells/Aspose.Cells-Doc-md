---
title: إظهار القيم كـ في جدول محوري
linktitle: إظهار القيم كـ في جدول محوري
description: عرض قيم حقول البيانات في جدول محوري كنسبة مئوية من الإجمالي، أو اختلاف عن عنصر أساسي، أو مجموعات تراكمية، أو تصنيفات، وأكثر باستخدام Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, JavaScript via C++, جدول محوري, إظهار القيم كـ, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /ar/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
عادةً ما يجمع جدول محوري كل حقل بيانات باستخدام دالة تجميع مثل `Sum` أو `Count`. ميزة **Show Values As** في Excel تستبدل كل نتيجة معروضة بحساب ثانوي مشتق من ذلك التجميع — على سبيل المثال، نسبة مئوية من الإجمالي الكلي، أو مجموع تراكمي، أو فرق عن عنصر أساسي مختار، أو تصنيف — وبالتالي يمكنك إجراء تحليل مقارن دون الحاجة إلى صيغ مساعدة أو أعمدة محسوبة.  
تشمل الاستخدامات الشائعة تحليل حصة الإجمالي، بما في ذلك النسب المئوية للصف أو العمود أو الإجمالي الكلي؛ وتقريرًا تراكمياً باستخدام مجموع تراكمي في حقل الفترة؛ وتحليل الانحراف مقابل عنصر مرجعي باستخدام الفرق أو الفرق النسبي عن عنصر أساسي؛ وتصنيف القيم من الأصغر إلى الأكبر أو من الأكبر إلى الأصغر.  
في Aspose.Cells for JavaScript via C++، يحدد تعداد `PivotShowValuesAsType` الحساب الثانوي. الخاصية للقراءة فقط `PivotField.showValuesSetting` تُعيد كائن `PivotShowValuesSetting`، حيث تُكوّن الخصائص القابلة للكتابة `showValuesAs` و`baseFieldIndex` و`baseItemIndex` السلوك؛ كما تُطبّق طريقة الاختصار `PivotField.showValuesAs(...)` نفس الإعدادات في استدعاء واحد. طبّق هذه الإعدادات على حقل بيانات أو قيمة يتم الحصول عليه من `PivotTable.dataFields`.

## **أعضاء تعداد PivotShowValuesAsType**
يحافظ حقل البيانات على دالة التجميع الخاصة به، مثل Sum أو Count، بينما تقوم ميزة إظهار القيم كـ بتحويل طريقة عرض القيمة المجمعة فقط. إلى جانب كتابة خصائص `PivotShowValuesSetting` مباشرة (انظر القسم الأخير)، تُطبق طريقة الاختصار ذات الاستدعاء الواحد نفس التكوين. تُوفر بطريقتين — إحداهما تُعنى بالحقل الأساسي والعنصر الأساسي بحسب الفهرس، والأخرى بحسب الاسم:

```html
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| المعامل | المعنى | متى يكون مطلوبًا |
| --- | --- | --- |
| `showValuesAsType` | حساب `PivotShowValuesAsType` الثانوي المراد تطبيقه. | دائمًا. |
| `baseField` | الفهرس الصفري للحقل الأساسي ضمن الحقول الأساسية لجدول المحور (مثال: فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي)، أو — في الصيغة التي تعتمد على الاسم — اسم الحقل الأساسي. | تنسيقات القاعدة الثمانية أدناه (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); استخدم `0` (أو `null` في صيغة الاسم) لكل تنسيق آخر. |
| `baseItem` | الفهرس الصفري للعنصر الأساسي، مع قيمتين خاصتين: -1 تُحدد العنصر السابق و-2 العنصر التالي (ربط JavaScript عبر C++ لا يصدر الثوابت المسماة — استخدم القيم الحرفية). صيغة الاسم تأخذ تسمية العنصر الأساسي بدلاً من ذلك، وتُعطى `null` عندما لا يتطلب التنسيق اختيار عنصر أساسي. | تُقيِّم ثلاثة تنسيقات تعتمد على العنصر الأساسي فقط (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`)؛ تُهمل تنسيقات الخمسة التي تعتمد على الحقل (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, كلا التصنيفين) — استخدم `0` أو `null`. |

| نوع الحساب | السلوك | معلمات العنصر الأساسي |
| --- | --- | --- |
| `Normal` | لا يوجد حساب ثانوي؛ تُعرض القيمة المجمعة كما هي (الافتراضي). | — |
| `DifferenceFrom` | تُظهر القيمة كفرق عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `baseItem` (فهرس أو تسمية، أو إشارة السابق/التالي) |
| `PercentageOf` | تُظهر القيمة كنسبة مئوية من قيمة عنصر أساسي في حقل أساسي. | `baseField` + `baseItem` (فهرس أو تسمية، أو إشارة السابق/التالي) |
| `PercentageDifferenceFrom` | تُظهر القيمة كنسبة الفرق عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `baseItem` (فهرس أو تسمية، أو إشارة السابق/التالي) |
| `RunningTotalIn` | تُظهر القيمة كمجموع تراكمي للعنصر المتتابع في حقل أساسي. | `baseField` (الحقل الذي يُحدد ترتيب العناصر لتجميع القيم) |
| `PercentageOfRow` | تُظهر القيمة كنسبة مئوية من إجمالي الصف. | — |
| `PercentageOfColumn` | تُظهر القيمة كنسبة مئوية من إجمالي العمود. | — |
| `PercentageOfTotal` | تُظهر القيمة كنسبة مئوية من الإجمالي الكلي. | — |
| `Index` | تُظهر القيمة باستخدام صيغة الفهرس في Excel ((القيمة * الإجمالي الكلي) / (إجمالي الصف * إجمالي العمود)). | — |
| `PercentageOfParentRowTotal` | تُظهر القيمة كنسبة مئوية من إجمالي الصف الأصلي (للحقول المتداخلة). | — |
| `PercentageOfParentColumnTotal` | تُظهر القيمة كنسبة مئوية من إجمالي العمود الأصلي (للحقول المتداخلة). | — |
| `PercentageOfParentTotal` | تُظهر القيمة كنسبة مئوية من إجمالي العنصر الأصلي. | `baseField` (الحقل الأصلي الذي يُعدّ الإجمالي مرجعًا) |
| `PercentageOfRunningTotalIn` | تُظهر القيمة كنسبة مئوية من مجموع تراكمي في حقل أساسي. | `baseField` (حقل التجميع) |
| `RankSmallestToLargest` | تصنّف القيمة من الأصغر (1) إلى الأكبر. | `baseField` (الحقل الذي تُحدد عناصره نطاق التصنيف) |
| `RankLargestToSmallest` | تصنّف القيمة من الأكبر (1) إلى الأصغر. | `baseField` (الحقل الذي تُحدد عناصره نطاق التصنيف) |

{{% alert color="primary" %}}
`showValuesAs(...)` يكتب خصائص `PivotShowValuesSetting` (`showValuesAs` و`baseFieldIndex` و`baseItemIndex`) — الطريقة والكائن الخاص بالخاصية طريقتان لتكوين الحالة نفسها، مما يعكس محددات الحقل الأساسي والعنصر الأساسي في نافذة إظهار القيم كـ ببرنامج Excel.
{{% /alert %}}

## **إظهار القيم كنسبة مئوية من الإجمالي**
استدعِ الطريقة `PivotField.showValuesAs` مع `PivotShowValuesAsType.PercentageOfTotal` لتحويل كل خلية حقل بيانات، بما في ذلك الإجمالي الكلي، إلى حصتها من إجمالي النتيجة. وبالتالي تُعرض الأرقام كنسب من مجموعة النتائج الكاملة. هذا التنسيق يقيس كل قيمة مقابل الإجمالي الكلي فقط، لذا لا يحتاج إلى حقل أساسي أو عنصر أساسي — الوسيطات اللاحقة (`0`, `0`) هي عناصر نائبة يتجاهلها التنسيق، كما هو موضح في جدول المعاملات أعلاه.

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
                // base arguments (0, 0) are placeholders the format ignores
                const dataField = pivotTable.dataFields.get(0);
                dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
                pivotTable.calculateData();
                // Body now reads (underlying values are fractions, shown with the
                // percentage format): Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
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
اقرأ التكوين الحالي عبر الخاصية `PivotField.showValuesSetting`: تُعيد هذه الخاصية للقراءة فقط كائن `PivotShowValuesSetting` الذي تصف خصائصه الحساب النشط لإظهار القيم كـ. لتغيير التكوين، استدعِ الطريقة `PivotField.showValuesAs` — فهي تُكتب جميع الإعدادات في استدعاء واحد، لذا لن تحتاج إلى تعيين الخصائص واحدةً تلو الأخرى.  
يعرض كائن `PivotShowValuesSetting` الحالة التي تُكتبها الخاصية `showValuesAs`:
- `showValuesAs` يختار حساب `PivotShowValuesAsType` الثانوي.
- `baseFieldIndex` يحدد الفهرس الصفري للحقل الأساسي ضمن حقول المحور. يُستخدم في التنسيقات التي تعتمد على القاعدة.
- `baseItemIndex` يحدد العنصر الأساسي: فهرس صفري لعنصر محوري محدد، أو إحدى القيمتين الخاصتين — -1 للعنصر السابق، -2 للعنصر التالي (الربط لا يصدر الثوابت المسماة). يُستخدم في التنسيقات التي تعتمد على العنصر الأساسي.
- `baseFieldName` و`baseItemCaption` هما عرضان للقراءة فقط يُظهران اسم الحقل الأساسي المُ resolved وتسمية العنصر الأساسي؛ على سبيل المثال، بعد اختيار إشارة العنصر السابق، تُعيد `baseItemCaption` القيمة `(previous)`.  
بعد استدعاء `showValuesAs`، استدعِ `PivotTable.calculateData()` مرة أخرى حتى يُعاد حساب جسم الجدول المحوري وإعادة عرضه وفقًا للتكوين المُحدَّث.

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
                    `ShowValuesAs: ${settings.showValuesAs}`,
                    `BaseFieldIndex: ${settings.baseFieldIndex}`,
                    `BaseItemIndex: ${settings.baseItemIndex}`,
                    `BaseFieldName: ${settings.baseFieldName}`,
                    `BaseItemCaption: ${settings.baseItemCaption}`
                ];
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                // Switch to a base-item calculation with the one-call method: difference
                // from the value of the previous item in the row field
                // (-1 is the previous-item sentinel; the binding does not export the constant)
                dataField.showValuesAs(
                    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
                    pivotTable.rowFields.get(0).baseIndex,
                    -1
                );
                pivotTable.calculateData();
                // Note: the percentage number format saved by the previous example still
                // clings to the data field cells; the underlying values are now differences
                // Re-read the applied configuration
                messages.push(`ShowValuesAs now: ${dataField.showValuesSetting.showValuesAs}`);
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
- [تطبيق النمط على جدول محوري](/cells/ar/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}