---
title: 实现类似Excel VBA范围的Cell.FormulaLocal，使用JavaScript通过C++
linktitle: 实现类似于Excel VBA Range.FormulaLocal的Cell.FormulaLocal
type: docs
weight: 30
url: /zh/javascript-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: 学习如何使用Aspose.Cells for JavaScript通过C++实现类似Excel VBA的Range.FormulaLocal的Cell.FormulaLocal。 
---

## **可能的使用场景**

Microsoft Excel公式在不同地区或语言中可能有不同的名称。例如，**SUM**函数在德语中称为**SUMME**。Aspose.Cells不能使用非英语的函数名称。在Microsoft Excel VBA中，有**Range.FormulaLocal**属性，返回该函数的本地名称。Aspose.Cells for JavaScript通过C++也提供了用于此目的的[**Cell.formulaLocal**](https://reference.aspose.com/cells/javascript-cpp/cell/#formulaLocal--)属性。然而，此属性仅在你实现[**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-)方法时有效。

## **实现类似于Excel VBA Range.FormulaLocal的Cell.FormulaLocal**

 以下示例代码说明如何实现 [**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-) 方法。该方法返回标准函数的本地名称。如果标准函数名为 **SUM** ，它返回 **UserFormulaLocal_SUM**。你可以根据自己的需要修改代码，并返回正确的本地函数名，例如在德语中 **SUM** 为 **SUMME**，俄语中 **TEXT** 为 **ТЕКСТ**。请同时参考下面的示例代码输出。

## **示例代码**

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

## **控制台输出**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
