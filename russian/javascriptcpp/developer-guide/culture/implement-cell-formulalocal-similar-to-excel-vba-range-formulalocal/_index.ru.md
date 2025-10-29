---
title: Реализуйте Cell.FormulaLocal, похожий на Excel VBA Range.FormulaLocal, с помощью JavaScript через C++
linktitle: Реализуйте свойство Cell.FormulaLocal аналогично Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /ru/javascript-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Узнайте, как реализовать Cell.FormulaLocal, похожий на Excel VBA Range.FormulaLocal, с помощью Aspose.Cells for JavaScript через C++. 
---

## **Возможные сценарии использования**

 Формулы Microsoft Excel могут иметь разные названия в разных странах или регионах или на разных языках. Например, функция **SUM** называется **SUMME** на немецком. Aspose.Cells не работает с неанглийскими названиями функций. В Microsoft Excel VBA есть свойство **Range.FormulaLocal**, которое возвращает название функции в соответствии с языком или регионом. Aspose.Cells for JavaScript через C++ также предоставляет свойство [**Cell.formulaLocal**](https://reference.aspose.com/cells/javascript-cpp/cell/#formulaLocal--) для этой цели. Однако это свойство работает только при реализации метода [**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-).

## **Реализовать Cell.FormulaLocal аналогично Excel VBA Range.FormulaLocal**

Следующий пример объясняет, как реализовать метод [**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-). Метод возвращает локальное имя стандартной функции. Если имя функции **SUM**, он возвращает **UserFormulaLocal_SUM**. Вы можете изменить код по своему усмотрению и возвращать правильные локальные имена функций, например, **SUM** — это **SUMME** на немецком, а **TEXT** — это **ТЕКСТ** на русском. Также обратитесь к выводу консоли приведенного ниже образца кода для справки.

## **Образец кода**

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

## **Вывод в консоль**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
