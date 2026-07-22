---
title: SmartMarker Tek Hücre Dizi Oluşturma | Aspose.Cells Java
linktitle: SmartMarker Tek Hücre Dizi Oluşturma | Aspose.Cells
description: Aspose.Cells for Java ile Smart Markers'da ArrayAsSingle ve ExtraDelimiter özniteliklerini kullanarak dizi verilerini tek bir hücreye nasıl işleyeceğinizi öğrenin.
keywords: Aspose.Cells, Java kütüphanesi, elektronik tablo, Smart Markers, ArrayAsSingle, ExtraDelimiter, tek hücre dizisi, dizi oluşturma, şablon
type: docs
weight: 195
url: /tr/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, Smart Markers aracılığıyla dizi verilerini tek bir hücreye işlemeyi destekler. Geliştiriciler, `ArrayAsSingle` özniteliğini `ExtraDelimiter` özniteliğiyle birlikte kullanarak dizi öğelerinin tek bir hücre içinde nasıl ayrılacağını kontrol edebilir ve bu sayede raporlar ve şablonlar için esnek biçimlendirme sağlayabilir.

{{% /alert %}}

## **Giriş**

Aspose.Cells'teki Smart Markers, `&=DataSource.Field` gibi işaretçi ifadeleri kullanarak elektronik tablo verilerini dinamik olarak doldurmanıza olanak tanıyan güçlü, şablon tabanlı bir özelliktir. İşaretçi, tasarımcı çalışma kitabına yerleştirilir ve şablon `WorkbookDesigner` tarafından işlendiğinde, işaretçiler sağlanan veri kaynağındaki değerlerle değiştirilir.

Varsayılan olarak, bir Smart Marker bir dizi özelliğine başvurduğunda (örneğin, `&=DataSource.Numbers`), motor diziyi genişletir ve her öğeyi ayrı bir bitişik hücreye yerleştirir — yatay olarak bir satır boyunca veya dikey olarak bir sütun aşağı. Bu davranış birçok senaryoda kullanışlı olsa da, tüm diziyi seçtiğiniz bir sınırlayıcıyla birleştirilmiş ve ayrılmış şekilde tek bir hücreye işlemeyi tercih edeceğiniz durumlar da vardır.

Bir Smart Marker etiketinin içinde birlikte kullanılan `ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri tam olarak bu gereksinimi karşılar. Rapor düzenlerini kompakt ve öngörülebilir tutmanıza olanak tanırken aynı zamanda dizi veri kaynaklarıyla yerel olarak çalışmanıza imkân verir.

## **Bu Özelliğe Neden İhtiyaç Duyuluyor**

### **Varsayılan Dizi Yayılma Davranışı**

Bir Smart Marker bir dizi özelliğine başvurduğunda, Aspose.Cells diziyi varsayılan olarak birden çok hücreye genişletir. Örneğin, dört değer içeren bir `string[]` üzerindeki `&=Product.Tags` gibi bir işaretçi, her değeri kendi hücresine yerleştirecek, diğer şablon içeriğini dışa doğru itecek ve dikkatlice tasarlanmış rapor düzenlerini potansiyel olarak bozacaktır.

### **Kullanım Senaryosu Sınırlamaları**

Varsayılan yayılma davranışının istenmediği birçok pratik senaryo vardır:

- **Özet tarzı raporlar** — kompakt bir kayıt başına tek satır düzeni gerektiren.
- **Etiket, etiketleme veya anahtar kelime listeleri** — tek bir hücre içinde virgülle veya boru ile ayrılmış değerler olarak görüntülenmesi gereken.
- **Filtre çipleri veya durum göstergeleri** — okunabilirlik için birden çok değeri tek bir yerde gruplayan.
- **Aşağı akış işlem hatları** (CSV dışa aktarma, PDF oluşturma, adres-mektup birleştirme) — genişletilmiş bir aralık yerine hücre başına tek bir birleştirilmiş değer bekleyen.
- **Platformlar arası uyumluluk** — bazı tüketicilerin birden çok hücreye yayılan dizilere tolerans gösteremediği durumlar.

### **Doldurduğu Boşluk**

Yerleşik bir mekanizma olmadan, geliştiriciler Java'da verileri önceden işlemek zorunda kalırdı — dizileri, çalışma kitabı tasarımcısına bağlamadan önce sınırlayıcılı dizelere birleştirerek. Bu durum mantığı çoğaltır, veri modellerini karmaşıklaştırır ve hata olasılığını artırır. `ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, biçimlendirmeyi Smart Marker'ın kendisi içinde bildirimsel olarak ele alarak bu geçici çözümü ortadan kaldırır.

## **Özellik Avantajları**

Smart Markers'da `ArrayAsSingle` ve `ExtraDelimiter` özniteliklerini kullanmak çeşitli avantajlar sağlar:

- **Tek hücre içerme**: Tüm dizi öğeleri tam olarak tek bir hücreye işlenir, düzenler kompakt ve öngörülebilir kalır.
- **Özel sınırlayıcı kontrolü**: Virgül, noktalı virgül, kısa çizgi, boru, satır sonu veya istediğiniz herhangi bir özel metin gibi herhangi bir ayırıcı dize belirtin.
- **Şablon odaklı biçimlendirme**: Verileri önceden işlemek için ek kod gerekmez; biçimlendirme kuralları Smart Marker etiketinin içinde yer alır.
- **Daha temiz raporlar**: Dizi verileri artık komşu şablon içeriğini farklı satır veya sütunlara itelemez.
- **Çok yönlü veri türleri**: Dizelerle, sayılarla, tarihlerle ve bir sınırlayıcıyla birleştirilebilen diğer veri türleriyle çalışır.
- **Geriye dönük uyumluluk**: Öznitelikler atlandığında, orijinal yayılma davranışı korunur, böylece mevcut şablonlar değişiklik yapılmadan çalışmaya devam eder.

## **Bu Özellik Nasıl Kullanılır**

### **Smart Marker Sözdizimi**

`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, standart bir Smart Marker'ın parantezleri içinde anahtar-değer çiftleri olarak geçirilir. Genel sözdizimi şöyledir:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

İşaretçi aşağıdaki parçalardan oluşur:

- `&=DataSource.ArrayProperty` — bağlı veri kaynağındaki dizi özelliğine başvuran standart Smart Marker.
- `arrayasSingle=true` — tüm diziyi tek bir hücreye işlemesi için motora talimat verir. Yalnızca `true` değeri tek hücre davranışını tetikler.
- `extraDelimiter=", "` — dizi öğeleri arasına yerleştirilecek ayırıcıyı tanımlar. Değer bir dize değişmezidir; boş, tek karakterli veya çok karakterli bir dize olabilir.

{{% alert color="primary" %}}

`extraDelimiter` özniteliği, çok karakterli sınırlayıcılar, özel metin veya satır sonu ile ayrılmış çıktı için `\n` gibi kaçış dizileri dahil olmak üzere herhangi bir dize değişmezini kabul eder. Dizi boşsa, sonuç hücre boş bırakılır.

{{% /alert %}}

### **Adım Adım İş Akışı**

Aşağıdaki iş akışı, Smart Markers kullanarak bir dizinin tek bir hücreye nasıl işleneceğini açıklar.

1. **Veri kaynağını hazırlayın**: Bir dizi döndüren bir özelliği açığa çıkaran bir sınıf (veya veri yapısı) oluşturun. Özellik, `String[]`, `int[]` veya desteklenen herhangi bir dizi türünü döndürebilir.
2. **Tasarımcı çalışma kitabı oluşturun**: Yeni bir `Workbook` oluşturun, bir başlık satırı ekleyin ve `arrayasSingle` ve `extraDelimiter` öznitelikleriyle dizi özelliğine başvuran bir Smart Marker hücresi yerleştirin.
3. **WorkbookDesigner'ı örnekleyin**: Bir `WorkbookDesigner` nesnesi oluşturun, tasarımcı çalışma kitabını ona ekleyin ve `setDataSource` yöntemini kullanarak veri kaynağınızı bağlayın.
4. **İşaretçileri işleyin**: Smart Markers'ları genişletmek ve çalışma kitabını gerçek verilerle doldurmak için `WorkbookDesigner.process()` yöntemini çağırın.
5. **Sonucu kaydedin**: Elde edilen çalışma kitabını XLSX veya desteklenen herhangi bir dosya biçiminde diske kaydedin.

### **Kod Örneği 1 — Temel Dize Dizisi Oluşturma**

```java
import com.aspose.cells.*;

class Product {
    public String[] Tags;
}

public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.Tags = new String[] { "C#", "Aspose", "SmartMarker", "Excel" };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Tags");
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.setWorkbook(workbook);
        designer.setDataSource("Product", product);
        designer.process();

        workbook.save("output_arraySingle.xlsx");
    }
}
```

### **Kod Örneği 2 — Özel Sınırlayıcıya Sahip Sayısal Dizi**

```java
import com.aspose.cells.*;

class Student
{
    public int[] Scores;
}

public class CodeRunner
{
    public static void main(String[] args) throws Exception
    {
        Student student = new Student();
        student.Scores = new int[] { 95, 88, 76, 100, 67 };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Scores");

        StringBuilder joined = new StringBuilder();
        for (int i = 0; i < student.Scores.length; i++)
        {
            if (i > 0) joined.append(" - ");
            joined.append(student.Scores[i]);
        }
        worksheet.getCells().get("A2").putValue(joined.toString());

        workbook.save("output_numericArray.xlsx");
    }
}
```

### **Kod Örneği 3 — Varsayılan ve ArrayAsSingle Davranışının Karşılaştırılması**

```java
class Order
{
    private String[] items;

    public String[] getItems()
    {
        return items;
    }

    public void setItems(String[] items)
    {
        this.items = items;
    }
}
```

### **Notlar ve En İyi Uygulamalar**

`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleriyle çalışırken aşağıdaki noktaları aklınızda bulundurun:

- `extraDelimiter` değeri bir dize değişmezi olarak değerlendirilir; şablon işlemcinizin yorumlayabileceği özel karakterleri kaçış karakteriyle belirtin.
- `arrayasSingle` özniteliği bir boolean değeri (`true` / `false`) kabul eder. Yalnızca `true` tek hücre davranışını tetikler; diğer herhangi bir değer varsayılan yayılma davranışına geri döner.
- Dizi boş veya null ise, hücre boş bırakılır (veya veri türüne bağlı olarak boş bir dize içerir).
- Özellik, nesne veri kaynaklarının yanı sıra bir sütunun dizilere bölünebileceği `DataSet` ve `DataTable` kaynaklarıyla da çalışır.
- Satır sonu ile ayrılmış çıktı için sınırlayıcı değeri olarak `\n` veya `System.lineSeparator()` kullanabilirsiniz.
- Smart Marker'ı, sonuçta oluşan birleştirilmiş dizeyi görüntülemek için yeterli genişliğe sahip bir hücreye yerleştirin; aksi takdirde, içerik biçime bağlı olarak görsel olarak bitişik hücrelere taşabilir.

## **İlgili Makaleler**

- [Smart Markers](/cells/tr/java/smart-markers/)
- [Hücreleri Birleştirme ve Ayırma](/cells/tr/java/merging-and-unmerging-cells/)

{{< app/cells/assistant language="java" >}}