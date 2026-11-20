---
title: Özet Alanı Öğelerinin Ayrık Gruplandırılması
linktitle: Ayrık Gruplandırılması
description: Aspose.Cells for JavaScript via C++ içinde DiscreteGroupItem ve PivotFieldGroupOptions.discreteGroupItems kullanarak özet alanı öğelerini meyve ve sebze gibi özel adlı gruplara nasıl gruplandıracağınızı öğrenin.
keywords: Aspose.Cells, özet tablo, ayrık gruplandırma, DiscreteGroupItem, PivotFieldGroupOptions, özet alanı öğelerini gruplandırma, özel gruplar, PivotField.group, Aspose.Cells for JavaScript via C++, Excel özet tablo
type: docs
weight: 90
url: /tr/javascript-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Otomatik gruplandırma, öğeleri veri türüne göre toplar; örneğin tarihleri aylara ve çeyreklere, sayıları ise aralıklara ayırır. Ayrık gruplandırma ise bunun tersini yapar: belirli ve birbirleriyle ilgisiz öğeleri özel adlı gruplarda toplar; örneğin ürünleri meyve ve sebze gruplarına, mağazaları bölgelere veya hesapları bölgelere ayırır. Aspose.Cells, ayrık gruplandırmayı `DiscreteGroupItem` sınıfı ve `PivotFieldGroupOptions.discreteGroupItems` özelliği aracılığıyla sağlar.
- Bir `DiscreteGroupItem`, bir grup adı ve o gruba ait öğelerden oluşur. Öğeler iki şekilde tanımlanabilir: adlarıyla (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) veya kaynak verideki sıfır tabanlı konumlarıyla (`new DiscreteGroupItem("fruit", [0, 3])`). Her iki biçim de aynı sonucu verir.
- Ayrık gruplandırma, seçenekler `PivotField.group(PivotFieldGroupOptions)` çağrısına aktarılarak özet tabloda satır veya sütun alanına yerleştirilen bir alana uygulanır.

## **Özet Alanı Öğelerini Öğe Adlarına Göre Gruplandırma**
Aşağıdaki örnek, küçük bir satış listesi (ürün, tarih ve tutar) oluşturur ve bu verilerden bir özet tablo oluşturur. Özet tabloda `product` alanı satır alanında, `date` alanı sütun alanında ve `amount` alanı veri alanında yer alır. Ardından öğe adlarına göre iki özel grup tanımlanır: meyve (üzüm, kiraz) ve sebze (havuç, patates). Sonuç, iki düzeyli bir satır düzenidir: grup adı dış düzeyde, özgün öğeler ise onun altında iç içe yer alır. Böylece eğilimler, her özel grup ve öğe bazında görülebilir.

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
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            const { Workbook, DiscreteGroupItem, PivotFieldGroupOptions } = AsposeCells;
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType =
                    AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // Group specific items into custom groups by item names
                const fruit = new DiscreteGroupItem("fruit", ["grape", "cherry"]);
                const vegetable = new DiscreteGroupItem("vegetable", ["carrot", "potato"]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

`calculateData()` çağrısından sonra özet tablonun satır alanı, genel toplam 260 ile birlikte meyveyi (üzüm 50, kiraz 80) ve sebzeyi (havuç 60, patates 70) gösterir. Sütun etiketlerinde dört tarih yer alır (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Özet Alanı Öğelerini Öğe Dizinlerine Göre Gruplandırma**
Öğe adları uzun veya yerelleştirilmiş olduğunda, `DiscreteGroupItem` sınıfının ikinci oluşturucusu öğeleri dizinlerine göre tanımlar. Dizinler, öğelerin kaynak veride göründükleri sıraya göre sıfır tabanlı konumlarıdır; alfabetik sıraya göre değildir. Yukarıdaki örnek veride üzüm 0, havuç 1, patates 2 ve kiraz 3 numaralı öğedir; dolayısıyla meyve `{ 0, 3 }`, sebze ise `{ 1, 2 }` olur. Sonuç, ada dayalı örnekle aynıdır.

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
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            const {
                Workbook,
                SaveFormat,
                DiscreteGroupItem,
                PivotFieldGroupOptions
            } = AsposeCells;
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
                // (zero-based positions in the order the items appear in the source data)
                const fruit = new DiscreteGroupItem("fruit", [0, 3]);
                const vegetable = new DiscreteGroupItem("vegetable", [1, 2]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotFieldByIndex.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

## **Not**

{{% alert color="primary" %}}
- Hiçbir özel gruba atanmayan öğeler kaybolmaz. Bunlar özet tabloda özel gruplarla aynı düzeyde kalır ve her biri ayrı bir tek öğeli girdi olarak yer alır. Yukarıdaki örnekte yalnızca meyve grubu tanımlanırsa havuç ve patates, meyve grubunun yanında bağımsız girdiler olarak satır alanında kalır.
- `PivotFieldGroupOptions.newPivotField` özelliği, ayrık gruplandırmanın düzenini denetler. Varsayılan değeri true olan bu özellik, gruplandırılan alanı orijinal alanın yanında yeni bir dış alan olarak ekleyerek yukarıda gösterilen iki düzeyli düzeni oluşturur (`rowFields` 2'ye büyür). Orijinal alanın değiştirilmesi için bu değeri false olarak ayarlayın; bu durumda satır alanı, yalnızca grup adlarını ve toplanmış değerlerini içeren tek düzeyli bir düzen gösterir: meyve 130 (50 + 80) ve sebze 130 (60 + 70).
- `DiscreteGroupItem` sınıfının ada dayalı ve dizine dayalı oluşturucuları aynı `discreteGroupItems` dizisi içinde birlikte kullanılabilir.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablodaki Özet Alanlarını Gruplandırma](/cells/tr/javascript-cpp/group-pivot-fields-in-the-pivot-table/)
- [Özet Tabloya Satır ve Sütun Alanları Ekleme](/cells/tr/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Özet Tabloları Etikete veya Değere Göre Filtreleme](/cells/tr/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [Özet Tabloya Biçim Uygulama](/cells/tr/javascript-cpp/apply-style-to-pivot-table/)
- [Özet Tabloyu Yenileme](/cells/tr/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}