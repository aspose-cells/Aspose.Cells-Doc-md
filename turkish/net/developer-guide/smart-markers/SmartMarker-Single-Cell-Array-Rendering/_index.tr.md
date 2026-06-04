---
title: SmartMarker Tek Hücre Dizi İşleme | Aspose.Cells .NET
description: Aspose.Cells for .NET ile Smart Markers'da ArrayAsSingle ve ExtraDelimiter niteliklerini kullanarak dizi verilerini tek bir hücreye nasıl işleyeceğinizi öğrenin.
keywords: Aspose.Cells, .NET kütüphanesi, elektronik tablo, Smart Markers, ArrayAsSingle, ExtraDelimiter, tek hücre dizisi, dizi işleme, şablon
type: docs
weight: 195
url: /tr/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells, Smart Markers aracılığıyla dizi verilerinin tek bir hücreye işlenmesini destekler. Geliştiriciler, `ArrayAsSingle` niteliğini `ExtraDelimiter` niteliğiyle birlikte kullanarak dizi öğelerinin tek bir hücre içinde nasıl ayrılacağını kontrol edebilir ve raporlar ile şablonlar için esnek biçimlendirme sağlayabilir.

{{% /alert %}}

## **Giriş**

Aspose.Cells'teki Smart Markers, `&=DataSource.Field` gibi işaretçi ifadelerini kullanarak elektronik tablo verilerini dinamik olarak doldurmanıza olanak tanıyan güçlü, şablon tabanlı bir özelliktir. İşaretçi, tasarımcı çalışma kitabına yerleştirilir ve şablon `WorkbookDesigner` tarafından işlendiğinde, işaretçiler sağlanan veri kaynağındaki değerlerle değiştirilir.

Varsayılan olarak, bir Smart Marker bir dizi özelliğine başvurduğunda (örneğin, `&=DataSource.Numbers`), motor diziyi genişletir ve her öğeyi ayrı bir bitişik hücreye yerleştirir — ya bir satır boyunca yatay olarak ya da bir sütun boyunca dikey olarak. Bu davranış birçok senaryoda kullanışlı olsa da, tüm diziyi tek bir hücreye işlemeyi, öğeleri birleştirilmiş ve istediğiniz bir sınırlayıcı ile ayrılmış şekilde oluşturmayı tercih edeceğiniz durumlar da vardır.

Bir Smart Marker etiketinin içinde birlikte kullanılan `ArrayAsSingle` ve `ExtraDelimiter` nitelikleri tam olarak bu gereksinimi karşılar. Rapor düzenlerini kompakt ve öngörülebilir tutarken dizi veri kaynaklarıyla yerel olarak çalışmanıza olanak tanır.

## **Bu Özelliğe Neden İhtiyaç Duyuluyor**

### **Varsayılan Dizi Yayılma Davranışı**

Bir Smart Marker bir dizi özelliğine başvurduğunda, Aspose.Cells diziyi varsayılan olarak birden fazla hücreye genişletir. Örneğin, dört değer içeren bir `string[]` üzerindeki `&=Product.Tags` gibi bir işaretçi, her değeri kendi hücresine yerleştirir, diğer şablon içeriğini dışa doğru iterek özenle tasarlanmış rapor düzenlerini potansiyel olarak bozar.

### **Kullanım Durumu Sınırlamaları**

Varsayılan yayılma davranışının istenmediği birçok pratik senaryo vardır:

- Kompakt bir kayıt başına tek satır düzeni gerektiren **özet stili raporlar**.
- Tek bir hücre içinde virgülle veya boru ile ayrılmış değerler olarak görüntülenmesi gereken **etiket, etiket veya anahtar kelime listeleri**.
- Okunabilirlik için birden fazla değeri tek bir yerde gruplandıran **filtre çipleri veya durum göstergeleri**.
- Genişletilmiş bir aralık yerine hücre başına tek bir birleşik değer bekleyen **aşağı akış işlem hatları** (CSV dışa aktarma, PDF işleme, posta birleştirme).
- Bazı tüketicilerin birden fazla hücreye yayılan dizilere tolerans gösteremeyeceği **çapraz platform uyumluluğu**.

### **Doldurduğu Boşluk**

Yerleşik bir mekanizma olmadan, geliştiriciler C# veya VB.NET'te verileri önceden işlemeye — dizileri çalışma kitabı tasarımcısına bağlamadan önce sınırlayıcı içeren dizelere birleştirmeye — zorlanırdı. Bu, mantığı çoğaltır, veri modellerini karmaşıklaştırır ve hata olasılığını artırır. `ArrayAsSingle` ve `ExtraDelimiter` nitelikleri, biçimlendirmeyi Smart Marker'ın içinde bildirimsel olarak işleyerek bu geçici çözümü ortadan kaldırır.

## **Özellik Avantajları**

Smart Markers'larınızda `ArrayAsSingle` ve `ExtraDelimiter` niteliklerini kullanmak birçok avantaj sağlar:

- **Tek hücre kapsama**: Tüm dizi öğeleri tam olarak tek bir hücreye işlenir, düzenler kompakt ve öngörülebilir kalır.
- **Özel sınırlayıcı kontrolü**: İstediğiniz herhangi bir ayırıcı dizesi belirtin — virgül, noktalı virgül, kısa çizgi, boru, yeni satır veya herhangi bir özel metin.
- **Şablon odaklı biçimlendirme**: Verileri önceden işlemek için ek kod gerekmez; biçimlendirme kuralları Smart Marker etiketinin içinde yer alır.
- **Daha temiz raporlar**: Dizi verileri artık komşu şablon içeriğini farklı satırlara veya sütunlara itmez.
- **Çok yönlü veri türleri**: Dizeler, sayılar, tarihler ve bir sınırlayıcı ile birleştirilebilen diğer veri türleriyle çalışır.
- **Geriye dönük uyumluluk**: Nitelikler atlandığında, orijinal yayılma davranışı korunur, böylece mevcut şablonlar değişmeden çalışmaya devam eder.

## **Bu Özellik Nasıl Kullanılır**

### **Smart Marker Sözdizimi**

`ArrayAsSingle` ve `ExtraDelimiter` nitelikleri, standart bir Smart Marker'ın parantezleri içinde anahtar-değer çiftleri olarak geçirilir. Genel sözdizimi şudur:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

İşaretçi aşağıdaki parçalardan oluşur:

- `&=DataSource.ArrayProperty` — bağlı veri kaynağındaki dizi özelliğine başvuran standart Smart Marker.
- `arrayasSingle=true` — motora tüm diziyi tek bir hücreye işlemesi talimatını verir. Yalnızca `true` değeri tek hücre davranışını tetikler.
- `extraDelimiter=", "` — dizi öğeleri arasına yerleştirilen ayırıcıyı tanımlar. Değer bir dize değişmezidir; boş, tek karakterli veya çok karakterli bir dize olabilir.

{{% alert color="primary" %}}

`extraDelimiter` niteliği, çok karakterli sınırlayıcılar, özel metinler veya yeni satırla ayrılmış çıktı için `\n` gibi kaçış dizileri dahil olmak üzere herhangi bir dize değişmezini kabul eder. Dizi boşsa, sonuç hücre boş bırakılır.

{{% /alert %}}

### **Adım Adım İş Akışı**

Aşağıdaki iş akışı, Smart Markers kullanarak bir dizinin tek bir hücreye nasıl işleneceğini açıklar.

1. **Veri kaynağını hazırlayın**: Bir dizi döndüren bir özelliği açığa çıkaran bir sınıf (veya veri yapısı) oluşturun. Özellik `string[]`, `int[]` veya desteklenen herhangi bir dizi türü döndürebilir.
2. **Tasarımcı çalışma kitabı oluşturun**: Yeni bir `Workbook` oluşturun, bir başlık satırı ekleyin ve `arrayasSingle` ve `extraDelimiter` nitelikleriyle dizi özelliğine başvuran bir Smart Marker hücresi yerleştirin.
3. **WorkbookDesigner'ı örnekleyin**: Bir `WorkbookDesigner` nesnesi oluşturun, tasarımcı çalışma kitabını ona ekleyin ve `SetDataSource` yöntemini kullanarak veri kaynağınızı bağlayın.
4. **İşaretçileri işleyin**: Smart Markers'ları genişletmek ve çalışma kitabını gerçek verilerle doldurmak için `WorkbookDesigner.Process()` yöntemini çağırın.
5. **Sonucu kaydedin**: Ortaya çıkan çalışma kitabını XLSX veya desteklenen başka bir dosya biçiminde diske kaydedin.

### **Kod Örneği 1 — Temel Dize Dizisi İşleme**

```csharp
using System;
using Aspose.Cells;

class Program
{
    public class Product
    {
        public string[] Tags { get; set; }
    }

    public static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];

        worksheet.Cells["A1"].PutValue("Tags");
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.Workbook = workbook;
        designer.SetDataSource("Product", product);
        designer.Process();

        workbook.Save("output_arraySingle.xlsx");
    }
}
```

### **Kod Örneği 2 — Özel Sınırlayıcılı Sayısal Dizi**

```csharp
using System;
using Aspose.Cells;

public class Student
{
    public int[] Scores { get; set; }
}

public class Program
{
    public static void Main()
    {
        Student student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];

        worksheet.Cells["A1"].PutValue("Scores");
        worksheet.Cells["A2"].PutValue("&=Student.Scores(arrayasSingle=true, extraDelimiter=\" - \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.Workbook = workbook;
        designer.SetDataSource("Student", student);
        designer.Process();

        workbook.Save("output_numericArray.xlsx");
    }
}
```

### **Kod Örneği 3 — Varsayılan ve ArrayAsSingle Davranışının Karşılaştırılması**

```csharp
using System;
using Aspose.Cells;

public class Program
{
    public static void Main()
    {
        var order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };

        var workbook = new Workbook();
        var sheet = workbook.Worksheets[0];
        var cells = sheet.Cells;

        // Bölüm 1: Varsayılan Akıllı İşaretleyici - değerler hücreler boyunca yatay olarak yayılır
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");

        // Bölüm 2: arrayasSingle ve extraDelimiter kullanarak yeni tek hücreli oluşturma
        cells["A4"].PutValue("Single Cell Rendering (arrayasSingle=true):");
        cells["A5"].PutValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

        // Veri kaynağını bağla ve Akıllı İşaretleyicileri işle
        var designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", order);
        designer.Process();

        // Ortaya çıkan çalışma kitabını kaydet
        workbook.Save("output_comparison.xlsx");
    }
}

public class Order
{
    public string[] Items { get; set; }
}
```

### **Notlar ve En İyi Uygulamalar**

`ArrayAsSingle` ve `ExtraDelimiter` nitelikleriyle çalışırken aşağıdaki noktaları aklınızda bulundurun:

- `extraDelimiter` değeri bir dize değişmezi olarak işlenir; şablon işlemcinizin yorumlayabileceği özel karakterleri kaçış yoluyla belirtin.
- `arrayasSingle` niteliği bir boole değeri kabul eder (`true` / `false`). Yalnızca `true` tek hücre davranışını tetikler; diğer herhangi bir değer varsayılan yayılma davranışına geri döner.
- Dizi boş veya null ise, hücre boş bırakılır (veya veri türüne bağlı olarak boş bir dize içerir).
- Özellik, bir sütunun dizilere bölünebileceği `DataSet` ve `DataTable` kaynaklarının yanı sıra nesne veri kaynaklarıyla da çalışır.
- Yeni satırla ayrılmış çıktı için sınırlayıcı değeri olarak `\n` veya `Environment.NewLine` kullanabilirsiniz.
- Smart Marker'ı, sonuçta birleştirilmiş dizeyi görüntülemek için yeterli genişliğe sahip bir hücreye yerleştirin; aksi takdirde, içerik biçime bağlı olarak bitişik hücrelere görsel olarak taşabilir.

## **İlgili Makaleler**

- [Smart Markers](/cells/tr/net/smart-markers/)
- [Hücreleri Birleştirme ve Ayırma](/cells/tr/net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="csharp" >}}