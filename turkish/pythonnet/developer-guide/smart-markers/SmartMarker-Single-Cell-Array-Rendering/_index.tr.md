---
title: Akıllı İşaretleyici Tek Hücreli Dizi Oluşturma | Aspose.Cells for Python via .NET
description: Aspose.Cells for Python via .NET ile Akıllı İşaretleyicilerde ArrayAsSingle ve ExtraDelimiter özniteliklerini kullanarak dizi verilerini tek bir hücreye nasıl oluşturacağınızı öğrenin.
keywords: Aspose.Cells, Python via .NET kütüphanesi, elektronik tablo, Akıllı İşaretleyiciler, ArrayAsSingle, ExtraDelimiter, tek hücreli dizi, dizi oluşturma, şablon
type: docs
weight: 195
url: /tr/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells, Akıllı İşaretleyiciler aracılığıyla dizi verilerinin tek bir hücreye dönüştürülmesini destekler. Geliştiriciler, `ArrayAsSingle` özniteliğini `ExtraDelimiter` özniteliğiyle birlikte kullanarak dizi öğelerinin tek bir hücre içinde nasıl ayrılacağını kontrol edebilir ve raporlar ile şablonlar için esnek biçimlendirme sağlayabilir.

{{% /alert %}}

## **Giriş**

Aspose.Cells'teki Akıllı İşaretleyiciler, `&=DataSource.Field` gibi işaretleyici ifadeleri kullanarak elektronik tablo verilerini dinamik olarak doldurmanıza olanak tanıyan güçlü, şablon tabanlı bir özelliktir. İşaretleyici, tasarımcı çalışma kitabına yerleştirilir ve şablon `WorkbookDesigner` tarafından işlendiğinde, işaretleyiciler sağlanan veri kaynağındaki değerlerle değiştirilir.

Varsayılan olarak, bir Akıllı İşaretleyici bir dizi özelliğine başvurduğunda (örneğin, `&=DataSource.Numbers`), motor diziyi genişletir ve her öğeyi ayrı bir bitişik hücreye yerleştirir — bir satır boyunca yatay olarak veya bir sütun boyunca dikey olarak. Bu davranış birçok senaryoda kullanışlı olsa da, tüm diziyi tek bir hücreye, öğeleri birleştirilmiş ve istediğiniz bir ayraçla ayrılmış şekilde dönüştürmeyi tercih edeceğiniz durumlar vardır.

`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, bir Akıllı İşaretleyici etiketinin içinde birlikte kullanıldığında, tam olarak bu gereksinimi karşılar. Rapor düzenlerini kompakt ve öngörülebilir tutarken dizi veri kaynaklarıyla yerel olarak çalışmanıza olanak tanır.

## **Bu Özelliğe Neden İhtiyaç Duyulur**

### **Varsayılan Dizi Yayılma Davranışı**

Bir Akıllı İşaretleyici bir dizi özelliğine başvurduğunda, Aspose.Cells diziyi varsayılan olarak birden fazla hücreye genişletir. Örneğin, dört değer içeren bir `string[]` üzerindeki `&=Product.Tags` gibi bir işaretleyici, her değeri kendi hücresine yerleştirir, diğer şablon içeriğini dışa doğru iter ve dikkatlice tasarlanmış rapor düzenlerini potansiyel olarak bozar.

### **Kullanım Senaryosu Sınırlamaları**

Varsayılan yayılma davranışının istenmediği birçok pratik senaryo vardır:

- Kayıt başına kompakt tek satırlık düzen gerektiren **özet tarzı raporlar**.
- Tek bir hücre içinde virgülle veya boru ile ayrılmış değerler olarak görüntülenmesi gereken **etiket, etiket veya anahtar kelime listeleri**.
- Okunabilirlik için birden fazla değeri tek bir yerde gruplandıran **filtre çipleri veya durum göstergeleri**.
- Genişletilmiş bir aralık yerine hücre başına tek bir birleşik değer bekleyen **aşağı akış işlem hatları** (CSV dışa aktarma, PDF oluşturma, posta birleştirme).
- Bazı tüketicilerin birden fazla hücreye yayılan dizilere tahammül edemeyeceği **platformlar arası uyumluluk**.

### **Doldurduğu Boşluk**

Yerleşik bir mekanizma olmadan, geliştiriciler verileri Python'da önceden işlemeye — dizileri çalışma kitabı tasarımcısına bağlamadan önce ayrılmış dizelere birleştirmeye — zorlanırdı. Bu, mantığı çoğaltır, veri modellerini karmaşıklaştırır ve hata olasılığını artırır. `ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, biçimlendirmeyi Akıllı İşaretleyicinin kendisi içinde bildirimsel olarak işleyerek bu geçici çözümü ortadan kaldırır.

## **Özellik Avantajları**

Akıllı İşaretleyicilerinizde `ArrayAsSingle` ve `ExtraDelimiter` özniteliklerini kullanmak çeşitli avantajlar sağlar:

- **Tek hücreli kapsama**: Tüm dizi öğeleri tam olarak bir hücreye dönüştürülür, bu da düzenleri kompakt ve öngörülebilir tutar.
- **Özel ayraç kontrolü**: Virgül, noktalı virgül, kısa çizgi, boru, yeni satır veya herhangi bir özel metin gibi istediğiniz herhangi bir ayraç dizesini belirtin.
- **Şablon tabanlı biçimlendirme**: Verileri önceden işlemek için ek kod gerekmez; biçimlendirme kuralları Akıllı İşaretleyici etiketinin içinde bulunur.
- **Daha temiz raporlar**: Dizi verileri artık komşu şablon içeriğini farklı satır veya sütunlara itmez.
- **Çok yönlü veri türleri**: Dizeler, sayılar, tarihler ve bir ayraçla birleştirilebilen diğer veri türleriyle çalışır.
- **Geriye dönük uyumluluk**: Öznitelikler atlandığında, orijinal yayılma davranışı korunur, böylece mevcut şablonlar değişiklik yapılmadan çalışmaya devam eder.

## **Bu Özellik Nasıl Kullanılır**

### **Akıllı İşaretleyici Sözdizimi**

`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, standart bir Akıllı İşaretleyicinin parantezleri içinde anahtar-değer çiftleri olarak iletilir. Genel sözdizimi şudur:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

İşaretleyici aşağıdaki parçalardan oluşur:

- `&=DataSource.ArrayProperty` — bağlı veri kaynağındaki dizi özelliğine başvuran standart Akıllı İşaretleyici.
- `arrayasSingle=true` — motora tüm diziyi tek bir hücreye dönüştürmesi talimatını verir. Yalnızca `true` değeri tek hücreli davranışı tetikler.
- `extraDelimiter=", "` — dizi öğeleri arasına yerleştirilen ayracı tanımlar. Değer bir dize sabitidir; boş, tek karakterli veya çok karakterli bir dize olabilir.

{{% alert color="primary" %}}

`extraDelimiter` özniteliği, çok karakterli ayraçlar, özel metinler veya yeni satırla ayrılmış çıktı için `\n` gibi kaçış dizileri dahil herhangi bir dize sabitini kabul eder. Dizi boşsa, sonuç hücre boş bırakılır.

{{% /alert %}}

### **Adım Adım İş Akışı**

Aşağıdaki iş akışı, Akıllı İşaretleyicileri kullanarak bir dizinin tek bir hücreye nasıl dönüştürüleceğini açıklar.

1. **Veri kaynağını hazırlayın**: Bir dizi döndüren bir özellik sunan bir sınıf (veya veri yapısı) oluşturun. Özellik, `list[str]`, `list[int]` veya desteklenen başka herhangi bir dizi türünü döndürebilir.
2. **Tasarımcı çalışma kitabı oluşturun**: Yeni bir `Workbook` oluşturun, bir başlık satırı ekleyin ve `arrayasSingle` ve `extraDelimiter` öznitelikleriyle dizi özelliğine başvuran bir Akıllı İşaretleyici hücresi yerleştirin.
3. **WorkbookDesigner'ı başlatın**: Bir `WorkbookDesigner` nesnesi oluşturun, tasarımcı çalışma kitabını ona ekleyin ve `set_data_source` yöntemini kullanarak veri kaynağınızı bağlayın.
4. **İşaretleyicileri işleyin**: Akıllı İşaretleyicileri genişletmek ve çalışma kitabını gerçek verilerle doldurmak için `WorkbookDesigner.process()` yöntemini çağırın.
5. **Sonucu kaydedin**: Ortaya çıkan çalışma kitabını XLSX veya desteklenen başka herhangi bir dosya biçiminde diske kaydedin.

### **Kod Örneği 1 — Temel Dize Dizisi Oluşturma**

```python
class Product:
    def __init__(self):
        self.Tags = []

product = Product()
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"]

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Tags")
worksheet.cells["A2"].put_value("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")

designer = ac.WorkbookDesigner()
designer.workbook = workbook
designer.set_data_source("Product", product)
designer.process()

workbook.save("output_arraySingle.xlsx")
```

### **Kod Örneği 2 — Özel Ayraçlı Sayısal Dizi**

```python
class Student:
    def __init__(self):
        self.scores = []


student = Student()
student.scores = [95, 88, 76, 100, 67]

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Scores")
worksheet.cells["A2"].put_value(" - ".join(str(s) for s in student.scores))

workbook.save("output_numericArray.xlsx")
```

### **Kod Örneği 3 — Varsayılan ve ArrayAsSingle Davranışının Karşılaştırılması**

```python
class Order:
    def __init__(self, items):
        self._items = items

    @property
    def Items(self):
        return self._items

    @Items.setter
    def Items(self, value):
        self._items = value

order = Order(["Apple", "Banana", "Cherry", "Date"])

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Bölüm 1: Varsayılan Akıllı İşaretleyici - değerler hücreler arasında yatay olarak yayılır
cells["A1"].put_value("Default Spreading Behavior:")
cells["A2"].put_value("&=Order.Items")

# Bölüm 2: arrayasSingle ve extraDelimiter kullanarak yeni tek hücreli işleme
cells["A4"].put_value("Single Cell Rendering (arrayasSingle=true):")
cells["A5"].put_value('&=Order.Items(arrayasSingle=true, extraDelimiter="; ")')

# Veri kaynağını bağla ve Akıllı İşaretleyicileri işle
designer = ac.WorkbookDesigner(workbook)
designer.set_data_source("Order", order)
designer.process()

# Sonuç çalışma kitabını kaydet
workbook.save("output_comparison.xlsx")
```

### **Notlar ve En İyi Uygulamalar**

`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleriyle çalışırken aşağıdaki noktaları aklınızda bulundurun:

- `extraDelimiter` değeri bir dize sabiti olarak kabul edilir; şablon işlemcinizin yorumlayabileceği özel karakterlerden kaçış yapın.
- `arrayasSingle` özniteliği bir boolean değeri kabul eder (`True` / `False`). Yalnızca `True` tek hücreli davranışı tetikler; diğer herhangi bir değer varsayılan yayılma davranışına geri döner.
- Dizi boş veya null ise, hücre boş bırakılır (veya veri türüne bağlı olarak boş bir dize içerir).
- Özellik, nesne veri kaynaklarının yanı sıra bir sütunun dizilere bölünebileceği `DataSet` ve `DataTable` kaynaklarıyla da çalışır.
- Yeni satırla ayrılmış çıktı için, ayraç değeri olarak `\n` veya `os.linesep` kullanabilirsiniz.
- Akıllı İşaretleyiciyi, sonuçta birleştirilmiş dizeyi görüntülemek için yeterli genişliğe sahip bir hücreye yerleştirin; aksi takdirde, içerik biçime bağlı olarak bitişik hücrelere görsel olarak taşabilir.

## **İlgili Makaleler**

- [Akıllı İşaretleyiciler](/cells/tr/python-net/smart-markers/)
- [Hücreleri Birleştirme ve Ayırma](/cells/tr/python-net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="python" >}}