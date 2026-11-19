---
title: Akıllı İşaret ile Tek Hücre Dizisi Oluşturma | Aspose.Cells for Python via Java
description: Aspose.Cells for Python via Java kitaplığında `arrayassingle` ve `arraydelimiter` Akıllı İşaret özniteliklerini kullanarak dizi verisini tek bir hücrede oluşturmayı öğrenin.
linktitle: Tek Hücre Dizi Oluşturma
url: /tr/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Python via Java kitaplığı, elektronik tablo, Akıllı İşaretler, arrayassingle, arraydelimiter, tek hücre dizisi, dizi oluşturma, şablon
type: docs
weight: 195
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, Akıllı İşaretler aracılığıyla bir dizi veri kaynağını tek bir hücrede oluşturabilir. `arrayassingle` özniteliği, öğeleri tek tek yayma varsayılan davranışını devre dışı bırakır; `arraydelimiter` özniteliği ise birleştirilen öğeler arasına yerleştirilecek ayırıcıyı belirler — varsayılan olarak virgül veya belirttiğiniz tek karakter ya da tırnak içinde çok karakterli dize.
{{% /alert %}}

## **Giriş**

Aspose.Cells'deki Akıllı İşaretler, `&=DataSource.Field` gibi işaret ifadelerini kullanarak elektronik tablo verilerini dinamik biçimde dolduran şablona dayalı bir özelliktir. İşaret, tasarım çalışma kitabına yerleştirilir ve şablon `WorkbookDesigner` tarafından işlendiğinde işaretler, sağlanan veri kaynağındaki değerlerle değiştirilir.
Varsayılan olarak, bir Akıllı İşaret bir dizi alanına başvurduğunda (örneğin, dört değerlik bir listeye bağlı `&=Product.Tags`), motor diziyi genişletir ve her öğeyi kendi hücresine yerleştirerek değerleri işaretin altındaki sütunda dikey olarak yayar. Bu davranış birçok senaryoda kullanışlı olsa da, öğeleri birleştirerek ve tercih ettiğiniz bir ayırıcıyla ayırarak dizinin tamamını tek bir hücrede oluşturmak istediğiniz durumlar vardır.
`arrayassingle` ve `arraydelimiter` öznitelikleri, bir Akıllı İşaret'in parantezleri içinde `name:value` biçiminde yazılarak tam olarak bu gereksinimi karşılar. Rapor düzenlerini kompakt ve öngörülebilir tutmanıza olanak tanırken dizi veri kaynaklarıyla doğrudan çalışmayı sürdürür.

## **Bu Özelliğe Neden İhtiyaç Var**

### **Varsayılan Dizi Yayma Davranışı**

Bir Akıllı İşaret dizi alanına başvurduğunda Aspose.Cells varsayılan olarak diziyi birden fazla hücreye yayılar. Örneğin, dört değer içeren bir listeye karşılık gelen `&=Product.Tags` işareti, her değeri işaretin altındaki kendi hücresine yerleştirir; diğer şablon içeriğini dışarı doğru iterek özenle tasarlanmış rapor düzenlerini bozabilir.

### **Kullanım Senaryosu Sınırları**

Varsayılan yayma davranışının istenmediği birçok pratik senaryo vardır:
- **Özet tarzı raporlar** — her kayıt için kompakt, tek satırlık bir düzen gerektirenler.
- **Etiket, ürün etiketi veya anahtar sözcük listeleri** — tek bir hücrede virgülle veya boru karakteriyle ayrılmış değerler olarak gösterilmesi gerekenler.
- **Filtre çipleri veya durum göstergeleri** — okunabilirlik için birden çok değeri tek bir yerde gruplayanlar.
- **Devam eden işlem hatları** (CSV dışa aktarma, PDF oluşturma, posta birleştirme) — genişletilmiş bir aralık yerine hücre başına tek bir birleştirilmiş değer bekleyenler.
- **Platformlar arası uyumluluk** — bazı tüketicilerin birden fazla hücreye yayılan dizileri kabul edemediği durumlar.

### **Karşıladığı Boşluk**

Yerleşik bir mekanizma olmadan, geliştiriciler veriyi Python'da önceden işlemek zorunda kalırdı — listeleri çalışma kitabı tasarımcısına bağlamadan önce ayırıcı içeren dizelere dönüştürürlerdi. Bu yaklaşım mantığı yineler, veri modellerini karmaşıklaştırır ve hata olasılığını artırır. `arrayassingle` ve `arraydelimiter` öznitelikleri, biçimlendirmeyi Akıllı İşaret'in kendisi içinde bildirimsel olarak ele ederek bu geçici çözümü ortadan kaldırır.

## **Özellik Avantajları**

Akıllı İşaret etiketlerinizde `arrayassingle` ve `arraydelimiter` özniteliklerini kullanmak çeşitli avantajlar sağlar:
- **Tek hücrede toplama**: Tüm dizi öğeleri tam olarak tek bir hücrede oluşturulur; bu, düzenleri kompakt ve öngörülebilir tutar.
- **Özel ayırıcı denetimi**: İstediğiniz ayırıcıyı belirtin — varsayılan virgül, noktalı virgül, tire, boru karakteri veya `" | "` gibi tırnak içinde çok karakterli bir dize.
- **Şablondan yönlendirilen biçimlendirme**: Veriyi önceden işlemek için ek kod gerekmez; biçimlendirme kuralları Akıllı İşaret etiketinin içinde bulunur.
- **Daha temiz raporlar**: Dizi verisi, bitişik şablon içeriğini artık farklı satırlara veya sütunlara itmez.
- **Esnek veri türleri**: Dize olarak işlenen sayısal değerler dâhil, JSON satırları aracılığıyla sağlanan dize dizileriyle çalışır.
- **Geriye uyumluluk**: Öznitelikler belirtilmediğinde özgün yayma davranışı korunur; böylece mevcut şablonlar değişiklik olmadan çalışmaya devam eder.

## **Bu Özellik Nasıl Kullanılır**

### **Akıllı İşaret Sözdizimi**

`arrayassingle` ve `arraydelimiter` öznitelikleri, standart bir Akıllı İşaret'in parantezleri içinde Aspose.Cells'in `name:value` öznitelik sözdizimini kullanır. Genel sözdizimi şöyledir:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

İşaret aşağıdaki bölümlerden oluşur:
- `&=DataSource.ArrayField` — bağlı veri kaynağındaki dizi alanına başvuran standart Akıllı İşaret.
- `arrayassingle:true` — öğeleri yaymak yerine dizinin tamamının tek bir hücrede oluşturulmasını sağlar.
- `arraydelimiter:;` — isteğe bağlıdır; dizi öğeleri arasına yerleştirilecek ayırıcıyı tanımlar. Belirtilmezse virgül kullanılır.

{{% alert color="warning" %}}
Öznitelikleri `name:value` biçiminde yazın (eşittir işareti değil, iki nokta işareti) ve birden fazla özniteliği **boşluk olmadan** virgülle ayırın. Virgülden sonra boşluk, ayrıştırılan değeri bir karakter kaydırır — `(arrayassingle:true, arraydelimiter:;)` ifadesi `;` yerine hatalı `:;` ayırıcısıyla birleştirir.
{{% /alert %}}

### **Ayırıcı Biçimleri**

- Tek bir karakter, iki noktadan hemen sonra gelir: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Çok karakterli ayırıcı çift tırnak içinde yazılır: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Adım Adım İş Akışı**

Bu iş akışı, Akıllı İşaretler kullanılarak bir dizinin tek bir hücrede nasıl oluşturulacağını açıklar.
1. **Veri kaynağını hazırlayın**: Her kaydı, alanının bir dizi tuttuğu bir JSON nesnesi olarak düzenleyin; örneğin `{"Tags": ["C#", "Aspose"]}`. `setDataSource` yöntemine aktarılan düz Python sınıf örnekleri ve sözlükler bu platformda bağlanamaz — desteklenen tablo biçimi JSON satırlarıdır.
2. **Tasarım çalışma kitabı oluşturun**: Yeni bir `Workbook` oluşturun, başlık satırı ekleyin ve dizi alanına başvuran, `arrayassingle` özniteliğini içeren bir Akıllı İşaret hücresi yerleştirin. Özel bir ayırıcı gerektiğinde `arraydelimiter` özniteliğini de ekleyin.
3. **WorkbookDesigner örneğini oluşturun**: Çalışma kitabının etrafında bir `WorkbookDesigner` oluşturun ve JSON satırlarını `setJsonDataSource` ile ilişkilendirin.
4. **İşaretleri işleyin**: Akıllı İşaretleri genişletmek ve çalışma kitabını gerçek verilerle doldurmak için `WorkbookDesigner.process()` yöntemini çağırın.
5. **Sonucu kaydedin**: Oluşturulan çalışma kitabını XLSX veya desteklenen başka bir dosya biçiminde diske kaydedin.

### **Kod Örneği 1 — Temel Dize Dizisi Oluşturma**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.getCells().get("A2").getStringValue())
workbook.save("output-array-single.xlsx")
```

Örnek, dizinin tamamının birleştirilmiş değerini yazdırır. Dört etiket, varsayılan virgülle ayrılarak tek bir hücrede yer alır:

```
C#,Aspose,SmartMarker,Excel
```

### **Kod Örneği 2 — Özel Ayırıcılı Sayısal Değerler**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Scores")
# arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]')
designer.process()
print(worksheet.getCells().get("A2").getStringValue())
workbook.save("output-array-numeric.xlsx")
```

Puanlar JSON dizeleri olarak sağlandığında, birleştirilmiş çıktı düz sayıları korur:

```
95-88-76-100-67
```

{{% alert color="note" %}}
JSON sayıları Java motoru üzerinden iletildiğinde `double` değerler olarak gelir; bu nedenle `[95, 88]` `95.0-88.0` olarak birleşir. Birleştirilmiş hücrede tam olarak tam sayı metnini istediğinizde JSON satırlarındaki sayıları tırnak içine alın.
{{% /alert %}}

### **Kod Örneği 3 — Varsayılan ile Tek Hücrede Oluşturmanın Karşılaştırılması**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner

workbook = Workbook()
cells = workbook.getWorksheets().get(0).getCells()
# Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default")
cells.get("B2").putValue("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell")
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).getStringValue() or ""
    c = cells.get(row, 2).getStringValue() or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

Varsayılan işaret, her öğe için B sütunu boyunca birer hücre doldururken `arrayassingle` işareti aynı diziyi C sütunundaki tek bir hücrede birleştirir:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Notlar ve En İyi Uygulamalar**

`arrayassingle` ve `arraydelimiter` öznitelikleriyle çalışırken aşağıdaki noktaları göz önünde bulundurun:
- Öznitelik değerleri `name:value` biçimini kullanır. `arrayassingle=true` gibi eşittir işareti biçimi tanınmaz ve varsayılan yayma davranışına sessizce geri döner.
- Öznitelikleri boşluksuz virgülle ayırın; virgülden sonraki boşluk ayırıcı değerini bir karakter kaydırır (yukarıdaki uyarıya bakın).
- `arraydelimiter` değeri, iki noktadan hemen sonra doğrudan yazılan tek bir karakter veya çift tırnak içine alınmış çok karakterli bir dize olabilir.
- `arraydelimiter` belirtilmediğinde öğeler virgülle birleştirilir.
- Dizi alanlarını `setJsonDataSource` satır nesneleriyle sağlayın; `setDataSource` yöntemine aktarılan düz Python nesneleri ve sözlükler bu platformda bağlanamaz.
- JSON sayıları Java motoru üzerinden `double` olarak gelir (`95`, `95.0` olarak birleşir); tam sayı metni önemliyse JSON satırlarındaki sayısal değerleri tırnak içine alın.
- Akıllı İşareti, birleştirilen sonuç dizesini görüntüleyecek kadar geniş bir hücreye yerleştirin; aksi halde biçime bağlı olarak içerik görsel olarak bitişik hücrelere taşabilir.

## **İlgili Makaleler**
- [Aspose.Cells for Python via Java ile Pivot Tablosuna Filtre Alanları Ekleme](/cells/tr/python-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via Java'da Pivot Tablolarına Stil Uygulama](/cells/tr/python-java/apply-style-to-pivot-table/)
- [Pivot tablosunda sayfa alanı düzenini değiştirme](/cells/tr/python-java/change-page-field-layout/)
- [Aspose.Cells for Python via Java'da Sparkline'ı Görüntüye ve HTML'e Dönüştürme](/cells/tr/python-java/convert-sparkline-to-image-and-html/)
- [Excel'i OFD biçimine dönüştürme](/cells/tr/python-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python" >}}