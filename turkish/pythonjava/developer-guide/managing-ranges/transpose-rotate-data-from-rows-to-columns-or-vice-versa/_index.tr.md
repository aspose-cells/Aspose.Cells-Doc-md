---
title: Aralığı Transpoze Etme
linktitle: Aralığı Transpoze Etme
description: Bu makale, Aspose.Cells for Python via Java kullanarak Excel dosyalarında satırlardan sütunlara veya tam tersi yönde verileri üç farklı yaklaşımla nasıl transpoze edeceğinizi veya döndüreceğinizi açıklar.
keywords: Aspose.Cells, Python via Java kütüphanesi, elektronik tablo, aralık transpoze etme, veri döndürme, transpoze fonksiyonu, dinamik dizi formülü, dizi formülü, Excel TRANSPOSE, Satırlardan Sütunlara
type: docs
weight: 80
url: /tr/python-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via Java, verileri satırları sütunlara, sütunları satırlara dönüştürecek şekilde transpoze etmeyi (döndürmeyi) üç farklı yolla destekler. İlk yaklaşım, yerinde `Range.transpose()` yöntemini kullanır ve her Excel sürümünde çalışır; ikincisi, Excel 365 veya Excel 2021'de otomatik olarak taşan modern bir dinamik dizi `=TRANSPOSE(...)` formülü yazmak için `Cell.setDynamicArrayFormula()` kullanır. Üçüncü yaklaşım ise eski Excel sürümleriyle uyumlu klasik Ctrl+Shift+Enter (CSE) dizi formülü yazmak için `Cell.setArrayFormula()` kullanır. Bu makale, her yaklaşımı adım adım talimatlar ve eksiksiz kod örnekleriyle açıklar.
{{% /alert %}}

## **Introduction**
Bir aralığı transpoze etmek, onu döndürmek anlamına gelir; böylece satır olan sütun, sütun olan satır olur ve veri esas çaprazı boyunca yansıtılır. Microsoft Excel'de `TRANSPOSE` çalışma sayfası fonksiyonu bu işlemi gerçekleştirir ve kavramsal referans [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) adresinde belgelenmiştir. Bu kavram, birçok iş ve raporlama senaryosunda faydalı olan bir hücre aralığına programatik olarak uygulanabilir.
- Çeyreklerin normalde sayfa genelinde, bölgelerin ise sayfa boyunca sıralandığı üç aylık veya yıllık satış raporlarını yeniden yönlendirmek veya bunun tersini yapmak.
- Gösterge panolarında veya grafiklerde eksen yönünü değiştirerek zaman serisinin sayfa genelinde değil sayfa boyunca akmasını sağlamak.
- Dış sistemlerden içe aktarılan verileri, aşağı akış analiz veya raporlama şablonlarının beklediği düzene uyacak şekilde yeniden şekillendirmek.
Makalenin geri kalanını somut hale getirmek için her örnek aşağıdaki küçük bölge-çeyrek bazında satış tablosunu kullanır. Örnek çalışma kitabında bu tablo **A1:D5** aralığını kaplar; sol üst köşe olarak **A1** boş bırakılır, **B1:D1** bölge başlıklarını, **A2:A5** ise çeyrek başlıklarını tutar.
| Bölge             | Avrupa    | Asya      | Kuzey Amerika |
|-------------------|-----------|-----------|---------------|
| 1. Çeyrek         | 21704714  | 8774099   | 12094215      |
| 2. Çeyrek         | 17987034  | 12214447  | 10873099      |
| 3. Çeyrek         | 19485029  | 14356879  | 15689543      |
| 4. Çeyrek         | 22567894  | 15763492  | 17456723      |
Makale daha sonra Aspose.Cells for Python via Java kullanarak bu verileri transpoze etmenin, her biri farklı bir Excel sürümüne ve kullanım senaryosuna uygun üç farklı yolunu sunar.

## **Approach 1 — Transpose Range in Place (Range.transpose)**
`TRANSPOSE` çalışma sayfası fonksiyonunu kullanmadan veriyi transpoze etmek istediğinizde bu yaklaşımı kullanın. **Her Excel sürümünde** çalışır ve dinamik dizilere bağımlılığı yoktur; bu da onu en güvenli sürümler arası uyumlu seçenek yapar. Yalnızca son transpoze edilmiş çıktıya ihtiyacınız olduğunda ve çalışma kitabında orijinal `TRANSPOSE` formülünü saklamanız gerekmediğinde idealdir.

### **API used**
`Range.transpose()`, `com.aspose.cells.Range` sınıfının bir örnek yöntemidir. Çağrıldığında, satırlarını ve sütunlarını değiştirerek aralığı yerinde çevirir; böylece satır olan sütun, sütun olan satır olur. Yöntem, formül yazmadan doğrudan temel hücreleri değiştirir.

### **Steps**
1. Kaynak çalışma kitabını `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))` çağrısıyla `.xlsx` biçimine ayarlanmış `LoadOptions` ile açın.
2. `workbook.getWorksheets().get(0)` kullanarak çalışma kitabından ilk çalışma sayfasını alın.
3. `worksheet.getCells()` aracılığıyla çalışma sayfasının hücre koleksiyonuna erişin.
4. `cells.createRange("A1:D5")` çağırarak **A1:D5** aralığını kapsayan kaynak aralığı oluşturun.
5. Aralığı yerinde döndürmek ve satırlarla sütunları değiştirmek için `source.transpose()` çağırın.
6. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.
Transpoze işleminden sonra başlangıç çapa aralığı, döndürülmüş verileri tutar. İlk satır (boş, **Avrupa**, **Asya**, **Kuzey Amerika**) ve ilk sütun (boş, **1. Çeyrek**, **2. Çeyrek**, **3. Çeyrek**, **4. Çeyrek**) şeklinde okunur. Orijinal her satış sütunu, transpoze edilmiş aralıkta bir satır haline gelir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, LoadOptions, LoadFormat
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
loadOptions = LoadOptions(LoadFormat.Xlsx)
workbook = Workbook(srcFile, loadOptions)
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
source = cells.createRange("A1:D5")
source.transpose()
workbook.save(outputFile)
jpype.shutdownJVM()
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
`=TRANSPOSE(A1:D5)` formülünü, kaynak veriler değişirse sonucun otomatik olarak güncellenmesi için çıktı çalışma kitabında canlı bir formül olarak korumak istediğinizde ve hedef Excel dosyası dinamik dizilerin ve taşma operatörünün desteklendiği **Excel 365 / Excel 2021 veya üstü** sürümlerde açılacaksa bu yaklaşımı kullanın.

### **API used**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)`, bir hücrenin formülünü **dinamik dizi formülü** olarak ayarlayan `com.aspose.cells.Cell` üzerinde bir yöntemdir. Excel formülü bir kez değerlendirir ve sonucu otomatik olarak çevreleyen hücrelere taşırır. Üçüncü parametre, `True` olarak ayarlandığında Aspose.Cells'e yazma zamanında sonuç değerlerini de hesaplaması talimatını verir.

### **Steps**
1. Kaynak çalışma kitabını `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))` kullanarak yükleyin.
2. İlk çalışma sayfasını alın ve `Cells` koleksiyonuna erişin.
3. `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", None, True)` çağırarak dinamik dizi formülünü kaynak aralığın hemen altındaki **A6** hücresine yerleştirin.
4. `None` argümanı varsayılan `FormulaParseOptions` öğesini geçer ve üçüncü `True` argümanı Aspose.Cells'e formülü dinamik dizi olarak ele almasını ve taşan değerlerin çalışma kitabına yazılması için değerlendirmesini söyler.
5. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.
**A6** hücresi `=TRANSPOSE(A1:D5)` formülünü tutar ve Excel sonucu otomatik olarak transpoze edilmiş verilere eşit 5 satır 4 sütunluk bir blok olan **A6:D10** bölgesine taşırır.

{{% alert color="primary" %}}
Bu yaklaşım **yalnızca Excel 365 / 2021 veya üstünde** çalışır. Eski Excel sürümleri dinamik dizi formüllerini doğru şekilde taşırmaz.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, LoadOptions, LoadFormat, FormulaParseOptions, SaveFormat
# ported code here
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", FormulaParseOptions(), True)
workbook.save(outFile, SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
Çalışma kitabında bir `TRANSPOSE` formülünün korunmasını istediğinizde, ancak hedef Excel dosyası dinamik dizi taşmasının desteklenmediği **eski Excel sürümlerinde (2021 öncesi, 2019, 2016, 2013 vb.)** açılabilecekse bu yaklaşımı kullanın. Klasik CSE (Ctrl+Shift+Enter) dizi formülü, tüm Excel sürümlerinin değerlendirebileceği eski sürümlerle uyumlu alternatiftir.

### **API used**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)`, bir hücreye **klasik dizi (CSE) formülü** atayan ve sonuç dizisinin boyutlarını belirten `com.aspose.cells.Cell` üzerinde bir yöntemdir. Aspose.Cells, Excel'in formülü bildirilen aralığı dolduran tek bir dizi ifadesi olarak değerlendirmesi için çok hücreli dizi formülü işaretçisini yazar.

### **Steps**
1. Kaynak çalışma kitabını önceki yaklaşımlarda açıklandığı şekilde yükleyin.
2. İlk çalışma sayfasını alın ve `Cells` koleksiyonuna erişin.
3. `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` çağırın. İkinci argüman `4` hedef dizinin satır sayısı, üçüncü argüman `5` ise sütun sayısıdır.
4. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.
**A6** hücresi dizi formülünün çapasıdır ve değerlendirilen dizi, A1:D5 kaynağının transpoze edilmiş boyutlarıyla eşleşen A6'dan başlayan 4 satır 5 sütunluk bir alana yayılır. Excel, sonuç aralığına tek bir dizi formülü işaretçisi yazar, böylece eski Excel sürümleri onu doğru şekilde değerlendirir.

{{% alert color="primary" %}}
CSE dizi formülleri, bir `TRANSPOSE` ifadesini değerlendirmenin klasik Excel yoludur ve bu yaklaşım Excel sürümleri arasında evrensel olarak uyumludur.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, LoadOptions, LoadFormat, Worksheet, Cells
# Load the source workbook with xlsx LoadOptions
srcFile = "source.xlsx"
workbook = Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))
# Access the first worksheet and its Cells collection
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# Set the classic CSE array formula on cell A6.
# The formula =TRANSPOSE(A1:D5) rotates the 5-row x 4-column source range
# into a 4-row x 5-column array. The second argument (4) is the number of rows
# and the third argument (5) is the number of columns of the resulting array.
# Aspose.Cells writes the CSE array-formula marker so Excel evaluates it as
# a single multi-cell array formula, compatible with older Excel versions
# (2019, 2016, 2013, etc.) that do not support dynamic array spilling.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)
# Save the workbook so the array-formula marker is persisted
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Comparison — When to Use Each Approach**
| Yaklaşım | API / Yöntem | Excel Sürümü | Kaynak formül korundu mu? | Çıktı aralığı |
|----------|--------------|--------------|--------------------------|---------------|
| Yaklaşım 1 — Yerinde transpoze | `Range.transpose()` | Tüm Excel sürümleri | Hayır (yalnızca değerler) | Başlangıç çapa aralığı, 5×4 |
| Yaklaşım 2 — Dinamik dizi formülü | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Evet (dinamik olarak taşar) | Çapadan taşar |
| Yaklaşım 3 — Klasik dizi formülü (CSE) | `Cell.setArrayFormula` | Tüm Excel sürümleri | Evet (çok hücreli dizi formülü) | Açık boyut, 4×5 |
Yalnızca transpoze edilmiş değerlerin dosyaya yazılmasına ihtiyaç duyduğunuz hızlı, sürümler arası bir dönüşüme ihtiyacınız olduğunda **Yaklaşım 1**'i kullanın. Modern Excel'in garantili olduğu ve formülün canlı kalmasını, kaynak değişirse güncellenmesini istediğinizde **Yaklaşım 2**'yi kullanın. Dinamik dizileri desteklemeyen eski sürümler dahil her Excel sürümünde korunmuş bir formülle en geniş uyumluluğa ihtiyaç duyduğunuzda **Yaklaşım 3**'ü kullanın.

## **Related Articles**
- [SmartMarker Tek Hücre Dizi İşleme | Aspose.Cells for Python via Java](/cells/tr/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Bir Hücreye Resim Ekleme](/cells/tr/python-java/inserting-an-image-into-a-cell/)
- [Excel Dosyalarını Birden Çok Dosyaya Bölme](/cells/tr/python-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python" >}}