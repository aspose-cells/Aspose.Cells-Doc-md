---
title: Akıllı İşaretleyici Tek Hücre Dizi Oluşturma | Aspose.Cells .NET
linktitle: Akıllı İşaretleyici Tek Hücre Dizi Oluşturma | Aspose.Cells .NET
description: Aspose.Cells for .NET ile Akıllı İşaretleyicilerdeki ArrayAsSingle ve ExtraDelimiter özniteliklerini kullanarak dizi verilerini tek bir hücreye nasıl oluşturacağınızı öğrenin.
keywords: Aspose.Cells, .NET kütüphanesi, elektronik tablo, Akıllı İşaretleyiciler, ArrayAsSingle, ExtraDelimiter, tek hücre dizisi, dizi oluşturma, şablon
type: docs
weight: 195
url: /tr/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, Akıllı İşaretleyiciler aracılığıyla dizi verilerini tek bir hücreye oluşturmayı destekler. Geliştiriciler, `ArrayAsSingle` özniteliğini `ExtraDelimiter` özniteliğiyle birlikte kullanarak dizi öğelerinin tek bir hücre içinde nasıl ayrılacağını kontrol edebilir ve raporlar ile şablonlar için esnek biçimlendirme sağlayabilir.
{{% /alert %}}

## **Introduction**
Aspose.Cells'deki Akıllı İşaretleyiciler, `&=DataSource.Field` gibi işaretleyici ifadeleri kullanarak elektronik tablo verilerini dinamik olarak doldurmanıza olanak tanıyan, şablon tabanlı güçlü bir özelliktir. İşaretleyici bir tasarımcı çalışma kitabına yerleştirilir ve şablon `WorkbookDesigner` tarafından işlendiğinde, işaretleyiciler sağlanan veri kaynağındaki değerlerle değiştirilir.
Varsayılan olarak, bir Akıllı İşaretleyici bir dizi özelliğine başvurduğunda (örneğin, `&=DataSource.Numbers`), motor diziyi genişletir ve her öğeyi ayrı bir bitişik hücreye yerleştirir — yatay olarak bir satır boyunca ya da dikey olarak bir sütun boyunca. Bu davranış birçok senaryoda kullanışlı olsa da, tüm diziyi seçtiğiniz bir sınırlayıcıyla ayrılmış ve birleştirilmiş biçimde tek bir hücreye oluşturmayı tercih edeceğiniz durumlar vardır.
Bir Akıllı İşaretleyici etiketi içinde birlikte kullanılan `ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri tam olarak bu gereksinimi karşılar. Rapor düzenlerini kompakt ve öngörülebilir tutarken yine de dizi veri kaynaklarıyla yerel olarak çalışmanıza olanak tanırlar.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
Bir Akıllı İşaretleyici bir dizi özelliğine başvurduğunda, Aspose.Cells diziyi varsayılan olarak birden çok hücreye genişletir. Örneğin, dört değer içeren bir `string[]` üzerindeki `&=Product.Tags` gibi bir işaretleyici, her değeri kendi hücresine yerleştirir, diğer şablon içeriğini dışa doğru iter ve özenle tasarlanmış rapor düzenlerini potansiyel olarak bozar.

### **Use Case Limitations**
Varsayılan yayılma davranışının istenmediği birçok pratik senaryo vardır:
- **Özet tarzı raporlar** — kayıt başına kompakt tek satır düzeni gerektiren.
- **Etiket veya anahtar kelime listeleri** — tek bir hücre içinde virgülle veya boru karakteriyle ayrılmış değerler olarak görüntülenmesi gereken.
- **Filtre çipleri veya durum göstergeleri** — okunabilirlik için birden çok değeri tek bir yerde gruplayan.
- **Aşağı yöndeki işlem hatları** (CSV dışa aktarma, PDF oluşturma, posta birleştirme) — genişletilmiş bir aralık yerine hücre başına tek bir birleşik değer bekleyen.
- **Platformlar arası uyumluluk** — bazı tüketicilerin birden çok hücreye yayılan dizilere tahammül edemediği durumlar.

### **The Gap It Fills**
Yerleşik bir mekanizma olmadan, geliştiriciler verileri C# veya VB.NET'te önceden işlemeye — dizileri çalışma kitabı tasarımcısına bağlamadan önce sınırlayıcılı dizelere birleştirmeye zorlanırdı. Bu, mantığı çoğaltır, veri modellerini karmaşıklaştırır ve hata olasılığını artırır. `ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, biçimlendirmeyi Akıllı İşaretleyicinin kendisi içinde bildirimsel olarak ele alarak bu geçici çözümü ortadan kaldırır.

## **Feature Benefits**
Akıllı İşaretleyicilerinizde `ArrayAsSingle` ve `ExtraDelimiter` özniteliklerini kullanmak birkaç avantaj sağlar:
- **Tek hücrede kapsama**: Tüm dizi öğeleri tam olarak tek bir hücreye oluşturulur, bu da düzenleri kompakt ve öngörülebilir tutar.
- **Özel sınırlayıcı kontrolü**: İstediğiniz herhangi bir ayırıcı dizeyi belirtin — virgül, noktalı virgül, kısa çizgi, boru karakteri, yeni satır veya herhangi bir özel metin.
- **Şablon odaklı biçimlendirme**: Verileri önceden işlemek için ek kod gerekmez; biçimlendirme kuralları Akıllı İşaretleyici etiketinin içinde yer alır.
- **Daha temiz raporlar**: Dizi verileri artık komşu şablon içeriğini farklı satır veya sütunlara itmez.
- **Çok yönlü veri türleri**: Dizeler, sayılar, tarihler ve sınırlayıcıyla birleştirilebilen diğer tüm veri türleriyle çalışır.
- **Geriye dönük uyumluluk**: Öznitelikler atlandığında, orijinal yayılma davranışı korunur, böylece mevcut şablonlar değişmeden çalışmaya devam eder.

## **How to Use This Feature**

### **Smart Marker Syntax**
`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, standart bir Akıllı İşaretleyicinin parantezleri içinde anahtar-değer çiftleri olarak geçirilir. Genel sözdizimi şöyledir:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

İşaretleyici aşağıdaki parçalardan oluşur:
- `&=DataSource.ArrayProperty` — bağlı veri kaynağındaki dizi özelliğine başvuran standart Akıllı İşaretleyici.
- `arrayasSingle=true` — motora tüm diziyi tek bir hücreye oluşturması talimatını verir. Yalnızca `true` değeri tek hücre davranışını tetikler.
- `extraDelimiter=", "` — dizi öğeleri arasına yerleştirilecek ayırıcıyı tanımlar. Değer bir dize sabitidir; boş, tek karakterli veya çok karakterli bir dize olabilir.

{{% alert color="primary" %}}
`extraDelimiter` özniteliği, çok karakterli sınırlayıcılar, özel metinler veya yeni satırla ayrılmış çıktı için `\n` gibi kaçış dizileri dahil olmak üzere herhangi bir dize sabitini kabul eder. Dizi boşsa, sonuç hücresi boş bırakılır.

### **Step-by-Step Workflow**
Aşağıdaki iş akışı, Akıllı İşaretleyicileri kullanarak bir dizinin tek bir hücreye nasıl oluşturulacağını açıklar.
1. **Veri kaynağını hazırlayın**: Bir dizi döndüren bir özellik sunan bir sınıf (veya veri yapısı) oluşturun. Özellik `string[]`, `int[]` veya desteklenen herhangi bir dizi türünü döndürebilir.
2. **Bir tasarımcı çalışma kitabı oluşturun**: Yeni bir `Workbook` oluşturun, bir başlık satırı ekleyin ve `arrayasSingle` ile `extraDelimiter` özniteliklerini kullanarak dizi özelliğine başvuran bir Akıllı İşaretleyici hücresi yerleştirin.
3. **WorkbookDesigner'ı örnekleyin**: Bir `WorkbookDesigner` nesnesi oluşturun, tasarımcı çalışma kitabını ona bağlayın ve `SetDataSource` yöntemini kullanarak veri kaynağınızı bağlayın.
4. **İşaretleyicileri işleyin**: Akıllı İşaretleyicileri genişletmek ve çalışma kitabını gerçek verilerle doldurmak için `WorkbookDesigner.Process()` yöntemini çağırın.
5. **Sonucu kaydedin**: Elde edilen çalışma kitabını diske XLSX veya desteklenen herhangi bir dosya biçiminde kaydedin.

### **Code Example 1 — Basic String Array Rendering**

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

### **Code Example 2 — Numeric Array with Custom Delimiter**

```csharp
public class Student
{
    public int[] Scores { get; set; }
}
public class Program
{
    public static void Main()
    {
        var student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };
        var workbook = new Workbook();
        var worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Scores");
        worksheet.Cells["A2"].PutValue(string.Join(" - ", student.Scores));
        workbook.Save("output_numericArray.xlsx");
    }
}
```

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

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
        // Bölüm 1: Varsayılan Akıllı İşaretleyici - değerler hücreler arasında yatay olarak yayılır
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

### **Notes & Best Practices**
`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleriyle çalışırken aşağıdaki noktaları akılda bulundurun:
- `extraDelimiter` değeri bir dize sabiti olarak ele alınır; şablon işlemcinizin yorumlayabileceği özel karakterleri kaçışla işaretleyin.
- `arrayasSingle` özniteliği bir boole değeri kabul eder (`true` / `false`). Yalnızca `true` tek hücre davranışını tetikler; diğer herhangi bir değer varsayılan yayılma davranışına geri döner.
- Dizi boş veya null ise, hücre boş bırakılır (veya veri türüne bağlı olarak boş bir dize içerir).
- Özellik, nesne veri kaynaklarıyla olduğu kadar bir sütunun dizilere bölünebildiği `DataSet` ve `DataTable` kaynaklarıyla da çalışır.
- Yeni satırla ayrılmış çıktı için, sınırlayıcı değeri olarak `\n` veya `Environment.NewLine` kullanabilirsiniz.
{{% /alert %}}

## Related Articles
- [Aspose.Cells for .NET'te Pivot Tablosuna Filtre Alanı Ekleme](/cells/tr/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .NET'te Pivot Tablolarına Stil Uygulama](/cells/tr/net/apply-style-to-pivot-table/)
- [Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme](/cells/tr/net/change-page-field-layout/)
- [Sparkline'ı Aspose.Cells for .NET'te Görüntüye ve HTML'ye Dönüştürme](/cells/tr/net/convert-sparkline-to-image-and-html/)
- [Excel'i OFD Biçimine Dönüştürme](/cells/tr/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}