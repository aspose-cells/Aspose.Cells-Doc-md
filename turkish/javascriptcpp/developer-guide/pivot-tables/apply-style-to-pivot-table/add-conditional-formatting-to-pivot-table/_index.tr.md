---
title: Pivot Tablosuna Koşullu Biçimlendirme Ekle
linktitle: Pivot Tablosuna Koşullu Biçimlendirme Ekle
description: Aspose.Cells for JavaScript via C++ içinde bir pivot tablosuna koşullu biçimlendirme ekleyin - bir kuralı applyTo ve PivotConditionFormatScopeType kapsamı ile veri bölgesine bağlayın, ya da hedefi addCellArea ve pivotAreas ile tanımlayın, ardından kuralları ve stilleri formatConditions.addCondition aracılığıyla ekleyin.
keywords: Aspose.Cells for JavaScript via C++, pivot tablosu, koşullu biçimlendirme, PivotConditionalFormat, ConditionalFormats, applyTo, PivotConditionFormatScopeType, Data, Field, Selection, addCellArea, pivotAreas, addPivotArea, formatConditions, addCondition, FormatConditionType
type: docs
weight: 30
url: /tr/javascript-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Üst sayfada ve kardeş sayfada açıklanan stiller statiktir – bir `PivotArea` veya `CellArea` bölgesi bir kez boyanır ve değerler ne olursa olsun stilini korur. Koşullu biçimlendirme ise kural tabanlı karşılığıdır – 200'ün üzerindeki her tutarı vurgulayın, orta yüzde elliyi gölgelendirin, ya da en düşük sıralı öğeleri işaretleyin – ve vurgulama, pivot tablosu yeniden hesaplandığında veya yenilendiğinde değerleri takip eder.  
Aspose.Cells içinde, pivot‑tablo koşullu biçimlendirme `pivotTable.conditionalFormats` koleksiyonunda bulunur. Her giriş, iki soruyu bağımsız olarak cevaplayan bir `PivotConditionalFormat` nesnesidir:
- **Kural nerede uygulanır?** Hedef bölge ya `applyTo(row, column, scope)` yöntemiyle (Excel kullanıcı arabiriminin kapsam seçicisini taklit eder) ya da `addCellArea(cellArea)` ve `pivotAreas` koleksiyonuyla açıkça tanımlanır.
- **Kural neyi test eder?** Bir veya birden fazla koşul, `formatConditions.addCondition(type, operatorType, formula1, formula2)` ile `formatConditions` koleksiyonuna eklenir ve her koşul kendi `style` öğesini taşır.

{{% alert color="primary" %}}
`PivotConditionalFormat` nesnesinin `formatConditions` nesnesinde `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` veya `formatConditions.addArea(cellArea)` metodlarını çağırmayın. Bu iki aşırı yükleme, normal çalışma sayfası koşullu biçimlendirme API'sinden miras alınmıştır ve pivot tablolar için çalışmaz – hücre alanı bir pivot alanına dönüştürülmez, bu yüzden istek sessizce yok sayılır. Bölgeyi her zaman `PivotConditionalFormat` nesnesi üzerinde (`applyTo`, `addCellArea` veya `pivotAreas`) tanımlayın ve kuralı `addCondition` aşırı yüklemelerinden biriyle ekleyin.
{{% /alert %}}

## **Kuralı Kapsamla Uygula (Excel UI Yöntemi)**
İlk yöntem, kuralı Excel kullanıcı arabiriminin yaptığı şekilde konumlandırır. Pivot tablosundaki bir hücre, sıfır‑tabanlı çalışma sayfası koordinatlarıyla adlandırılır ve bir `PivotConditionFormatScopeType` kapsamı, Aspose.Cells'e kuralın o hücreden ne kadar uzanması gerektiğini söyler:
- `PivotConditionFormatScopeType.Data` – pivot tablosunun ürettiği tüm değer hücreleri, ara toplamlar dahil.
- `PivotConditionFormatScopeType.Field` – hücrenin tanımladığı alana ait değer hücreleri, ara toplamlar hariç. Hücre bir alan etiketi (ör. satır‑alan etiketi) olmalıdır; bir değer hücresi geçirilirse istisna oluşur.
- `PivotConditionFormatScopeType.Selection` – hücrenin seçtiği kesişimdeki değer hücreleri, genellikle tek bir değer hücresi.
Aşağıdaki örnek, sol‑üst köşesi E3'te olan bir meyve‑satışları pivot tablosu oluşturur, `Data` kapsamı ile F4 (satır 3, sütun 5) hücresine bir koşullu biçim ekler ve 200'ü geçen her tutarı kırmızı üzerinde beyaz kalın olarak vurgular. Apple 220, Banana 330, Cherry 200 ve toplam 750 değerleriyle kural F4, F5 ve F7 hücrelerini renklendirir – çözülen bölge tüm veri sütunu F4:F7 olur ve yalnızca kuralı geçen hücreler ışıldar.

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
    // Pivot table with its top-left corner at E3
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Anchor the conditional format at F4 (row 3, column 5) with the Data scope
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    format.applyTo(3, 5, PivotConditionFormatScopeType.Data);
    // Rule - highlight amounts greater than 200
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
    const style = workbook.createStyle();
    style.font.isBold = true;
    style.font.color = Color.White;
    style.foregroundColor = Color.Red;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    // wb.save(SaveFormat.Xlsx) returns the file as bytes
    fs.writeFileSync("PivotConditionalFormatData.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4, F5, and F7");
    process.exit(0);
});
```

Aynı kuralı satır‑alan etiketi E4 (satır 3, sütun 4) üzerinde `Field` kapsamı ile eklemek, ara‑toplam satırı olmadan aynı veri sütunu F4:F6'ya çözülür – çünkü kapsam artık tüm değer alanı yerine `Fruit` alanını tanımlar. `Selection` kapsamı F4'te konumlandırıldığında yalnızca F4 hücresini kapsar.

## **Bölgeyi El İle Tanımla**
İkinci yöntem, kapsam seçiciyi atlayıp bölgeyi `PivotConditionalFormat` üzerinde doğrudan adlandırır.

### **addCellArea ile bir çalışma sayfası dikdörtgeni**
`addCellArea(cellArea)` verilen dikdörtgeni kuralın hedefi olarak kaydeder. Koordinatlar sıfır‑tabanlı çalışma sayfası koordinatlarıdır ve bölge tam olarak sağlanan dikdörtgendir – veri sütununa genişleme ya da ara‑toplam mantığı yoktur. İlgi duyulan hücreler mevcut pivot düzeninde bilinen sabit bir dikdörtgen olduğunda bunu kullanın.

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
    // Target the rectangle F4:F6 (the value cells without the grand total)
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new CellArea();
    area.startRow = 3;
    area.startColumn = 5;
    area.endRow = 5;
    area.endColumn = 5;
    format.addCellArea(area);
    // Rule - italic on light yellow for amounts between 150 and 300
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
`pivotAreas`, kardeş sayfanın statik stiller için kullandığı aynı anlamsal‑bölge modelidir. Bir `PivotArea` oluşturun, `select` veya `selectField` ile bir alan ya da bölge seçin ve `pivotAreas.addPivotArea(pivotArea)` ile ekleyin. Anlamsal bir bölge alanına bağlı kalır, bu yüzden koşullu biçim alan yenilendiğinde ve düzen değiştiğinde alanı takip eder. `pivotAreas.add(pivotArea)` aşırı yüklemesi hâlâ çalışır ancak eskimiş olarak işaretlenmiştir – `addPivotArea` tercih edilmelidir.

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
    // Attach the rule to the Amount data field as a semantic region
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new PivotArea(pivotTable);
    area.selectField(PivotFieldType.Data, "Amount");
    format.pivotAreas.addPivotArea(area);
    // Rule - grey text for amounts below 150
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

## **Kurallar Nerede Saklanır ve Yeniden Yüklemede Nasıl Korunur**
Her `conditionalFormats.add()` çağrısı, pivot tabloya bir `PivotConditionalFormat` ekler. Koşullar, formülleri ve stilleri çalışma kitabıyla birlikte kaydedilir – ilk örnekte Node ile kaydedilen dosya yeniden açıldığında aynı kural, tipi, operatörü ve formülü bozulmadan görünür ve `getCellAreas()` aynı bölgeyi raporlar. Bu platformda bir koşulun `type` ve `operator` özellikleri sayısal enum değerleri olarak ortaya çıkar. Hiç koşul almamış girişler, çalışma kitabı kaydedildiğinde atılır; Excel'in kuralı olmayan bir koşullu biçimlendirmeyi göz ardı etmesiyle aynı davranıştır.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook } = AsposeCells;
AsposeCells.onReady().then(() => {
    // Reload the file written by the first example
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
    // This prints:
    // Conditional formats: 1
    // Format 0: 1 2 formula1==200   (type 1 = CellValue, operator 2 = GreaterThan)
    //     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
    process.exit(0);
});
```

## **İlgili Makaleler**
- [Pivot Tablosuna Stil Uygulama](/cells/tr/javascript-cpp/apply-style-to-pivot-table/)
- [Pivot Tablosunun Bir Bölümünü Biçimlendirme](/cells/tr/javascript-cpp/format-part-of-pivot-table/)
- [Pivot Tablosunda İlk 10’u Göster veya Filtrele](/cells/tr/javascript-cpp/top-10-show-or-filter-in-pivot-table/)
- [Pivot Tablolarını Etiket veya Değer ile Filtreleme](/cells/tr/javascript-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}