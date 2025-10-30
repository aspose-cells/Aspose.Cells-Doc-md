---
title: Hücreden Tablo Erişimi ve Satır ve Sütun Oflsetleriyle İçeriğe Değer Ekleme, JavaScript ile C++ kullanarak
linktitle: Hücreden Tablo Erişimi ve Satır ve Sütun Ofsetleri Kullanarak Değerler Eklemek
type: docs
weight: 230
url: /tr/javascript-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}  

Normalde, Tablo veya List Objesi içine değerleri [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) yöntemini kullanarak eklersiniz. Ancak bazen, Tablo veya List Objesi içine değerleri satır ve sütun ofsetleri kullanarak eklemeniz gerekebilir.  

Bir hücreden Tablo veya Liste Nesnesine erişmek için [**Cell.table**](https://reference.aspose.com/cells/javascript-cpp/cell/#table--) özelliğini kullanın. İçeriğine değer eklemek için satır ve sütun ofsetlerini kullanın, [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/javascript-cpp/listobject/#putCellValue-number-number-object-) metodunu kullanın.  

{{% /alert %}}  

Aşağıdaki ekran görüntüsü, kod içinde kullanılan kaynak Excel dosyasını göstermektedir. Boş tabloyu içerir ve tablo içinde bulunan D5 hücresini vurgular. Bu tablonun D5 hücresinden [**Cell.table**](https://reference.aspose.com/cells/javascript-cpp/cell/#table--) özelliği kullanılarak erişeceğiz ve ardından içindeki değerleri hem [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) hem de [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/javascript-cpp/listobject/#putCellValue-number-number-object-) metodlarıyla ekleyeceğiz.  

## Örnek  

### Kaynak ve çıktı dosyalarını karşılaştıran ekran görüntüleri  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

Aşağıdaki ekran görüntüsü, kod tarafından oluşturulan çıktı Excel dosyasını göstermektedir. D5 hücresinin bir değeri olduğunu ve tablonun 2,2 ofsetindeki F6 hücresinin bir değeri olduğunu görebilirsiniz.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### Düğmeden tabloya erişmek ve satır ile sütun ofsetleri kullanarak içindekileri eklemek için JavaScript kodu  

Yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükleyen ve tablo içine değer ekleyen ve yukarıda gösterilen çıktı Excel dosyasını oluşturan aşağıdaki örnek kod verilmiştir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Accessing Table Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell D5 which lies inside the table
            const cell = worksheet.cells.get("D5");

            // Put value inside the cell D5
            cell.value = "D5 Data";

            // Access the Table from this cell
            const table = cell.table;

            // Add some value using Row and Column Offset
            table.putCellValue(2, 2, "Offset [2,2]");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
