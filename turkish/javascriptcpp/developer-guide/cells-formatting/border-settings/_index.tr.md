---
title: Kenar Ayarları
linktitle: Kenar Ayarları
description: Aspose.Cells kütüphanesini JavaScript C++ kullanarak hücrelerin sınır stilini ve rengini nasıl ayarlayacağınızı göstermek için kullanın. Kenarların genişliği, stili ve rengini ayarlayarak hücrelerin görünümünü ve görünüşünü daha iyi kontrol edebilirsiniz.
keywords: Aspose.Cells, Hücre Kenar Ayarları, JavaScript via C++, Kenar Genişi, Kenar Stili, Kenar Rengi
type: docs
weight: 40
url: /tr/javascript-cpp/cells-border-settings/
---

## **Hücrelere Kenarlık Eklemek**

Microsoft Excel, hücreleri kenarlıklar ekleyerek biçimlendirmeye izin verir. Kenarlık tipi, eklendiği konuma göre değişir. Örneğin, üst kenarlık, hücrenin üst konumuna eklenmiş bir kenarlıktır. Kullanıcılar ayrıca kenarlıkların çizgi stilini ve rengini değiştirebilir.

Aspose.Cells for JavaScript via C++ ile geliştiriciler, Microsoft Excel'de olduğu gibi kenarlar ekleyebilir ve görünümlerini özelleştirebilir.

### **Hücrelere Kenarlık Eklemek**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasındaki her sayfaya erişim sağlayan [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir. Bir sayfa, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunu sağlar. [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfının bir nesnesini temsil eder.

Aspose.Cells, [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) özelliğini [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfında sağlar. [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-), bir hücrenin biçimlendirme stilini ayarlamak için kullanılır. [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) sınıfı, hücrelere kenar eklemek için özellikler sağlar.

#### **Bir Hücreye Sınır Ekleme**

Geliştiriciler, bir hücreye kenarlık eklemek için [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesinin [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) koleksiyonunu kullanabilir. Kenarlık türü, [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) koleksiyonuna indeks olarak geçirilir. Tüm kenarlık türleri önceden tanımlanmış [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype) enum'unda yer alır.

**Sınır numaralandırması**

|**Sınır Türleri**|**Açıklama**|
| :- | :- |
|BottomBorder|Alt sınır çizgisi|
|DiagonalDown|Sol üstten sağ alt köşeye çapraz çizgi|
|DiagonalUp|Sol alttan sağ üste çapraz çizgi|
|LeftBorder|Sol sınır çizgisi|
|RightBorder|Sağ sınır çizgisi|
|TopBorder|Üst sınır çizgisi|

[**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) koleksiyonu tüm kenarlıkları depolar. [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) koleksiyonundaki her kenarlık, [**Border**](https://reference.aspose.com/cells/javascript-cpp/border) nesnesi tarafından temsil edilir ve bu nesne, sırasıyla [**color**](https://reference.aspose.com/cells/javascript-cpp/border/#color-color-) ve [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-) özellikleri ile kenarlığın çizgi rengi ve stilini ayarlamayı sağlar.

Bir kenarın çizgi rengini ayarlamak için, JavaScript'in parçası olan Color enumerasyonunu kullanarak bir renk seçin ve bunu Kenar nesnesinin renk özelliğine atan.

Kenarın çizgi stili, [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype) enum'undan bir çizgi stili seçilerek ayarlanır.

**HücreSınırTürü numaralandırması**

|**Çizgi Stilleri**|**Açıklama**|
| :- | :- |
|DashDot|İnce tireli kesikli çizgi|
|DashDotDot|İnce tireli kesik noktalı çizgi|
|Dashed|Kesikli çizgi|
|Dotted|Noktalı çizgi|
|Double|Çift çizgi|
|Hair|Saç inceliğinde çizgi|
|MediumDashDot|Orta tireli kesikli çizgi|
|MediumDashDotDot|Orta tireli kesik noktalı çizgi|
|MediumDashed|Orta kesikli çizgi|
|None|No Line|
|Medium|Orta Çizgi|
|SlantedDashDot|Eğik orta kesikli çizgi|
|Thick|Kalın çizgi|
|Thin|İnce çizgi|
Çizgi stillerinden birini seçin ve ardından onu [**Border**](https://reference.aspose.com/cells/javascript-cpp/border) nesnesinin [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-) özelliğine atayın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Borders to A1 Cell Example</h1>
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
            // This example creates a new workbook and adds borders to cell A1.
            // No try/catch is used so errors propagate for testing.

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Create a style object
            const style = cell.style;

            // Setting the line style and color of the top border
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the bottom border
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the left border
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the right border
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;

            // Apply the border styles to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Her iki çizgi stili ve rengi aynı anda ayarlamalısınız. İki çapraz kenar çizgisi aynı çizgi stiline ve renge sahip olmalıdır.
{{% /alert %}}

#### **Hücre Aralığına Sınırlar Ekleme**

Sadece bir hücre yerine hücre aralığına da sınırlar eklemek mümkündür. Bunu yapmak için önce, [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunun [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) yöntemini çağırarak bir hücre aralığı oluşturun. Aşağıdaki parametreleri alır:

- İlk Sütun, aralığın ilk sütunu.
- İlk Sütun, aralığın ilk sütunu.
- Satır Sayısı, aralıktaki satır sayısı.
- Sütun Sayısı, aralıktaki sütun sayısı.

[**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) yöntemi, belirtilen hücre aralığını içeren bir [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) nesnesi döner. [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) nesnesi, aşağıdaki parametreleri alan bir [**outlineBorder**](https://reference.aspose.com/cells/javascript-cpp/range/#outlineBorder-bordertype-cellbordertype-cellscolor-) yöntemi sağlar ve hücre aralığına sınır ekler:

- **Sınır Türü**, [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype) enumerasyonundan seçilen sınır tipi.
- **Çizgi Stili**, sınır çizgi stili, [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype) enumerasyonundan seçilir.
- **Renk**, Renk sıralamasından seçilen çizgi rengi.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Apply Borders</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color } = AsposeCells;

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
            // This example creates a new workbook, writes to A1, creates a range and applies borders, then offers the file for download.
            const workbook = new Workbook();

            const worksheet = workbook.worksheets.get(0);

            const cell = worksheet.cells.get("A1");

            cell.putValue("Hello World From Aspose");

            const range = worksheet.cells.createRange(0, 0, 1, 3);

            // Applying borders using property assignment conversions for setter methods
            range.outlineBorder = [BorderType.TopBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.BottomBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.LeftBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.RightBorder, CellBorderType.Thick, Color.Blue];

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and borders applied successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
