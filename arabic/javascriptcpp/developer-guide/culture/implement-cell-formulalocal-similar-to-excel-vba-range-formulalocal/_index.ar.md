---
title: تنفيذ Cell.FormulaLocal مماثل ل Excel VBA Range.FormulaLocal باستخدام JavaScript عبر C++
linktitle: تنفيذ Cell.FormulaLocal مماثل لـ Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /ar/javascript-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: تعلم كيفية تنفيذ Cell.FormulaLocal مماثل ل Excel VBA Range.FormulaLocal باستخدام Aspose.Cells for JavaScript عبر C++. 
---

## **سيناريوهات الاستخدام المحتملة**

 قد تمتلك صيغ Microsoft Excel أسماء مختلفة حسب locale أو المنطقة أو اللغة. على سبيل المثال، دالة **SUM** تسمى **SUMME** بالألمانية. لا يمكن لـ Aspose.Cells التعامل مع أسماء الدوال غير الإنجليزية. في Microsoft Excel VBA، هناك الخاصية **Range.FormulaLocal** التي تُرجع اسم الدالة حسب لغتها أو منطقتها. Aspose.Cells for JavaScript عبر C++ يوفر أيضًا [**Cell.formulaLocal**](https://reference.aspose.com/cells/javascript-cpp/cell/#formulaLocal--) لهذه الغاية. ومع ذلك، ستعمل هذه الخاصية فقط عندما تقوم بتنفيذ `[**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-)`.

## **تنفيذ Cell.FormulaLocal مماثل لـ Excel VBA Range.FormulaLocal**

يشرح رمز العينة التالي كيفية تنفيذ طريقة [**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-). تعيد الطريقة الاسم المحلي للوظيفة القياسية. إذا كان اسم الوظيفة القياسية هو **SUM**، فستُعيد **UserFormulaLocal_SUM**. يمكنك تعديل الكود حسب حاجتك وإرجاع الأسماء الصحيحة للوظائف المحلية، على سبيل المثال، يكون **SUM** هو **SUMME** بالألمانية و **TEXT** هو **ТЕКСТ** بالروسية. يُرجى أيضًا مراجعة مخرجات وحدة التحكم للرمز المقدم أدناه للمرجع.

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Globalization Example</h1>
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

        // Define GS class implementing localization override
        class GS extends AsposeCells.GlobalizationSettings {
            localFunctionName(standardName) {
                // Change the SUM function name as per your needs.
                if (standardName === "SUM") {
                    return "UserFormulaLocal_SUM";
                }

                // Change the AVERAGE function name as per your needs.
                if (standardName === "AVERAGE") {
                    return "UserFormulaLocal_AVERAGE";
                }

                return "";
            }
        }

        document.getElementById('runExample').addEventListener('click', () => {
            const resultDiv = document.getElementById('result');

            // Create workbook
            const wb = new Workbook();

            // Assign GlobalizationSettings implementation class
            wb.settings.globalizationSettings = new GS();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access some cell
            const cell = ws.cells.get("C4");

            // Assign SUM formula and get its FormulaLocal
            cell.formula = "SUM(A1:A2)";
            const formulaLocal1 = cell.formulaLocal;

            // Assign AVERAGE formula and get its FormulaLocal
            cell.formula = "=AVERAGE(B1:B2, B5)";
            const formulaLocal2 = cell.formulaLocal;

            resultDiv.innerHTML = `<p>Formula Local 1: ${formulaLocal1}</p><p>Formula Local 2: ${formulaLocal2}</p>`;

            // Save the workbook and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

## **مخرجات الوحدة**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
