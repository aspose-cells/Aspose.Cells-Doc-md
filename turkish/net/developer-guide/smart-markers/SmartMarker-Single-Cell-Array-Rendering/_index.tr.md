---
title: Akıllı İşaret Tek Hücre Dizisi Oluşturma | Aspose.Cells for .Net
description: `arrayassingle` ve `arraydelimiter` Akıllı İşaret özniteliklerini kullanarak Aspose.Cells for .Net ürününde dizi verisini tek hücreye oluşturmayı öğrenin.
linktitle: Tek Hücrede Dizi Oluşturma | Aspose.Cells
url: /tr/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, .NET kitaplığı, elektronik tablo, Akıllı İşaretler, arrayassingle, arraydelimiter, tek hücre dizisi, dizi oluşturma, şablon
type: docs
weight: 195
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, Akıllı İşaretler aracılığıyla bir dizi veri kaynağını tek bir hücreye oluşturabilir. `arrayassingle` özniteliği, öğelerin varsayılan olarak tek tek hücrelere yayılmasını devre dışı bırakır; `arraydelimiter` özniteliği ise birleştirilen öğeler arasına yerleştirilecek ayırıcıyı belirler. Bu ayırıcı varsayılan olarak virgüldür veya belirttiğiniz herhangi bir tek karakter ya da tırnak içinde çok karakterli dize olabilir.
{{% /alert %}}

## **Giriş**

Aspose.Cells içindeki Akıllı İşaretler, `&=DataSource.Field` gibi işaret ifadelerini kullanarak elektronik tablo verilerini dinamik olarak dolduran, şablona dayalı bir özelliktir. İşaret, tasarım çalışma kitabına yerleştirilir ve şablon `WorkbookDesigner` tarafından işlendiğinde işaretler, sağlanan veri kaynağındaki değerlerle değiştirilir.
Varsayılan olarak, bir Akıllı İşaret bir dizi özelliğine başvurduğunda (örneğin, dört değerlik `string[]` öğesine bağlanan `&=Product.Tags`), motor diziyi genişletir ve her öğeyi kendi hücresine yerleştirerek değerleri işaretin altındaki sütunda dikey olarak yayar. Bu davranış birçok senaryoda kullanışlı olsa da, dizinin tamamını öğeleri birleştirilmiş ve tercih ettiğiniz bir ayırıcıyla ayrılmış şekilde tek bir hücreye oluşturmak isteyebileceğiniz durumlar vardır.
`arrayassingle` ve `arraydelimiter` öznitelikleri, Akıllı İşaret'in parantezleri içinde `name:value` biçiminde yazılarak bu gereksinimi doğrudan karşılar. Rapor düzenlerini kompakt ve öngörülebilir tutmanıza olanak tanırken dizi veri kaynaklarıyla doğrudan çalışmanızı sağlar.

## **Bu Özelliğe Neden İhtiyaç Var**

### **Varsayılan Dizi Yayılma Davranışı**

Bir Akıllı İşaret bir dizi özelliğine başvurduğunda Aspose.Cells varsayılan olarak diziyi birden fazla hücreye yayınlar. Örneğin, dört değer içeren bir `string[]` üzerinde `&=Product.Tags` gibi bir işaret, her değeri işaretin altındaki kendi hücresine yerleştirir; diğer şablon içeriğini kaydırabilir ve özenle tasarlanmış rapor düzenlerini bozabilir.

### **Kullanım Senaryosu Sınırlamaları**

Varsayılan yayılma davranışının istenmediği birçok pratik senaryo vardır:
- **Özet tarzı raporlar** her kayıt için kompakt, tek satırlık bir düzen gerektirir.
- **Etiket, ad veya anahtar sözcük listeleri** virgülle veya dikey çizgiyle ayrılmış değerler olarak tek hücrede görüntülenmelidir.
- **Filtre çipleri veya durum göstergeleri** okunabilirlik için birden fazla değeri tek bir yerde gruplar.
- **Sonraki işlem hatları** (CSV dışa aktarma, PDF oluşturma, posta birleştirme), genişletilmiş bir aralık yerine hücre başına tek birleştirilmiş değer bekler.
- **Platformlar arası uyumluluk**, bazı tüketicilerin birden fazla hücreye yayılan dizileri kabul edememesi durumunda gereklidir.

### **Doldurduğu Boşluk**

Yerleşik bir mekanizma olmadan, geliştiriciler dizileri çalışma kitabı tasarımcısına bağlamadan önce C# veya VB.NET içinde önceden işlemek zorunda kalır; dizileri ayraçlı dizelere birleştirirler. Bu yaklaşım mantığı yineler, veri modellerini karmaşıklaştırır ve hata olasılığını artırır. `arrayassingle` ve `arraydelimiter` öznitelikleri, biçimlendirmeyi Akıllı İşaret'in kendisi içinde bildirimsel olarak ele alarak bu geçici çözümü ortadan kaldırır.

## **Özellik Avantajları**

Akıllı İşaretlerde `arrayassingle` ve `arraydelimiter` özniteliklerini kullanmak çeşitli avantajlar sağlar:
- **Tek hücrede toplama**: Tüm dizi öğeleri tam olarak bir hücreye oluşturulur; düzenler kompakt ve öngörülebilir kalır.
- **Özel ayırıcı denetimi**: İstediğiniz ayırıcıyı belirtin — varsayılan virgül, noktalı virgül, tire, dikey çizgi veya `" | "` gibi tırnak içinde çok karakterli dize.
- **Şablondan yönlendirilen biçimlendirme**: Veriyi önceden işlemek için ek kod gerekmez; biçimlendirme kuralları Akıllı İşaret etiketinin içinde bulunur.
- **Daha temiz raporlar**: Dizi verisi, komşu şablon içeriğini farklı satırlara veya sütunlara itmez.
- **Çok yönlü veri türleri**: Nesne veri kaynaklarındaki dize ve sayısal dizilerle çalışır.
- **Geriye uyumluluk**: Öznitelikler atlandığında özgün yayılma davranışı korunur; böylece mevcut şablonlar değişiklik yapılmadan çalışmaya devam eder.

## **Bu Özelliği Nasıl Kullanılır**

### **Akıllı İşaret Sözdizimi**

`arrayassingle` ve `arraydelimiter` öznitelikleri, standart bir Akıllı İşaret'in parantezleri içinde Aspose.Cells tarafından sunulan `name:value` öznitelik sözdizimini kullanır. Genel sözdizimi şöyledir:

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

İşaret aşağıdaki bölümlerden oluşur:
- `&=DataSource.ArrayProperty` — bağlı veri kaynağındaki dizi özelliğine başvuran standart Akıllı İşaret.
- `arrayassingle:true` — öğeleri yaymak yerine motorun dizinin tamamını tek hücreye oluşturmasını sağlar.
- `arraydelimiter:;` — isteğe bağlıdır; dizi öğeleri arasına yerleştirilecek ayırıcıyı tanımlar. Atlandığında virgül kullanılır.

{{% alert color="warning" %}}
Öznitelikleri `name:value` biçiminde yazın (eşittir işareti değil, iki nokta) ve birden fazla özniteliği virgülle **boşluksuz** ayırın. Virgülden sonra boşluk bırakmak, ayrıştırılan değeri bir karakter kaydırır; `(arrayassingle:true, arraydelimiter:;)` ifadesi, `;` yerine hatalı `:;` ayırıcısıyla birleştirir.
{{% /alert %}}

### **Ayırıcı Biçimleri**

- Tek karakter, iki noktadan hemen sonra yazılır: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Çok karakterli ayırıcı çift tırnak içinde yazılır: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Adım Adım İş Akışı**

Aşağıdaki iş akışı, Akıllı İşaretler kullanılarak bir dizinin tek hücreye nasıl oluşturulacağını açıklar.
1. **Veri kaynağını hazırlayın**: `string[]` veya `int[]` gibi bir dizi döndüren özelliği sunan bir sınıf oluşturun ve bu sınıfın `List<T>` koleksiyonunu bağlayın; böylece motor her satır için bir kayıt okur.
2. **Tasarım çalışma kitabı oluşturun**: Yeni bir `Workbook` oluşturun, başlık satırı ekleyin ve dizi özelliğine başvuran `arrayassingle` özniteliğine sahip bir Akıllı İşaret hücresi yerleştirin; özel bir ayırıcı gerektiğinde `arraydelimiter` özniteliğini de ekleyin.
3. **WorkbookDesigner örneğini oluşturun**: Çalışma kitabının çevresinde bir `WorkbookDesigner` oluşturun ve veri kaynağınızı `SetDataSource` ile bağlayın.
4. **İşaretleri işleyin**: Akıllı İşaretleri genişletmek ve çalışma kitabını gerçek verilerle doldurmak için `WorkbookDesigner.Process()` yöntemini çağırın.
5. **Sonucu kaydedin**: Oluşturulan çalışma kitabını XLSX veya desteklenen başka bir dosya biçiminde diske kaydedin.

### **Kod Örneği 1 — Temel Dize Dizisi Oluşturma**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Product
    {
        public string[] Tags { get; set; }
    }

    static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Product", new List<Product> { product });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-single.xlsx");
    }
}
```

Örnek, dizinin tamamının birleştirilmiş değerini yazdırır. Dört etiket, varsayılan virgülle ayrılarak tek bir hücreye yerleşir:

```
C#,Aspose,SmartMarker,Excel
```

### **Kod Örneği 2 — Özel Ayırıcılı Sayısal Dizi**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Student
    {
        public int[] Scores { get; set; }
    }

    static void Main()
    {
        Student student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Scores");
        // arraydelimiter:- joins the numbers with a hyphen
        worksheet.Cells["A2"].PutValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Student", new List<Student> { student });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-numeric.xlsx");
    }
}
```

Sayısal diziler, dize dizileriyle tam olarak aynı şekilde birleştirilir; her öğe düz sayısal metnini korur:

```
95-88-76-100-67
```

### **Kod Örneği 3 — Varsayılan ile Tek Hücreye Oluşturmanın Karşılaştırılması**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Order
    {
        public string[] Items { get; set; }
    }

    static void Main()
    {
        Order order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        Cells cells = sheet.Cells;
        // Column B: default marker — values spread vertically down the column
        cells["B1"].PutValue("Default");
        cells["B2"].PutValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells["C1"].PutValue("Single cell");
        cells["C2"].PutValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", new List<Order> { order });
        designer.Process();
        for (int row = 1; row <= 5; row++)
        {
            string b = cells[row, 1].StringValue;
            string c = cells[row, 2].StringValue;
            if (!string.IsNullOrEmpty(b) || !string.IsNullOrEmpty(c))
                Console.WriteLine($"B{row + 1}=[{b}]  C{row + 1}=[{c}]");
        }
        workbook.Save("output-array-comparison.xlsx");
    }
}
```

Varsayılan işaret, her öğe için B sütununda bir hücre kullanırken `arrayassingle` işareti aynı diziyi C sütununda tek bir hücreye toplar:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Notlar ve En İyi Uygulamalar**

`arrayassingle` ve `arraydelimiter` öznitelikleriyle çalışırken aşağıdaki noktaları göz önünde bulundurun:
- Öznitelik değerleri `name:value` biçimini kullanır. `arrayassingle=true` gibi eşittir işareti kullanılan biçim tanınmaz ve sessizce varsayılan yayılma davranışına geri döner.
- Öznitelikleri virgülle ve boşluksuz ayırın; virgülden sonra boşluk, ayırıcı değerini bir karakter kaydırır (yukarıdaki uyarıya bakın).
- `arraydelimiter` değeri, iki noktadan hemen sonra doğrudan yazılan tek bir karakter veya çift tırnak içine alınmış çok karakterli bir dize olabilir.
- `arraydelimiter` atlandığında öğeler virgülle birleştirilir.
- Veri kaynağı, motorun kayıtları listelemesine izin vermelidir: dizi özelliğini sunan öğe türüne sahip bir `List<T>` (veya başka bir koleksiyon) bağlayın. Tek bir nesneyi bağlamak, gövde işaretlerinin çözümlenmeden kalmasına neden olur.
- Aynı öznitelikler dize ve sayısal diziler için çalışır; her öğe düz değer metniyle oluşturulur.

## **İlgili Makaleler**
- [Aspose.Cells for .NET'te PivotTable'a filtre alanları ekleme](/cells/tr/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .NET'te Pivot Tablolarına Stil Uygulama](/cells/tr/net/apply-style-to-pivot-table/)
- [Pivot tablosunda sayfa alanı düzenini değiştirme](/cells/tr/net/change-page-field-layout/)
- [Aspose.Cells for .NET'te Sparkline'ı Görüntüye ve HTML'e Dönüştürme](/cells/tr/net/convert-sparkline-to-image-and-html/)
- [Excel'i OFD biçimine dönüştürme](/cells/tr/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}