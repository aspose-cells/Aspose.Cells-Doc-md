---
title: Pivot Tablosunun Bir Bölümünü Biçimlendirme
linktitle: Pivot Tablosunun Bir Bölümünü Biçimlendirme
description: Aspose.Cells for Node.js via Java ortamında bir pivot tablosunun bir bölümünü, PivotTable.format aracılığıyla anlamsal PivotArea bölgelerine veya CellArea dikdörtgenlerine stiller uygulayarak biçimlendirin; biçimler PivotTable.getPivotFormats() içinde saklanır ve pivot tablo yenilendiğinde korunur.
keywords: Aspose.Cells for Node.js via Java, pivot tablosu, biçimlendirme, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Node.js via Java
type: docs
weight: 20
url: /tr/nodejs-java/format-part-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
`PivotTable.formatAll` tüm pivot tabloya tek bir stil uygular ve üst sayfada ele alınır. Etiketler, değerler, toplamlar veya raporun belirli bölgeleri arasında ayrım yapmaz.  
Gerçekte, genellikle bir pivot tablosunun yalnızca bir kısmı vurgulanmak istenir. Yaygın hedefler, bir satır alanına ait etiketler, bir alan tarafından üretilen değer hücreleri, toplam satırı veya ilk iki öğe satırı gibi keyfi bir dikdörtgen olabilir.  
Pivot tablosunun çalışma sayfası hücrelerine doğrudan stil uygulamak aynı şey değildir. Excel, pivot tablo biçimlendirmesini olağan hücre stili kayıtları yerine anlamsal `PivotArea` bölgeleri olarak depolar. Bir pivot‑alan biçimi, bir alanın etiketleri veya veri değerleri gibi bir bölgeye bağlı kalır ve pivot tablo yeniden hesaplandığında, yenilendiğinde veya genişletildiğinde yeniden çözülür. Öte yandan, bir hücreye doğrudan yazılan stil, o hücre konumuna aittir ve pivot modeli tarafından izlenmez.  
Aspose.Cells, hem bu iki biçimlendirme türü de kullanılabilsin diye tam `PivotTable.format` aşırı yükleme ailesini sunar:  
- `format(PivotArea, Style)` stili, `PivotArea.select` veya `PivotArea.selectField` ile oluşturulan anlamsal bir bölgeye bağlar.  
- `format(CellArea, Style)` stili, pivot tablo içindeki bir çalışma sayfası dikdörtgenine bağlar.  
- `format(int row, int column, Style)` tek bir hücreyi hedef alır.  
- `formatAll(Style)` tüm pivot tabloyu biçimlendirir.  

## **Bir Pivot Alanını Biçimlendirme**
Anlamsal alan iş akışı, bir vurgunun bir alanı veya raporun bir bölgesiyle birlikte kalması gerektiğinde önerilen yöntemdir.  
1. `new PivotArea(pivotTable)` ile bir `PivotArea` oluşturun. Nesne, o belirli pivot tabloya ait bir anlamsal bölgeyi tanımlar.  
2. Belirli bir eksende sıfır tabanlı konumuna göre bir alanı seçmek için `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` kullanın.  
   - `PivotTableSelectionType.DATA_AND_LABEL` alanın hem etiketlerini hem de verilerini seçer.  
   - `PivotTableSelectionType.LABEL_ONLY` yalnızca alanın etiketlerini seçer.  
   - `PivotTableSelectionType.DATA_ONLY` yalnızca alanın veri hücrelerini seçer.  
3. Alanı ad ile seçmek için `PivotArea.selectField(PivotFieldType axisType, string fieldName)` kullanın. Bir satır alanı adla seçildiğinde bölge, o alanın öğeleri tarafından üretilen değer hücrelerine çözülür.  
4. `Workbook.createStyle()` ile bir `Style` oluşturun, yazı tipini, ön plan rengini ve katı arka plan desenini yapılandırın ve stili `PivotTable.format(area, style)` metoduna geçirin.  
5. `PivotArea` aşırı yüklemesine yapılan her çağrı, `PivotTable.getPivotFormats()` içine bir `PivotTableFormat` girdisi ekler.  
6. Alan‑ankrajlı biçimler, pivot verisi hesaplandığında boyanır. Bu nedenle, biçimleri uyguladıktan sonra `PivotTable.calculateData()` çağırarak stillerin görünür olmasını sağlayın.  
Aşağıdaki örnek, küçük bir meyve‑satış pivot tablosu oluşturur, `Fruit` satır etiketlerini `PivotArea.select` ve `PivotTableSelectionType.LABEL_ONLY` ile, aynı satır alanının ürettiği değer hücrelerini `PivotArea.selectField` ile biçimlendirir ve ardından pivot tabloyu yeniden hesaplayarak iki stilin de boyanmasını sağlar.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
// Fruit sales data
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.getYellow());
labelStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.ROW,
    0,
    AsposeCells.PivotTableSelectionType.LABEL_ONLY
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.getLightGreen());
valueStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Pivot Tablosunun bir Cell Area'sını Biçimlendirme**
İlgili bölge bir anlamsal pivot bölgesi yerine düz bir çalışma sayfası dikdörtgeni olduğunda `PivotTable.format(CellArea, Style)` kullanın.  
`CellArea`, `StartRow`, `StartColumn`, `EndRow` ve `EndColumn` açık alanlarıyla tanımlanır. Değerler sıfır tabanlı çalışma sayfası koordinatlarıdır ve bitiş koordinatları dikdörtgene dahil edilen son satır ve sütunu belirtir; böylece alan, başlangıç konumundan bitiş konumuna kadar olan hücreleri kapsar.  
Alan‑ankrajlı bir biçimlemenin aksine, `CellArea` biçimi hücrelere hemen uygulanır. Stilin görünmesi için ayrı bir `calculateData()` çağrısına ihtiyaç yoktur.  
`CellArea` dikdörtgeni etiket hücreleri ve değer hücrelerini birlikte içerebilir. Sonraki bölüm, Aspose.Cells ve Excel'in bu dikdörtgeni içsel olarak nasıl temsil ettiğini açıklar.  
Aşağıdaki örnek, pivot tablosunun `E4:F5` dikdörtgenini italik, açık mavi bir stil ile biçimlendirir ve çalışma kitabını başka bir yeniden hesaplama yapmadan kaydeder.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(
    AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF)
);
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Pivot Alanları ve Cell Area'ların Nasıl Haritalandığı**
Excel, pivot tablo biçimlendirmesini olağan çalışma sayfası hücre stili kayıtları yerine `pivotArea` kayıtları olarak depolar. Aynı model Aspose.Cells tarafından da kullanılır; böylece bir biçimlendirme isteği kaydedildiğinde pivot alanlarına çevrilir.  
Kullanıcı tarafından sağlanan `CellArea` ile içsel olarak depolanan pivot alanları arasındaki ilişki her iki yönde de çoktan‑çoğa bir ilişkidir.  
- `CellArea`'den birden fazla pivot alanı üretilebilir. Dikdörtgen hem etiket hücrelerini hem de değer hücrelerini kapsıyorsa, pivot modeli etiket biçimlendirmesini ve veri biçimlendirmesini bağımsız olarak ele aldığı için, bu, ayrı etiket ve veri kurallarına bölünür.  
- Bir pivot alanı, birden çok ayrık `CellArea` örneğine çözülebilir. Grand‑total satırı gibi anlamsal bir bölge ya da öğeleri kesintisiz olmayan bir alan, birden fazla dikdörtgeni kapsayabilir. Bu yüzden `PivotArea.getCellAreas()` tek bir dikdörtgen yerine bir koleksiyon döndürür.  
`PivotTable.format` aracılığıyla yapılan her biçimlendirme işlemi `PivotTable.getPivotFormats()` içinde kaydedilir. Her `PivotTableFormat` girdisi ilişkili `PivotArea` ve ona uygulanan `Style`'ı gösterir. `PivotArea` aşırı yüklemesi, her çağrıda tam bir giriş ekler; farklı anlamsal bölgeler içeren bir `CellArea` ise birden fazla giriş ekleyebilir.  
Kaydedilen bölgeleri ayırt etmek için, her `PivotArea` `getOnlyLabel()` ve `getOnlyData()` bayraklarını gösterir. Aşağıdaki örnek, hem etiketleri hem de değerleri kapsayan tek bir dikdörtgeni biçimlendirir, `PivotTable.getPivotFormats()`'ı inceler ve her kaydedilen pivot alanının çözdüğü `CellArea` koordinatlarını yazdırır.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (let j = 0; j < resolvedAreas.length; j++) {
        const resolved = resolvedAreas[j];
        console.log(
            `    rows ${resolved.StartRow + 1}-${resolved.EndRow + 1}, columns ${resolved.StartColumn + 1}-${resolved.EndColumn + 1}`
        );
    }
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=true, OnlyData=false
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=false, OnlyData=true
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Biçimler, olağan hücre stilleri yerine pivot alanları olarak depolandığı için yeniden hesaplamalar ve yenilemelerde korunur. Pivot tablo `PivotTable.refreshData()` ile yenilendiğinde, `calculateData()` ile yeniden hesaplandığında veya kaydedilip tekrar yüklendiğinde, her depolanmış pivot alanı bölgesinin mevcut konumuna yeniden çözülür ve stili yeniden uygulanır.
{{% /alert %}}

Bir vurgunun yenilemeler boyunca bir alana veya anlamsal bir bölgeye bağlı kalması gerektiğinde `select` veya `selectField` ile oluşturulmuş bir `PivotArea` kullanın; mevcut pivot‑tablo düzeninde sabit bir dikdörtgeni biçimlendirmek yeterli olduğunda bir `CellArea` kullanın. Tek hücreyi hedefleyen `format(int row, int column, Style)` aşırı yüklemesi bireysel bir hücreyi hedef alır. Tüm pivot tabloyu bir kerede yeniden biçimlendirmek istediğinizde, üst sayfada ele alınan `formatAll` metodunu kullanın.

## **İlgili Makaleler**
- [Pivot Tablosuna Stil Uygulama](/cells/tr/nodejs-java/apply-style-to-pivot-table/)
- [Pivot Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/nodejs-java/manage-value-fields/)
- [Pivot Tablosunu Yenileme](/cells/tr/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}