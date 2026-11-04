---
title: Aspose.Cells for JavaScript via C++ ile Özet Tabloya Satır ve Sütun Alanları Ekleme
linktitle: Aspose.Cells for JavaScript via C++ ile Özet Tabloya Satır ve Sütun Alanları Ekleme
description: Aspose.Cells for JavaScript via C++ ile bir özet tabloya satır ve sütun alanları eklemeyi ve PivotField.SetSubtotals ile PivotFieldSubtotalType kullanarak özet tablo alanlarının alt toplamlarını denetlemeyi öğrenin.
keywords: Aspose.Cells, JavaScript via C++, özet tablo, satır alanı, sütun alanı, PivotField, setSubtotals, PivotFieldSubtotalType, alt toplamlar, JavaScript, Excel özet tablosu
type: docs
weight: 220
url: /tr/javascript-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Bir Alanı Satır veya Sütun Bölgesine Ekleme**
`pivotTable.addFieldToArea(fieldType, fieldName)` yöntemi, kaynak verideki temel bir alanı dört özet tablo bölgesinden birine taşır. `fieldType` argümanı aşağıdaki `PivotFieldType` değerlerinden birini kabul eder.
- `Row` — sol tarafa dikey olarak yerleştirilen alanlar
- `Column` — üst tarafa yatay olarak yerleştirilen alanlar
- `Data` — değerleri toplulaştırılan alanlar
- `Page` — rapor filtreleri olarak kullanılan alanlar
Alanların iç içe sıralaması önemlidir. `Category` alanını önce, `Item` alanını ise sonra satır bölgesine eklemek, dış gruplaması `Category` ve iç gruplaması `Item` olan bir özet tablo oluşturur. Sırayı tersine çevirmek hiyerarşiyi de tersine çevirir.

## **Özet Tablo Alanlarının Alt Toplamları**
`pivotField.setSubtotals(subtotalType, shown)` yöntemi, bir özet tablo alanı için hangi alt toplam satırlarının görüntüleneceğini denetler. Her çağrı tek bir alt toplam türünü bağımsız olarak açar veya kapatır. `shown = true` değerinin geçirilmesi alt toplamı görüntüler, `shown = false` değerinin geçirilmesi ise onu gizler. Her çağrı yalnızca bir türü etkilediğinden, yöntemi farklı `subtotalType` değerleriyle birden fazla kez çağırmak özel bir alt toplam kümesi oluşturur.
`PivotFieldSubtotalType` enum'u kullanılabilir alt toplam türlerini tanımlar.
- `Automatic` — Aspose.Cells varsayılan seçimi yapar (sayısal alanlar için genellikle `Sum`)
- `None` — tüm alt toplam satırlarını bastırır
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
Alt toplamlar yalnızca satır bölgesinde (veya sütun bölgesinde) iki veya daha fazla özet tablo alanı bulunduğunda görüntülenir. Tek alanlı bir düzende gruplar arasında alt toplam oluşturulacak anlamlı bir öğe bulunmadığından, `setSubtotals` çağrılarının bu durumda görünür bir etkisi olmaz. Bu nedenle makale, her örnekte alt toplam sınırının `Category` grupları arasında görünür olması için dış sıralaması `Category`, iç sıralaması `Item` olan iki satır alanı yerleştirir.
{{% /alert %}}

## **Senaryo 1 — Otomatik (Varsayılan) Alt Toplamlar**
`setSubtotals` çağrısı hiç yapılmadığında, Aspose.Cells sayısal alanlara `Automatic` seçimini uygular. Aşağıdaki örnek, dış sıralamadaki `Category` satır alanında `setSubtotals(PivotFieldSubtotalType.Automatic, true)` çağrısı yaparak bu davranışı açıkça ortaya koyar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get(0, 0).value = "Category";
            cells.get(0, 1).value = "Item";
            cells.get(0, 2).value = "Year";
            cells.get(0, 3).value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTable = worksheet.pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);
            pivotTable.calculateData();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_automatic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Senaryo 2 — Tüm Alt Toplamları Bastırma (None)**
`setSubtotals(PivotFieldSubtotalType.None, true)` çağrısı, özet tablodaki tüm alt toplam satırlarını kaldırır ve yalnızca alan satırları ile en alttaki genel toplamı bırakır. Bu, özet satırları olmadan ham ve gruplandırılmış verileri görüntülemek istediğinizde yararlıdır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const headers = ["Category", "Item", "Year", "Amount"];
            for (let j = 0; j < headers.length; j++) {
                worksheet.cells.get(0, j).value = headers[j];
            }
            const data = [
                ["Fruit", "Apple", 2020, 100],
                ["Fruit", "Apple", 2021, 150],
                ["Fruit", "Banana", 2020, 80],
                ["Fruit", "Banana", 2021, 90],
                ["Vegetable", "Carrot", 2020, 50],
                ["Vegetable", "Carrot", 2021, 60],
                ["Vegetable", "Daikon", 2020, 40],
                ["Vegetable", "Daikon", 2021, 45]
            ];
            for (let i = 0; i < data.length; i++) {
                for (let j = 0; j < data[i].length; j++) {
                    worksheet.cells.get(i + 1, j).value = data[i][j];
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_none.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Senaryo 3 — Özel Alt Toplam Kümesi (Sum + Average)**
Tek bir alt toplam türüyle sınırlı değilsiniz. Her `setSubtotals` çağrısı yalnızca bir tür üzerinde etkilidir; bu nedenle yöntemi bir kez `Sum`, bir kez de `Average` ile çağırmak, her `Category` grubu için iki alt toplam satırından oluşan özel bir küme oluşturur.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get("A1").value = "Category";
            cells.get("B1").value = "Item";
            cells.get("C1").value = "Year";
            cells.get("D1").value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTables = worksheet.pivotTables;
            const pivotTable = pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_custom.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Özet**
Üç senaryo yalnızca tek noktada farklılık gösterir: `setSubtotals` çağrıları. Geri kalan her şey — veri seti, alanlar ve bunların atandığı bölgeler — aynıdır; bu da düzenlerin doğrudan karşılaştırılabilmesini sağlar.
- **Alanları yerleştirme.** `pivotTable.addFieldToArea(PivotFieldType.Row, fieldName)` kaynak verideki bir sütunu bir bölgeye taşır. Aynı bölgede çağrıların sırası görüntüleme sırasını belirler; dolayısıyla ilk çağrı en dış grubu oluşturur. Alt toplamların hesaplanabilmesi için aynı bölgede iki veya daha fazla alan gerekir: tek alan bulunduğunda gruplar arasında alt toplam oluşturulacak bir şey yoktur.
- **Senaryo 1 — otomatik alt toplamlar.** `setSubtotals` çağrısı yapılmaması seçimi Excel'e bırakır; Excel, sayısal alanlara kendi varsayılan alt toplamını uygular. `setSubtotals` çağrısını `PivotFieldSubtotalType.Automatic` ile yapmak, bu seçimi örtük bırakmak yerine açıkça kaydeder.
- **Senaryo 2 — alt toplam yok.** `setSubtotals` çağrısının `PivotFieldSubtotalType.None` ile yapılması varsayılan alt toplamı kapatır; böylece özet tablo alan satırlarını ve genel toplamı korur, ancak Excel'in aksi hâlde aralarına ekleyeceği alt toplam satırlarını kaldırır.
- **Senaryo 3 — seçilmiş küme.** Her çağrı tam olarak bir alt toplam türünü açar veya kapatır ve çağrılar birbirini sıfırlamak yerine birikir. Dolayısıyla yöntemi bir kez `PivotFieldSubtotalType.Sum` ve bir kez `PivotFieldSubtotalType.Average` ile çağırmak her iki türü de etkin bırakır; özet tablo bir `Sum` alt toplamı, bir `Average` alt toplamı ve genel toplam görüntüler.

{{% alert color="primary" %}}
Alt toplamlarla ilgili hiçbir şey satır bölgesine özgü değildir. `pivotTable.getColumnFields()` yönteminden alınan bir alan üzerinde aynı `setSubtotals` çağrıları, sütun ekseninde aynı üç düzeni oluşturur; çünkü bu ayar, alanın bulunduğu eksene değil, özet tablo alanına aittir.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablolarında Sayfa Alanları](/cells/tr/javascript-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for JavaScript via C++ ile Özet Tablolarını Yenileme](/cells/tr/javascript-cpp/refresh-pivot-table/)
- [Özet Tablolarına Stil Uygulama](/cells/tr/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}