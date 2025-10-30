---
title: Orijinal Değerler Kullanarak Veri Arama
type: docs
weight: 380
url: /tr/javascript-cpp/search-data-using-original-values/
description: Orijinal Değerleri Kullanarak Arama Yapmayı öğrenmek için Aspose.Cells for JavaScript aracılığıyla C++ API kullanın.
keywords: Orijinal Değerleri Kullanarak Veri Arama JavaScript aracılığıyla C++, Orijinal Değerleri Kullanarak Veri Bul JavaScript aracılığıyla C++, Orijinal Değerlerle Veri Arama JavaScript aracılığıyla C++, Orijinal Değerlerle Veri Bul JavaScript aracılığıyla C++
---

{{% alert color="primary" %}}  

Bazen verinin değeri bazı şekilde biçimlendirildiği için gizlidir. Örneğin, D4 hücresinin değeri =Sum(A1:A2) ve değeri 20'dir ancak --- olarak biçimlendirilmiştir, bu nedenle 20 değeri gizlidir ve Microsoft Excel bulma seçenekleri kullanılarak bulunamaz. Bununla birlikte, Aspose.Cells kullanarak [**LookInType.OriginalValues**](https://reference.aspose.com/cells/javascript-cpp/lookintype) kullanarak bulunabilir.  

{{% /alert %}}  

Aşağıdaki örnek kod yukarıdaki noktayı açıklar. Microsoft Excel bulma seçenekleri kullanılarak bulunamayan D4 hücresini [**LookInType.OriginalValues**](https://reference.aspose.com/cells/javascript-cpp/lookintype) kullanarak bulur ancak Aspose.Cells kullanarak bulabilir. Daha fazla bilgi için kod içindeki yorumları okuyun.  

## Orijinal değerleri kullanarak veri arama JavaScript kodu  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Formatted Value</title>
    </head>
    <body>
        <h1>Find Formatted Value Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FindOptions, Worksheet, Cell, Utils } = AsposeCells;

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

            // Add 10 in cell A1 and A2
            worksheet.cells.get("A1").value = 10;
            worksheet.cells.get("A2").value = 10;

            // Add Sum formula in cell D4 but customize it as ---
            const cell = worksheet.cells.get("D4");

            let style = cell.style;
            style.custom = "---";
            cell.style = style;

            // The result of formula will be 20 but 20 will not be visible because the cell is formatted as ---
            cell.formula = "=Sum(A1:A2)";

            // Calculate the workbook
            workbook.calculateFormula();

            // Create find options, we will search 20 using original values otherwise 20 will never be found because it is formatted as ---
            const options = new FindOptions();
            options.lookInType = AsposeCells.LookInType.OriginalValues;
            options.lookAtType = AsposeCells.LookAtType.EntireContent;

            let foundCell = null;
            const obj = 20;

            // Find 20 which is Sum(A1:A2) and formatted as ---
            foundCell = worksheet.cells.find(obj, foundCell, options);

            // Print the found cell to the page
            const resultDiv = document.getElementById('result');
            if (foundCell) {
                resultDiv.innerHTML = `<p style="color: green;">Found cell: ${foundCell.name}, value: ${foundCell.value}</p>`;
            } else {
                resultDiv.innerHTML = `<p style="color: red;">Cell not found.</p>`;
            }

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';
        });
    </script>
</html>
```


## Örnek Kod Tarafından Oluşturulan Konsol Çıktısı  



{{< highlight java >}}  

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]  

{{< /highlight >}}
