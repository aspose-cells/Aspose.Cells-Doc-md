---
title: Aralığı Devrik Çevirme
linktitle: Aralığı Devrik Çevirme
description: Bu makale, Aspose.Cells for Node.js via C++ kullanarak Excel dosyalarındaki verileri satırlardan sütunlara veya ters yönde devrik çevirmeyi ya da döndürmeyi üç farklı yaklaşımla açıklar.
keywords: Aspose.Cells, Node.js via C++ kitaplığı, elektronik tablo, aralığı devrik çevirme, veriyi döndürme, devrik çevirme fonksiyonu, dinamik dizi formülü, dizi formülü, Excel TRANSPOSE, Satırlardan Sütunlara
type: docs
weight: 80
url: /tr/nodejs-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++, verilerin satırlardan sütunlara, sütunlardan satırlara dönüştürülmesini (döndürülmesini) üç farklı yöntemle destekler. İlk yaklaşım, yerinde `range.transpose()` yöntemini kullanır ve her Excel sürümünde çalışır; ikincisi ise Excel 365 veya Excel 2021'de otomatik olarak yayılan modern bir dinamik dizi `=TRANSPOSE(...)` formülü yazmak için `cell.setDynamicArrayFormula()` yöntemini kullanır. Üçüncü yaklaşım ise eski Excel sürümleriyle uyumlu klasik bir Ctrl+Shift+Enter (CSE) dizi formülü yazmak için `cell.setArrayFormula()` yöntemini kullanır. Bu makale, her yaklaşımı adım adım talimatlar ve eksiksiz kod örnekleriyle ele alır.
{{% /alert %}}

## **Introduction**
Bir aralığı devrik çevirmek, onu döndürmek, yani satır olanı sütun, sütun olanı satır yapmak ve böylece veriyi esas köşegeni boyunca yansıtmak anlamına gelir. Microsoft Excel'de `TRANSPOSE` çalışma sayfası fonksiyonu bu işlemi gerçekleştirir ve kavramsal referans [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) adresinde belgelenmiştir. Bu kavram, birçok iş ve raporlama senaryosunda faydalı olan, bir hücre aralığına programatik olarak uygulanabilir.
- Çeyreklerin normalde sayfa boyunca, bölgelerin ise sayfa boyunca uzandığı çeyreklik veya yıllık satış raporlarını yeniden yönlendirmek ya da bunun tersini yapmak.
- Pano tablolarında veya grafiklerde, zaman serisinin sayfa boyunca değil sayfa aşağısında ilerlemesi için eksen yönelimini değiştirmek.
- Dış sistemlerden içe aktarılan verileri, aşağı akış analiz veya raporlama şablonlarının beklediği düzene uyacak şekilde yeniden şekillendirmek.
Makalenin geri kalanını somut hale getirmek için, her örnek aşağıdaki bölge-çeyrek bazlı küçük satış tablosunu kullanır. Örnek çalışma kitabında bu tablo **A1:D5** aralığını kaplar; **A1** sol üst köşe olarak boş bırakılır, **B1:D1** bölge başlıklarını, **A2:A5** ise çeyrek başlıklarını içerir.
| Bölge              | Avrupa    | Asya      | Kuzey Amerika |
|--------------------|-----------|-----------|---------------|
| Çeyrek 1           | 21704714  | 8774099   | 12094215      |
| Çeyrek 2           | 17987034  | 12214447  | 10873099      |
| Çeyrek 3           | 19485029  | 14356879  | 15689543      |
| Çeyrek 4           | 22567894  | 15763492  | 17456723      |
Makale daha sonra Aspose.Cells for Node.js via C++ kullanarak bu verileri devrik çevirmenin, her biri farklı bir Excel sürümüne ve kullanım durumuna uygun üç farklı yolunu sunar.

## **Approach 1 — Transpose Range in Place (range.transpose)**
`TRANSPOSE` çalışma sayfası fonksiyonunu devreye sokmadan veriyi devrik çevirmek istediğinizde bu yaklaşımı kullanın. **Her Excel sürümünde** çalışır ve dinamik dizilere bağımlılığı yoktur; bu da onu en güvenli sürümler arası uyumlu seçenek yapar. Yalnızca son devrik çıktıya ihtiyaç duyduğunuzda ve çalışma kitabında orijinal `TRANSPOSE` formülünü korumanız gerekmediğinde idealdir.

### **API used**
`range.transpose()`, `Aspose.Cells.Range` sınıfında bir örnek yöntemidir. Çağrıldığında, aralığı satır ve sütunlarını değiştirerek yerinde çevirir; böylece satır olan sütun, sütun olan satır olur. Yöntem, bir formül yazmadan doğrudan temel hücreleri değiştirir.

### **Steps**
1. `LoadOptions` değerini `.xlsx` biçimine ayarlanmış şekilde kaynak çalışma kitabını `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` çağrısıyla açın.
2. `workbook.getWorksheets().get(0)` kullanarak çalışma kitabından ilk çalışma sayfasını alın.
3. `worksheet.getCells()` aracılığıyla çalışma sayfasının hücre koleksiyonuna erişin.
4. `cells.createRange("A1:D5")` çağırarak **A1:D5** aralığını kapsayan kaynak aralığı oluşturun.
5. Aralığı satır ve sütunları değiştirerek yerinde döndürmek için `source.transpose()` yöntemini çağırın.
6. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.
Devrik çevirme işleminden sonra başlangıçtaki çapa aralığı döndürülmüş veriyi tutar. İlk satır (boş, **Avrupa**, **Asya**, **Kuzey Amerika**) ve ilk sütun (boş, **Çeyrek 1**, **Çeyrek 2**, **Çeyrek 3**, **Çeyrek 4**) olarak okunur. Satışların orijinal her sütunu, devrik çevrilmiş aralıkta bir satır haline gelir.

```javascript
var srcFile = "source.xlsx";
var outputFile = "transposed.xlsx";
var workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
var worksheet = workbook.getWorksheets().get(0);
var cells = worksheet.getCells();
var source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
`=TRANSPOSE(A1:D5)` formülünü çıktı çalışma kitabında canlı bir formül olarak korumak ve böylece kaynak veriler değişirse sonucun otomatik olarak güncellenmesini istediğinizde, hedef Excel dosyasının dinamik dizilerin ve yayılma operatörünün desteklendiği **Excel 365 / Excel 2021 veya üzeri** bir sürümde açılacağı durumlarda bu yaklaşımı kullanın.

### **API used**
`cell.setDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)`, `Aspose.Cells.Cell` üzerinde, hücrenin formülünü **dinamik dizi formülü** olarak ayarlayan bir yöntemdir. Excel formülü bir kez değerlendirir ve sonucu otomatik olarak çevreleyen hücrelere yayar. Üçüncü parametre `true` olarak ayarlandığında, Aspose.Cells'e yazma zamanında sonuç değerlerini de hesaplaması talimatını verir.

### **Steps**
1. Kaynak çalışma kitabını `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` kullanarak yükleyin.
2. İlk çalışma sayfasını alın ve `Cells` koleksiyonuna erişin.
3. `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)` çağırarak kaynak aralığının hemen altındaki **A6** hücresine dinamik dizi formülünü yerleştirin.
4. `null` argümanı varsayılan `FormulaParseOptions` değerini geçer ve üçüncü `true` argümanı Aspose.Cells'e formülü dinamik dizi olarak ele almasını ve yayılan değerlerin çalışma kitabına yazılması için değerlendirmesini söyler.
5. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.
**A6** hücresi `=TRANSPOSE(A1:D5)` formülünü tutar ve Excel sonucu otomatik olarak **A6:D10** bölgesine yayar; bu da devrik çevrilmiş veriye eşdeğer 5 satır ve 4 sütunluk bir bloktur.

{{% alert color="primary" %}}
Bu yaklaşım **yalnızca Excel 365 / 2021 veya üzeri** sürümlerde çalışır. Eski Excel sürümleri dinamik dizi formüllerini doğru şekilde yaymaz.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, opts);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
Çalışma kitabında bir `TRANSPOSE` formülünün korunmasını istediğiniz ancak hedef Excel dosyasının dinamik dizi yayılımının desteklenmediği **eski Excel sürümlerinde (2021 öncesi, 2019, 2016, 2013 vb.)** açılabileceği durumlarda bu yaklaşımı kullanın. Klasik CSE (Ctrl+Shift+Enter) dizi formülü, tüm Excel sürümlerinin değerlendirebileceği eski sürümlerle uyumlu alternatiftir.

### **API used**
`cell.setArrayFormula(string arrayFormula, int nRows, int nColumns)`, `Aspose.Cells.Cell` üzerinde, çapa hücreye **klasik dizi (CSE) formülü** atayan ve sonuç dizisinin boyutlarını belirleyen bir yöntemdir. Aspose.Cells, çok hücreli dizi formülü işaretçisini yazar; böylece Excel formülü, belirtilen aralığı dolduran tek bir dizi ifadesi olarak değerlendirir.

### **Steps**
1. Kaynak çalışma kitabını önceki yaklaşımlarda açıklandığı şekilde yükleyin.
2. İlk çalışma sayfasını alın ve `Cells` koleksiyonuna erişin.
3. `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` çağrısını yapın. İkinci argüman `4` hedef dizinin satır sayısı, üçüncü argüman `5` ise sütun sayısıdır.
4. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.
**A6** hücresi dizi formülünün çapasıdır ve değerlendirilen dizi, A1:D5 kaynağının devrik boyutlarıyla eşleşen şekilde A6'dan başlayarak 4 satır ve 5 sütun olarak yayılır. Excel, sonuç aralığı boyunca tek bir dizi formülü işaretçisi yazar; böylece eski Excel sürümleri onu doğru şekilde değerlendirir.

{{% alert color="primary" %}}
CSE dizi formülleri, `TRANSPOSE` ifadesini değerlendirmenin klasik Excel yoludur ve bu yaklaşım Excel sürümleri arasında evrensel olarak uyumludur.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
// Load the source workbook with xlsx LoadOptions
const srcFile = "source.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
// Access the first worksheet and its Cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Set the classic CSE array formula on cell A6.
// The formula =TRANSPOSE(A1:D5) rotates the 5-row x 4-column source range
// into a 4-row x 5-column array. The second argument (4) is the number of rows
// and the third argument (5) is the number of columns of the resulting array.
// Aspose.Cells writes the CSE array-formula marker so Excel evaluates it as
// a single multi-cell array formula, compatible with older Excel versions
// (2019, 2016, 2013, etc.) that do not support dynamic array spilling.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Save the workbook so the array-formula marker is persisted
workbook.save("output.xlsx");
```

## **Comparison — When to Use Each Approach**
| Yaklaşım | API / Yöntem | Excel Sürümü | Kaynak formül korunuyor mu? | Çıktı aralığı |
|----------|--------------|---------------|----------------------------|---------------|
| Yaklaşım 1 — Yerinde devrik çevirme | `range.transpose()` | Tüm Excel sürümleri | Hayır (yalnızca değerler) | Başlangıç çapa aralığı, 5×4 |
| Yaklaşım 2 — Dinamik dizi formülü | `cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Evet (dinamik olarak yayılır) | Çapadan yayılır |
| Yaklaşım 3 — Klasik dizi formülü (CSE) | `cell.setArrayFormula` | Tüm Excel sürümleri | Evet (çok hücreli dizi formülü) | Açık boyut, 4×5 |
Yalnızca devrik çevrilmiş değerlerin dosyaya yazılmasına ihtiyaç duyduğunuz hızlı, sürümler arası bir dönüşüme ihtiyacınız olduğunda **Yaklaşım 1**'i kullanın. Modern Excel'in garanti olduğu ve formülün canlı kalmasını, kaynak değişirse güncellenmesini istediğiniz durumlarda **Yaklaşım 2**'yi kullanın. Dinamik dizileri desteklemeyen eski sürümler dahil her Excel sürümünde korunan bir formülle en geniş uyumluluğa ihtiyaç duyduğunuzda **Yaklaşım 3**'ü kullanın.

## **Related Articles**
- [SmartMarker Tek Hücreli Dizi Oluşturma](/cells/tr/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Bir Hücreye Resim Ekleme](/cells/tr/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Excel Dosyalarını Birden Çok Dosyaya Bölme](/cells/tr/nodejs-cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}