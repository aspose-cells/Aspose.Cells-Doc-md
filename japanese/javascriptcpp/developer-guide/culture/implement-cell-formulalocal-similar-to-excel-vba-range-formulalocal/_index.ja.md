---
title: JavaScriptをC++経由でExcel VBAのRange.FormulaLocalに類似したCell.FormulaLocalを実装する
linktitle: Excel VBAのRange.FormulaLocalに類似したCell.FormulaLocalの実装
type: docs
weight: 30
url: /ja/javascript-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Aspose.Cells for JavaScriptを使用して、Excel VBAのRange.FormulaLocalに類似したCell.FormulaLocalを実装する方法を学びます。 
---

## **可能な使用シナリオ**

Microsoft Excelの関数名は異なるロケールや地域、言語によって異なる場合があります。例えば、**SUM**関数はドイツ語では**SUMME**と呼ばれます。Aspose.Cellsは英語以外の関数名には対応していません。Microsoft Excel VBAには、その言語や地域に応じた関数名を返す**Range.FormulaLocal**プロパティがあります。Aspose.Cells for JavaScriptをC++で使用すると、その目的のために[**Cell.formulaLocal**](https://reference.aspose.com/cells/javascript-cpp/cell/#formulaLocal--)プロパティも提供されます。ただし、このプロパティは[**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-)メソッドを実装した場合にのみ動作します。

## **Excel VBAのRange.FormulaLocalと同様にCell.FormulaLocalを実装する**

次のサンプルコードは、[**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-)メソッドを実装する方法を説明しています。このメソッドは、標準関数のローカル名を返します。標準関数が**SUM**の場合、**UserFormulaLocal_SUM**を返します。必要に応じてコードを変更し、正しいローカル関数名（例：ドイツ語では**SUMME**、ロシア語では**ТЕКСТ**）を返してください。以下に示すサンプルコードのコンソール出力も参照してください。

## **サンプルコード**

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

## **コンソール出力**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
