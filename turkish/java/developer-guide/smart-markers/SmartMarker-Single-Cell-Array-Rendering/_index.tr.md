---
title: Akıllı İşaretçilerle Tek Hücrede Dizi Oluşturma | Aspose.Cells for Java
linktitle: Akıllı İşaretçilerle Tek Hücrede Dizi Oluşturma | Aspose.Cells for Java
description: arrayassingle ve arraydelimiter Akıllı İşaretçi özniteliklerini kullanarak dizi verisini tek bir hücrede nasıl oluşturacağınızı Aspose.Cells for Java ile öğrenin.
keywords: Aspose.Cells, Java kitaplığı, elektronik tablo, Akıllı İşaretçiler, arrayassingle, arraydelimiter, tek hücre dizisi, dizi oluşturma, şablon
type: docs
weight: 195
url: /tr/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, Akıllı İşaretçiler aracılığıyla bir dizi veri kaynağını tek hücrede işleyebilir. `arrayassingle` özniteliği, öğelerin tek tek yayılmasına yönelik varsayılan davranışı devre dışı bırakır; `arraydelimiter` özniteliği ise birleştirilen öğeler arasına yerleştirilecek ayırıcıyı belirler. Ayırıcı varsayılan olarak virgüldür; belirttiğiniz tek bir karakter veya tırnak içine alınmış çok karakterli bir dize de kullanılabilir.
{{% /alert %}}

## **Giriş**

Aspose.Cells içindeki Akıllı İşaretçiler, `&=DataSource.Field` gibi işaretçi ifadelerini kullanarak elektronik tablo verisini dinamik olarak dolduran şablona dayalı bir özelliktir. İşaretçi, tasarım çalışma kitabına yerleştirilir ve şablon `WorkbookDesigner` tarafından işlendiğinde sağlanan veri kaynağındaki değerlerle değiştirilir.
Varsayılan olarak, bir Akıllı İşaretçi bir dizi özelliğine başvurduğunda (örneğin, dört değer içeren bir `String[]` dizisine bağlı `&=Product.Tags` işaretçisi), motor diziyi genişletir ve her öğeyi kendi hücresine yerleştirerek değerleri işaretçinin bulunduğu sütunda aşağı doğru yayar. Bu davranış birçok senaryoda kullanışlı olsa da, tüm diziyi öğeleri birleştirerek ve kendiniz seçtiğiniz bir ayırıcıyla ayırarak tek hücreye yerleştirmek istediğiniz durumlar vardır.
`arrayassingle` ve `arraydelimiter` öznitelikleri, bir Akıllı İşaretçi'nin parantezleri içinde `name:value` biçiminde yazılarak tam olarak bu ihtiyacı karşılar. Bu öznitelikler, rapor düzenlerini kompakt ve öngörülebilir tutarken dizi veri kaynaklarıyla doğrudan çalışmanızı sağlar.

## **Bu Özelliğe Neden İhtiyaç Duyulur**

### **Varsayılan Dizi Yayma Davranışı**

Bir Akıllı İşaretçi bir dizi özelliğine başvurduğunda Aspose.Cells varsayılan olarak diziyi birden fazla hücreye yayar. Örneğin, `&=Product.Tags` işaretçisi dört değer içeren bir `String[]` dizisine başvurduğunda her değer işaretçinin altındaki ayrı bir hücreye yerleştirilir; bu durum diğer şablon içeriğini kaydırarak özenle tasarlanmış rapor düzenlerini bozabilir.

### **Kullanım Senaryolarındaki Sınırlamalar**

Varsayılan yayma davranışının uygun olmadığı birçok pratik senaryo bulunur:
- **Özet raporları** — kayıt başına tek satırlık, kompakt bir düzen gerektiren raporlar.
- **Etiket, ad etiketi veya anahtar kelime listeleri** — tek bir hücre içinde virgülle veya dikey çizgiyle ayrılmış değerler olarak gösterilmesi gerekenler.
- **Filtre çipleri veya durum göstergeleri** — okunabilirlik için birden fazla değeri tek bir yerde gruplayanlar.
- **Devamındaki işlem hatları** (CSV dışa aktarma, PDF oluşturma, posta birleştirme) — genişletilmiş bir aralık yerine hücre başına tek birleştirilmiş değer bekleyenler.
- **Platformlar arası uyumluluk** — dizilerin birden fazla hücreye yayılmasını kabul edemeyen bazı tüketiciler.

### **Doldurduğu Boşluk**

Yerleşik bir mekanizma bulunmadığında geliştiriciler veriyi Java'da önceden işlemek zorunda kalırdı; dizileri çalışma kitabı tasarımcısına bağlamadan önce ayırıcı içeren dizelere birleştirirlerdi. Bu yaklaşım mantığı tekrarlar, veri modellerini karmaşıklaştırır ve hata olasılığını artırır. `arrayassingle` ve `arraydelimiter` öznitelikleri, biçimlendirmeyi doğrudan Akıllı İşaretçi'nin içinde ele alarak bu geçici çözümü ortadan kaldırır.

## **Özellik Avantajları**

Akıllı İşaretçilerde `arrayassingle` ve `arraydelimiter` özniteliklerini kullanmak birçok avantaj sağlar:
- **Tek hücrede toplama**: Tüm dizi öğeleri tam olarak tek hücrede oluşturulur; düzenler kompakt ve öngörülebilir kalır.
- **Özel ayırıcı denetimi**: İstediğiniz ayırıcıyı belirtin — varsayılan virgül, noktalı virgül, tire, `|` karakteri veya `" | "` gibi tırnak içine alınmış çok karakterli bir dize.
- **Şablona dayalı biçimlendirme**: Veriyi önceden işlemek için ek kod gerekmez; biçimlendirme kuralları Akıllı İşaretçi etiketinin içinde yer alır.
- **Daha temiz raporlar**: Dizi verisi, komşu şablon içeriğini artık farklı satırlara veya sütunlara kaydırmaz.
- **Esnek veri türleri**: Dize dizileriyle ve JavaBean veri kaynaklarından dize olarak işlenen sayısal değerlerle çalışır.
- **Geriye uyumluluk**: Öznitelikler belirtilmediğinde önceki yayma davranışı korunur; böylece mevcut şablonlar değişiklik yapmadan çalışmaya devam eder.

## **Bu Özellik Nasıl Kullanılır**

### **Akıllı İşaretçi Sözdizimi**

`arrayassingle` ve `arraydelimiter` öznitelikleri, standart bir Akıllı İşaretçi'nin parantezleri içinde Aspose.Cells tarafından sunulan `name:value` öznitelik sözdizimini kullanır. Genel sözdizimi şöyledir:

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

İşaretçi aşağıdaki bölümlerden oluşur:
- `&=DataSource.ArrayProperty` — bağlı veri kaynağındaki dizi özelliğine başvuran standart Akıllı İşaretçi.
- `arrayassingle:true` — öğeleri yaymak yerine tüm dizinin tek bir hücrede oluşturulmasını motora bildirir.
- `arraydelimiter:;` — isteğe bağlıdır; dizi öğeleri arasına yerleştirilecek ayırıcıyı tanımlar. Belirtilmediğinde virgül kullanılır.

{{% alert color="warning" %}}
Öznitelikleri `name:value` biçiminde yazın (eşittir işareti değil, iki nokta) ve birden fazla özniteliği virgülle **boşluksuz** ayırın. Virgülden sonra boşluk bırakmak, ayrıştırılan değeri bir karakter kaydırır — `(arrayassingle:true, arraydelimiter:;)` ifadesi, `;` yerine hatalı `:;` ayırıcısıyla birleştirir.
{{% /alert %}}

### **Ayırıcı Biçimleri**

- Tek karakter doğrudan iki noktadan sonra yazılır: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Çok karakterli ayırıcı çift tırnak içinde yazılır: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Adım Adım İş Akışı**

Aşağıdaki iş akışı, Akıllı İşaretçiler aracılığıyla bir diziyi tek hücrede nasıl oluşturacağınızı açıklar.
1. **Veri kaynağını hazırlayın**: `String[] getTags()` gibi bir dizi döndüren getter içeren `public` bir bean sınıfı oluşturun ve motorun her satır için bir kayıt okumasını sağlamak üzere bu bean'lerin `java.util.List` koleksiyonunu bağlayın. Yalnızca `public` alanlardan oluşan bir bean bağlanmaz — motor JavaBean getter'larını okur.
2. **Tasarım çalışma kitabı oluşturun**: Yeni bir `Workbook` oluşturun, bir başlık satırı ekleyin ve dizi özelliğine başvuran `arrayassingle` özniteliğini (özel bir ayırıcı gerektiğinde `arraydelimiter` özniteliğini de içeren) bir Akıllı İşaretçi hücresine yerleştirin.
3. **WorkbookDesigner örneğini oluşturun**: Çalışma kitabı için bir `WorkbookDesigner` oluşturun ve listenizi `setDataSource` ile bağlayın.
4. **İşaretçileri işleyin**: Akıllı İşaretçileri genişleterek ve çalışma kitabını gerçek verilerle doldurmak için `WorkbookDesigner.process()` yöntemini çağırın.
5. **Sonucu kaydedin**: Oluşturulan çalışma kitabını XLSX veya desteklenen diğer bir dosya biçiminde diske kaydedin.

### **Kod Örneği 1 — Temel Dize Dizisi Oluşturma**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    // The bean must be public and expose a getter; public fields bind nothing
    public static class Product {
        private String[] tags;
        public String[] getTags() { return tags; }
        public void setTags(String[] tags) { this.tags = tags; }
    }

    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.setTags(new String[] { "C#", "Aspose", "SmartMarker", "Excel" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Product", Arrays.asList(product));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-single.xlsx");
    }
}
```

Örnek, dizinin tamamı için birleştirilmiş değeri yazdırır. Dört etiket, varsayılan virgülle ayrılarak tek hücrede oluşturulur:

```
C#,Aspose,SmartMarker,Excel
```

### **Kod Örneği 2 — Özel Ayırıcı ile Sayısal Değerler**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Student {
        private String[] scores;
        public String[] getScores() { return scores; }
        public void setScores(String[] scores) { this.scores = scores; }
    }

    public static void main(String[] args) throws Exception {
        Student student = new Student();
        student.setScores(new String[] { "95", "88", "76", "100", "67" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Scores");
        // arraydelimiter:- joins the values with a hyphen
        worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Student", Arrays.asList(student));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-numeric.xlsx");
    }
}
```

Nümerik değerler, dizi özelliği `String[]` döndürdüğünde dize değerleriyle tam olarak aynı şekilde birleştirilir:

```
95-88-76-100-67
```

{{% alert color="note" %}}
Java'da dizi özelliğini `String[]` olarak tutun. `int[]` gibi bir temel tür dizisi tek hücrede birleştirildiğinde, sayılar yerine dizi nesnesinin `toString` metnini (örneğin `[I@1a2b3c4d`) oluşturur. Bunun nedeni, birleştirme işleminin her öğenin dize biçimi üzerinde çalışması ve temel tür dizisinin tek bir opak öğe olarak ele alınmasıdır.
{{% /alert %}}

### **Kod Örneği 3 — Varsayılan Yayma ile Tek Hücreli İşlemenin Karşılaştırılması**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Order {
        private String[] items;
        public String[] getItems() { return items; }
        public void setItems(String[] items) { this.items = items; }
    }

    public static void main(String[] args) throws Exception {
        Order order = new Order();
        order.setItems(new String[] { "Apple", "Banana", "Cherry", "Date" });
        Workbook workbook = new Workbook();
        Cells cells = workbook.getWorksheets().get(0).getCells();
        // Column B: default marker — values spread vertically down the column
        cells.get("B1").putValue("Default");
        cells.get("B2").putValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells.get("C1").putValue("Single cell");
        cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Order", Arrays.asList(order));
        designer.process();
        for (int row = 1; row <= 5; row++) {
            String b = cells.get(row, 1).getStringValue();
            String c = cells.get(row, 2).getStringValue();
            if (b != null && !b.isEmpty() || c != null && !c.isEmpty())
                System.out.println("B" + (row + 1) + "=[" + b + "]  C" + (row + 1) + "=[" + c + "]");
        }
        workbook.save("output-array-comparison.xlsx");
    }
}
```

Varsayılan işaretçi, her öğe için B sütununda birer hücre doldururken `arrayassingle` işaretçisi aynı diziyi C sütununda tek hücrede toplar:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Notlar ve En İyi Uygulamalar**

`arrayassingle` ve `arraydelimiter` öznitelikleriyle çalışırken aşağıdaki noktaları göz önünde bulundurun:
- Öznitelik değerleri `name:value` biçimindedir. `arrayassingle=true` gibi eşittir işareti içeren biçim tanınmaz; işaretçi sessizce varsayılan yayma davranışına geri döner.
- Birden fazla özniteliği virgülle ayırın ve virgülden sonra boşluk bırakmayın; boşluk, ayırıcı değerini bir karakter kaydırır (yukarıdaki uyarıya bakın).
- `arraydelimiter` değeri, iki noktadan hemen sonra doğrudan yazılmış tek bir karakter veya çift tırnak içine alınmış çok karakterli bir dize olabilir.
- `arraydelimiter` belirtilmediğinde öğeler virgülle birleştirilir.
- Dizi getter'ları içeren `public` JavaBean'lerden oluşan bir `java.util.List` koleksiyonu bağlayın. Tek bir bean nesnesi veya yalnızca `public` alanlar işaretçilerin çözülmesini sağlamaz.
- Dizi özelliklerini `String[]` olarak tutun; birleştirildiğinde temel tür `int[]`, `toString` metnini oluşturur (yukarıdaki nota bakın).
- Akıllı İşaretçi'yi, oluşan birleştirilmiş dizeyi göstermeye yetecek genişliğe sahip bir hücreye yerleştirin; aksi takdirde içerik, biçime bağlı olarak görsel olarak komşu hücrelere taşabilir.

## **İlgili Makaleler**
- [Aspose.Cells for Java'te PivotTable'a filtre alanları ekleme](/cells/tr/java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Java'da Pivot Tablolarına Stil Uygulama](/cells/tr/java/apply-style-to-pivot-table/)
- [Pivot tablosunda sayfa alanı düzenini değiştirme](/cells/tr/java/change-page-field-layout/)
- [Aspose.Cells for Java'da Sparkline'ı Görüntüye ve HTML'e Dönüştürme](/cells/tr/java/convert-sparkline-to-image-and-html/)
- [Excel'i OFD biçimine dönüştürme](/cells/tr/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}