---
title: Aspose.Cells for .NET'te PivotTable'a filtre alanları ekleme
linktitle: Filtre Alanları Ekleme
description: Aspose.Cells for .NET kullanarak pivot tablolarda filtre alanları eklemeyi ve yapılandırmayı öğrenin, filtre alanı ekleme, tek seçimli filtreleme ve çoklu seçim filtreleme dahil.
keywords: Aspose.Cells, .NET, pivot tablosu, filtre alanı, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /tr/net/add-filter-field-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, pivot tablolardaki filtre alanlarının tüm yaşam döngüsünü destekler. Üst düzey bir kolaylık API'si veya alt düzey `PageFields` koleksiyonu aracılığıyla bir filtre alanı ekleyebilir, filtreni tek seçim modunda yönlendirebilir, her sayfa öğesini göstermek için temizleyebilir veya alanı Excel'deki onay kutusu kullanıcı arayüzü aracılığıyla kullanıcıların aynı anda birkaç sayfa öğesi seçmesine olanak tanıyan çoklu seçime geçirebilirsiniz.
{{% /alert %}}

## **Giriş**

Bir filtre alanı, pivot gövdesinin kaynak verilerin *hangi alt kümesini* görüntüleyeceğini kontrol eden bir pivot alanıdır. Son kullanıcılar bunu Excel'de oluşturulan pivot'un üst kısmında bir açılır menü olarak görür ve kullanılabilir sayfa öğelerinden birini seçmek, pivot gövdesini yalnızca o sayfa öğesine ait kayıtların özetleneceği şekilde yeniden oluşturur. Bir pivot alanı, `PivotFieldType.Row`, `PivotFieldType.Column` veya `PivotFieldType.Data` yerine `PivotFieldType.Page` olarak kaydedildiğinde filtre alanı olur.

Bir filtre alanı iki davranışla çalışabilir. Varsayılan **tek seçim** davranışında aynı anda yalnızca bir sayfa öğesi görünür, böylece pivot gövdesi tam olarak bir alt kümeyi özetler. **Çoklu seçim** davranışında ise alan bir onay kutusu listesi sunar ve pivot gövdesi işaretlenen her sayfa öğesinin birleşimini özetler. Aynı kaynak alan, tek bir özelliği değiştirerek bu davranışlar arasında ileri geri taşınabilir.

Aspose.Cells for .NET, bir filtre alanı kaydetmek için iki eşdeğer yol sunar. Üst düzey API, kaynak sütun adını alan ve alanı tek bir çağrıyla ekleyen `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` yöntemidir. Alt düzey API ise zaten bir `PivotField` referansına sahip olduğunuzda ve aynı alan örneğini filtre alanına eklemek istediğinizde kullanılan `PivotTable.PageFields.Add(PivotField)` yöntemidir. Her iki API de aynı `PageFields` koleksiyonunu doldurur ve bu makalenin geri kalanı aralarında nasıl seçim yapılacağını ve her filtreleme modunun nasıl yönlendirileceğini gösterir.

## **filtre alanı Ekleme**

filtre alanına bir pivot alanı kaydetmenin iki yolu vardır. Üst düzey çağrı, kaynak sütun adını bir dize olarak alır ve en yaygın yoldur. Alt düzey çağrı, mevcut bir `PivotField` örneğini kabul eder ve aynı alan nesnesinin birden çok pivot alanında yeniden kullanılması gerektiğinde kullanışlıdır. Her iki çağrı da alanı `PivotTable.PageFields` içine yerleştirir; bundan sonra oluşturulan pivot'un üst kısmında sayfa açılır menüsü olarak görünür.

### AddFieldToArea ile filtre alanı Ekleme

Aşağıdaki örnek, küçük bir Fruit / Year / Amount veri kümesi oluşturur, E3 hücresine bir pivot tablo yerleştirir; satır alanında `Fruit`, veri alanında `Amount` ve filtre alanında `Year` bulunur, pivot'u yeniler ve çalışma kitabını kaydeder.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Yeni bir çalışma kitabı oluştur
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// Başlık satırını ayarla
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 9 satır örnek veri doldur: Meyve, Yıl, Miktar
object[,] data = new object[,]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    worksheet.Cells[i + 1, 0].PutValue(data[i, 0]);
    worksheet.Cells[i + 1, 1].PutValue(data[i, 1]);
    worksheet.Cells[i + 1, 2].PutValue(data[i, 2]);
}

// E3 hücresine bağlı bir özet tablo ekle
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Alanları kendi alanlarına ekle: Meyve Satır olarak, Miktar Veri olarak, Yıl Sayfa alanı olarak
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// Özet tablo verilerini yenile ve hesapla
pivotTable.RefreshData();
pivotTable.CalculateData();

// Çalışma kitabını kaydet
workbook.Save("pageFieldSample.xlsx");
```

### PageFields.Add ile filtre alanı Ekleme

Zaten bir `PivotField` örneğiyle çalışırken, onu doğrudan `PivotTable.PageFields.Add` yöntemine geçirebilirsiniz. Pivot tablo ve filtre alanı, önceki senaryoda olduğu gibi tam olarak oluşturulur; yalnızca son filtre alanı kaydı alt düzey API çağrısıyla değiştirilir.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — Pivot tablosu ve sayfa alanı tam olarak Senaryo 1a'daki gibi oluşturulur
//   (Meyve/Yıl/Tutar verileri, pivot E3'te, Meyve→Satır, Tutar→Veri).
//   Aşağıda Yıl PivotField'ını BaseFields koleksiyonundan alıp
//   PageFields.Add'a geçiriyoruz — AddFieldToArea'nın düşük seviyeli
//   alternatifidir. Sonuç, Senaryo 1a ile işlevsel olarak aynıdır.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// Başlıklar
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

// Örnek veri (9 satır)
sheet.Cells["A2"].PutValue("apple");    sheet.Cells["B2"].PutValue("2020"); sheet.Cells["C2"].PutValue(100);
sheet.Cells["A3"].PutValue("apple");    sheet.Cells["B3"].PutValue("2021"); sheet.Cells["C3"].PutValue(150);
sheet.Cells["A4"].PutValue("apple");    sheet.Cells["B4"].PutValue("2022"); sheet.Cells["C4"].PutValue(200);
sheet.Cells["A5"].PutValue("grape");    sheet.Cells["B5"].PutValue("2020"); sheet.Cells["C5"].PutValue(300);
sheet.Cells["A6"].PutValue("grape");    sheet.Cells["B6"].PutValue("2021"); sheet.Cells["C6"].PutValue(400);
sheet.Cells["A7"].PutValue("grape");    sheet.Cells["B7"].PutValue("2022"); sheet.Cells["C7"].PutValue(500);
sheet.Cells["A8"].PutValue("blueberry"); sheet.Cells["B8"].PutValue("2020"); sheet.Cells["C8"].PutValue(250);
sheet.Cells["A9"].PutValue("blueberry"); sheet.Cells["B9"].PutValue("2021"); sheet.Cells["C9"].PutValue(350);
sheet.Cells["A10"].PutValue("blueberry");sheet.Cells["B10"].PutValue("2022"); sheet.Cells["C10"].PutValue(450);

// A1:C10 aralığını kapsayacak şekilde E3'e pivot tablo ekle
int pivotIndex = sheet.PivotTables.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// Meyve -> Satır, Tutar -> Veri (Yıl aşağıda Sayfa'ya gidecek)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Düşük seviyeli yaklaşım: mevcut Yıl PivotField'ını BaseFields'dan alın
// ve PageFields.Add(PivotField) aracılığıyla Sayfa alanına kaydedin.
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);

// Yeni sayfa alanının kaydedilen çalışma kitabına yansıtılması için yenileyin
pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **Tek Seçim Filtreleme (Bir Sayfa Öğesi Gösterme)**

Varsayılan tek seçim davranışında filtre alanı tek bir açılır menü olarak işlenir ve `PivotField.CurrentPageItem` tamsayısı, hangi sayfa öğesinin pivot gövdesini yönlendireceğini seçer. Belirli bir dizin atamak o öğeyi seçer; özel bekçi değeri olan `0x7FFD` (ondalık 32765) atamak filtreyi temizler, böylece her sayfa öğesi aynı anda özetlenir. Tek seçim varsayılandır; açıkça etkinleştirmeniz gerekmez.

### Tüm Öğeleri Gösterme

`CurrentPageItem` değerini sihirli değer olan `0x7FFD` olarak ayarlamak, filtreni temizlemeye eşdeğerdir: pivot gövdesi, hiçbir filtre uygulanmamış gibi her sayfa öğesini özetler.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

class Program
{
    static void Main()
    {
        // Yeni bir çalışma kitabı oluştur
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];

        // Fruit/Year/Amount verilerini doldur
        sheet.Cells["A1"].PutValue("Fruit");
        sheet.Cells["B1"].PutValue("Year");
        sheet.Cells["C1"].PutValue("Amount");

        object[,] data = new object[,]
        {
            {"Apple", 2022, 100},
            {"Apple", 2023, 150},
            {"Banana", 2022, 80},
            {"Banana", 2023, 120},
            {"Cherry", 2022, 200},
            {"Cherry", 2023, 250}
        };

        for (int r = 0; r < data.GetLength(0); r++)
        {
            for (int c = 0; c < data.GetLength(1); c++)
            {
                sheet.Cells[r + 1, c].PutValue(data[r, c]);
            }
        }

        // E3 konumunda pivot tablo oluştur
        var pivotTables = sheet.PivotTables;
        int index = pivotTables.Add("=A1:C7", "E3", "PivotTable1");
        PivotTable pivotTable = pivotTables[index];

        // Pivot alanlarını yapılandır: Fruit→Satır, Amount→Veri, Year→Sayfa
        pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
        pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
        pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

        pivotTable.RefreshData();
        pivotTable.CalculateData();

        // Sayfa filtresini temizle, böylece sayfa alanındaki her öğe görünür olsun.
        // 0x7FFD (ondalık 32765), "tüm öğeler" anlamına gelen özel sentinel değeridir —
        // Excel'in sayfa alanı açılır menüsünde "(Tümü)" seçmeye eşdeğerdir.
        pivotTable.PageFields[0].CurrentPageItem = 0x7FFD;

        workbook.Save("output.xlsx");
    }
}
```

### Belirli Bir Öğeyi Gösterme

`CurrentPageItem` değerini gerçek bir dizine ayarlamak yalnızca o sayfa öğesini seçer. Dizin, filtre alanının sıralanmış öğe listesindeki öğenin konumudur; örneğin `1` sıralamadan sonra ikinci öğeyi seçer.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Çalışma kitabı oluştur
var workbook = new Workbook();
var sheet = workbook.Worksheets[0];
var cells = sheet.Cells;

// Örnek veri ekle (Meyve/Yıl/Tutar)
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");

cells["A2"].PutValue("Apple");
cells["B2"].PutValue("2020");
cells["C2"].PutValue("100");

cells["A3"].PutValue("Apple");
cells["B3"].PutValue("2021");
cells["C3"].PutValue("150");

cells["A4"].PutValue("Banana");
cells["B4"].PutValue("2020");
cells["C4"].PutValue("200");

cells["A5"].PutValue("Banana");
cells["B5"].PutValue("2021");
cells["C5"].PutValue("250");

// E3'e pivot tablo ekle
var pivotTables = sheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables[pivotIndex];

// Alanları ekle: Meyve→Satır, Tutar→Veri, Yıl→Sayfa
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// Sayfa alanına özel işlemler
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = sıralı düzende ikinci öğe (ör. "2021")

// Pivot tabloyu yenile ve hesapla
pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **Çoklu Seçim Filtreleme**

Çoklu seçim filtreleme, sayfa açılır menüsünü bir onay kutusu listesine dönüştürür ve son kullanıcının aynı anda birkaç sayfa öğesi seçmesine olanak tanır. Aspose.Cells, birlikte çalışan iki özellik sunar. `PivotField.IsMultipleItemSelectionAllowed` değeri, çoklu seçim kullanıcı arayüzünün etkili olmasından önce `true` olarak ayarlanmalıdır. Etkinleştirildikten sonra, `PivotItem.IsHidden` onay kutusu listesinde hangi öğelerin görüneceğini kontrol eder; böylece her öğeyi gösterebilir veya yalnızca belirli öğeleri beyaz listeye alabilirsiniz.

Aşağıdaki kod, Senaryo 1a'da oluşturulan aynı Year filtre alanında çoklu seçimi etkinleştirir ve ardından iki kalıp gösterir: Bölüm A, her giriş için `IsHidden` değerini `false` bırakarak her sayfa öğesini ortaya çıkarırken, Bölüm B yalnızca seçtiğiniz kaynak değerleri beyaz listeye alır ve diğer her şeyi `switch (pivotItems[i].GetStringValue())` bloğu aracılığıyla gizler.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — Pivot tablosu ve sayfa alanı tam olarak şu şekilde oluşturulur
//   Senaryo 1a'da olduğu gibi (Fruit/Year/Amount verileri, E3'te pivot, Fruit→Satır,
//   Amount→Veri, Year→Sayfa AddFieldToArea aracılığıyla).
//   Aşağıda sayfa alanına çoklu seçim filtreleme uyguluyoruz.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;

// Örnek veri: Fruit | Year | Amount
cells[0, 0].PutValue("Fruit");
cells[0, 1].PutValue("Year");
cells[0, 2].PutValue("Amount");

string[,] data = new string[,]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    cells[i + 1, 0].PutValue(data[i, 0]);
    cells[i + 1, 1].PutValue(Convert.ToInt32(data[i, 1]));
    cells[i + 1, 2].PutValue(Convert.ToInt32(data[i, 2]));
}

Worksheet pivotSheet = workbook.Worksheets.Add("Pivot");
PivotTableCollection pivots = pivotSheet.PivotTables;
int pivotIndex = pivots.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = pivots[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// — Sayfa alanında çoklu seçimi etkinleştir
pivotTable.PageFields[0].IsMultipleItemSelectionAllowed = true;

// Bölüm A — TÜM öğeleri seç (her öğeyi görünür yap)
PivotItemCollection pivotItems = pivotTable.PageFields[0].PivotItems;
for (int i = 0; i < pivotItems.Count; i++)
{
    pivotItems[i].IsHidden = false;
}

// Bölüm B — yalnızca kaynak değere göre belirli öğeleri seç
for (int i = 0; i < pivotItems.Count; i++)
{
    switch (pivotItems[i].GetStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems[i].IsHidden = false;
            break;
        default:
            pivotItems[i].IsHidden = true;
            break;
    }
}

pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

> **Not:** `PivotItem.IsHidden` aracılığıyla çoklu seçim filtreleme kullanırken, **en az bir `PivotItem` görünür kalmalıdır** (`IsHidden == false`). Her öğe gizlenmişse, Excel dosyayı açarken ya çöker ya da boş bir pivot oluşturur. Çoklu seçim beyaz listenizin kaynak verilerinizden en az bir öğe içerdiğini her zaman doğrulayın.

## **Hangi API'yi ve Hangi Modu Kullanmalıyım?**

Aşağıdaki tablo, her senaryoyu ayrıntılı olarak okumadan doğru kombinasyonu seçebilmeniz için her API'nin ve modun ne zaman kullanılacağını özetler.

| Senaryo / Kullanım Durumu | Önerilen API | Kullanılan Özellik | Notlar |
|---|---|---|---|
| Kaynak sütun adına göre filtre alanı ekleme (en yaygın) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Üst düzey, tek satır. Bir `PivotField` referansına ihtiyacınız yoksa bunu kullanın. |
| Zaten bir `PivotField` nesneniz olduğunda filtre alanı ekleme | `PivotTable.PageFields.Add(PivotField)` | n/a | Alan nesnesi başka bir yerden alındığında veya yeniden kullanılması gerektiğinde kullanın. |
| Tek bir sayfa öğesine filtreleme (varsayılan mod) | `PivotField.CurrentPageItem` | belirli bir dizine ayarla | Örneğin, `1` sıralanmış listedeki ikinci öğeyi gösterir. |
| Tüm öğeleri gösterme / filtreni temizleme | `PivotField.CurrentPageItem` | `0x7FFD` olarak ayarla | Sihirli değer `0x7FFD` (ondalık 32765), "tüm öğeler" için bekçi değeridir. |
| Excel'de çoklu seçim kullanıcı arayüzünü etkinleştirme | `PivotField.IsMultipleItemSelectionAllowed` | `true` olarak ayarla | Herhangi bir `IsHidden` çağrısının etkili olmasından önce gereklidir. |
| Çoklu seçim listesinde tek tek öğeleri gizleme / gösterme | `PivotItem.IsHidden` | öğe bazında ayarla | En az bir öğe görünür kalmalıdır (`IsHidden == false`). |

{{% alert color="primary" %}}
Çoklu seçim filtrelemeyi yapılandırırken görünürlük kısıtlamasını her zaman hatırlayın. Çoklu seçim filtre alanındaki her `PivotItem` gizlenmişse, Excel açılırken çöker veya boş bir pivot oluşturur. Beyaz listenizi kaynak verilerinize göre oluşturun, böylece en az bir öğe görünür kalır ve kaydedilen çalışma kitaplarınız her makinede güvenilir şekilde açılır.
{{% /alert %}}



{{< app/cells/assistant language="csharp" >}}