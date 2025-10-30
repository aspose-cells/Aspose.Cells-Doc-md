---
title: JavaScript ile C++ kullanarak Excel VBA Range.FormulaLocal a benzer Cell.FormulaLocal uygulayın
linktitle: Excel VBA Range.FormulaLocal benzeri Cell.FormulaLocal ı Uygula
type: docs
weight: 30
url: /tr/javascript-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: C++.scripte Aspose.Cells for JavaScript kullanarak Excel VBA Range.FormulaLocal a benzer Cell.FormulaLocal uygulamayı öğrenin. 
---

## **Olası Kullanım Senaryoları**

Microsoft Excel Formülleri farklı yerel veya bölge veya dilde farklı isimlere sahip olabilir. Örneğin, **SUM** fonksiyonu Almanca'da **SUMME** olarak adlandırılır. Aspose.Cells İngilizce olmayan fonksiyon adlarıyla çalışamaz. Microsoft Excel VBA'da, dil veya bölgeye göre fonksiyon adını döndüren **Range.FormulaLocal** özelliği vardır. Aspose.Cells for JavaScript C++ kullanarak bu amaçla [**Cell.formulaLocal**](https://reference.aspose.com/cells/javascript-cpp/cell/#formulaLocal--) özelliği sağlar. Ancak, bu özellik sadece [**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-) metodunu uyguladığınızda çalışır.

## **Excel VBA Range.FormulaLocal benzeri Cell.FormulaLocal'ı uygulamanın nasıl olduğunu aşağıdaki örnek kod açıklar. Metod, standart fonksiyonun yerel adını döndürür. Standart fonksiyon adı **SUM** ise **UserFormulaLocal_SUM** döndürür. Kodu ihtiyaçlarınıza göre değiştirebilir ve doğru yerel fonksiyon adlarını döndürebilirsiniz, örneğin **SUM** Almanca'da **SUMME** ve Rusça'da **TEXT** için **ТЕКСТ** olur. Lütfen aşağıdaki örnek kodun konsol çıktısını inceleyin.**

Aşağıdaki örnek kod, [**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-) metodunun nasıl uygulanacağını açıklar. Metod, standart fonksiyonun yerel adını döner. Eğer standart fonksiyon adı **SUM** ise, **UserFormulaLocal_SUM** döner. Kodunuzu ihtiyaçlarınıza göre değiştirebilir ve doğru yerel fonksiyon adlarını dönebilirsiniz, örn. **SUM** Almanca'da **SUMME**, **TEXT** Rusça'da **ТЕКСТ**. Ayrıca, aşağıdaki örnek kodun konsol çıktısına bakmak faydalı olacaktır.

## **Örnek Kod**

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

## **Konsol Çıktısı**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
