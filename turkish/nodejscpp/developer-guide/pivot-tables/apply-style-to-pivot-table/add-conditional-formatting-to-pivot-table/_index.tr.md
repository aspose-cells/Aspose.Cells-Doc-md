---
title: Pivot Tablosuna Koşullu Biçimlendirme Ekle
linktitle: Pivot Tablosuna Koşullu Biçimlendirme Ekle
description: Aspose.Cells for Node.js via C++ içinde bir pivot tablosuna koşullu biçimlendirme ekleyin - bir kuralı applyTo ve PivotConditionFormatScopeType kapsamı ile veri bölgesine bağlayın ya da hedefi addCellArea ve pivotAreas ile tanımlayın, ardından formatConditions.addCondition aracılığıyla kuralları ve stilleri ekleyin.
keywords: Aspose.Cells for Node.js via C++, özet tablo, koşullu biçimlendirme, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via C++
type: docs
weight: 30
url: /tr/nodejs-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Üst sayfasında ve kardeş sayfasında açıklanan stiller statiktir - bir `PivotArea` veya `CellArea` bölgesi bir kez boyanır ve değerler ne olursa olsun stili korur. Koşullu biçimlendirme ise kural‑tabanlı bir eşdeğerdir - 200'ün üzerindeki her tutarı vurgulamak, orta yüzde elliyi gölgelendirmek veya en düşük sıralı öğeleri işaretlemek - ve vurgulama, özet tablo yeniden hesaplandığında veya yenilendiğinde değerleri takip eder. Aspose.Cells içinde, özet tablo koşullu biçimlendirme `pivotTable.getConditionalFormats()` koleksiyonunda bulunur. Her giriş, bağımsız olarak iki soruya yanıt veren bir `PivotConditionalFormat` nesnesidir:
- **Kural nerede uygulanır?** Hedef bölge, Excel kullanıcı arabiriminin kapsam seçicisini taklit eden `applyTo(row, column, scope)` yöntemiyle veya bölgeyi açıkça adlandıran `addCellArea(cellArea)` ve `pivotConditionalFormat.getPivotAreas()` koleksiyonuyla tanımlanabilir.
- **Kural neyi test eder?** Bir veya daha fazla koşul, `pivotConditionalFormat.getFormatConditions()` üzerinden elde edilen `formatConditions` nesnesine `formatConditions.addCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)` ile eklenir ve her koşul kendi stilini `getStyle()` aracılığıyla taşır.

{{% alert color="primary" %}}
`formatConditions.add(cellArea, type, operatorType, formula1, formula2)` veya `formatConditions.addArea(cellArea)` metodlarını bir pivot koşullu formatının `formatConditions` nesnesinde çağırmayın. Bu iki aşırı yükleme, normal çalışma sayfası koşullu‑biçimlendirme API'sinden kalıtılmıştır ve özet tablolar için çalışmaz – `cellArea` hiçbir zaman bir `pivotArea`'ya dönüştürülmez, bu yüzden istek sessizce yoksayılır. Bölgeyi doğrudan `pivotConditionalFormat` nesnesi üzerinde (`applyTo`, `addCellArea` veya `getPivotAreas()`) tanımlayın ve kuralı `addCondition` aşırı yüklemelerinden biriyle ekleyin.
{{% /alert %}}

## **Bir Kuralı Kapsam ile Uygula (Excel UI Yöntemi)**
İlk yöntem, kuralı Excel kullanıcı arabiriminin yaptığı gibi konumlandırır. Özet tablosunun bir hücresi, sıfır‑tabanlı çalışma sayfası koordinatlarıyla adlandırılır ve bir `PivotConditionFormatScopeType` kapsamı, Aspose.Cells'in bu hücreden ne kadar uzağa kadar kuralın uzanacağını belirler:
- `PivotConditionFormatScopeType.DATA` - özet tablosunun ürettiği tüm değer hücreleri, toplam satırları da dahil.
- `PivotConditionFormatScopeType.FIELD` - hücrenin tanımladığı alana ait değer hücreleri, toplam satırları hariç. Hücre bir alan etiketi (örneğin satır‑alan etiketi) olmalıdır; değer hücresi verilirse bir istisna fırlatılır.
- `PivotConditionFormatScopeType.SELECTION` - hücrenin seçtiği kesişimin değer hücreleri, tipik olarak tek bir değer hücresi.
Aşağıdaki örnek, E3 köşesinde başlayan bir meyve‑satışları özet tablosu oluşturur, `DATA` kapsamı ile F4 hücresinde (`row 3, column 5`) bir koşullu biçimlendirme sabitleyerek 200'ün üzerindeki her tutarı kırmızı üzerine beyaz kalın karakterle vurgular. Apple 220, Banana 330, Cherry 200 ve toplam 750 değerleriyle, kural F4, F5 ve F7'yı boyar – çözülen bölge tüm veri sütunu F4:F7'dir ve sadece kuralı geçen hücreler aydınlanır.

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
// Üst sol köşesi E3 olan özet tablo
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Koşullu biçimi F4'te (satır 3, sütun 5) Veri kapsamı ile bağla
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.Data);
// Kural - 200'den büyük tutarları vurgula
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.GreaterThan,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.White);
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Aynı kuralı satır‑alan etiketi E4 (`row 3, column 4`) üzerinde `FIELD` kapsamı ile sabitlemek, toplam satırını hariç tutarak F4:F6'ya uygulanır – aynı veri sütunu ancak toplam satırı olmadan – çünkü kapsam artık `Fruit` alanını tanımlar, tüm değer alanını değil. `SELECTION` kapsamı F4'te sabitlenirse yalnızca F4 çözülür.

## **Bölgeyi Manuel Olarak Tanımla**
İkinci yöntem, kapsam seçiciyi atlayıp bölgeyi `PivotConditionalFormat` üzerinde açıkça adlandırır.

### **addCellArea ile bir çalışma sayfası dikdörtgeni**
`addCellArea(cellArea)` verilen dikdörtgeni kuralın hedefi olarak kaydeder. Koordinatlar sıfır‑tabanlı çalışma sayfası koordinatlarıdır ve bölge tam olarak sağlanan dikdörtgendir – veri sütununa genişleme ya da toplam‑satırı mantığı yoktur. İlgi duyulan hücreler mevcut özet tablo düzeninin bilinen sabit bir dikdörtgeni olduğunda bu yöntemi kullanın.

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
// F4:F6 dikdörtgenini hedefle (toplam satırı içermeyen değer hücreleri)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.CellArea();
area.startRow = 3;
area.startColumn = 5;
area.endRow = 5;
area.endColumn = 5;
format.addCellArea(area);
// Kural - 150 ile 300 arasındaki tutarlar için açık sarı renkte italik
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.Between,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setIsItalic(true);
style.setForegroundColor(AsposeCells.Color.LightYellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **getPivotAreas ile anlamsal bir özet tablo bölgesi**
`pivotConditionalFormat.getPivotAreas()` aynı anlamsal‑bölge modelini sunar; kardeş sayfa statik stiller için bunu kullanır. Bir `PivotArea` oluşturun, `select` veya `selectField` ile bir alan veya bölge seçin ve `pivotAreas.addPivotArea(pivotArea)` ile ekleyin. Anlamsal bir bölge alanına bağlı kalır, bu yüzden koşullu biçimlendirme, özet tablo yenilendiğinde ve düzen değiştiğinde alanı izler. `pivotAreas.add(pivotArea)` aşırı yüklemesi hâlâ derlenebilir ancak eski olarak işaretlenmiştir – `addPivotArea` tercih edilmelidir.

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
// Kuralı Amount veri alanına semantik bir bölge olarak ekle
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.Data, "Amount");
format.getPivotAreas().addPivotArea(area);
// Kural - 150'nin altındaki tutarlar için gri metin
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.LessThan,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Gray);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Kuralların Nerede Saklandığı ve Yeniden Yüklemede Nasıl Korunduğu**
Her `conditionalFormats.add()` çağrısı, özet tabloya bir `PivotConditionalFormat` ekler. Koşullar, formüller ve stiller çalışma kitabıyla birlikte kaydedilir – aşağıdaki örnekte dosya yeniden açıldığında aynı kural, türü, operatörü ve formülü korunmuş şekilde görülür ve `getCellAreas()` aynı bölgeleri rapor eder. Hiçbir koşul almamış girişler, çalışma kitabı kaydedildiğinde düşer; Excel, kuralı olmayan bir koşullu biçimlendirmeyi aynı şekilde atar.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
console.log("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (let i = 0; i < pivotTable.getConditionalFormats().getCount(); i++) {
    const format = pivotTable.getConditionalFormats().get(i);
    for (let j = 0; j < format.getFormatConditions().getCount(); j++) {
        const condition = format.getFormatConditions().get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    for (const area of format.getCellAreas()) {
        console.log(`    rows ${area.startRow + 1}-${area.endRow + 1}, columns ${area.startColumn + 1}-${area.endColumn + 1}`);
    }
}
// Bu çıktı:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1=200
//     rows 4-7, columns 6-6        (F4:F7, çözülen veri bölgesi)
```

## **İlgili Makaleler**
- [Özet Tablosuna Stil Uygulama](/cells/tr/nodejs-cpp/apply-style-to-pivot-table/)
- [Özet Tablosunun Bir Bölümünü Biçimlendirme](/cells/tr/nodejs-cpp/format-part-of-pivot-table/)
- [Özet Tablosunda İlk 10'u Göster veya Filtrele](/cells/tr/nodejs-cpp/top-10-show-or-filter-in-pivot-table/)
- [Özet Tablosunu Etikete veya Değere Göre Filtreleme](/cells/tr/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}