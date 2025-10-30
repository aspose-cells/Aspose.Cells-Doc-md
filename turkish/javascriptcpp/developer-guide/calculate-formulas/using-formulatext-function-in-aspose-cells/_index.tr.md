---
title: C++ ile Script kullanarak FormulaText fonksiyonunu kullanmak
linktitle: Aspose.Cells te FormulaText Fonksiyonu Kullanma
description: Bu makale, Microsoft Excel deki formülleri işlemek için Aspose.Cells kitaplığında FormulaText fonksiyonunun nasıl kullanılacağını tanıtmaktadır. Hücrelerin formül metnini almak ve ayarlamak ile değiştirilmiş Excel dosyalarını JavaScript via C++ kullanarak kaydetmeyi öğrenin.
keywords: Aspose.Cells, Excel, FormulaText fonksiyonları JavaScript via C++
type: docs
weight: 60
url: /tr/javascript-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText, Excel 2013 ve sonrası fonksiyonudur. Eski sürümler olan Excel 2010 veya 2007 vb. tarafından desteklenmemektedir. Adından da anlaşılacağı gibi, verilen bir hücrede bulunan formülün metnini yazdırır. Bu makale, bu fonksiyonun nasıl kullanılacağını C++ ile Script kullanarak gösterecektir.

{{% /alert %}} 

Aşağıdaki örnek kod, C++ ile Script kullanarak FormulaText kullanımını gösterir. Kod önce A1 hücresine bir formül yazar, sonra A2 hücresinde formülün metnini FormulaText kullanarak yazdırır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - FormulaText</h1>
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

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some formula in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.formula = "=Sum(B1:B10)";

            // Get the text of the formula in cell A2 using FORMULATEXT function
            const cellA2 = worksheet.cells.get("A2");
            cellA2.formula = "=FormulaText(A1)";

            // Calculate the workbook
            workbook.calculateFormula();

            // Print the results of A2, It will now print the text of the formula inside cell A1
            console.log(cellA2.stringValue);

            resultDiv.innerHTML = `<p style="color: green;">Operation completed successfully! Formula text: ${cellA2.stringValue}</p>`;
        });
    </script>
</html>
```
## **Konsol Çıktısı**


{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
