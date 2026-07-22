---
title: SmartMarker Tek Hücre Dizi İşleme | Aspose.Cells Python via Java
linktitle: SmartMarker Tek Hücre Dizi İşleme | Aspose.Cells Python
description: Aspose.Cells for Python via Java'da Akıllı İşaretleyicilerde ArrayAsSingle ve ExtraDelimiter özniteliklerini kullanarak dizi verilerini tek bir hücreye nasıl işleyeceğinizi öğrenin.
keywords: Aspose.Cells, Python via Java kitaplığı, elektronik tablo, Akıllı İşaretleyiciler, ArrayAsSingle, ExtraDelimiter, tek hücre dizisi, dizi işleme, şablon
type: docs
weight: 195
url: /tr/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, Akıllı İşaretleyiciler aracılığıyla dizi verilerinin tek bir hücreye işlenmesini destekler. Geliştiriciler, `ArrayAsSingle` özniteliğini `ExtraDelimiter` özniteliğiyle birlikte kullanarak dizi öğelerinin tek bir hücre içinde nasıl ayrılacağını kontrol edebilir ve raporlar ile şablonlar için esnek biçimlendirme sağlayabilir.

{{% /alert %}}

## **Giriş**

Aspose.Cells'teki Akıllı İşaretleyiciler, `&=DataSource.Field` gibi işaretleyici ifadeleri kullanarak elektronik tablo verilerini dinamik olarak doldurmanıza olanak tanıyan güçlü, şablon tabanlı bir özelliktir. İşaretleyici, bir tasarımcı çalışma kitabına yerleştirilir ve şablon `WorkbookDesigner` tarafından işlendiğinde, işaretleyiciler sağlanan veri kaynağından gelen değerlerle değiştirilir.

Varsayılan olarak, bir Akıllı İşaretleyici bir dizi özelliğine başvurduğunda (örneğin, `&=DataSource.Numbers`), motor diziyi genişletir ve her öğeyi ayrı bir bitişik hücreye yerleştirir — ya bir satır boyunca yatay olarak ya da bir sütun boyunca dikey olarak. Bu davranış birçok senaryoda kullanışlı olsa da, tüm diziyi öğeleri birleştirilmiş ve seçtiğiniz bir sınırlayıcı ile ayrılmış şekilde tek bir hücreye işlemeyi tercih edeceğiniz durumlar da vardır.

Bir Akıllı İşaretleyici etiketi içinde birlikte kullanılan `ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, tam olarak bu gereksinimi karşılar. Bu öznitelikler, dizi veri kaynaklarıyla yerel olarak çalışırken rapor düzenlerini kompakt ve öngörülebilir tutmanıza olanak tanır.

## **Bu Özelliğe Neden İhtiyaç Duyulur**

### **Varsayılan Dizi Yayılma Davranışı**

Bir Akıllı İşaretleyici bir dizi özelliğine başvurduğunda, Aspose.Cells varsayılan olarak diziyi birden çok hücreye genişletir. Örneğin, dört değer içeren bir `string[]` üzerindeki `&=Product.Tags` gibi bir işaretleyici, her değeri kendi hücresine yerleştirir, diğer şablon içeriklerini dışa doğru iter ve dikkatlice tasarlanmış rapor düzenlerini bozabilir.

### **Kullanım Senaryosu Sınırlamaları**

Varsayılan yayılma davranışının istenmediği birçok pratik senaryo vardır:

- **Özet tarzı raporlar** — kayıt başına kompakt tek satırlık bir düzen gerektiren.
- **Etiket, başlık veya anahtar kelime listeleri** — tek bir hücre içinde virgülle veya boru karakteriyle ayrılmış değerler olarak görüntülenmesi gereken.
- **Filtre öğeleri veya durum göstergeleri** — okunabilirlik için birden çok değeri tek bir yerde gruplayan.
- **Alt işlem hatları** (CSV dışa aktarma, PDF işleme, posta birleştirme) — genişletilmiş bir aralık yerine hücre başına tek bir birleştirilmiş değer bekleyen.
- **Platformlar arası uyumluluk** — bazı tüketicilerin birden çok hücreye yayılan dizilere tahammül edemeyeceği durumlar.

### **Doldurduğu Boşluk**

Yerleşik bir mekanizma olmadan, geliştiriciler Python'da verileri önceden işlemeye — dizileri çalışma kitabı tasarımcısına bağlamadan önce sınırlayıcıya sahip dizelere birleştirmeye — zorlanırdı. Bu durum mantığı çoğaltır, veri modellerini karmaşıklaştırır ve hata olasılığını artırır. `ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, biçimlendirmeyi Akıllı İşaretleyicinin kendisi içinde bildirimsel olarak işleyerek bu geçici çözümü ortadan kaldırır.

## **Özellik Avantajları**

Akıllı İşaretleyicilerinizde `ArrayAsSingle` ve `ExtraDelimiter` özniteliklerini kullanmak çeşitli avantajlar sağlar:

- **Tek hücrede sınırlandırma**: Tüm dizi öğeleri tam olarak tek bir hücreye işlenir, düzenler kompakt ve öngörülebilir kalır.
- **Özel sınırlayıcı kontrolü**: Virgül, noktalı virgül, kısa çizgi, boru, yeni satır veya herhangi bir özel metin gibi istediğiniz herhangi bir ayırıcı dizeyi belirtin.
- **Şablon tabanlı biçimlendirme**: Verileri önceden işlemek için ek kod gerekmez; biçimlendirme kuralları Akıllı İşaretleyici etiketinin içinde bulunur.
- **Daha temiz raporlar**: Dizi verileri artık komşu şablon içeriğini farklı satır veya sütunlara itelemez.
- **Çok yönlü veri türleri**: Dizeler, sayılar, tarihler ve sınırlayıcı ile birleştirilebilen diğer tüm veri türleriyle çalışır.
- **Geriye dönük uyumluluk**: Öznitelikler atlandığında, orijinal yayılma davranışı korunur, böylece mevcut şablonlar değişiklik olmadan çalışmaya devam eder.

## **Bu Özellik Nasıl Kullanılır**

### **Akıllı İşaretleyici Sözdizimi**

`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, standart bir Akıllı İşaretleyicinin parantezleri içinde anahtar-değer çiftleri olarak iletilir. Genel sözdizimi şöyledir:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

İşaretleyici aşağıdaki parçalardan oluşur:

- `&=DataSource.ArrayProperty` — bağlı veri kaynağındaki dizi özelliğine başvuran standart Akıllı İşaretleyici.
- `arrayasSingle=true` — motora tüm diziyi tek bir hücreye işlemesi talimatını verir. Yalnızca `true` değeri tek hücre davranışını tetikler.
- `extraDelimiter=", "` — dizi öğeleri arasına yerleştirilen ayırıcıyı tanımlar. Değer bir dize sabitidir; boş, tek karakterli veya çok karakterli bir dize olabilir.

{{% alert color="primary" %}}

`extraDelimiter` özniteliği, çok karakterli sınırlayıcılar, özel metinler veya yeni satırla ayrılmış çıktı için `\n` gibi kaçış dizileri dahil herhangi bir dize sabitini kabul eder. Dizi boşsa, sonuç hücre boş bırakılır.

{{% /alert %}}

### **Adım Adım İş Akışı**

Aşağıdaki iş akışı, bir diziyi Akıllı İşaretleyicileri kullanarak tek bir hücreye nasıl işleyeceğinizi açıklar.

1. **Veri kaynağını hazırlayın**: Bir dizi döndüren bir özellik sunan bir sınıf (veya veri yapısı) oluşturun. Özellik, `string[]`, `int[]` veya desteklenen herhangi bir dizi türünü döndürebilir.
2. **Tasarımcı çalışma kitabı oluşturun**: Yeni bir `Workbook` oluşturun, bir başlık satırı ekleyin ve `arrayasSingle` ile `extraDelimiter` özniteliklerini kullanarak dizi özelliğine başvuran bir Akıllı İşaretleyici hücresi yerleştirin.
3. **WorkbookDesigner'ı örnekleyin**: Bir `WorkbookDesigner` nesnesi oluşturun, tasarımcı çalışma kitabını ona ekleyin ve `set_data_source` yöntemini kullanarak veri kaynağınızı bağlayın.
4. **İşaretleyicileri işleyin**: Akıllı İşaretleyicileri genişletmek ve çalışma kitabını gerçek verilerle doldurmak için `WorkbookDesigner.process()` yöntemini çağırın.
5. **Sonucu kaydedin**: Ortaya çıkan çalışma kitabını XLSX veya desteklenen herhangi bir dosya biçiminde diske kaydedin.

### **Kod Örneği 1 — Temel Dize Dizisi İşleme**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

class Product:
    def __init__(self, tags):
        self._tags = tags
    
    def getTags(self):
        return self._tags

product = Product(["C#", "Aspose", "SmartMarker", "Excel"])

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Tags")
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")

designer = WorkbookDesigner()
designer.setWorkbook(workbook)
designer.setDataSource("Product", product)
designer.process()

workbook.save("output_arraySingle.xlsx")

jpype.shutdownJVM()
```

### **Kod Örneği 2 — Özel Sınırlayıcı ile Sayısal Dizi**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook

# Student sınıfını tanımla
class Student:
    def __init__(self):
        self.Scores = []

student = Student()
student.Scores = [95, 88, 76, 100, 67]

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Scores")
worksheet.getCells().get("A2").putValue(" - ".join(str(s) for s in student.Scores))

workbook.save("output_numericArray.xlsx")

jpype.shutdownJVM()
```

### **Kod Örneği 3 — Varsayılan ve ArrayAsSingle Davranışlarının Karşılaştırılması**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

# Veri kaynağını bir sözlük olarak tanımlayın (Order sınıfına eşdeğer)
order = {"Items": ["Apple", "Banana", "Cherry", "Date"]}

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Bölüm 1: Varsayılan Akıllı İşaretleyici - değerler hücreler boyunca yatay olarak yayılır
cells.get("A1").putValue("Default Spreading Behavior:")
cells.get("A2").putValue("&=Order.Items")

# Bölüm 2: arrayasSingle ve extraDelimiter kullanarak yeni tek hücreli oluşturma
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):")
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")")

# Veri kaynağını bağlayın ve Akıllı İşaretleyicileri işleyin
designer = WorkbookDesigner(workbook)
designer.setDataSource("Order", order)
designer.process()

# Ortaya çıkan çalışma kitabını kaydedin
workbook.save("output_comparison.xlsx")

jpype.shutdownJVM()
```

### **Notlar ve En İyi Uygulamalar**

`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleriyle çalışırken aşağıdaki noktaları aklınızda bulundurun:

- `extraDelimiter` değeri bir dize sabiti olarak ele alınır; şablon işlemcinizin yorumlayabileceği özel karakterleri kaçış karakteriyle belirtin.
- `arrayasSingle` özniteliği bir boole değeri (`true` / `false`) kabul eder. Yalnızca `true` tek hücre davranışını tetikler; diğer herhangi bir değer varsayılan yayılma davranışına geri döner.
- Dizi boş veya null ise, hücre boş bırakılır (veya veri türüne bağlı olarak boş bir dize içerir).
- Özellik, nesne veri kaynaklarının yanı sıra bir sütunun dizilere bölünebileceği `DataSet` ve `DataTable` kaynaklarıyla da çalışır.
- Yeni satırla ayrılmış çıktı için sınırlayıcı değeri olarak `\n` veya platformun yeni satır sabitini kullanabilirsiniz.
- Akıllı İşaretleyiciyi, sonuçta ortaya çıkan birleştirilmiş dizeyi görüntülemek için yeterli genişliğe sahip bir hücreye yerleştirin; aksi takdirde, içerik biçime bağlı olarak görsel olarak bitişik hücrelere taşabilir.

## **İlgili Makaleler**

- [Akıllı İşaretleyiciler](/cells/tr/python-java/smart-markers/)

{{< app/cells/assistant language="python" >}}