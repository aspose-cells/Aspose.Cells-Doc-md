---
title: ...
linktitle: ...
description: ...
keywords: ...
type: docs
weight: 80
url: /tr/python-net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET, satırların sütunlara ve sütunların satırlara dönüşmesi şeklinde verilerin devrik çevrilmesini (döndürülmesini) üç farklı yöntemle destekler. İlk yaklaşım, yerinde `range.transpose()` yöntemini kullanır ve her Excel sürümünde çalışır; ikincisi ise Excel 365 veya Excel 2021'de otomatik olarak taşan modern bir dinamik dizi `=TRANSPOSE(...)` formülü yazmak için `cell.set_dynamic_array_formula()` kullanır. Üçüncü yaklaşım, eski Excel sürümleriyle uyumlu klasik Ctrl+Shift+Enter (CSE) dizi formülünü yazmak için `cell.set_array_formula()` kullanır. Bu makale her yaklaşımı adım adım talimatlar ve eksiksiz kod örnekleriyle açıklar.
{{% /alert %}}

## **Introduction**
Bir aralığı devrik çevirmek, ana köşegeni boyunca yansıtılarak bir satır olanın sütun, bir sütun olanın satır olacak şekilde döndürülmesi anlamına gelir. Microsoft Excel'de `TRANSPOSE` çalışma sayfası işlevi bu işlemi gerçekleştirir ve kavramsal referans [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) adresinde belgelenmiştir. Bu kavram, bir hücre aralığına programlı olarak uygulanabilir ve bu da birçok iş ve raporlama senaryosunda kullanışlıdır.
- Çeyreklerin normalde sayfa boyunca, bölgelerin ise sayfa boyunca aşağı doğru yer aldığı (veya tam tersi) çeyreklik veya yıllık satış raporlarını yeniden yönlendirme.
- Gösterge tablolarında veya grafiklerde eksen yönünü değiştirerek zaman serisinin sayfa boyunca yatay yerine dikey olarak akmasını sağlama.
- Dış sistemlerden içe aktarılan verileri, aşağı akış analiz veya raporlama şablonlarının beklediği düzene uyacak şekilde yeniden şekillendirme.
Makalenin geri kalanını somut hale getirmek için her örnek aşağıdaki küçük bölge-çeyrek bazında satış tablosunu kullanır. Örnek çalışma kitabında bu tablo **A1:D5** aralığını kaplar; **A1** sol üst köşede boş bırakılır, **B1:D1** bölge başlıklarını, **A2:A5** ise çeyrek başlıklarını tutar.
| Bölge            | Avrupa    | Asya      | Kuzey Amerika |
|------------------|-----------|-----------|---------------|
| 1. Çeyrek        | 21704714  | 8774099   | 12094215      |
| 2. Çeyrek        | 17987034  | 12214447  | 10873099      |
| 3. Çeyrek        | 19485029  | 14356879  | 15689543      |
| 4. Çeyrek        | 22567894  | 15763492  | 17456723      |
Makale daha sonra Aspose.Cells for Python via .NET kullanılarak bu verilerin devrik çevrilmesine yönelik, her biri farklı bir Excel sürümüne ve kullanım senaryosuna uygun üç farklı yol sunar.

## **Approach 1 — Transpose Range in Place (range.transpose)**
Verileri `TRANSPOSE` çalışma sayfası işlevini devreye sokmadan devrik çevirmek istediğinizde bu yaklaşımı kullanın. **Excel'in her sürümünde** çalışır ve dinamik dizilere bağımlılığı yoktur; bu da onu sürümler arası en güvenli uyumlu seçenek haline getirir. Yalnızca son devrik çıktıya ihtiyaç duyduğunuzda ve özgün `TRANSPOSE` formülünü çalışma kitabında tutmanıza gerek olmadığında idealdir.

### **API used**
`range.transpose()`, `Aspose.Cells.Range` sınıfında bir örnek yöntemidir. Çağrıldığında, satırları ve sütunları değiştirerek aralığı yerinde çevirir; böylece satır olan sütun, sütun olan satır olur. Yöntem, formül yazmadan doğrudan temel hücreleri değiştirir.

### **Steps**
1. `LoadOptions` öğesini `.xlsx` biçimine ayarlayarak `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))` çağrısıyla kaynak çalışma kitabını açın.
2. `workbook.worksheets[0]` kullanarak çalışma kitabından ilk çalışma sayfasını alın.
3. `worksheet.cells` aracılığıyla çalışma sayfasının hücre koleksiyonuna erişin.
4. `cells.create_range("A1:D5")` çağırarak **A1:D5** aralığını kapsayan kaynak aralığı oluşturun.
5. Aralığı yerinde döndürmek ve satırlarla sütunları değiştirmek için `source.transpose()` çağrısını yapın.
6. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.
Devrik çevirme işleminden sonra ilk bağlantı aralığı döndürülmüş verileri tutar. İlk satır (boş, **Avrupa**, **Asya**, **Kuzey Amerika**) ve ilk sütun (boş, **1. Çeyrek**, **2. Çeyrek**, **3. Çeyrek**, **4. Çeyrek**) olarak okunur. Orijinal her bir satış sütunu, devrik çevrilmiş aralıkta bir satır haline gelir.

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.XLSX))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
source = cells.create_range("A1:D5")
source.transpose()
workbook.save(outputFile)
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
`=TRANSPOSE(A1:D5)` formülünü çıktı çalışma kitabında, kaynak veriler değişirse sonucun otomatik olarak güncellenmesini sağlayacak canlı bir formül olarak korumak istediğinizde ve hedef Excel dosyası dinamik dizilerin ve taşma operatörünün desteklendiği **Excel 365 / Excel 2021 veya üstü** bir sürümde açılacaksa bu yaklaşımı kullanın.

### **API used**
`cell.set_dynamic_array_formula(formula, options, calculate_value)`, `Aspose.Cells.Cell` üzerinde hücrenin formülünü **dinamik dizi formülü** olarak ayarlayan bir yöntemdir. Excel formülü bir kez değerlendirir ve sonucu otomatik olarak çevreleyen hücrelere taşırır. Üçüncü parametre `True` olarak ayarlandığında Aspose.Cells'e yazma zamanında sonuç değerlerini de hesaplaması talimatını verir.

### **Steps**
1. Kaynak çalışma kitabını `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))` kullanarak yükleyin.
2. İlk çalışma sayfasını alın ve `cells` koleksiyonuna erişin.
3. `cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", None, True)` çağrısıyla dinamik dizi formülünü kaynak aralığının hemen altındaki **A6** hücresine yerleştirin.
4. `None` bağımsız değişkeni varsayılan `FormulaParseOptions` öğesini geçer ve üçüncü bağımsız değişken `True` Aspose.Cells'e formülü dinamik dizi olarak ele almasını ve taşan değerlerin çalışma kitabına yazılması için değerlendirmesini söyler.
5. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.
**A6** hücresi `=TRANSPOSE(A1:D5)` formülünü tutar ve Excel sonucu otomatik olarak devrik verilere eşit 5 satır 4 sütunluk bir blok olan **A6:D10** bölgesine taşırır.

{{% alert color="primary" %}}
Bu yaklaşım yalnızca **Excel 365 / 2021 veya üstünde** çalışır. Eski Excel sürümleri dinamik dizi formüllerini doğru şekilde taşırmaz.
{{% /alert %}}

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", ac.FormulaParseOptions(), True)
workbook.save(outFile, ac.SaveFormat.Xlsx)
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
Çalışma kitabında bir `TRANSPOSE` formülünün korunmasını istediğinizde ancak hedef Excel dosyası dinamik dizi taşmasının desteklenmediği **eski Excel sürümlerinde (2021 öncesi, 2019, 2016, 2013 vb. dahil)** açılabilecekse bu yaklaşımı kullanın. Klasik CSE (Ctrl+Shift+Enter) dizi formülü, tüm Excel sürümlerinin değerlendirebileceği eski sürümlerle uyumlu alternatiftir.

### **API used**
`cell.set_array_formula(array_formula, n_rows, n_columns)`, `Aspose.Cells.Cell` üzerinde bağlantı hücresine **klasik dizi (CSE) formülü** atayan ve sonuç dizisinin boyutlarını bildiren bir yöntemdir. Aspose.Cells, çok hücreli dizi formülü işaretini yazar; böylece Excel formülü, belirtilen aralığı dolduran tek bir dizi ifadesi olarak değerlendirir.

### **Steps**
1. Kaynak çalışma kitabını önceki yaklaşımlarda açıklandığı şekilde yükleyin.
2. İlk çalışma sayfasını alın ve `cells` koleksiyonuna erişin.
3. `cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)` çağrısını yapın. İkinci bağımsız değişken `4` hedef dizinin satır sayısı, üçüncü bağımsız değişken `5` ise sütun sayısıdır.
4. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.
**A6** hücresi dizi formülünün bağlantı noktasıdır ve değerlendirilen dizi A6'dan başlayarak 4 satır 5 sütun olarak uzanır; A1:D5 kaynağının devrik boyutlarıyla eşleşir. Excel, sonuç aralığı boyunca tek bir dizi formülü işareti yazar; böylece eski Excel sürümleri onu doğru şekilde değerlendirir.

{{% alert color="primary" %}}
CSE dizi formülleri, bir `TRANSPOSE` ifadesini değerlendirmenin klasik Excel yoludur ve bu yaklaşım Excel sürümleri arasında evrensel olarak uyumludur.
{{% /alert %}}

```python
import aspose.cells as ac
# Load the source workbook with xlsx LoadOptions
srcFile = "source.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
# Access the first worksheet and its Cells collection
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Set the classic CSE array formula on cell A6.
# The formula =TRANSPOSE(A1:D5) rotates the 5-row x 4-column source range
# into a 4-row x 5-column array. The second argument (4) is the number of rows
# and the third argument (5) is the number of columns of the resulting array.
# Aspose.Cells writes the CSE array-formula marker so Excel evaluates it as
# a single multi-cell array formula, compatible with older Excel versions
# (2019, 2016, 2013, etc.) that do not support dynamic array spilling.
cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)
# Save the workbook so the array-formula marker is persisted
workbook.save("output.xlsx")
```

## **Comparison — When to Use Each Approach**
| Yaklaşım | API / Yöntem | Excel Sürümü | Kaynak formül korunuyor mu? | Çıktı aralığı |
|----------|--------------|---------------|-----------------------------|---------------|
| Yaklaşım 1 — Yerinde devrik çevirme | `range.transpose()` | Tüm Excel sürümleri | Hayır (yalnızca değerler) | İlk bağlantı aralığı, 5×4 |
| Yaklaşım 2 — Dinamik dizi formülü | `cell.set_dynamic_array_formula` | Excel 365 / 2021+ | Evet (dinamik olarak taşar) | Bağlantı noktasından taşar |
| Yaklaşım 3 — Klasik dizi formülü (CSE) | `cell.set_array_formula` | Tüm Excel sürümleri | Evet (çok hücreli dizi formülü) | Açık boyut, 4×5 |
Yalnızca devrik çevrilmiş değerlerin dosyaya yazılmasına ihtiyaç duyduğunuz hızlı, sürümler arası bir dönüşüm için **Yaklaşım 1'i** kullanın. Modern Excel'in garanti olduğu ve formülün canlı kalmasını ve kaynak değişirse güncellenmesini istediğiniz durumlarda **Yaklaşım 2'yi** kullanın. Dinamik dizileri desteklemeyen eski sürümler dahil her Excel sürümünde korunan bir formülle en geniş uyumluluğa ihtiyaç duyduğunuzda **Yaklaşım 3'ü** kullanın.

## **Related Articles**
- [Akıllı İşaretleyici Tek Hücre Dizi Oluşturma | Aspose.Cells for Python via .NET](/cells/tr/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Bir Hücreye Görüntü Ekleme](/cells/tr/python-net/inserting-an-image-into-a-cell/)
- [Excel Dosyalarını Birden Çok Dosyaya Bölme](/cells/tr/python-net/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python-net" >}}