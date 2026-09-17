---
title: Aralığı Devrik Çevirme
linktitle: Aralığı Devrik Çevirme
description: Bu makale, Aspose.Cells for Java kullanarak Excel dosyalarında satırlardan sütunlara veya tam tersine verileri devrik çevirmeyi veya döndürmeyi, üç farklı yaklaşımla açıklamaktadır.
keywords: Aspose.Cells, Java kütüphanesi, elektronik tablo, aralığı devrik çevirme, veriyi döndürme, devrik çevirme fonksiyonu, dinamik dizi formülü, dizi formülü, Excel TRANSPOSE, Satırlardan Sütunlara
type: docs
weight: 80
url: /tr/java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Java, satırları sütunlara ve sütunları satırlara dönüştürerek verileri devrik çevirmeyi (döndürmeyi) üç farklı şekilde destekler. İlk yaklaşım, yerinde `Range.transpose()` yöntemini kullanır ve her Excel sürümünde çalışır, ikincisi ise Excel 365 veya Excel 2021'de otomatik olarak yayılan modern dinamik dizi `=TRANSPOSE(...)` formülü yazmak için `Cell.setDynamicArrayFormula()` kullanır. Üçüncü yaklaşım, eski Excel sürümleriyle uyumlu klasik Ctrl+Shift+Enter (CSE) dizi formülü yazmak için `Cell.setArrayFormula()` kullanır. Bu makale, her yaklaşımı adım adım talimatlar ve eksiksiz kod örnekleriyle anlatmaktadır.
{{% /alert %}}

## **Introduction**
Bir aralığı devrik çevirmek, onu ana çaprazı boyunca yansıtacak şekilde döndürmek anlamına gelir; böylece bir satır olan şey bir sütun, bir sütun olan şey de bir satır haline gelir. Microsoft Excel'de `TRANSPOSE` çalışma sayfası fonksiyonu bu işlemi gerçekleştirir ve kavramsal referans [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) adresinde belgelenmiştir. Bu konsept, birçok iş ve raporlama senaryosunda faydalı olan, bir hücre aralığına programatik olarak uygulanabilir.
- Çeyreklerin normalde sayfa boyunca, bölgelerin ise sayfa boyunca aşağıya doğru sıralandığı (ya da tam tersi) çeyreklik veya yıllık satış raporlarını yeniden yönlendirme.
- Gösterge tablolarında veya grafiklerde eksen yönünü, bir zaman serisinin sayfa boyunca değil aşağıya doğru ilerlemesini sağlayacak şekilde değiştirme.
- Harici sistemlerden içe aktarılan verileri, aşağı akış analiz veya raporlama şablonlarının beklediği düzene uyacak şekilde yeniden şekillendirme.
Makalenin geri kalanını somut hale getirmek için her örnek, aşağıdaki küçük bölgeye göre çeyrek satış tablosunu kullanır. Örnek çalışma kitabında bu tablo **A1:D5** aralığını kaplar; **A1** sol üst köşede boş bırakılır, **B1:D1** bölge başlıklarını, **A2:A5** ise çeyrek başlıklarını tutar.
| Bölge             | Avrupa    | Asya      | Kuzey Amerika |
|-------------------|-----------|-----------|---------------|
| Ç1.Çeyrek         | 21704714  | 8774099   | 12094215      |
| Ç2.Çeyrek         | 17987034  | 12214447  | 10873099      |
| Ç3.Çeyrek         | 19485029  | 14356879  | 15689543      |
| Ç4.Çeyrek         | 22567894  | 15763492  | 17456723      |
Makale daha sonra Aspose.Cells for Java kullanarak bu verileri devrik çevirmenin üç farklı yolunu sunar; her biri farklı bir Excel sürümüne ve kullanım senaryosuna uygundur.

## **Approach 1 — Transpose Range in Place (Range.transpose)**
`TRANSPOSE` çalışma sayfası fonksiyonunu kullanmadan verileri devrik çevirmek istediğinizde bu yaklaşımı kullanın. **Excel'in her sürümünde** çalışır ve dinamik dizilere bağımlılığı yoktur; bu da onu sürümler arası en güvenli uyumlu seçenek haline getirir. Yalnızca son devrik çıktıya ihtiyaç duyduğunuzda ve çalışma kitabında orijinal `TRANSPOSE` formülünü saklamanız gerekmediğinde idealdir.

### **API used**
`Range.transpose()`, `com.aspose.cells.Range` sınıfında bir örnek yöntemidir. Çağrıldığında, satırlarını ve sütunlarını değiştirerek aralığı yerinde çevirir; böylece bir satır olan şey bir sütun, bir sütun olan şey de bir satır haline gelir. Yöntem, formül yazmadan doğrudan temel hücreleri değiştirir.

### **Steps**
1. `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` çağırarak kaynak çalışma kitabını `.xlsx` formatına ayarlanmış `LoadOptions` ile açın.
2. `workbook.getWorksheets().get(0)` kullanarak çalışma kitabından ilk çalışma sayfasını alın.
3. `worksheet.getCells()` aracılığıyla çalışma sayfasının hücre koleksiyonuna erişin.
4. `cells.createRange("A1:D5")` çağırarak **A1:D5** aralığını kapsayan kaynak aralığı oluşturun.
5. Satırları ve sütunları yerinde döndürmek için `source.transpose()` çağırın.
6. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.
Devrik çevirme işleminden sonra ilk başlangıç aralığı döndürülmüş veriyi tutar. İlk satır (boş, **Avrupa**, **Asya**, **Kuzey Amerika**) şeklinde, ilk sütun ise (boş, **Ç1.Çeyrek**, **Ç2.Çeyrek**, **Ç3.Çeyrek**, **Ç4.Çeyrek**) şeklinde okunur. Satışların orijinal sütunlarının her biri devrik çevrilmiş aralıkta bir satır haline gelir.

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
source.transpose();
workbook.save(outputFile);
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
Çıktı çalışma kitabında `=TRANSPOSE(A1:D5)` formülünü, kaynak veri değişirse sonucun otomatik olarak güncelleneceği canlı bir formül olarak korumak istediğinizde ve hedef Excel dosyası dinamik dizilerin ve yayılma operatörünün desteklendiği **Excel 365 / Excel 2021 veya üstü** sürümlerde açılacaksa bu yaklaşımı kullanın.

### **API used**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)`, `com.aspose.cells.Cell` üzerinde, hücrenin formülünü **dinamik dizi formülü** olarak ayarlayan bir yöntemdir. Excel, formülü bir kez değerlendirir ve sonucu otomatik olarak çevreleyen hücrelere yayar. `true` olarak ayarlanan üçüncü parametre, Aspose.Cells'e yazma zamanında sonuç değerlerini de hesaplaması talimatını verir.

### **Steps**
1. Kaynak çalışma kitabını `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` kullanarak yükleyin.
2. İlk çalışma sayfasını alın ve `Cells` koleksiyonuna erişin.
3. `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)` çağırarak dinamik dizi formülünü, kaynak aralığın hemen altına **A6** hücresine yerleştirin.
4. `null` argümanı varsayılan `FormulaParseOptions` değerlerini geçer ve üçüncü `true` argümanı, Aspose.Cells'e formülü dinamik dizi olarak değerlendirmesini ve yayılan değerlerin çalışma kitabına yazılmasını sağlar.
5. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.
**A6** hücresi `=TRANSPOSE(A1:D5)` formülünü tutar ve Excel sonucu otomatik olarak **A6:D10** bölgesine, devrik çevrilmiş verilere eşit 5 satır ve 4 sütunluk bir bloğa yayar.

{{% alert color="primary" %}}
Bu yaklaşım **yalnızca Excel 365 / 2021 veya üstünde** çalışır. Eski Excel sürümleri dinamik dizi formüllerini doğru şekilde yaymaz.
{{% /alert %}}

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.save(outFile, SaveFormat.XLSX);
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
Çalışma kitabında bir `TRANSPOSE` formülünün korunmasını istediğinizde, ancak hedef Excel dosyası dinamik dizi yayılımının desteklenmediği **eski Excel sürümlerinde (2021 öncesi, 2019, 2016, 2013 vb.)** açılabilecekse bu yaklaşımı kullanın. Klasik CSE (Ctrl+Shift+Enter) dizi formülü, tüm Excel sürümlerinin değerlendirebileceği eski sürümlerle uyumlu alternatiftir.

### **API used**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)`, `com.aspose.cells.Cell` üzerinde, **klasik dizi (CSE) formülünü** başlangıç hücresine atayan ve sonuç dizisinin boyutlarını bildiren bir yöntemdir. Aspose.Cells, çok hücreli dizi formülü işaretçisini yazar; böylece Excel formülü, belirtilen aralığı dolduran tek bir dizi ifadesi olarak değerlendirir.

### **Steps**
1. Kaynak çalışma kitabını önceki yaklaşımlarda açıklandığı şekilde yükleyin.
2. İlk çalışma sayfasını alın ve `Cells` koleksiyonuna erişin.
3. `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` çağırın. İkinci argüman `4`, hedef dizinin satır sayısı, üçüncü argüman `5` ise sütun sayısıdır.
4. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.
**A6** hücresi dizi formülünün başlangıç noktasıdır ve değerlendirilen dizi, A1:D5 kaynağının devrik boyutlarıyla eşleşecek şekilde A6'dan başlayarak 4 satır ve 5 sütun boyunca uzanır. Excel, sonuç aralığına tek bir dizi formülü işaretçisi yazar; böylece eski Excel sürümleri de onu doğru şekilde değerlendirir.

{{% alert color="primary" %}}
CSE dizi formülleri, bir `TRANSPOSE` ifadesini değerlendirmenin klasik Excel yoludur ve bu yaklaşım Excel sürümleri arasında evrensel olarak uyumludur.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Kaynak çalışma kitabını xlsx LoadOptions ile yükle
String srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
// İlk çalışma sayfasına ve onun Cells koleksiyonuna eriş
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
// A6 hücresine klasik CSE dizi formülünü ayarla.
// =TRANSPOSE(A1:D5) formülü, 5 satır x 4 sütunluk kaynak aralığını
// 4 satır x 5 sütunluk bir diziye dönüştürür. İkinci argüman (4) sonuçtaki
// dizinin satır sayısı, üçüncü argüman (5) ise sütun sayısıdır.
// Aspose.Cells, CSE dizi formülü işaretini yazar; böylece Excel bunu
// dinamik dizi taşmasını desteklemeyen eski Excel sürümleriyle (2019, 2016,
// 2013 vb.) uyumlu, tek bir çok hücreli dizi formülü olarak değerlendirir.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Çalışma kitabını kaydet, böylece dizi formülü işareti kalıcı hale gelir
workbook.save("output.xlsx");
```

## **Comparison — When to Use Each Approach**
| Yaklaşım | API / Yöntem | Excel Sürümü | Kaynak formül korunuyor mu? | Çıktı aralığı |
|----------|--------------|---------------|--------------------------|--------------|
| Yaklaşım 1 — Yerinde devrik çevirme | `Range.transpose()` | Tüm Excel sürümleri | Hayır (yalnızca değerler) | İlk başlangıç aralığı, 5×4 |
| Yaklaşım 2 — Dinamik dizi formülü | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Evet (dinamik olarak yayılır) | Başlangıç noktasından yayılır |
| Yaklaşım 3 — Klasik dizi formülü (CSE) | `Cell.setArrayFormula` | Tüm Excel sürümleri | Evet (çok hücreli dizi formülü) | Açık boyut, 4×5 |
Hızlı, sürümler arası uyumlu bir dönüşüme ihtiyaç duyduğunuzda ve yalnızca devrik çevrilmiş değerlerin dosyaya yazılmasını istediğinizde **Yaklaşım 1'i** kullanın. Modern Excel'in garanti olduğu ve formülün canlı kalmasını, kaynak değişirse güncellenmesini istediğinizde **Yaklaşım 2'yi** kullanın. Dinamik dizileri desteklemeyen eski sürümler dahil her Excel sürümünde korunan bir formülle en geniş uyumluluğa ihtiyaç duyduğunuzda **Yaklaşım 3'ü** kullanın.

## **Related Articles**
- [SmartMarker Tek Hücreli Dizi Oluşturma | Aspose.Cells Java](/cells/tr/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Hücreye Resim Ekleme](/cells/tr/java/inserting-an-image-into-a-cell/)
- [Excel Dosyalarını Birden Fazla Dosyaya Bölme](/cells/tr/java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="java" >}}