---
title: Pivot Tablosuna Koşullu Biçimlendirme Ekleme
linktitle: Pivot Tablosuna Koşullu Biçimlendirme Ekleme
description: Aspose.Cells for Node.js via Java içinde bir Pivot Tablosuna koşullu biçimlendirme ekleyin, bir kuralı applyTo ve bir PivotConditionFormatScopeType kapsamı ile veri bölgesine bağlayın veya hedefi addCellArea ve getPivotAreas ile tanımlayın, ardından kuralları ve stilleri getFormatConditions().addCondition aracılığıyla ekleyin.
keywords: Aspose.Cells, Pivot Tablosu, koşullu biçimlendirme, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via Java
type: docs
weight: 30
url: /tr/nodejs-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Üst sayfada ve kardeş sayfada tanımlanan stiller statiktir - bir `PivotArea` veya `CellArea` bölgesi bir kez boyanır ve değerler ne olursa olsun stilini korur. Koşullu biçimlendirme kural‑güdümlü bir karşılıktır - 200'ün üzerindeki her tutarı vurgular, ortadaki yüzde elliyi gölgelendirir veya en alt sıralanan öğeleri işaretler - ve vurgulama, pivot tablosu yeniden hesaplandığında veya yenilendiğinde değerleri izler.
Aspose.Cells for Node.js via Java'da, pivot‑tablo koşullu biçimlendirme `pivotTable.getConditionalFormats()` koleksiyonunda bulunur. Her giriş, iki soruyu bağımsız olarak yanıtlayan bir `PivotConditionalFormat` nesnesidir:
- **Kural nerede uygulanır?** Hedef bölge, Excel kullanıcı arayüzünün kapsam seçicisini yansıtan `applyTo(int row, int column, PivotConditionFormatScopeType scope)` yöntemiyle veya `addCellArea(CellArea)` ve `getPivotAreas()` koleksiyonuyla açıkça bölgeyi adlandırarak tanımlanır.
- **Kural neyi test eder?** Bir veya daha fazla koşul, `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` kullanılarak `getFormatConditions()`'a eklenir ve her koşul kendi `getStyle()`'ını taşır.

{{% alert color="primary" %}}
Pivot koşullu biçimlendirme nesnesinin `getFormatConditions()` objesi üzerinde `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` veya `FormatConditionCollection.addArea(CellArea)` metodlarını çağırmayın. Bu iki aşırı yükleme, normal çalışma sayfası koşullu biçimlendirme API'sinden miras alınmıştır ve pivot tablolar için çalışmaz – hücre bölgesi pivot bölgesine dönüştürülmez, bu yüzden istek sessizce yok sayılır. Her zaman bölgeyi `PivotConditionalFormat` nesnesi üzerinde (`applyTo`, `addCellArea` veya `getPivotAreas()`) tanımlayın ve kuralı `addCondition` aşırı yüklemelerinden biriyle ekleyin.
{{% /alert %}}

## **Kuralı Kapsamla Uygula (Excel UI Yöntemi)**
İlk yöntem, kuralı Excel kullanıcı arayüzünün yaptığı gibi konumlandırır. Pivot tablosunun bir hücresi, sıfır‑tabanlı çalışma sayfası koordinatlarıyla adlandırılır ve bir `PivotConditionFormatScopeType` kapsamı, Aspose.Cells'e kuralın o hücreden ne kadar uzanması gerektiğini bildirir:
- `PivotConditionFormatScopeType.DATA` – pivot tablosunun ürettiği tüm değer hücreleri, genel toplamlar dahil.
- `PivotConditionFormatScopeType.FIELD` – hücrenin tanımladığı alana ait değer hücreleri, genel toplamlar hariç. Hücre, bir satır‑alan etiketi gibi bir alan hücresi olmalıdır; bir değer hücresi geçirilirse istisna fırlatılır.
- `PivotConditionFormatScopeType.SELECTION` – hücrenin seçtiği kesişimdeki sadece değer hücreleri, genellikle tek bir değer hücresi.
Aşağıdaki örnek, sol üst köşesi E3'te bulunan bir meyve‑satışları pivot tablosu oluşturur, `DATA` kapsamı ile hücre F4'te (satır 3, sütun 5) bir koşullu biçimlendirme bağlar ve 200'ün üzerindeki her tutarı kırmızı üzerinde beyaz kalın olarak vurgular. Apple 220, Banana 330, Cherry 200 ve toplam 750 değerleriyle, kural F4, F5 ve F7 hücrelerini renklendirir – çözülen bölge tüm veri sütunu F4:F7'dir ve yalnızca kuralı geçen hücreler aydınlanır.

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
// Üst sol köşesi E3'te olan pivot tablo
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Koşullu biçimi F4'te (satır 3, sütun 5) Veri kapsamı ile bağla
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.DATA);
// Kural - 200'den büyük tutarları vurgula
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.GREATER_THAN,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getWhite());
style.setForegroundColor(AsposeCells.Color.getRed());
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

`FIELD` kapsamı ile aynı kuralı satır‑alan etiketi E4'te (satır 3, sütun 4) bağlamak, bölgeyi F4:F6'ya çözer – toplam satırı olmayan aynı veri sütunu – çünkü kapsam artık tüm değer alanı yerine `Fruit` alanını tanımlar. `SELECTION` kapsamı F4'te bağlandığında sadece F4'ü çözer.

## **Bölgeyi Manuel Olarak Tanımlama**
İkinci yöntem, kapsam seçiciyi atlar ve bölgeyi `PivotConditionalFormat` üzerinde açıkça adlandırır.

### **addCellArea ile bir çalışma sayfası dikdörtgeni**
`addCellArea(CellArea)` verilen dikdörtgeni kuralın hedefi olarak kaydeder. Koordinatlar sıfır‑tabanlı çalışma sayfası koordinatlarıdır ve bölge tam olarak sağlanan dikdörtgendir – veri sütununa genişleme ve toplam satırı mantığı yoktur. İlginç hücreler mevcut pivot düzeninin bilinen sabit bir dikdörtgeni olduğunda kullanın.

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
// F4:F6 dikdörtgenini hedefle (toplam satırı olmayan değer hücreleri)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const cellArea = new AsposeCells.CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Kural - 150 ile 300 arasındaki tutarlar için açık sarı renkte italik
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.BETWEEN,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 255, 255, 224));
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **PivotAreas ile anlamsal bir pivot bölgesi**
`getPivotAreas()` kardeş sayfanın statik stiller için kullandığı aynı anlamsal‑bölge modelidir. Bir `PivotArea` oluşturun, `select` veya `selectField` ile bir alan veya bölge seçin ve `getPivotAreas().addPivotArea(PivotArea)` ile ekleyin. Anlamsal bir bölge alanına bağlı kalır, bu yüzden koşullu biçimlendirme, pivot tablo yenilendiğinde ve düzen değiştiğinde alanı izler. `getPivotAreas().add(PivotArea)` aşırı yüklemesi hâlâ derlenir ancak eski olarak işaretlenmiştir – `addPivotArea` tercih edin.

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
// Kuralı Amount veri alanına anlamsal bir bölge olarak ekle
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Kural - 150'nin altındaki tutarlar için gri metin
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.LESS_THAN,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Kuralların Nerede Saklandığı ve Yeniden Yüklemede Nasıl Korunduğu**
`getConditionalFormats()` üzerinde yapılan her `add()` çağrısı, pivot tabloya bir `PivotConditionalFormat` ekler. Koşullar, formülleri ve stilleri çalışma kitabıyla birlikte kaydedilir – aşağıdaki örnekte dosya yeniden açıldığında aynı kural, tipi, operatörü ve formülü bozulmadan gösterilir ve `getCellAreas()` aynı bölgeleri rapor eder. Koşul almayan girdiler, çalışma kitabı kaydedildiğinde silinir; bu, Excel'in kuralı olmayan bir koşullu biçimlendirmeyi atmasıyla aynı şekildedir.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const conditionalFormats = pivotTable.getConditionalFormats();
console.log("Conditional formats: " + conditionalFormats.getCount());
for (let i = 0; i < conditionalFormats.getCount(); i++) {
    const format = conditionalFormats.get(i);
    const formatConditions = format.getFormatConditions();
    for (let j = 0; j < formatConditions.getCount(); j++) {
        const condition = formatConditions.get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    const cellAreas = format.getCellAreas();
    for (let k = 0; k < cellAreas.length; k++) {
        const area = cellAreas[k];
        console.log(`    rows ${area.StartRow + 1}-${area.EndRow + 1}, columns ${area.StartColumn + 1}-${area.EndColumn + 1}`);
    }
}
// Bu yazdırır:
// Koşullu biçimler: 1
// Biçim 0: CellValue GreaterThan formula1==200
//     satırlar 4-7, sütunlar 6-6        (F4:F7, çözülen veri bölgesi)
```

## **İlgili Makaleler**
- [Pivot Tablosuna Stil Uygulama](/cells/tr/nodejs-java/apply-style-to-pivot-table/)
- [Pivot Tablosunun Bir Bölümünü Biçimlendirme](/cells/tr/nodejs-java/format-part-of-pivot-table/)
- [Pivot Tablosunda İlk 10 Gösterme veya Filtreleme](/cells/tr/nodejs-java/top-10-show-or-filter-in-pivot-table/)
- [Etiket veya Değere Göre Pivot Tablolarını Filtreleme](/cells/tr/nodejs-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}