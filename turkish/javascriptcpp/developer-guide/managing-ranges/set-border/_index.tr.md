---
title: JavaScript ile Aralık Kenarlığını Ayarlama
linktitle: Aralık Sınırı Ayarlama
type: docs
weight: 600
url: /tr/javascript-cpp/set-range-border/
---

## **Olası Kullanım Senaryoları**  
Bir aralık için kenarlık ayarlamak istediğinizde, her hücreyi tek tek ayarlamanıza gerek yoktur. Aralık üzerinde kenarlık ayarlayabilirsiniz. C++ kullanarak JavaScript ile bu özellik sunulmaktadır.  
Bu makale, C++ kullanarak JavaScript ile aralıkta kenarlık ayarlayan örnek kod sağlar.  

## **Excel'de Aralık Sınırı Ayarlama**  
Excel'de bir aralığın sınırını ayarlamak için şu adımları takip edebilirsiniz:  
1. Sınırlıyı uygulamak istediğiniz hücre aralığını seçin.  
2. Kurdele'nin "Ana Sayfa" sekmesinde, "Yazı Tipi" grubunu bulun.  
3. "Yazı Tipi" grubu içinde, "Kenarlıklar" açılır düğmesine tıklayın.  
<br>  
<img src="border.png" />  
4. Açılır menüde istenilen kenar tipini seçin. Ön ayarlı kenar stilleri arasından seçim yapabilir veya kendi kenarınızı özelleştirebilirsiniz.  
5. İstenilen kenar stili seçildikten sonra, kenar seçilen hücre aralığına uygulanır.  

## **C++ kullanarak JavaScript ile Aralık Kenarlığı Ayarlama**  
Bu örnek aşağıdakileri göstermektedir:  

1. Bir çalışma kitabı oluşturma.  
2. İlk çalışma sayfasındaki hücrelere veri ekleyin.  
3. Bir [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) oluşturun.  
4. Aralığın iç kenarını ayarlayın.  
5. Aralığın dış kenarını ayarlayın.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            // Instantiate a new workbook
            const workbook = new Workbook();
            // Obtaining the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.putValue("Fruit");
            cell = cells.get("B1");
            cell.putValue("Count");
            cell = cells.get("C1");
            cell.putValue("Price");

            cell = cells.get("A2");
            cell.putValue("Apple");
            cell = cells.get("A3");
            cell.putValue("Mango");
            cell = cells.get("A4");
            cell.putValue("Blackberry");
            cell = cells.get("A5");
            cell.putValue("Cherry");

            cell = cells.get("B2");
            cell.putValue(5);
            cell = cells.get("B3");
            cell.putValue(3);
            cell = cells.get("B4");
            cell.putValue(6);
            cell = cells.get("B5");
            cell.putValue(4);

            cell = cells.get("C2");
            cell.putValue(5);
            cell = cells.get("C3");
            cell.putValue(20);
            cell = cells.get("C4");
            cell.putValue(30);
            cell = cells.get("C5");
            cell.putValue(60);

            // Create a range (A1:C5).
            const range = cells.createRange("A1", "C5");

            // set inner border of range
            const innerColor = workbook.createCellsColor();
            innerColor.color = AsposeCells.Color.Red;
            range.insideBorders = {
                borderType: AsposeCells.BorderType.Vertical,
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: innerColor
            };
            innerColor.color = AsposeCells.Color.Green;
            range.insideBorders = {
                borderType: AsposeCells.BorderType.Horizontal,
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: innerColor
            };

            // set outer border of range
            const outerColor = workbook.createCellsColor();
            outerColor.color = AsposeCells.Color.Blue;
            range.outlineBorders = {
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: outerColor
            };

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
