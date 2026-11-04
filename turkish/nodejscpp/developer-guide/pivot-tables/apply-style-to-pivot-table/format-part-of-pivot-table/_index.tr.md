---
title: Pivot Tablosunun Bir Bölümünü Biçimlendirme
linktitle: Pivot Tablosunun Bir Bölümünü Biçimlendirme
description: Aspose.Cells for Node.js via C++ ile PivotTable.format aracılığıyla anlamsal PivotArea bölgelerine veya CellArea dikdörtgenlerine stiller uygulayarak bir pivot tablosunun bir bölümünü biçimlendirin; biçimler PivotTable.getPivotFormats() içinde saklanır ve pivot tablo yenilendiğinde korunur.
keywords: Aspose.Cells, Node.js via C++, pivot tablosu, biçim, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, selectField, formatAll
type: docs
weight: 20
url: /tr/nodejs-cpp/format-part-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
`PivotTable.formatAll` tek bir stili tüm pivot tablosuna uygular ve ana sayfada ele alınmıştır. Etiketler, değerler, toplamlar veya raporun belirli bölgeleri arasında ayrım yapmaz.  
Pratikte, bir pivot tablosunun yalnızca bir kısmının öne çıkması gerekir. Yaygın hedefler arasında bir satır alanına ait etiketler, bir alan tarafından üretilen değer hücreleri, genel toplam satırı veya ilk iki öğe satırı gibi isteğe bağlı bir dikdörtgen bulunur.  
Bir pivot tablosunun çalışma sayfasındaki hücrelere doğrudan stil uygulamak aynı şey değildir. Excel, pivot‑tablosu biçimlendirmesini sıradan hücre‑stil kayıtları yerine anlamsal `PivotArea` bölgeleri olarak saklar. Bir pivot‑alan biçimi, bir alanın etiketleri veya veri değerleri gibi bir bölgeye bağlı kalır ve pivot tablo yeniden hesaplandığında, yenilendiğinde veya genişletildiğinde yeniden çözülür. Öte yandan bir hücreye doğrudan yazılan stil, o hücre konumuna aittir ve pivot modeli tarafından izlenmez.  
Aspose.Cells, her iki biçimlendirme türünün de kullanılabilmesi için tam `PivotTable.format` aşırı yükleme ailesini sunar:
- `format(PivotArea, Style)` stili, `PivotArea.select` veya `PivotArea.selectField` ile oluşturulan anlamsal bir bölgeye bağlar.
- `format(CellArea, Style)` stili, pivot tablo içindeki bir çalışma sayfası dikdörtgenine bağlar.
- `format(number row, number column, Style)` tek bir hücreyi hedef alır.
- `formatAll(Style)` tüm pivot tabloyu biçimlendirir.

## **Pivot Alanını Biçimlendirme**
Anlamsal alan iş akışı, vurgunun bir alana veya rapor bölgesine bağlı kalması gerektiğinde önerilen yaklaşımdır.
1. `new PivotArea(pivotTable)` ile bir `PivotArea` oluşturun. Bu nesne, o belirli pivot tabloya ait bir anlamsal bölgeyi tanımlar.
1. Belirli bir eksende sıfır‑tabanlı konumuna göre bir alanı `PivotArea.select(PivotFieldType axisType, number fieldPosition, PivotTableSelectionType selectionType)` ile seçin.
   - `PivotTableSelectionType.DataAndLabel` alanın hem etiketlerini hem de verilerini seçer.
   - `PivotTableSelectionType.LabelOnly` yalnızca alanın etiketlerini seçer.
   - `PivotTableSelectionType.DataOnly` yalnızca alanın veri hücrelerini seçer.
1. `PivotArea.selectField(PivotFieldType axisType, string fieldName)` ile bir alanı adını belirterek seçin. Bir satır alanı adla seçildiğinde, bölge o alanın öğeleri tarafından üretilen değer hücrelerine çözülür.
1. `workbook.createStyle()` ile bir `Style` oluşturun, yazı tipini, ön plan rengini ve katı arka plan desenini yapılandırın ve stili `pivotTable.format(area, style)` metoduna aktarın.
1. `PivotArea` aşırı yüklemesine yapılan her çağrı, `pivotTable.getPivotFormats()` listesine bir `PivotTableFormat` girdisi ekler.
1. Alan‑bağlı biçimler, pivot verileri hesaplandığında uygulanır. Bu nedenle, biçimler uygulandıktan sonra stillerin görünür olması için `pivotTable.calculateData()` çağrısı yapılmalıdır.  
Aşağıdaki örnek, küçük bir meyve‑satışları pivot tablosu oluşturur, `Fruit` satır etiketlerini `PivotArea.select` ve `PivotTableSelectionType.LabelOnly` ile biçimlendirir, aynı satır alanı tarafından üretilen değer hücrelerini `PivotArea.selectField` ile biçimlendirir ve ardından pivot tabloyu yeniden hesaplayarak iki stilin de uygulanmasını sağlar.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setIsBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.Yellow);
labelStyle.setPattern(AsposeCells.BackgroundType.Solid);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.Row,
    0,
    AsposeCells.PivotTableSelectionType.LabelOnly
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.LightGreen);
valueStyle.setPattern(AsposeCells.BackgroundType.Solid);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Pivot Tablosunun Hücre Alanını Biçimlendirme**
İlgili bölge bir anlamsal pivot bölgesi yerine basit bir çalışma sayfası dikdörtgeni olduğunda `PivotTable.format(CellArea, Style)` kullanın.  
`CellArea`, `startRow`, `startColumn`, `endRow` ve `endColumn` özellikleriyle tanımlanır. Değerler sıfır‑tabanlı çalışma sayfası koordinatlarıdır ve son koordinatlar, dikdörtgenin içinde yer alan son satır ve sütunu belirler; böylece alan, başlangıç konumundan son konuma kadar tüm hücreleri kapsar.  
Alan‑bağlı bir biçimden farklı olarak, `CellArea` biçimi hücrelere anında uygulanır. Stil görünmesi için başka bir `pivotTable.calculateData()` çağrısına gerek yoktur.  
`CellArea` dikdörtgeni etiket hücreleri ve değer hücrelerini birlikte içerebilir. Sonraki bölüm, Aspose.Cells ve Excel'in bu dikdörtgeni içsel olarak nasıl temsil ettiğini açıklar.  
Aşağıdaki örnek, pivot tablosunun `E4:F5` dikdörtgenini italik, açık mavi bir stil ile biçimlendirir ve çalışma kitabını başka bir yeniden hesaplama yapmadan kaydeder.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Pivot Alanları ve Hücre Alanları Nasıl Eşlenir**
Excel, pivot‑tablo biçimlendirmesini sıradan çalışma sayfası hücre‑stil kayıtları yerine `pivotArea` kayıtları olarak saklar. Aynı model Aspose.Cells tarafından da kullanılır; bu nedenle bir biçimlendirme isteği kaydedildiğinde pivot alanlarına dönüştürülür.  
Kullanıcı tarafından sağlanan `CellArea` ile içsel olarak depolanan pivot alanları arasındaki ilişki her iki yönde de çok‑çok’tür.
- Bir `CellArea` birden fazla pivot alanı oluşturabilir. Dikdörtgen hem etiket hücrelerini hem de değer hücrelerini kapsıyorsa, pivot modeli etiket biçimlendirmesini ve veri biçimlendirmesini bağımsız olarak ele aldığı için bu durum ayrı etiket ve veri kurallarına bölünür.
- Bir pivot alanı, birden fazla ayrı `CellArea` örneğine çözülebilir. Genel toplam satırı gibi anlamsal bir bölge ya da öğeleri kesintisiz olmayan bir alan, birden çok dikdörtgeni kapsayabilir. Bu nedenle `PivotArea.getCellAreas()` tek bir dikdörtgen yerine bir koleksiyon döndürür.  
`pivotTable.format()` ile yapılan her biçimlendirme işlemi `pivotTable.getPivotFormats()` içinde kaydedilir. Her `PivotTableFormat` girdisi, ilişkili `PivotArea` ve ona uygulanan `Style`ı gösterir. `PivotArea` aşırı yüklemesi her çağrı için tam bir giriş ekler, oysa farklı anlamsal bölgelere sahip bir `CellArea` birden çok giriş ekleyebilir.  
Depolanan bölgeleri ayırt etmek için her `PivotArea`, `getOnlyLabel()` ve `getOnlyData()` bayraklarını sunar. Aşağıdaki örnek, hem etiketleri hem de değerleri kapsayan tek bir dikdörtgeni biçimlendirir, `pivotTable.getPivotFormats()` inceler ve her saklanan pivot alanının çözüldüğü `CellArea` koordinatlarını yazdırır.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (const resolved of resolvedAreas) {
        console.log(
            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, ` +
            `columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
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
Biçimler sıradan hücre stilleri yerine pivot alanları olarak saklandığı için yeniden hesaplamalar ve yenilemeler sırasında korunur. Pivot tablo `pivotTable.refreshData()` ile yenilendiğinde, `pivotTable.calculateData()` ile yeniden hesaplandığında veya kaydedilip yeniden yüklendiğinde, depolanan her pivot alanı bölgesinin mevcut konumuna yeniden çözülür ve stili tekrar uygulanır.
{{% /alert %}}

Vurgunun yenilemeler boyunca bir alana veya anlamsal bir bölgeye bağlı kalması gerektiğinde `select` veya `selectField` ile oluşturulmuş bir `PivotArea` kullanın, mevcut pivot‑tablo düzeninde sabit bir dikdörtgeni biçimlendirmek yeterli olduğunda ise bir `CellArea` kullanın. Tek hücre `format(number row, number column, Style)` aşırı yüklemesi bireysel bir hücreyi hedef alır. Tüm pivot tablosunun bir kerede yeniden stilendirilmesi gerektiğinde, ana sayfada ele alınan `formatAll` kullanın.

## **İlgili Makaleler**
- [Pivot Tablosuna Stil Uygulama](/cells/tr/nodejs-cpp/apply-style-to-pivot-table/)
- [Pivot Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/nodejs-cpp/manage-value-fields/)
- [Pivot Tablosunu Yenileme](/cells/tr/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}