---
title: Aralığı Devrik Çevirme
linktitle: Aralığı Devrik Çevirme
description: Bu makale, Aspose.Cells for .NET kullanarak Excel dosyalarındaki verileri satırlardan sütunlara veya ters yönde devrik çevirme veya döndürme işlemini üç farklı yaklaşımla açıklar.
keywords: Aspose.Cells, .NET kütüphanesi, elektronik tablo, aralığı devrik çevirme, veriyi döndürme, devrik çevirme fonksiyonu, dinamik dizi formülü, dizi formülü, Excel TRANSPOSE, Satırlardan Sütunlara
type: docs
weight: 80
url: /tr/net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for .NET, satırların sütunlara ve sütunların satırlara dönüşecek şekilde verileri devrik çevirmeyi (döndürmeyi) üç farklı şekilde destekler. İlk yaklaşım, yerinde çalışan `Range.Transpose()` yöntemini kullanır ve her Excel sürümünde çalışır; ikincisi, Excel 365 veya Excel 2021'de otomatik olarak dökülen modern bir dinamik dizi `=TRANSPOSE(...)` formülü yazmak için `Cell.SetDynamicArrayFormula()` yöntemini kullanır. Üçüncü yaklaşım ise, eski Excel sürümleriyle uyumlu klasik Ctrl+Shift+Enter (CSE) dizi formülü yazmak için `Cell.SetArrayFormula()` yöntemini kullanır. Bu makale, her yaklaşımı adım adım talimatlar ve eksiksiz kod örnekleri ile anlatır.
{{% /alert %}}

## **Giriş**
Bir aralığı devrik çevirmek, onu döndürmek; yani satır olanın sütun, sütun olanın satır olması ve verilerin esas köşegeni boyunca yansıtılması anlamına gelir. Microsoft Excel'de `TRANSPOSE` çalışma sayfası fonksiyonu bu işlemi gerçekleştirir ve kavramsal referans [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) adresinde belgelenmiştir. Bu konsept, birçok iş ve raporlama senaryosunda faydalı olan bir hücre aralığına programatik olarak uygulanabilir.
- Çeyreklerin normalde sayfa boyunca yatay olarak, bölgelerin ise sayfa boyunca dikey olarak sıralandığı veya bunun tersi olduğu üç aylık veya yıllık satış raporlarını yeniden yönlendirme.
- Gösterge tablolarında veya grafiklerde eksen yönünü değiştirerek zaman serisinin yatay yerine dikey olarak sayfa boyunca ilerlemesini sağlama.
- Dış sistemlerden içe aktarılan verileri, aşağı akış analiz veya raporlama şablonlarının beklediği düzene uyacak şekilde yeniden şekillendirme.
Makalenin geri kalanını somut hale getirmek için her örnek aşağıdaki bölge-çeyrek bazında küçük satış tablosunu kullanır. Örnek çalışma kitabında bu tablo **A1:D5** aralığını kaplar; sol üst köşe olarak **A1** boş bırakılır, **B1:D1** bölge başlıklarını tutar ve **A2:A5** çeyrek başlıklarını tutar.
| Bölge             | Avrupa     | Asya       | Kuzey Amerika  |
|-------------------|-----------|-----------|---------------|
| Ç1. Çeyrek        | 21704714  | 8774099   | 12094215      |
| Ç2. Çeyrek        | 17987034  | 12214447  | 10873099      |
| Ç3. Çeyrek        | 19485029  | 14356879  | 15689543      |
| Ç4. Çeyrek        | 22567894  | 15763492  | 17456723      |
Makale daha sonra Aspose.Cells for .NET kullanarak bu verileri devrik çevirmenin üç farklı yolunu, her biri farklı bir Excel sürümü ve kullanım senaryosuna uygun olacak şekilde sunar.

## **Yaklaşım 1 — Yerinde Aralığı Devrik Çevirme (Range.Transpose)**
`TRANSPOSE` çalışma sayfası fonksiyonunu devreye sokmadan verileri devrik çevirmek istediğinizde bu yaklaşımı kullanın. **Her Excel sürümünde** çalışır ve dinamik dizilere bağımlılığı yoktur; bu da onu en güvenli, sürümler arası uyumlu seçenek yapar. Yalnızca son devrik çıktıya ihtiyacınız olduğunda ve çalışma kitabında orijinal `TRANSPOSE` formülünü tutmanız gerekmediğinde idealdir.

### **Kullanılan API**
`Range.Transpose()`, `Aspose.Cells.Range` sınıfının bir örnek yöntemidir. Çağrıldığında, satırlarını ve sütunlarını değiştirerek aralığı yerinde çevirir; böylece satır olan sütun, sütun olan satır olur. Yöntem, formül yazmadan doğrudan temeldeki hücreleri değiştirir.

### **Adımlar**
1. `LoadOptions` değerini `.xlsx` formatına ayarlayarak `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` çağrısıyla kaynak çalışma kitabını açın.
2. `workbook.Worksheets[0]` kullanarak çalışma kitabından ilk çalışma sayfasını alın.
3. `worksheet.Cells` aracılığıyla çalışma sayfasının hücre koleksiyonuna erişin.
4. `cells.CreateRange("A1:D5")` çağırarak **A1:D5** aralığını kapsayan kaynak aralığı oluşturun.
5. Aralığı yerinde döndürmek, satırları ve sütunları değiştirmek için `source.Transpose()` çağrısını yapın.
6. Çalışma kitabını `workbook.Save(outputFile)` ile kaydedin.
Devrik çevirme sonrasında bu çapa aralığı döndürülmüş verileri tutar. İlk satır (boş, **Avrupa**, **Asya**, **Kuzey Amerika**) şeklinde ve ilk sütun (boş, **Ç1. Çeyrek**, **Ç2. Çeyrek**, **Ç3. Çeyrek**, **Ç4. Çeyrek**) şeklinde okunur. Orijinal her satış sütunu, devrik çevrilmiş aralıkta bir satır haline gelir.

```csharp
using System;
using System.IO;
using Aspose.Cells;
string srcFile = "source.xlsx";
string outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
var source = cells.CreateRange("A1:D5");
source.Transpose();
workbook.Save(outputFile);
```

## **Yaklaşım 2 — Dinamik Dizi Formülü ile Devrik Çevirme (Excel 365 / 2021)**
Çıktı çalışma kitabında `=TRANSPOSE(A1:D5)` formülünü, kaynak veri değişirse sonucun otomatik olarak güncellenmesini sağlayacak canlı bir formül olarak korumak istediğinizde ve hedef Excel dosyası dinamik dizilerin ve dökme operatörünün desteklendiği **Excel 365 / Excel 2021 veya üstü** sürümlerde açılacaksa bu yaklaşımı kullanın.

### **Kullanılan API**
`Cell.SetDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)`, hücrenin formülünü **dinamik dizi formülü** olarak ayarlayan `Aspose.Cells.Cell` üzerinde bir yöntemdir. Excel formülü bir kez değerlendirir ve sonucu otomatik olarak çevreleyen hücrelere döker. `true` olarak ayarlanan üçüncü parametre, Aspose.Cells'e sonuç değerlerini yazma zamanında da hesaplaması talimatını verir.

### **Adımlar**
1. Kaynak çalışma kitabını `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` kullanarak yükleyin.
2. İlk çalışma sayfasını alın ve `Cells` koleksiyonuna erişin.
3. `cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)` çağırarak dinamik dizi formülünü kaynak aralığının hemen altındaki **A6** hücresine yerleştirin.
4. `new FormulaParseOptions()` argümanı varsayılan `FormulaParseOptions` ayarlarını kullanır ve üçüncü argüman olan `true` Aspose.Cells'e formülü dinamik dizi olarak değerlendirmesi ve dökülen değerlerin çalışma kitabına yazılması talimatını verir.
5. Çalışma kitabını `workbook.Save(outputFile)` ile kaydedin.
**A6** hücresi `=TRANSPOSE(A1:D5)` formülünü tutar ve Excel sonucu otomatik olarak devrik çevrilmiş verilere eşit 4 satır ve 5 sütundan oluşan **A6:E9** bölgesine döker.

{{% alert color="primary" %}}
Bu yaklaşım **yalnızca Excel 365 / 2021 veya üstünde** çalışır. Eski Excel sürümleri dinamik dizi formüllerini doğru şekilde dökmez.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
string srcFile = "source.xlsx";
string outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.Save(outFile, SaveFormat.Xlsx);
```

## **Yaklaşım 3 — Klasik Dizi Formülü ile Devrik Çevirme (CSE)**
Çalışma kitabında bir `TRANSPOSE` formülünün korunmasını istediğinizde, ancak hedef Excel dosyası dinamik dizi dökümünün desteklenmediği **eski Excel sürümlerinde (2021 öncesi, 2019, 2016, 2013 vb.)** açılabilecekse bu yaklaşımı kullanın. Klasik CSE (Ctrl+Shift+Enter) dizi formülü, tüm Excel sürümlerinin değerlendirebileceği eski sürümlerle uyumlu alternatiftir.

### **Kullanılan API**
`Cell.SetArrayFormula(string arrayFormula, int nRows, int nColumns)`, çapa hücresine **klasik dizi (CSE) formülü** atayan ve sonuç dizisinin boyutlarını bildiren `Aspose.Cells.Cell` üzerinde bir yöntemdir. Aspose.Cells, Excel'in formülü bildirilen aralığı dolduran tek bir dizi ifadesi olarak değerlendirmesi için çok hücreli dizi formülü işaretçisini yazar.

### **Adımlar**
1. Önceki yaklaşımlarda açıklandığı gibi kaynak çalışma kitabını yükleyin.
2. İlk çalışma sayfasını alın ve `Cells` koleksiyonuna erişin.
3. `cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` çağrısını yapın. İkinci argüman `4` hedef dizinin satır sayısı, üçüncü argüman `5` ise sütun sayısıdır.
4. Çalışma kitabını `workbook.Save(outputFile)` ile kaydedin.
**A6** hücresi dizi formülünün çapasıdır ve değerlendirilen dizi A6'dan başlayarak 4 satır ve 5 sütun boyunca uzanır; bu, A1:D5 kaynağının devrik çevrilmiş boyutlarıyla eşleşir. Excel, sonuç aralığı boyunca tek bir dizi formülü işaretçisi yazar; böylece eski Excel sürümleri onu doğru şekilde değerlendirir.

{{% alert color="primary" %}}
CSE dizi formülleri, `TRANSPOSE` ifadesini değerlendirmenin klasik Excel yoludur ve bu yaklaşım Excel sürümlerinde evrensel olarak uyumludur.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
// Kaynak çalışma kitabını xlsx LoadOptions ile yükle
string srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
// İlk çalışma sayfasına ve Cells koleksiyonuna eriş
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
// A6 hücresinde klasik CSE dizi formülünü ayarla.
// =TRANSPOSE(A1:D5) formülü, 5 satır x 4 sütun kaynak aralığını
// 4 satır x 5 sütunluk bir diziye döndürür. İkinci argüman (4) satır sayısıdır
// ve üçüncü argüman (5) sonuç dizisinin sütun sayısıdır.
// Aspose.Cells, CSE dizi formülü işaretini yazar, böylece Excel bunu
// eski Excel sürümleriyle uyumlu tek bir çok hücreli dizi formülü olarak değerlendirir
// (2019, 2016, 2013 vb.) dinamik dizi yayılımını desteklemez.
cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Dizi formülü işaretinin kalıcı olması için çalışma kitabını kaydet
workbook.Save("output.xlsx");
```

## **Karşılaştırma — Her Yaklaşımı Ne Zaman Kullanmalı**
| Yaklaşım | API / Yöntem | Excel Sürümü | Kaynak formül korunuyor mu? | Çıktı aralığı |
|----------|--------------|---------------|--------------------------|--------------|
| Yaklaşım 1 — Yerinde devrik çevirme | `Range.Transpose()` | Tüm Excel sürümleri | Hayır (yalnızca değerler) | İlk çapa aralığı, 5×4 |
| Yaklaşım 2 — Dinamik dizi formülü | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | Evet (dinamik olarak dökülür) | Çapadan dökülür |
| Yaklaşım 3 — Klasik dizi formülü (CSE) | `Cell.SetArrayFormula` | Tüm Excel sürümleri | Evet (çok hücreli dizi formülü) | Açık boyut, 4×5 |
Hızlı, sürümler arası bir dönüşüme ihtiyaç duyduğunuzda ve dosyaya yalnızca devrik çevrilmiş değerlerin yazılmasını istediğinizde **Yaklaşım 1**'i kullanın. Modern Excel'in garanti olduğu ve formülün canlı kalmasını, kaynak değişirse güncellenmesini istediğinizde **Yaklaşım 2**'yi kullanın. Dinamik dizileri desteklemeyen eski sürümler dahil her Excel sürümünde korunmuş bir formülle en geniş uyumluluğa ihtiyaç duyduğunuzda **Yaklaşım 3**'ü kullanın.

{{< app/cells/assistant language="csharp" >}}