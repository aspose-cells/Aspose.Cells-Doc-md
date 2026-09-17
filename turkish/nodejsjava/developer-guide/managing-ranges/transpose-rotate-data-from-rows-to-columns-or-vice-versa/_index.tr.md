---
title: Aralığı Devrik Çevirme
linktitle: Aralığı Devrik Çevirme
description: Bu makale, Aspose.Cells for Node.js via Java kullanarak Excel dosyalarındaki verileri satırlardan sütunlara veya tersine nasıl devrik çevireceğinizi veya döndüreceğinizi, üç farklı yaklaşımla açıklar.
keywords: Aspose.Cells, Node.js via Java kitaplığı, elektronik tablo, aralığı devrik çevirme, veriyi döndürme, TRANSPOSE işlevi, dinamik dizi formülü, dizi formülü, Excel TRANSPOSE, Satırları Sütunlara
type: docs
weight: 80
url: /tr/nodejs-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java, satırların sütunlara, sütunların satırlara dönüşmesi şeklinde verilerin devrik çevrilmesini (döndürülmesini) üç farklı yöntemle destekler. İlk yaklaşım, yerinde çalışan `Range.transpose()` yöntemini kullanır ve her Excel sürümünde çalışır. İkincisi, Excel 365 veya Excel 2021'de otomatik olarak dökülen modern bir dinamik dizi `=TRANSPOSE(...)` formülü yazmak için `Cell.setDynamicArrayFormula()` kullanır. Üçüncü yaklaşım ise, eski Excel sürümleriyle uyumlu klasik Ctrl+Shift+Enter (CSE) dizi formülünü yazmak için `Cell.setArrayFormula()` kullanır. Bu makale her yaklaşımı adım adım talimatlar ve tam kod örnekleri ile birlikte açıklar.
{{% /alert %}}

## **Introduction**
Bir aralığı devrik çevirmek, onu ana çaprazı boyunca yansıtarak satır olanı sütun, sütun olanı satır yapacak şekilde döndürmek anlamına gelir. Microsoft Excel'de `TRANSPOSE` çalışma sayfası işlevi bu işlemi gerçekleştirir ve kavramsal referans [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) adresinde belgelenmiştir. Bu kavram, bir hücre aralığına programatik olarak uygulanabilir ve birçok iş ve raporlama senaryosunda yararlıdır.
- Çeyreklerin normalde sayfa genelinde, bölgelerin ise sayfa boyunca sıralandığı çeyreklik veya yıllık satış raporlarını yeniden yönlendirmek veya bunun tersini yapmak.
- Gösterge tablolarında veya grafiklerde eksen yönelimini değiştirerek bir zaman serisinin sayfa boyunca değil sayfa genelinde ilerlemesini sağlamak.
- Dış sistemlerden içe aktarılan verileri, aşağı akış analiz veya raporlama şablonlarının beklediği düzene uyacak şekilde yeniden şekillendirmek.
Makalenin geri kalanını somut hale getirmek için her örnek aşağıdaki küçük bölge-çeyrek bazlı satış tablosunu kullanır. Örnek çalışma kitabında bu tablo **A1:D5** aralığını kaplar; **A1** sol üst köşede boş bırakılmıştır, **B1:D1** bölge başlıklarını ve **A2:A5** çeyrek başlıklarını tutar.
| Bölge             | Avrupa   | Asya      | Kuzey Amerika |
|-------------------|----------|----------|---------------|
| Çeyrek 1          | 21704714 | 8774099  | 12094215      |
| Çeyrek 2          | 17987034 | 12214447 | 10873099      |
| Çeyrek 3          | 19485029 | 14356879 | 15689543      |
| Çeyrek 4          | 22567894 | 15763492 | 17456723      |
Makale daha sonra Aspose.Cells for Node.js via Java kullanarak bu verileri devrik çevirmenin üç farklı yolunu sunar; her biri farklı bir Excel sürümüne ve kullanım senaryosuna uygundur.

## **Approach 1 — Transpose Range in Place (Range.transpose)**
`TRANSPOSE` çalışma sayfası işlevini devreye sokmadan verileri devrik çevirmek istediğinizde bu yaklaşımı kullanın. **Excel'in her sürümünde** çalışır ve dinamik dizilere bağımlılığı yoktur, bu da onu sürümler arası en güvenli uyumlu seçenek haline getirir. Yalnızca son devrik çıktıya ihtiyaç duyduğunuzda ve orijinal `TRANSPOSE` formülünü çalışma kitabında tutmanız gerekmediğinde idealdir.

### **API used**
`Range.transpose()`, `com.aspose.cells.Range` sınıfında bir örnek yöntemidir. Çağrıldığında, satırları ve sütunları değiştirerek aralığı yerinde çevirir; böylece satır olan sütun, sütun olan satır olur. Yöntem, formül yazmadan doğrudan temel hücreleri değiştirir.

### **Steps**
1. Kaynak çalışma kitabını `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` çağırarak `LoadOptions` değerinin `.xlsx` biçimine ayarlandığı şekilde açın.
2. `workbook.getWorksheets().get(0)` kullanarak çalışma kitabından ilk çalışma sayfasını alın.
3. `worksheet.getCells()` aracılığıyla çalışma sayfasının hücre koleksiyonuna erişin.
4. `cells.createRange("A1:D5")` çağırarak **A1:D5** aralığını kapsayan kaynak aralığı oluşturun.
5. Satırları ve sütunları yerinde değiştirmek için `source.transpose()` çağırın.
6. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.
Devrik çevirme işleminden sonra ilk başlangıç aralığı döndürülmüş verileri tutar. İlk satır (boş, **Avrupa**, **Asya**, **Kuzey Amerika**) ve ilk sütun (boş, **Çeyrek 1**, **Çeyrek 2**, **Çeyrek 3**, **Çeyrek 4**) olarak okunur. Orijinal her satış sütunu, devrik çevrilmiş aralıkta bir satır haline gelir.

```python
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outputFile = "transposed.xlsx";
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, loadOptions);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
const source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
Çıktı çalışma kitabında `=TRANSPOSE(A1:D5)` formülünü, kaynak veriler değiştiğinde sonucun otomatik olarak güncellenmesini sağlayacak canlı bir formül olarak korumak istediğinizde ve hedef Excel dosyası dinamik dizilerin ve döküm operatörünün desteklendiği **Excel 365 / Excel 2021 veya üzeri** bir sürümde açılacağında bu yaklaşımı kullanın.

### **API used**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)`, `com.aspose.cells.Cell` üzerinde hücrenin formülünü **dinamik dizi formülü** olarak ayarlayan bir yöntemdir. Excel formülü bir kez değerlendirir ve sonucu otomatik olarak çevreleyen hücrelere döker. `true` olarak ayarlanan üçüncü parametre, Aspose.Cells'e yazma zamanında sonuç değerlerini de hesaplamasını söyler.

### **Steps**
1. Kaynak çalışma kitabını `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` kullanarak yükleyin.
2. İlk çalışma sayfasını alın ve `Cells` koleksiyonuna erişin.
3. `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)` çağırarak dinamik dizi formülünü kaynak aralığın hemen altındaki **A6** hücresine yerleştirin.
4. `null` bağımsız değişkeni varsayılan `FormulaParseOptions` değerlerini geçer ve üçüncü bağımsız değişken olan `true`, Aspose.Cells'e formülü dinamik dizi olarak değerlendirmesini ve dökülen değerlerin çalışma kitabına yazılmasını sağlar.
5. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.
**A6** hücresi `=TRANSPOSE(A1:D5)` formülünü tutar ve Excel sonucu otomatik olarak **A6:D10** bölgesine, devrik çevrilmiş verilere eşit 5 satır 4 sütunluk bir bloğa döker.

{{% alert color="primary" %}}
Bu yaklaşım **yalnızca Excel 365 / 2021 veya üzerinde** çalışır. Eski Excel sürümleri dinamik dizi formüllerini doğru şekilde dökmez.
{{% /alert %}}

```python
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
Çalışma kitabında bir `TRANSPOSE` formülünün korunmasını istediğinizde, ancak hedef Excel dosyası dinamik dizi dökmeyi desteklemeyen **eski Excel sürümlerinde (2021 öncesi, 2019, 2016, 2013 ve benzeri)** açılabilecekse bu yaklaşımı kullanın. Klasik CSE (Ctrl+Shift+Enter) dizi formülü, tüm Excel sürümlerinin değerlendirebileceği eski sürümlerle uyumlu alternatiftir.

### **API used**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)`, `com.aspose.cells.Cell` üzerinde başlangıç hücresine **klasik dizi (CSE) formülü** atayan ve sonuç dizisinin boyutlarını bildiren bir yöntemdir. Aspose.Cells çok hücreli dizi formülü işaretini yazar; böylece Excel formülü, bildirilen aralığı dolduran tek bir dizi ifadesi olarak değerlendirir.

### **Steps**
1. Kaynak çalışma kitabını önceki yaklaşımlarda açıklandığı şekilde yükleyin.
2. İlk çalışma sayfasını alın ve `Cells` koleksiyonuna erişin.
3. `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` çağırın. İkinci bağımsız değişken olan `4`, hedef dizinin satır sayısıdır ve üçüncü bağımsız değişken olan `5` sütun sayısıdır.
4. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.
**A6** hücresi dizi formülünün başlangıç noktasıdır ve değerlendirilen dizi, A1:D5 kaynağının devrik çevrilmiş boyutlarıyla eşleşen A6'dan başlayarak 4 satır 5 sütun olarak yayılır. Excel, sonuç aralığı boyunca tek bir dizi formülü işareti yazar; böylece eski Excel sürümleri onu doğru şekilde değerlendirir.

{{% alert color="primary" %}}
CSE dizi formülleri, bir `TRANSPOSE` ifadesini değerlendirmenin klasik Excel yoludur ve bu yaklaşım Excel sürümleri arasında evrensel olarak uyumludur.
{{% /alert %}}

```python
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
| Yaklaşım 1 — Yerinde devrik çevirme | `Range.transpose()` | Tüm Excel sürümleri | Hayır (yalnızca değerler) | İlk başlangıç aralığı, 5×4 |
| Yaklaşım 2 — Dinamik dizi formülü | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Evet (dinamik olarak dökülür) | Başlangıç noktasından dökülür |
| Yaklaşım 3 — Klasik dizi formülü (CSE) | `Cell.setArrayFormula` | Tüm Excel sürümleri | Evet (çok hücreli dizi formülü) | Açık boyut, 4×5 |
Yalnızca devrik çevrilmiş değerlerin dosyaya yazılmasına ihtiyaç duyduğunuz hızlı, sürümler arası bir dönüşüm istediğinizde **Yaklaşım 1**'i kullanın. Modern Excel'in garanti olduğu ve formülün canlı kalmasını, kaynak değiştiğinde güncellenmesini istediğinizde **Yaklaşım 2**'yi kullanın. Dinamik dizileri desteklemeyen eski sürümler dahil her Excel sürümünde korunmuş bir formülle en geniş uyumluluğa ihtiyaç duyduğunuzda **Yaklaşım 3**'ü kullanın.

## **Related Articles**
- [SmartMarker Tek Hücre Dizi Oluşturma | Aspose.Cells for Node.js via Java](/cells/tr/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Bir Hücreye Görsel Ekleme](/cells/tr/nodejs-java/inserting-an-image-into-a-cell/)
- [Excel Dosyalarını Birden Fazla Dosyaya Bölme](/cells/tr/nodejs-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-java" >}}