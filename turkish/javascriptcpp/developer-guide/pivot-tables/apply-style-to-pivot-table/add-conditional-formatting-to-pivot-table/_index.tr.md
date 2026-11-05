---
title: Pivot Tablosuna Koşullu Biçimlendirme Ekle
linktitle: Pivot Tablosuna Koşullu Biçimlendirme Ekle
description: Aspose.Cells for JavaScript via C++ içinde bir pivot tablosuna koşullu biçimlendirme ekleyin - bir kuralı applyTo ve bir PivotConditionFormatScopeType kapsamıyla veri bölgesine bağlayın veya hedefi addCellArea ve pivotAreas ile tanımlayın, ardından formatConditions.addCondition aracılığıyla kuralları ve stilleri ekleyin.
keywords: Aspose.Cells for JavaScript via C++, pivot tablo, koşullu biçimlendirme, PivotConditionalFormat, ConditionalFormats, applyTo, PivotConditionFormatScopeType, Data, Field, Selection, addCellArea, pivotAreas, addPivotArea, formatConditions, addCondition, FormatConditionType
type: docs
weight: 30
url: /tr/javascript-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Üst sayfada ve kardeş sayfada açıklanan stiller statiktir – bir `PivotArea` veya `CellArea` bölgesi bir kez boyanır ve değerler ne olursa olsun stilini korur. Koşullu biçimlendirme ise kural‑tabanlı bir karşılıktır – 200 ‘nin üzerindeki her tutarı vurgulayın, ortadaki yüzde elliyi gölgelendirin veya en düşük sıralı öğeleri işaretleyin – ve vurgulama, pivot tablo yeniden hesaplandığında veya yenilendiğinde değerleri izler.

{{% alert color="primary" %}}
`formatConditions` nesnesinde bir pivot koşullu formatın `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` veya `formatConditions.addArea(cellArea)` metodunu çağırmayın. Bu iki aşırı yükleme, normal çalışma sayfası koşullu biçimlendirme API'sinden devralınmıştır ve pivot tablolar için çalışmaz – hücre bölgesi hiçbir zaman pivot bölgesine dönüştürülmez, bu yüzden istek sessizce yok sayılır. Bölgeyi her zaman `PivotConditionalFormat` üzerinde (`applyTo`, `addCellArea` veya `pivotAreas`) tanımlayın ve kuralı `addCondition` aşırı yüklemelerinden biriyle ekleyin.
{{% /alert %}}

## **Kuralı Kapsamla Uygula (Excel UI Yöntemi)**
İlk yöntem, kuralı Excel kullanıcı arayüzünün yaptığı şekilde konumlandırır. Pivot tablosundaki bir hücre, sıfır‑tabanlı çalışma sayfası koordinatlarıyla adlandırılır ve bir `PivotConditionFormatScopeType` kapsamı, Aspose.Cells'e kuralın bu hücreden ne kadar uzağa uzanması gerektiğini söyler:
- `PivotConditionFormatScopeType.Data` – pivot tablonun ürettiği tüm değer hücreleri, toplam satırları da dahil.
- `PivotConditionFormatScopeType.Field` – hücrenin tanımladığı alana ait değer hücreleri, toplam satırları hariç. Hücre bir alan hücresi (örneğin satır‑alan etiketi) olmalıdır; değer hücresi verilirse istisna fırlatılır.
- `PivotConditionFormatScopeType.Selection` – hücrenin seçtiği kesişimdeki yalnızca değer hücreleri, tipik olarak tek bir değer hücresi.
Aşağıdaki örnek, sol üst köşesi E3 olan bir meyve‑satış pivot tablosu oluşturur, `Data` kapsamıyla F4 hücresine (satır 3, sütun 5) bir koşullu biçim ekler ve 200 ‘nin üzerindeki tüm tutarları kırmızı üzerinde kalın beyaz olarak vurgular. Apple 220, Banana 330, Cherry 200 ve toplam 750 değerleriyle kural F4, F5 ve F7 hücrelerini boyar – çözülen bölge bütün veri sütunu F4:F7'dir ve yalnızca kuralı geçen hücreler aydınlanır.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotConditionFormatScopeType,
        FormatConditionType, OperatorType, Color, BackgroundType } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    // Üst sol köşesi E3 olan pivot tablo
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Koşullu formatı F4'te (satır 3, sütun 5) Veri kapsamı ile sabitle
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    format.applyTo(3, 5, PivotConditionFormatScopeType.Data);
    // Kural - 200'den büyük tutarları vurgula
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
    const style = workbook.createStyle();
    style.font.isBold = true;
    style.font.color = Color.White;
    style.foregroundColor = Color.Red;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    // wb.save(SaveFormat.Xlsx) dosyayı bayt olarak döndürür
    fs.writeFileSync("PivotConditionalFormatData.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4, F5, and F7");
    process.exit(0);
});
```

Aynı kuralı satır‑alan etiketi E4 (satır 3, sütun 4) üzerinde `Field` kapsamıyla bağladığınızda bölge F4:F6 olarak çözülür – toplam satırı içermeyen aynı veri sütunu – çünkü kapsam artık bütün değer alanı yerine `Fruit` alanını tanımlar. `Selection` kapsamı F4'te bağlandığında ise yalnızca F4 hücresi çözülür.

## **Bölgeyi Manuel Olarak Tanımlayın**
İkinci yöntem, kapsam seçicisini atlayıp bölgeyi `PivotConditionalFormat` üzerinde açıkça tanımlar.

### **addCellArea ile bir çalışma sayfası dikdörtgeni**
`addCellArea(cellArea)` verilen dikdörtgeni kuralın hedefi olarak kaydeder. Koordinatlar sıfır‑tabanlı çalışma sayfası koordinatlarıdır ve bölge tam olarak sağlanan dikdörtgendir – veri sütununa bir genişleme ya da toplam satırı mantığı yoktur. İlginç hücreler mevcut pivot düzeninin bilinen sabit bir dikdörtgeni olduğunda kullanın.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType,
        FormatConditionType, OperatorType, Color, BackgroundType, CellArea } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // F4:F6 dikdörtgenini hedefle (genel toplam olmadan değer hücreleri)
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new CellArea();
    area.startRow = 3;
    area.startColumn = 5;
    area.endRow = 5;
    area.endColumn = 5;
    format.addCellArea(area);
    // Kural - 150 ile 300 arasındaki tutarlar için açık sarı üzerinde italik
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.Between, "150", "300");
    const style = workbook.createStyle();
    style.font.isItalic = true;
    style.foregroundColor = Color.LightYellow;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatCellArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4 and F6");
    process.exit(0);
});
```

### **pivotAreas ile anlamsal bir pivot bölgesi**
`pivotAreas` kardeş sayfanın statik stiller için kullandığı aynı anlamsal‑bölge modelidir. Bir `PivotArea` oluşturun, `select` veya `selectField` ile bir alan veya bölge seçin ve `pivotAreas.addPivotArea(pivotArea)` ile ekleyin. Anlamsal bir bölge alanına bağlı kalır, bu yüzden koşullu biçim, pivot tablo yenilendiğinde ve düzen kaydırıldığında alanı izler. `pivotAreas.add(pivotArea)` aşırı yüklemesi hâlâ çalışır ancak eski olarak işaretlenmiştir – `addPivotArea` tercih edilmelidir.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotArea,
        FormatConditionType, OperatorType, Color } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Kuralı, Amount veri alanına anlamsal bir bölge olarak ekle
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new PivotArea(pivotTable);
    area.selectField(PivotFieldType.Data, "Amount");
    format.pivotAreas.addPivotArea(area);
    // Kural - 150'nin altındaki tutarlar için gri metin
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
    const style = workbook.createStyle();
    style.font.color = Color.Gray;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatPivotArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule is attached to the Amount value cells");
    process.exit(0);
});
```

## **Kuralların Nerede Saklandığı ve Yeniden Yüklemede Nasıl Korunduğu**
Her `conditionalFormats.add()` çağrısı, pivot tabloya bir `PivotConditionalFormat` ekler. Koşullar, formülleri ve stiller çalışma kitabıyla birlikte kaydedilir – Node’da ilk örnekle kaydedilen dosya yeniden açıldığında aynı kural türü, operatör ve formül bozulmadan gösterilir ve `getCellAreas()` aynı bölgeyi raporlar. Bu platformda bir koşulun `type` ve `operator` özellikleri sayısal enum değerleri olarak ortaya çıkar. Hiç koşul almamış girişler, çalışma kitabı kaydedildiğinde düşürülür; Excel’de hiçbir kuralı olmayan bir koşullu biçimin atılmasıyla aynı mantık uygulanır.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
AsposeCells.onReady().then(() => {
    // İlk örnek tarafından yazılan dosyayı yeniden yükle
    const workbook = new Workbook(new Uint8Array(fs.readFileSync("PivotConditionalFormatData.xlsx")));
    const pivotTable = workbook.worksheets.get(0).pivotTables.get(0);
    console.log("Conditional formats: " + pivotTable.conditionalFormats.count);
    for (let i = 0; i < pivotTable.conditionalFormats.count; i++) {
        const format = pivotTable.conditionalFormats.get(i);
        for (let j = 0; j < format.formatConditions.count; j++) {
            const condition = format.formatConditions.get(j);
            console.log("Format " + i + ": " + condition.type + " " + condition.operator + " formula1=" + condition.formula1);
        }
        const areas = format.getCellAreas();
        for (const area of areas)
            console.log("    rows " + (area.startRow + 1) + "-" + (area.endRow + 1) +
                        ", columns " + (area.startColumn + 1) + "-" + (area.endColumn + 1));
    }
    // Bu şu çıktıyı verir:
    // Koşullu biçimler: 1
    // Biçim 0: 1 2 formula1==200   (tip 1 = HücreDeğeri, operatör 2 = Büyükten)
    //     satırlar 4-7, sütunlar 6-6        (F4:F7, çözülen veri bölgesi)
    process.exit(0);
});
```

## **İlgili Makaleler**
- [Pivot Tablosuna Stil Uygulama](/cells/tr/javascript-cpp/apply-style-to-pivot-table/)
- [Pivot Tablosunun Bir Bölümünü Biçimlendirme](/cells/tr/javascript-cpp/format-part-of-pivot-table/)
- [Pivot Tablosunda İlk 10 Göster veya Filtreleme](/cells/tr/javascript-cpp/top-10-show-or-filter-in-pivot-table/)
- [Pivot Tablolarını Etiket veya Değer ile Filtreleme](/cells/tr/javascript-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}