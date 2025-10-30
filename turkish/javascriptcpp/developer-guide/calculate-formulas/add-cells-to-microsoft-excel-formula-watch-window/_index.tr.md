---
title: JavaScript aracılığıyla C++ ile Cells i Microsoft Excel Formül İzleme Penceresine ekle
linktitle: Microsoft Excel Formül İzleme Penceresine Hücreler Ekle
description: Aspose.Cells kütüphanesini kullanarak JavaScript aracılığıyla C++ ile Excel de formül izleme penceresine hücre ekleme. Varolan bir Excel dosyasını yükleyerek veya yeni bir dosya oluşturarak, içindeki hücreleri hareket ettirebilir ve formüller ayarlayabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, Formül İzleme Penceresi, Hücreler, Ekleme, JavaScript aracılığıyla C++
type: docs
weight: 60
url: /tr/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel İzleme Penceresi, hücre değerlerini ve formüllerini rahatça izlemek için kullanışlı bir araçtır. Excel'de *Formüller > İzleme* penceresine tıklayarak *İzleme Penceresi*ni açabilirsiniz. Bu pencereyi kullanmak için *İzleme Ekle* düğmesi vardır ve bu düğme, inceleme için hücreleri eklemenizi sağlar. Benzer şekilde, [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cellwatchcollection/#add-number-number-) yöntemi kullanılarak hücreler *İzleme Penceresi*ne Aspose.Cells API'si kullanılarak eklenebilir.

## **Microsoft Excel Formül İzleme Penceresine Hücreler Ekleme**

Aşağıdaki örnek kod, C1 ve E1 hücrelerinin formüllerini ayarlar ve her ikisini de İzleme Penceresine ekler. Ardından çalışma kitabını [çıktı Excel dosyası](67338481.xlsx) olarak kaydeder. Çıktı Excel dosyasını açıp *İzleme Penceresi*ni görüntülediğinizde, her iki hücreyi de ekrandaki gibi göreceksiniz.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Cells to Formula Watch Window</h1>
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
            // This example creates a new workbook (like the original JavaScript example).
            // If a user-selected file is provided, it will be ignored for this specific example.
            if (!fileInput) {
                document.getElementById('result').innerHTML = '<p style="color: red;">File input not available.</p>';
                return;
            }

            // Instantiate a new empty workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some integer values in cell A1 and A2
            ws.cells.get("A1").value = 10;
            ws.cells.get("A2").value = 30;

            // Access cell C1 and set its formula
            const c1 = ws.cells.get("C1");
            c1.formula = "=Sum(A1,A2)";

            // Add cell C1 into cell watches by name
            ws.cellWatches.add(c1.name);

            // Access cell E1 and set its formula
            const e1 = ws.cells.get("E1");
            e1.formula = "=A2*A1";

            // Add cell E1 into cell watches by its row and column indices
            ws.cellWatches.add(e1.row, e1.column);

            // Save workbook to output XLSX format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
