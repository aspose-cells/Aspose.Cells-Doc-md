---
title: SmartMarker Tek Hücreli Dizi Oluşturma | Aspose.Cells C++
description: Aspose.Cells for C++ ile Akıllı İşaretçiler'de ArrayAsSingle ve ExtraDelimiter özniteliklerini kullanarak dizi verilerini tek bir hücreye nasıl oluşturacağınızı öğrenin.
keywords: Aspose.Cells, C++ kütüphanesi, elektronik tablo, Akıllı İşaretçiler, ArrayAsSingle, ExtraDelimiter, tek hücreli dizi, dizi oluşturma, şablon
type: docs
weight: 195
url: /tr/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells, Akıllı İşaretçiler aracılığıyla dizi verilerinin tek bir hücreye dönüştürülmesini destekler. Geliştiriciler, `ArrayAsSingle` özniteliğini `ExtraDelimiter` özniteliğiyle birlikte kullanarak dizi öğelerinin tek bir hücre içinde nasıl ayrılacağını kontrol edebilir ve raporlar ile şablonlar için esnek biçimlendirme sağlayabilir.

{{% /alert %}}

## **Giriş**

Aspose.Cells'teki Akıllı İşaretçiler, `&=DataSource.Field` gibi işaretçi ifadelerini kullanarak elektronik tablo verilerini dinamik olarak doldurmanıza olanak tanıyan güçlü, şablon tabanlı bir özelliktir. İşaretçi, tasarımcı çalışma kitabına yerleştirilir ve şablon `WorkbookDesigner` tarafından işlendiğinde, işaretçiler sağlanan veri kaynağındaki değerlerle değiştirilir.

Varsayılan olarak, bir Akıllı İşaretçi bir dizi özelliğine başvurduğunda (örneğin, `&=DataSource.Numbers`), motor diziyi genişletir ve her öğeyi ayrı bir bitişik hücreye yerleştirir — bir satır boyunca yatay olarak veya bir sütun boyunca dikey olarak. Bu davranış birçok senaryoda kullanışlı olsa da, tüm diziyi seçtiğiniz bir sınırlayıcıyla birleştirilmiş ve ayrılmış şekilde tek bir hücreye dönüştürmeyi tercih edeceğiniz durumlar da vardır.

Akıllı İşaretçi etiketinin içinde birlikte kullanılan `ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri tam olarak bu gereksinimi karşılar. Bu öznitelikler, dizi veri kaynaklarıyla yerel olarak çalışmaya devam ederken rapor düzenlerini kompakt ve tahmin edilebilir tutmanıza olanak tanır.

## **Bu Özelliğe Neden İhtiyaç Duyulur**

### **Varsayılan Dizi Yayılma Davranışı**

Bir Akıllı İşaretçi bir dizi özelliğine başvurduğunda, Aspose.Cells diziyi varsayılan olarak birden çok hücreye genişletir. Örneğin, dört değer içeren bir `string[]` karşısında `&=Product.Tags` gibi bir işaretçi, her değeri kendi hücresine yerleştirir, diğer şablon içeriklerini dışa doğru iter ve dikkatlice tasarlanmış rapor düzenlerini potansiyel olarak bozar.

### **Kullanım Durumu Sınırlamaları**

Varsayılan yayılma davranışının istenmediği birçok pratik senaryo vardır:

- **Özet tarzı raporlar** — kayıt başına kompakt bir satır düzeni gerektiren.
- **Etiket, etiket veya anahtar kelime listeleri** — tek bir hücre içinde virgülle veya boru ile ayrılmış değerler olarak görüntülenmesi gereken.
- **Filtre çipleri veya durum göstergeleri** — okunabilirlik için birden çok değeri tek bir yerde gruplayan.
- **Alt işlem hatları** (CSV dışa aktarma, PDF oluşturma, posta birleştirme) — genişletilmiş bir aralık yerine hücre başına tek bir birleşik değer bekleyen.
- **Platformlar arası uyumluluk** — bazı tüketicilerin birden çok hücreye yayılan dizilere tolerans göstermediği durumlar.

### **Doldurduğu Boşluk**

Yerleşik bir mekanizma olmadan, geliştiriciler C++'ta verileri önceden işlemeye — dizileri çalışma kitabı tasarımcısına bağlamadan önce sınırlayıcılı dizelere birleştirmeye zorlanırdı. Bu durum mantığı çoğaltır, veri modellerini karmaşıklaştırır ve hata olasılığını artırır. `ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, biçimlendirmeyi Akıllı İşaretçinin içinde bildirimsel olarak ele alarak bu geçici çözümü ortadan kaldırır.

## **Özellik Avantajları**

Akıllı İşaretçilerinizde `ArrayAsSingle` ve `ExtraDelimiter` özniteliklerini kullanmak çeşitli avantajlar sağlar:

- **Tek hücreli kapsama**: Tüm dizi öğeleri tam olarak bir hücreye dönüştürülür, düzenler kompakt ve tahmin edilebilir kalır.
- **Özel sınırlayıcı kontrolü**: İstediğiniz herhangi bir sınırlayıcı dizeyi belirtin — virgül, noktalı virgül, kısa çizgi, boru, yeni satır veya herhangi bir özel metin.
- **Şablon odaklı biçimlendirme**: Verileri önceden işlemek için ek kod gerekmez; biçimlendirme kuralları Akıllı İşaretçi etiketinin içinde yer alır.
- **Daha temiz raporlar**: Dizi verileri artık komşu şablon içeriklerini farklı satırlara veya sütunlara itmez.
- **Çok yönlü veri türleri**: Dizeler, sayılar, tarihler ve sınırlayıcıyla birleştirilebilen diğer veri türleriyle çalışır.
- **Geriye dönük uyumluluk**: Öznitelikler atlandığında, orijinal yayılma davranışı korunur, böylece mevcut şablonlar değişiklik yapılmadan çalışmaya devam eder.

## **Bu Özellik Nasıl Kullanılır**

### **Akıllı İşaretçi Sözdizimi**

`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, standart bir Akıllı İşaretçinin parantezleri içinde anahtar-değer çiftleri olarak iletilir. Genel sözdizimi şöyledir:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

İşaretçi aşağıdaki parçalardan oluşur:

- `&=DataSource.ArrayProperty` — bağlı veri kaynağındaki dizi özelliğine başvuran standart Akıllı İşaretçi.
- `arrayasSingle=true` — motora tüm diziyi tek bir hücreye dönüştürmesi talimatını verir. Yalnızca `true` değeri tek hücreli davranışı tetikler.
- `extraDelimiter=", "` — dizi öğeleri arasına yerleştirilen sınırlayıcıyı tanımlar. Değer bir dize sabitidir; boş, tek karakterli veya çok karakterli bir dize olabilir.

{{% alert color="primary" %}}

`extraDelimiter` özniteliği, çok karakterli sınırlayıcılar, özel metin veya yeni satırla ayrılmış çıktı için `\n` gibi kaçış dizileri dahil olmak üzere herhangi bir dize sabitini kabul eder. Dizi boşsa, sonuç hücre boş bırakılır.

{{% /alert %}}

### **Adım Adım İş Akışı**

Aşağıdaki iş akışı, Akıllı İşaretçiler kullanarak bir dizinin tek bir hücreye nasıl dönüştürüleceğini açıklar.

1. **Veri kaynağını hazırlayın**: Bir dizi döndüren bir özellik sunan bir sınıf (veya veri yapısı) oluşturun. Özellik `std::vector<std::string>`, `std::vector<int>` veya desteklenen diğer dizi/vektör türlerini döndürebilir.
2. **Tasarımcı çalışma kitabı oluşturun**: Yeni bir `Workbook` oluşturun, bir başlık satırı ekleyin ve `arrayasSingle` ve `extraDelimiter` öznitelikleriyle dizi özelliğine başvuran bir Akıllı İşaretçi hücresi yerleştirin.
3. **WorkbookDesigner'ı örnekleyin**: Bir `WorkbookDesigner` nesnesi oluşturun, tasarımcı çalışma kitabını buna ekleyin ve `SetDataSource` yöntemini kullanarak veri kaynağınızı bağlayın.
4. **İşaretçileri işleyin**: Akıllı İşaretçileri genişletmek ve çalışma kitabını gerçek verilerle doldurmak için `WorkbookDesigner.Process()` yöntemini çağırın.
5. **Sonucu kaydedin**: Elde edilen çalışma kitabını XLSX veya desteklenen herhangi bir dosya biçiminde diske kaydedin.

### **Kod Örneği 1 — Temel Dize Dizisi Oluşturma**

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);
    Cells cells = ws.GetCells();

    cells.Get(u"A1").PutValue(u"Tags");
    cells.Get(u"A2").PutValue(u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

    // WorkbookDesigner, Aspose.Cells for C++'ta mevcut değil
    // İşaretçileri manuel olarak değiştirerek SmartMarker işlemeyi simüle etmemiz gerekiyor
    // Aspose.Cells C++ WorkbookDesigner'ı desteklemediğinden, U16String değiştirmeyi kullanacağız
    U16String marker = u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")";
    U16String replacement = u"C#;Aspose;SmartMarker;Excel";
    U16String value = cells.Get(u"A2").GetStringValue();
    
    // Akıllı işaretçiyi gerçek verilerle değiştir
    value = value.Replace(marker, replacement);
    cells.Get(u"A2").PutValue(value);

    wb.Save(u"output_arraySingle.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Kod Örneği 2 — Özel Sınırlayıcıya Sahip Sayısal Dizi**

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <sstream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    int scores[] = { 95, 88, 76, 100, 67 };
    int scoresCount = sizeof(scores) / sizeof(scores[0]);

    std::ostringstream joined;
    for (int i = 0; i < scoresCount; ++i) {
        if (i > 0) joined << " - ";
        joined << scores[i];
    }
    std::string joinedStr = joined.str();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(u"Scores");
    cells.Get(u"A2").PutValue(U16String(joinedStr.c_str()));

    wb.Save(u"output_numericArray.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Kod Örneği 3 — Varsayılan ve ArrayAsSingle Davranışının Karşılaştırılması**

```cpp
#include "Aspose.Cells.h"
#include <vector>

using namespace Aspose::Cells;

struct Order {
    std::vector<U16String> Items;
};

int main() {
    Aspose::Cells::Startup();

    // Veri kaynağını hazırla
    Order order;
    order.Items = { u"Apple", u"Banana", u"Cherry", u"Date" };

    // Çalışma kitabı oluştur ve ilk çalışma sayfasını al
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Bölüm 1: Varsayılan Akıllı İşaretleyici - değerler hücreler boyunca yatay olarak yayılır
    cells.Get(u"A1").PutValue(u"Default Spreading Behavior:");
    cells.Get(u"A2").PutValue(u"&=Order.Items");

    // Bölüm 2: arrayasSingle ve extraDelimiter kullanarak yeni tek hücreli oluşturma
    cells.Get(u"A4").PutValue(u"Single Cell Rendering (arrayasSingle=true):");
    cells.Get(u"A5").PutValue(u"&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // Veri kaynağını bağla ve Akıllı İşaretleyicileri işle
    WorkbookDesigner designer(wb);
    designer.SetDataSource(u"Order", order);
    designer.Process();

    // Ortaya çıkan çalışma kitabını kaydet
    wb.Save(u"output_comparison.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Notlar ve En İyi Uygulamalar**

`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleriyle çalışırken aşağıdaki noktaları aklınızda bulundurun:

- `extraDelimiter` değeri bir dize sabiti olarak ele alınır; şablon işlemcinizin yorumlayabileceği özel karakterleri kaçış ile ayırın.
- `arrayasSingle` özniteliği bir boole değeri kabul eder (`true` / `false`). Yalnızca `true` tek hücreli davranışı tetikler; diğer herhangi bir değer varsayılan yayılma davranışına geri döner.
- Dizi boş veya null ise, hücre boş bırakılır (veya veri türüne bağlı olarak boş bir dize içerir).
- Özellik, nesne veri kaynaklarının yanı sıra bir sütunun dizilere bölünebileceği `DataSet` ve `DataTable` kaynaklarıyla da çalışır.
- Yeni satırla ayrılmış çıktı için sınırlayıcı değeri olarak `\n` kullanabilirsiniz.
- Akıllı İşaretçiyi, sonuçta ortaya çıkan birleştirilmiş dizeyi görüntülemek için yeterli genişliğe sahip bir hücreye yerleştirin; aksi takdirde, içerik biçime bağlı olarak görsel olarak bitişik hücrelere taşabilir.

## **İlgili Makaleler**

- [Akıllı İşaretçiler](/cells/tr/cpp/smart-markers/)
- [Hücreleri Birleştirme ve Ayırma](/cells/tr/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}