---
title: Aspose.Cells for .NET'te PivotTable'a filtre alanları ekleme
linktitle: Filtre Alanları Ekleme
description: Aspose.Cells for Node.js via Java kullanarak pivot tablolarda filtre alanları eklemeyi ve yapılandırmayı öğrenin; filtre alanı ekleme, tek seçimli filtreleme ve çoklu seçim filtreleme dahil.
keywords: Aspose.Cells, Node.js via Java, pivot tablosu, filtre alanı, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /tr/nodejs-java/add-filter-field-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, pivot tablolarındaki filtre alanlarının tüm yaşam döngüsünü destekler. Üst düzey bir kolaylık API'si veya daha düşük seviyeli `PageFields` koleksiyonu aracılığıyla bir filtre alanı ekleyebilir, filtreni tek seçim modunda çalıştırabilir, her sayfa öğesini göstermek için temizleyebilir veya Excel'deki onay kutusu kullanıcı arayüzü aracılığıyla kullanıcıların aynı anda birkaç sayfa öğesi seçebilmesi için alanı çoklu seçime geçirebilirsiniz.
{{% /alert %}}

## **Giriş**

Bir filtre alanı, pivot gövdesinin kaynak verilerin *hangi alt kümesini* görüntüleyeceğini kontrol eden bir pivot alanıdır. Son kullanıcılar bunu Excel'de işlenmiş bir pivot tablonun üst kısmında bir açılır menü olarak görür ve kullanılabilir sayfa öğelerinden birini seçmek, yalnızca o sayfa öğesine ait kayıtların özetlenmesi için pivot gövdesini yeniden oluşturur. Bir pivot alanı, `PivotFieldType.Row`, `PivotFieldType.Column` veya `PivotFieldType.Data` yerine `PivotFieldType.Page` olarak kaydedildiğinde bir filtre alanı haline gelir.

Bir filtre alanı iki davranışta çalışabilir. Varsayılan **tek seçim** davranışında aynı anda yalnızca bir sayfa öğesi görünür; bu nedenle pivot gövdesi tam olarak bir alt kümeyi özetler. **Çoklu seçim** davranışında ise alan bir onay kutusu listesi sunar ve pivot gövdesi işaretlenen her sayfa öğesinin birleşimini özetler. Aynı kaynak alanı, tek bir özellik değiştirilerek bu davranışlar arasında ileri geri taşınabilir.

Aspose.Cells for Node.js via Java, bir filtre alanını kaydetmek için iki eşdeğer yol sunar. Üst düzey API, `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` yöntemidir; bu yöntem kaynak sütun adını alır ve alanı tek bir çağrıda ekler. Daha düşük seviyeli API ise `pivotTable.getPageFields().add(PivotField)` yöntemidir; bu yöntem, zaten bir `PivotField` referansına sahip olduğunuzda ve aynı alan örneğini filtre alanına eklemek istediğinizde kullanılır. Her iki API de aynı `PageFields` koleksiyonunu doldurur ve bu makalenin devamı, aralarında nasıl seçim yapılacağını ve her filtreleme modunun nasıl yönlendirileceğini göstermektedir.

## **filtre alanı Ekleme**

Bir pivot alanını filtre alanına kaydetmenin iki yolu vardır. Üst düzey çağrı, kaynak sütun adını bir dize olarak alır ve en yaygın yoldur. Daha düşük seviyeli çağrı, mevcut bir `PivotField` örneğini kabul eder ve aynı alan nesnesinin birden çok pivot alanında yeniden kullanılması gerektiğinde kullanışlıdır. Her iki çağrı da alanı `pivotTable.getPageFields()` içine yerleştirir; ardından alan, işlenmiş pivot tablonun üst kısmında sayfa açılır menüsü olarak görünür.

### addFieldToArea ile filtre alanı Ekleme

Aşağıdaki örnek, küçük bir Meyve / Yıl / Tutar veri kümesi oluşturur, E3 hücresinde `Fruit` satır alanında, `Amount` veri alanında ve `Year` filtre alanında bir pivot tablo yerleştirir, pivotu yeniler ve çalışma kitabını kaydeder.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Başlık satırını ayarla
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 satır örnek veri doldur: Meyve, Yıl, Miktar
var data = [
    [ "apple", 2020, 100 ],
    [ "banana", 2021, 200 ],
    [ "apple", 2021, 150 ],
    [ "grape", 2020, 120 ],
    [ "orange", 2022, 180 ],
    [ "banana", 2020, 90 ],
    [ "grape", 2021, 130 ],
    [ "apple", 2022, 170 ],
    [ "orange", 2021, 110 ]
];

for (var i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}

// E3 hücresine sabitlenmiş bir pivot tablo ekle
var pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Alanları bölgelerine ekle: Meyve Satır olarak, Miktar Veri olarak, Yıl Sayfa alanı olarak
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Pivot tablo verilerini yenile ve hesapla
pivotTable.refreshData();
pivotTable.calculateData();

// Çalışma kitabını kaydet
workbook.save("pageFieldSample.xlsx");
```

### getPageFields().add ile filtre alanı Ekleme

Zaten bir `PivotField` örneğiyle çalışıyorsanız, onu doğrudan `pivotTable.getPageFields().add` yöntemine geçirebilirsiniz. Pivot tablo ve filtre alanı, önceki senaryodaki ile tam olarak aynı şekilde oluşturulur; yalnızca son filtre alanı kaydı, daha düşük seviyeli API çağrısıyla değiştirilir.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Başlıklar
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// Örnek veriler (9 satır)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// E3 konumunda, A1:C10 aralığını kapsayan pivot tablo ekle
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Fruit -> Satır, Amount -> Veri (Year aşağıda Sayfa alanına gidecek)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Düşük seviye yaklaşım: BaseFields'tan mevcut Year PivotField'ını al
// ve PageFields.Add(PivotField) aracılığıyla Sayfa alanına kaydet.
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// Yeni sayfa alanının kaydedilen çalışma kitabında yansıtılması için yenile
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Tek Seçim Filtreleme (Bir Sayfa Öğesi Gösterme)**

Varsayılan tek seçim davranışında, filtre alanı tek bir açılır menü olarak işlenir ve `PivotField.CurrentPageItem` tamsayısı, pivot gövdesini hangi sayfa öğesinin yönlendireceğini seçer. Belirli bir dizin atamak o öğeyi seçer; özel gösterge değeri olan `0x7FFD` (ondalık 32765) atamak ise filtreyi temizler, böylece her sayfa öğesi aynı anda özetlenir. Tek seçim varsayılandır; bunu açıkça etkinleştirmeniz gerekmez.

### Tüm Öğeleri Gösterme

`CurrentPageItem` öğesini sihirli değer olan `0x7FFD` olarak ayarlamak, filtreni temizlemeye eşdeğerdir; pivot gövdesi, hiçbir filtre uygulanmamış gibi her sayfa öğesini özetler.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);

// Fruit/Yıl/Miktar verilerini doldur
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

var data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (var r = 0; r < data.length; r++) {
    for (var c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// E3 hücresinde pivot tablo oluştur
var pivotTables = sheet.getPivotTables();
var index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
var pivotTable = pivotTables.get(index);

// Pivot alanlarını yapılandır: Fruit→Satır, Amount→Veri, Year→Sayfa
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.refreshData();
pivotTable.calculateData();

// Sayfa filtresini temizle, böylece sayfa alanındaki her öğe görünür olsun.
// 0x7FFD (ondalık 32765) "tüm öğeler" anlamına gelen özel bekçi değeridir —
// Excel'in sayfa alanı açılır menüsünde "(Tümü)" seçmeye eşdeğerdir.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### Belirli Bir Öğeyi Gösterme

`CurrentPageItem` öğesini gerçek bir dizine ayarlamak yalnızca o sayfa öğesini seçer. Dizin, filtre alanının sıralanmış öğe listesindeki konumdur; dolayısıyla örneğin `1` sıralamadan sonra ikinci öğeyi seçer.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Örnek veri ekle (Meyve/Yıl/Miktar)
cells.get("A1").setValue("Fruit");
cells.get("B1").setValue("Year");
cells.get("C1").setValue("Amount");

cells.get("A2").setValue("Apple");
cells.get("B2").setValue("2020");
cells.get("C2").setValue("100");

cells.get("A3").setValue("Apple");
cells.get("B3").setValue("2021");
cells.get("C3").setValue("150");

cells.get("A4").setValue("Banana");
cells.get("B4").setValue("2020");
cells.get("C4").setValue("200");

cells.get("A5").setValue("Banana");
cells.get("B5").setValue("2021");
cells.get("C5").setValue("250");

// E3'e pivot tablo ekle
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// Alanları ekle: Meyve→Satır, Miktar→Veri, Yıl→Sayfa
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Sayfa alanına özel işlemler
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = sıralanmış listedeki ikinci öğe (örn. "2021")

// Pivot tabloyu yenile ve hesapla
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Çoklu Seçim Filtreleme**

Çoklu seçim filtreleme, sayfa açılır menüsünü bir onay kutusu listesine dönüştürür ve son kullanıcının aynı anda birkaç sayfa öğesi seçmesine olanak tanır. Aspose.Cells, birlikte çalışan iki özellik sunar. Çoklu seçim kullanıcı arayüzünün geçerli olabilmesi için `PivotField.IsMultipleItemSelectionAllowed` öğesinin önce `true` olarak ayarlanması gerekir. Etkinleştirildikten sonra, `PivotItem.IsHidden` onay kutusu listesinde hangi öğelerin görüneceğini kontrol eder; böylece her öğeyi gösterebilir veya yalnızca belirli öğeleri beyaz listeye alabilirsiniz.

Aşağıdaki kod, Senaryo 1a'da oluşturulan aynı Year filtre alanında çoklu seçimi etkinleştirir ve ardından iki model gösterir: Bölüm A, her girdi için `IsHidden` değerini `false` olarak bırakarak her sayfa öğesini gösterir; Bölüm B ise `switch (pivotItems[i].getStringValue())` bloğu aracılığıyla yalnızca seçtiğiniz kaynak değerleri beyaz listeye alır ve diğer her şeyi gizler.

```javascript
const AsposeCells = require("aspose.cells");

// — Pivot tablo ve sayfa alanı, Senaryo 1a'dakiyle tam olarak aynı şekilde
//   oluşturulur (Meyve/Yıl/Tutar verileri, E3'te pivot, Meyve→Satır,
//   Tutar→Veri, Yıl→AddFieldToArea ile Sayfa).
//   Aşağıda sayfa alanında çoklu seçim filtrelemesi uyguluyoruz.

const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();

// Örnek veri: Meyve | Yıl | Tutar
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

const data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

const pivotSheet = workbook.getWorksheets().add("Pivot");
const pivots = pivotSheet.getPivotTables();
const pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
const pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, "Year");

// — Sayfa alanında çoklu seçimi etkinleştir
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);

// Bölüm A — TÜM öğeleri seç (her öğeyi görünür yap)
const pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setHidden(false);
}

// Bölüm B — Yalnızca kaynak değere göre belirli öğeleri seç
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **Not:** `PivotItem.IsHidden` aracılığıyla çoklu seçim filtrelemesi kullanırken, **en az bir `PivotItem` görünür kalmalıdır** (`IsHidden == false`). Her öğe gizliyse, Excel dosyayı açarken ya çöker ya da boş bir pivot işler. Çoklu seçim beyaz listenizin kaynak verilerinizden en az bir öğe içerdiğini her zaman doğrulayın.

## **Hangi API ve Hangi Mod Kullanılmalı?**

Aşağıdaki tablo, her API'nin ve modun ne zaman kullanılacağını özetler; böylece her senaryoyu ayrıntılı olarak okumadan doğru kombinasyonu seçebilirsiniz.

| Senaryo / Kullanım Durumu | Önerilen API | Kullanılan Özellik | Notlar |
|---|---|---|---|
| filtre alanını kaynak sütun adına göre ekleme (en yaygın) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | yok | Üst düzey, tek satır. Bir `PivotField` referansına ihtiyacınız yoksa bunu kullanın. |
| Zaten bir `PivotField` nesneniz olduğunda filtre alanı ekleme | `pivotTable.getPageFields().add(PivotField)` | yok | Alan nesnesi başka bir yerden alındığında veya yeniden kullanılması gerektiğinde kullanın. |
| Tek bir sayfa öğesine filtreleme (varsayılan mod) | `PivotField.CurrentPageItem` | belirli bir dizine ayarlayın | Örneğin, `1` sıralanmış listedeki ikinci öğeyi gösterir. |
| Tüm öğeleri gösterme / filtreni temizleme | `PivotField.CurrentPageItem` | `0x7FFD` olarak ayarlayın | Sihirli değer `0x7FFD` (ondalık 32765), "tüm öğeler" için gösterge değeridir. |
| Excel'de çoklu seçim kullanıcı arayüzünü etkinleştirme | `PivotField.IsMultipleItemSelectionAllowed` | `true` olarak ayarlayın | Herhangi bir `IsHidden` çağrısının geçerli olabilmesi için gereklidir. |
| Çoklu seçim listesindeki tek tek öğeleri gizleme / gösterme | `PivotItem.IsHidden` | öğe bazında ayarlayın | En az bir öğe görünür kalmalıdır (`IsHidden == false`). |

{{% alert color="primary" %}}
Çoklu seçim filtrelemesini yapılandırırken görünürlük kısıtlamasını her zaman aklınızda bulundurun. Çoklu seçim filtre alanındaki her `PivotItem` gizliyse, Excel dosyayı açarken çöker veya boş bir pivot işler. Beyaz listenizi, en az bir öğenin görünür kalacağı şekilde kaynak verilerinize göre oluşturun; böylece kaydedilen çalışma kitaplarınız her makinede güvenilir şekilde açılır.
{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}