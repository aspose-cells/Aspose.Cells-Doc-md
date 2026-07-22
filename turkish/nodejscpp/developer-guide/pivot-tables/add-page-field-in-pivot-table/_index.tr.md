---
title: Pivot Tablolarda Sayfa Alanları
linktitle: Pivot Tablolarda Sayfa Alanları
description: Aspose.Cells for Node.js via C++ kullanarak pivot tablolara sayfa alanları eklemeyi ve yapılandırmayı öğrenin, sayfa alanı ekleme, tek seçimli filtreleme ve çoklu seçim filtrelemeyi içerir.
keywords: Aspose.Cells, Node.js via C++, pivot tablo, sayfa alanı, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /tr/nodejs-cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, pivot tablolardaki sayfa alanlarının tüm yaşam döngüsünü destekler. Üst düzey kolaylık API'si aracılığıyla veya alt düzey `PageFields` koleksiyonu aracılığıyla bir sayfa alanı ekleyebilir, sayfa filtresini tek seçim modunda çalıştırabilir, her sayfa öğesini göstermek için temizleyebilir veya Excel'deki onay kutusu kullanıcı arayüzü aracılığıyla kullanıcıların bir defada birden çok sayfa öğesi seçebilmesi için alanı çoklu seçime geçirebilirsiniz.
{{% /alert %}}

## **Giriş**

Sayfa alanı, pivot gövdesinin kaynak verilerin *hangi alt kümesini* görüntüleyeceğini kontrol eden bir pivot alanıdır. Son kullanıcılar bunu Excel'de işlenmiş bir pivot'ın üst kısmında bir açılır menü olarak görür ve mevcut sayfa öğelerinden birini seçmek, yalnızca o sayfa öğesine ait kayıtların özetleneceği şekilde pivot gövdesini yeniden oluşturur. Bir pivot alanı, `PivotFieldType.Row`, `PivotFieldType.Column` veya `PivotFieldType.Data` yerine `PivotFieldType.Page` olarak kaydedildiğinde sayfa alanı haline gelir.

Bir sayfa alanı iki davranışta çalışabilir. Varsayılan **tek seçim** davranışında aynı anda yalnızca bir sayfa öğesi görünür, dolayısıyla pivot gövdesi tam olarak bir alt kümeyi özetler. **Çoklu seçim** davranışında ise alan bir onay kutusu listesi sunar ve pivot gövdesi işaretlenen her sayfa öğesinin birleşimini özetler. Aynı kaynak alan, tek bir özelliğin değiştirilmesiyle bu davranışlar arasında ileri geri taşınabilir.

Aspose.Cells for Node.js via C++, bir sayfa alanını kaydetmek için iki eşdeğer yol sunar. Üst düzey API, kaynak-sütun adını alan ve tek bir çağrıda alanı ekleyen `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` yöntemidir. Alt düzey API, zaten bir `PivotField` referansına sahip olduğunuzda ve aynı alan örneğini sayfa alanına eklemek istediğinizde kullanılan `PivotTable.pageFields.add(PivotField)` yöntemidir. Her iki API de aynı `PageFields` koleksiyonunu doldurur ve bu makalenin geri kalanı aralarında nasıl seçim yapılacağını ve her bir filtreleme modunun nasıl çalıştırılacağını gösterir.

## **Sayfa Alanı Ekleme**

Bir pivot alanını sayfa alanına kaydetmenin iki yolu vardır. Üst düzey çağrı, kaynak-sütun adını bir dize olarak alır ve en yaygın yoldur. Alt düzey çağrı, mevcut bir `PivotField` örneğini kabul eder ve aynı alan nesnesinin birden çok pivot alanında yeniden kullanılması gerektiğinde kullanışlıdır. Her iki çağrı da alanı `PivotTable.pageFields` içine yerleştirir; bundan sonra alan, işlenmiş pivot'ın üst kısmında sayfa açılır menüsü olarak görünür.

### addFieldToArea ile Sayfa Alanı Ekleme

Aşağıdaki örnek, küçük bir Meyve / Yıl / Tutar veri kümesi oluşturur, E3 hücresine bir pivot tablo yerleştirir, satır alanına `Fruit`, veri alanına `Amount` ve sayfa alanına `Year` koyar, pivot'u yeniler ve çalışma kitabını kaydeder.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Başlık satırını ayarla
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 satır örnek veriyi doldur: Meyve, Yıl, Miktar
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

// E3 hücresine bağlı bir pivot tablo ekle
var pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Alanları ilgili bölümlere ekle: Satır olarak Meyve, Veri olarak Miktar, Sayfa alanı olarak Yıl
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Pivot tablo verilerini yenile ve hesapla
pivotTable.refreshData();
pivotTable.calculateData();

// Çalışma kitabını kaydet
workbook.save("pageFieldSample.xlsx");
```

### pageFields.add ile Sayfa Alanı Ekleme

Zaten bir `PivotField` örneğiyle çalışıyorsanız, onu doğrudan `PivotTable.pageFields.add` yöntemine geçebilirsiniz. Pivot tablo ve sayfa alanı, önceki senaryodakiyle tam olarak aynı şekilde oluşturulur; yalnızca son sayfa alanı kaydı alt düzey API çağrısıyla değiştirilir.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Başlıklar
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// Örnek veriler (9 satır)
sheet.getCells().get("A2").putValue("apple");     sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");     sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");     sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");     sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");     sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");     sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// A1:C10 aralığını kapsayacak şekilde E3 konumuna pivot tablosu ekle
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Fruit -> Satır, Amount -> Veri (Year aşağıda Sayfa alanına eklenecek)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Düşük seviyeli yaklaşım: BaseFields içindeki mevcut Year PivotField'ını al
// ve PageFields.Add(PivotField) aracılığıyla Sayfa alanına kaydet
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// Yeni sayfa alanının kaydedilen çalışma kitabında yansıtılması için yenile
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Tek Seçim Filtreleme (Bir Sayfa Öğesi Gösterme)**

Varsayılan tek seçim davranışında, sayfa alanı tek bir açılır menü olarak işlenir ve `PivotField.currentPageItem` tamsayısı, pivot gövdesini hangi sayfa öğesinin çalıştıracağını seçer. Belirli bir dizin atamak o öğeyi seçer; özel gösterge değeri `0x7FFD` (ondalık 32765) atamak filtreyi temizler, böylece her sayfa öğesi bir defada özetlenir. Tek seçim varsayılandır; bunu açıkça etkinleştirmeniz gerekmez.

### Tüm Öğeleri Gösterme

`currentPageItem` öğesini sihirli değer olan `0x7FFD` değerine ayarlamak, sayfa filtresini temizlemeye eşdeğerdir: pivot gövdesi, hiçbir filtre uygulanmamış gibi her sayfa öğesini özetler.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Meyve/Yıl/Miktar verilerini doldur
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

let data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (let r = 0; r < data.length; r++) {
    for (let c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// E3'te özet tablo oluştur
let pivotTables = sheet.getPivotTables();
let index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
let pivotTable = pivotTables.get(index);

// Özet tablo alanlarını yapılandır: Fruit→Satır, Amount→Veri, Year→Sayfa
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.refreshData();
pivotTable.calculateData();

// Sayfa filtresini temizle, böylece sayfa alanındaki her öğe görünür.
// 0x7FFD (ondalık 32765), "tüm öğeler" anlamına gelen özel bekçi değeridir —
// Excel'in sayfa alanı açılır menüsünde "(Tümü)" seçmeye eşdeğerdir.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### Belirli Bir Öğeyi Gösterme

`currentPageItem` öğesini gerçek bir dizine ayarlamak yalnızca o bir sayfa öğesini seçer. Dizin, sayfa alanının sıralanmış öğe listesindeki öğenin konumudur, dolayısıyla örneğin `1` değeri sıralamadan sonra ikinci öğeyi seçer.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Örnek veri ekle (Meyve/Yıl/Miktar)
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");

cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");

cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");

cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");

cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");

// E3'e pivot tablo ekle
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// Alanları ekle: Fruit→Satır, Amount→Veri, Year→Sayfa
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Sayfa alanına özel işlemler
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = sıralanmış listedeki ikinci öğe (ör. "2021")

// Pivot tabloyu yenile ve hesapla
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Çoklu Seçim Filtreleme**

Çoklu seçim filtreleme, sayfa açılır menüsünü bir onay kutusu listesine dönüştürür ve son kullanıcının aynı anda birkaç sayfa öğesi seçmesine olanak tanır. Aspose.Cells birlikte çalışan iki özellik sunar. `PivotField.isMultipleItemSelectionAllowed` öğesinin, çoklu seçim kullanıcı arayüzünün geçerli olması için `true` olarak ayarlanması gerekir. Etkinleştirildikten sonra, `PivotItem.isHidden` öğesi onay kutusu listesinde hangi öğelerin görüneceğini kontrol eder; böylece her öğeyi gösterebilir veya yalnızca belirli öğeleri beyaz listeye alabilirsiniz.

Aşağıdaki kod, Senaryo 1a'da oluşturulan aynı Year sayfa alanında çoklu seçimi etkinleştirir ve ardından iki desen gösterir: Bölüm A, her giriş için `isHidden` öğesini `false` olarak bırakarak her sayfa öğesini ortaya çıkarırken, Bölüm B yalnızca seçtiğiniz kaynak değerlerini beyaz listeye alır ve `switch (pivotItems[i].getStringValue())` bloğu aracılığıyla diğer her şeyi gizler.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cells = sheet.getCells();

// Örnek veri: Meyve | Yıl | Miktar
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

let data = [
    ["apple", "2019", "100"],
    ["apple", "2020", "150"],
    ["apple", "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape", "2019", "120"],
    ["grape", "2020", "170"],
    ["grape", "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

let pivotSheet = workbook.getWorksheets().add("Pivot");
let pivots = pivotSheet.getPivotTables();
let pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
let pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// — Sayfa alanında çoklu seçimi etkinleştir
pivotTable.getPageFields().get(0).setIsMultipleItemSelectionAllowed(true);

// Bölüm A — TÜM öğeleri seç (her öğeyi görünür yap)
let pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setIsHidden(false);
}

// Bölüm B — Yalnızca belirli öğeleri kaynak değere göre seç
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setIsHidden(false);
            break;
        default:
            pivotItems.get(i).setIsHidden(true);
            break;
    }
}

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **Not:** `PivotItem.isHidden` aracılığıyla çoklu seçim filtreleme kullanırken, **en az bir `PivotItem` görünür kalmalıdır** (`isHidden == false`). Her öğe gizlenirse, Excel dosyayı açarken kilitlenir veya boş bir pivot oluşturur. Çoklu seçim beyaz listenizin kaynak verilerinizden en az bir öğe içerdiğini her zaman doğrulayın.

## **Hangi API'yi ve Hangi Modu Kullanmalıyım?**

Aşağıdaki tablo, her senaryoyu ayrıntılı olarak okumadan doğru kombinasyonu seçebilmeniz için her API'nin ve modun ne zaman kullanılacağını özetler.

| Senaryo / Kullanım Durumu | Önerilen API | Kullanılan Özellik | Notlar |
|---|---|---|---|
| Kaynak-sütun adına göre sayfa alanı ekleme (en yaygın) | `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | yok | Üst düzey, tek satır. Bir `PivotField` referansına ihtiyacınız olmadıkça bunu kullanın. |
| Zaten bir `PivotField` nesneniz varken sayfa alanı ekleme | `PivotTable.pageFields.add(PivotField)` | yok | Alan nesnesi başka bir yerden alındığında veya yeniden kullanılması gerektiğinde kullanın. |
| Tek bir sayfa öğesine filtreleme (varsayılan mod) | `PivotField.currentPageItem` | belirli bir dizine ayarla | Örneğin, `1` sıralanmış listedeki ikinci öğeyi gösterir. |
| Tüm öğeleri gösterme / sayfa filtresini temizleme | `PivotField.currentPageItem` | `0x7FFD` değerine ayarla | Sihirli değer olan `0x7FFD` (ondalık 32765), "tüm öğeler" için göstergedir. |
| Excel'de çoklu seçim kullanıcı arayüzünü etkinleştirme | `PivotField.isMultipleItemSelectionAllowed` | `true` olarak ayarla | Herhangi bir `isHidden` çağrısının geçerli olmasından önce gereklidir. |
| Çoklu seçim listesindeki tek tek öğeleri gizleme / gösterme | `PivotItem.isHidden` | öğeye göre ayarla | En az bir öğe görünür kalmalıdır (`isHidden == false`). |

{{% alert color="primary" %}}
Çoklu seçim filtrelemeyi yapılandırırken görünürlük kısıtlamasını her zaman hatırlayın. Çoklu seçim sayfa alanındaki her `PivotItem` gizlenirse, Excel açılırken kilitlenir veya boş bir pivot oluşturur. Beyaz listenizi kaynak verilerinize göre oluşturun, böylece en az bir öğe görünür kalır ve kaydedilen çalışma kitaplarınız her makinede güvenilir şekilde açılır.
{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}