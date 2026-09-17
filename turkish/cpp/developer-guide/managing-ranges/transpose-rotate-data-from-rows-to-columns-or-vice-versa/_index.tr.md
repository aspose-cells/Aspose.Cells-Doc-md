---
title: Aralığı Devrik Dönüştürme
linktitle: Aralığı Devrik Dönüştürme
description: Bu makale, Aspose.Cells for C++ kullanarak Excel dosyalarındaki verileri satırlardan sütunlara ya da tersi yönde devrik dönüştürmenin veya döndürmenin üç farklı yaklaşımla nasıl yapılacağını açıklar.
keywords: Aspose.Cells, C++ kitaplığı, elektronik tablo, aralığı devrik dönüştürme, verileri döndürme, TRANSPOSE işlevi, dinamik dizi formülü, dizi formülü, Excel TRANSPOSE, Satırlardan Sütunlara
type: docs
weight: 80
url: /tr/cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for C++, satırların sütunlara, sütunların satırlara dönüşeceği şekilde verileri devrik dönüştürmeyi (döndürmeyi) üç farklı yöntemle destekler. İlk yaklaşım, yerinde çalışan `Range.Transpose()` yöntemini kullanır ve her Excel sürümünde çalışır; ikinci yaklaşım, Excel 365 veya Excel 2021'de otomatik olarak taşan modern bir dinamik dizi `=TRANSPOSE(...)` formülü yazmak için `Cell.SetDynamicArrayFormula()` kullanır. Üçüncü yaklaşım ise eski Excel sürümleriyle uyumlu klasik Ctrl+Shift+Enter (CSE) dizi formülü yazmak için `Cell.SetArrayFormula()` kullanır. Bu makale, her yaklaşımı adım adım talimatlar ve eksiksiz kod örnekleriyle anlatır.
{{% /alert %}}

## **Introduction**
Bir aralığı devrik dönüştürmek, onu ana çaprazı boyunca yansıtacak şekilde döndürmek, yani bir satır olan şeyin sütun, bir sütun olan şeyin satır olması anlamına gelir. Microsoft Excel'de `TRANSPOSE` çalışma sayfası işlevi bu işlemi gerçekleştirir ve kavramsal referans [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) adresinde belgelenmiştir. Bu konsept bir hücre aralığına programlı olarak uygulanabilir; bu da birçok iş ve raporlama senaryosunda faydalıdır.
- Çeyreklerin normalde sayfa genelinde, bölgelerin ise sayfa boyunca sıralandığı çeyreklik veya yıllık satış raporlarını yeniden yönlendirmek ya da bunun tersini yapmak.
- Gösterge panolarında veya grafiklerde eksen yönelimini değiştirerek bir zaman serisinin sayfa genelinde değil sayfa boyunca ilerlemesini sağlamak.
- Dış sistemlerden içe aktarılan verileri, aşağı akış analizinin veya raporlama şablonlarının beklediği düzene uyacak şekilde yeniden şekillendirmek.
Makalenin geri kalanını somut hale getirmek için her örnek aşağıdaki bölgeye ve çeyreğe göre küçük satış tablosunu kullanır. Örnek çalışma kitabında bu tablo **A1:D5** aralığını kaplar; sol üst köşe olarak **A1** boş bırakılır, **B1:D1** bölge başlıklarını ve **A2:A5** çeyrek başlıklarını tutar.
| Bölge             | Avrupa     | Asya       | Kuzey Amerika |
|-------------------|------------|------------|---------------|
| Ç1                | 21704714   | 8774099    | 12094215      |
| Ç2                | 17987034   | 12214447   | 10873099      |
| Ç3                | 19485029   | 14356879   | 15689543      |
| Ç4                | 22567894   | 15763492   | 17456723      |
Makale daha sonra Aspose.Cells for C++ kullanılarak bu verileri devrik dönüştürmenin üç farklı yolunu sunar; her biri farklı bir Excel sürümüne ve kullanım durumuna uygundur.

## **Approach 1 — Transpose Range in Place (Range.Transpose)**
`TRANSPOSE` çalışma sayfası işlevini devreye sokmadan verileri devrik dönüştürmek istediğinizde bu yaklaşımı kullanın. **Her Excel sürümünde** çalışır ve dinamik dizilere bağımlılığı yoktur; bu da onu sürümler arası en güvenli uyumlu seçenek haline getirir. Yalnızca son devrik dönüştürülmüş çıktıya ihtiyaç duyduğunuzda ve çalışma kitabında orijinal `TRANSPOSE` formülünü tutmanız gerekmediğinde idealdir.

### **API used**
`Range.Transpose()`, `Aspose.Cells.Range` sınıfında bir örnek yöntemidir. Çağrıldığında, aralığı satır ve sütunlarını değiştirerek yerinde çevirir; böylece satır olan sütun, sütun olan satır olur. Yöntem, formül yazmadan doğrudan temel hücreleri değiştirir.

### **Steps**
1. `LoadOptions` öğesini `.xlsx` biçimine ayarlayarak kaynak çalışma kitabını `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))` oluşturmak suretiyle açın.
2. `workbook.GetWorksheets().Get(0)` kullanarak çalışma kitabından ilk çalışma sayfasını alın.
3. `worksheet.GetCells()` aracılığıyla çalışma sayfasının hücre koleksiyonuna erişin.
4. `cells.CreateRange(u"A1:D5")` çağırarak **A1:D5** aralığını kapsayan kaynak aralığı oluşturun.
5. Aralığı yerinde döndürmek, satırları ve sütunları değiştirmek için `source.Transpose()` çağırın.
6. Çalışma kitabını `workbook.Save(outputFile)` ile kaydedin.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    U16String srcFile(u"source.xlsx");
    U16String outputFile(u"transposed.xlsx");
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(srcFile, loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Range source = cells.CreateRange(u"A1:D5");
    source.Transpose();
    workbook.Save(outputFile);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
`=TRANSPOSE(A1:D5)` formülünü çıktı çalışma kitabında, kaynak veriler değişirse sonucun otomatik olarak güncellenmesini sağlayan canlı bir formül olarak korumak istediğinizde ve hedef Excel dosyası dinamik dizilerin ve taşma operatörünün desteklendiği **Excel 365 / Excel 2021 veya sonrasında** açılacaksa bu yaklaşımı kullanın.

### **API used**
`Cell.SetDynamicArrayFormula(const char* formula, FormulaParseOptions options, bool calculateValue)`, `Aspose.Cells.Cell` üzerinde hücrenin formülünü **dinamik dizi formülü** olarak ayarlayan bir yöntemdir. Excel formülü bir kez değerlendirir ve sonucu otomatik olarak çevreleyen hücrelere taşırır. Üçüncü parametre `true` olarak ayarlandığında, Aspose.Cells'e yazma anında sonuç değerlerini de hesaplaması talimatını verir.

### **Steps**
1. `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))` oluşturarak kaynak çalışma kitabını yükleyin.
2. `workbook.GetWorksheets().Get(0)` aracılığıyla ilk çalışma sayfasını alın ve `worksheet.GetCells()` üzerinden `Cells` koleksiyonuna erişin.
3. `cells.Get(u"A6").SetDynamicArrayFormula(u"=TRANSPOSE(A1:D5)", nullptr, true)` çağırarak dinamik dizi formülünü kaynak aralığın hemen altındaki **A6** hücresine yerleştirin.
4. `nullptr` bağımsız değişkeni varsayılan `FormulaParseOptions` öğesini geçer ve üçüncü bağımsız değişken olan `true`, Aspose.Cells'e formülü dinamik dizi olarak değerlendirmesi ve taşan değerlerin çalışma kitabına yazılması için talimat verir.
5. Çalışma kitabını `workbook.Save(outputFile)` ile kaydedin.
**A6** hücresi `=TRANSPOSE(A1:D5)` formülünü tutar ve Excel sonucu otomatik olarak devrik dönüştürülmüş verilere eşit 5 satır ve 4 sütunluk bir blok olan **A6:D10** bölgesine taşırır.

{{% alert color="primary" %}}
Bu yaklaşım **yalnızca Excel 365 / 2021 veya sonrasında** çalışır. Eski Excel sürümleri dinamik dizi formüllerini doğru şekilde taşırmaz.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    std::string srcFile = "source.xlsx";
    std::string outFile = "output_transpose_dynamic.xlsx";
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(U16String(srcFile.c_str()), loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(u"A6");
    FormulaParseOptions options;
    cell.SetDynamicArrayFormula(U16String("=TRANSPOSE(A1:D5)"), options, true);
    workbook.Save(U16String(outFile.c_str()), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
Çalışma kitabında bir `TRANSPOSE` formülünün korunmasını istediğinizde, ancak hedef Excel dosyasının dinamik dizi taşmasının desteklenmediği **eski Excel sürümlerinde (2021 öncesi, 2019, 2016, 2013 vb. dahil)** açılabileceği durumlarda bu yaklaşımı kullanın. Klasik CSE (Ctrl+Shift+Enter) dizi formülü, tüm Excel sürümlerinin değerlendirebileceği eski sürümlerle uyumlu alternatiftir.

### **API used**
`Cell.SetArrayFormula(const char* arrayFormula, int nRows, int nColumns)`, `Aspose.Cells.Cell` üzerinde **klasik dizi (CSE) formülünü** bağlantı hücresine atayan ve sonuç dizisinin boyutlarını bildiren bir yöntemdir. Aspose.Cells, Excel'in formülü bildirilen aralığı dolduran tek bir dizi ifadesi olarak değerlendirmesi için çok hücreli dizi formülü işaretini yazar.

### **Steps**
2. `workbook.GetWorksheets().Get(0)` aracılığıyla ilk çalışma sayfasını alın ve `worksheet.GetCells()` üzerinden `Cells` koleksiyonuna erişin.
3. `cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5)` çağırın. İkinci bağımsız değişken olan `4` hedef dizinin satır sayısı, üçüncü bağımsız değişken olan `5` ise sütun sayısıdır.
4. Çalışma kitabını `workbook.Save(outputFile)` ile kaydedin.
**A6** hücresi dizi formülünün bağlantı noktasıdır ve değerlendirilen dizi A1:D5 kaynağının devrik dönüştürülmüş boyutlarıyla eşleşen şekilde A6'dan başlayarak 4 satır ve 5 sütun kaplar. Excel, eski sürümlerin doğru şekilde değerlendirmesi için sonuç aralığına tek bir dizi formülü işareti yazar.

{{% alert color="primary" %}}
CSE dizi formülleri, bir `TRANSPOSE` ifadesini değerlendirmenin klasik Excel yoludur ve bu yaklaşım Excel sürümleri arasında evrensel olarak uyumludur.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Kaynak çalışma kitabını xlsx LoadOptions ile yükle
    std::string srcFile = "source.xlsx";
    Workbook workbook(U16String(srcFile.c_str()), LoadOptions(LoadFormat::Xlsx));
    // İlk çalışma sayfasına ve onun Cells koleksiyonuna erişim
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // A6 hücresinde klasik CSE dizi formülünü ayarla.
    // =TRANSPOSE(A1:D5) formülü, 5 satır x 4 sütun kaynak aralığını
    // 4 satır x 5 sütunluk bir diziye döndürür. İkinci bağımsız değişken (4),
    // sonuç dizisindeki satır sayısıdır ve üçüncü bağımsız değişken (5)
    // sütun sayısıdır.
    // Aspose.Cells, Excel'in bunu tek bir çok hücreli dizi formülü olarak
    // değerlendirmesi için CSE dizi formülü işaretini yazar; bu, dinamik
    // dizi taşmasını desteklemeyen eski Excel sürümleriyle (2019, 2016,
    // 2013 vb.) uyumludur.
    cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5);
    // Dizi formülü işaretinin kalıcı olması için çalışma kitabını kaydet
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Comparison — When to Use Each Approach**
| Yaklaşım | API / Yöntem | Excel Sürümü | Kaynak formül korundu mu? | Çıktı aralığı |
|----------|--------------|---------------|--------------------------|---------------|
| Yaklaşım 1 — Yerinde devrik dönüştürme | `Range.Transpose()` | Tüm Excel sürümleri | Hayır (yalnızca değerler) | İlk bağlantı aralığı, 5×4 |
| Yaklaşım 2 — Dinamik dizi formülü | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | Evet (dinamik olarak taşar) | Bağlantı noktasından itibaren taşar |
| Yaklaşım 3 — Klasik dizi formülü (CSE) | `Cell.SetArrayFormula` | Tüm Excel sürümleri | Evet (çok hücreli dizi formülü) | Açık boyut, 4×5 |
Yalnızca devrik dönüştürülmüş değerlerin dosyaya yazılmasına ihtiyaç duyduğunuzda hızlı, sürümler arası bir dönüşüm için **Yaklaşım 1**'i kullanın. Modern Excel'in garanti olduğu ve kaynak değişirse formülün canlı kalmasını ve güncellenmesini istediğinizde **Yaklaşım 2**'yi kullanın. Dinamik dizileri desteklemeyen eski sürümler dahil her Excel sürümünde korunan bir formülle en geniş uyumluluğa ihtiyaç duyduğunuzda **Yaklaşım 3**'ü kullanın.

## **Related Articles**
- [SmartMarker Tek Hücre Dizi Oluşturma | Aspose.Cells for C++](/cells/tr/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Bir Hücreye Resim Ekleme](/cells/tr/cpp/inserting-an-image-into-a-cell/)
- [Excel Dosyalarını Birden Çok Dosyaya Bölme](/cells/tr/cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="" >}}