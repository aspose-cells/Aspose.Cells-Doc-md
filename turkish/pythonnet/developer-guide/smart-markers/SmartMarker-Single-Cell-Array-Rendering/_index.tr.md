---
title: Akıllı İşaretçilerle Dizilerin Tek Hücreye İşlenmesi | Aspose.Cells for Python via .NET
description: Aspose.Cells for Python via .NET içinde arrayassingle ve arraydelimiter Akıllı İşaretçi özniteliklerini kullanarak dizi verisini tek bir hücreye işlemeyi öğrenin.
linktitle: Dizilerin Tek Hücreye İşlenmesi | Aspose.Cells
url: /tr/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Python via .NET kitaplığı, elektronik tablo, Akıllı İşaretçiler, arrayassingle, arraydelimiter, tek hücre dizisi, dizi işleme, şablon
type: docs
weight: 195
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, Akıllı İşaretçiler aracılığıyla bir dizi veri kaynağını tek bir hücreye işleyebilir. `arrayassingle` özniteliği, öğelerin varsayılan olarak tek tek hücrelere yayılmasını kapatır ve `arraydelimiter` özniteliği, birleştirilen öğeler arasına yerleştirilecek ayırıcıyı seçer — varsayılan olarak virgül veya belirttiğiniz herhangi bir tek karakter ya da çift tırnak içine alınmış çok karakterli dize.
{{% /alert %}}

## **Giriş**

Aspose.Cells içindeki Akıllı İşaretçiler, `&=DataSource.Field` gibi işaretçi ifadelerini kullanarak elektronik tablo verilerini dinamik olarak dolduran şablon tabanlı bir özelliktir. İşaretçi tasarım çalışma kitabına yerleştirilir ve şablon `WorkbookDesigner` tarafından işlendiğinde işaretçiler, sağlanan veri kaynağındaki değerlerle değiştirilir.
Varsayılan olarak, bir Akıllı İşaretçi bir dizi alanına başvurduğunda (örneğin, dört değer içeren bir listeye bağlı `&=Product.Tags`), işlem motoru diziyi genişletir ve her öğeyi kendi hücresine yerleştirerek değerleri işaretçinin altındaki sütunda dikey olarak yayar. Bu davranış birçok senaryoda kullanışlı olsa da, öğelerin birleştirilerek tercih ettiğiniz ayırıcıyla ayrılması ve dizinin tamamının tek bir hücreye işlenmesini tercih edebileceğiniz durumlar da vardır.
`arrayassingle` ve `arraydelimiter` öznitelikleri, bir Akıllı İşaretçinin parantezleri içinde `name:value` biçiminde yazılarak tam olarak bu ihtiyacı karşılar. Bu öznitelikler, dizi veri kaynaklarıyla doğrudan çalışırken rapor düzenlerini kompakt ve öngörülebilir tutmanızı sağlar.

## **Bu Özelliğe Neden İhtiyaç Duyulur**

### **Varsayılan Dizi Yayma Davranışı**

Bir Akıllı İşaretçi bir dizi alanına başvurduğunda Aspose.Cells varsayılan olarak diziyi birden fazla hücreye yayar. Örneğin, dört değer içeren bir listede `&=Product.Tags` gibi bir işaretçi, her değeri işaretçinin altındaki kendi hücresine yerleştirir; bu durum diğer şablon içeriğini kaydırarak özenle tasarlanmış rapor düzenlerini bozabilir.

### **Kullanım Alanı Kısıtlamaları**

Varsayılan yayma davranışının istenmediği birçok pratik senaryo vardır:
- **Özet türü raporlar**: Kayıt başına tek satırlık, kompakt bir düzen gerektiren raporlar.
- **Etiket, ad veya anahtar sözcük listeleri**: Tek hücrede virgülle veya boru simgesiyle ayrılmış değerler olarak gösterilmesi gereken listeler.
- **Filtre rozetleri veya durum göstergeleri**: Okunabilirlik için birden fazla değeri tek bir yerde gruplayan öğeler.
- **Sonraki işlem hatları** (CSV dışa aktarma, PDF işleme, posta birleştirme): Hücre başına genişletilmiş bir aralık yerine tek bir birleştirilmiş değer bekleyen işlemler.
- **Platformlar arası uyumluluk**: Bazı tüketicilerin birden fazla hücreye yayılan dizileri kabul edemediği durumlar.

### **Doldurduğu Boşluk**

Yerleşik bir mekanizma olmadan, geliştiriciler verileri Python'da önceden işlemek zorunda kalırdı — listeleri, çalışma kitabı tasarım aracına bağlanmadan önce ayraçlı dizelere birleştirirdi. Bu yaklaşım mantığı yineler, veri modellerini karmaşıklaştırır ve hata olasılığını artırır. `arrayassingle` ve `arraydelimiter` öznitelikleri, biçimlendirmeyi Akıllı İşaretçinin kendisi içinde bildirimsel olarak ele alarak bu geçici çözümü ortadan kaldırır.

## **Özelliğin Avantajları**

Akıllı İşaretçilerde `arrayassingle` ve `arraydelimiter` özniteliklerini kullanmak birçok avantaj sağlar:
- **Tek hücrede toplama**: Tüm dizi öğeleri tam olarak bir hücreye işlenir; bu, düzenleri kompakt ve öngörülebilir tutar.
- **Özel ayırıcı denetimi**: İstediğiniz ayırıcıyı belirtin — varsayılan virgül, noktalı virgül, tire, boru simgesi veya `" | "` gibi çift tırnak içine alınmış çok karakterli bir dize.
- **Şablondan yönlendirilen biçimlendirme**: Verileri önceden işlemek için ek kod gerekmez; biçimlendirme kuralları Akıllı İşaretçi etiketinin içinde bulunur.
- **Daha temiz raporlar**: Dizi verisi, komşu şablon içeriğini farklı satır veya sütunlara itmez.
- **Esnek veri türleri**: JSON satırları olarak sağlanan dize listeleri ve sayısal listelerle çalışır.
- **Geriye uyumluluk**: Öznitelikler belirtilmediğinde özgün yayma davranışı korunur; böylece mevcut şablonlar değişiklik olmadan çalışmaya devam eder.

## **Bu Özellik Nasıl Kullanılır?**

### **Akıllı İşaretçi Sözdizimi**

Akıllı İşaretçi öznitelikleri, standart bir Akıllı İşaretçinin parantezleri içinde Aspose.Cells'in `name:value` öznitelik sözdizimini kullanır. Genel sözdizimi şöyledir:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

İşaretçi aşağıdaki bölümlerden oluşur:
- `&=DataSource.ArrayField` — Bağlı veri kaynağındaki dizi alanına başvuran standart Akıllı İşaretçi.
- `arrayassingle:true` — Öğeleri yaymak yerine işlem motoruna dizinin tamamını tek bir hücreye işlemesini söyler.
- `arraydelimiter:;` — İsteğe bağlıdır; dizi öğeleri arasına yerleştirilecek ayırıcıyı tanımlar. Belirtilmediğinde virgül kullanılır.

{{% alert color="warning" %}}
Öznitelikleri `name:value` biçiminde yazın (eşittir işareti değil, iki nokta) ve birden fazla özniteliği virgülle **boşluk bırakmadan** ayırın. Virgülden sonra boşluk bırakmak, ayrıştırılan değeri bir karakter kaydırır — `(arrayassingle:true, arraydelimiter:;)` ifadesi `;` yerine hatalı `:;` ayırıcısıyla birleştirir.
{{% /alert %}}

### **Ayırıcı Biçimleri**

- Tek karakter doğrudan iki noktadan sonra yazılır: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Çok karakterli ayırıcı çift tırnak içine alınarak yazılır: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Adım Adım İş Akışı**

Aşağıdaki iş akışı, Akıllı İşaretçiler kullanılarak bir dizinin tek bir hücreye nasıl işleneceğini açıklar.
1. **Veri kaynağını hazırlayın**: Her kaydı, bir alanı dizi içeren bir JSON nesnesi olarak düzenleyin; örneğin `{"Tags": ["C#", "Aspose"]}`. `set_data_source` aracılığıyla geçirilen düz Python sınıf örnekleri, sözlükler ve listeler bu platformda dizi alanlarına bağlanmaz — JSON satırları desteklenen tablo biçimidir.
2. **Tasarım çalışma kitabı oluşturun**: Yeni bir `Workbook` oluşturun, bir başlık satırı ekleyin ve dizi alanına başvuran `arrayassingle` özniteliğini içeren bir Akıllı İşaretçi hücresi yerleştirin (özel bir ayırıcı gerektiğinde `arraydelimiter` özniteliğini de ekleyin).
3. **`WorkbookDesigner` örneğini oluşturun**: Çalışma kitabı çevresinde bir `WorkbookDesigner` oluşturun ve JSON satırlarını `set_json_data_source` ile ekleyin.
4. **İşaretçileri işleyin**: Akıllı İşaretçileri genişleterek çalışma kitabını gerçek verilerle doldurmak için `WorkbookDesigner.process()` yöntemini çağırın.
5. **Sonucu kaydedin**: Oluşturulan çalışma kitabını XLSX veya desteklenen başka bir dosya biçiminde diske kaydedin.

### **Kod Örneği 1 — Temel Dize Dizisi İşleme**

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.cells.get("A2").put_value("&=Product.Tags(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-single.xlsx")
```

Bu örnek, dizinin tamamının birleştirilmiş değerini yazdırır. Dört etiket, varsayılan virgülle ayrılarak tek bir hücreye yerleştirilir:

```
C#,Aspose,SmartMarker,Excel
```

### **Kod Örneği 2 — Özel Ayırıcılı Sayısal Dizi**

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Scores")
# arraydelimiter:- joins the numbers with a hyphen
worksheet.cells.get("A2").put_value("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Student",
    '[{"Scores": [95, 88, 76, 100, 67]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-numeric.xlsx")
```

JSON sayıları, tıpkı dizeler gibi birleştirilir — her öğe kendi düz sayısal metnini korur:

```
95-88-76-100-67
```

### **Kod Örneği 3 — Varsayılan İşleme ile Tek Hücreli İşlemenin Karşılaştırılması**

```python
import aspose.cells as ac

workbook = ac.Workbook()
cells = workbook.worksheets[0].cells
# Column B: default marker — values spread vertically down the column
cells.get("B1").put_value("Default")
cells.get("B2").put_value("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").put_value("Single cell")
cells.get("C2").put_value("&=Order.Items(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).string_value or ""
    c = cells.get(row, 2).string_value or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

Varsayılan işaretçi B sütununda aşağı doğru her öğe için bir hücre doldururken, `arrayassingle` işaretçisi aynı diziyi C sütunundaki tek bir hücrede toplar:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Notlar ve En İyi Uygulamalar**

`arrayassingle` ve `arraydelimiter` öznitelikleriyle çalışırken aşağıdaki noktaları göz önünde bulundurun:
- Öznitelik değerleri `name:value` biçimindedir. `arrayassingle=true` gibi eşittir işaretli biçim tanınmaz ve varsayılan yayma davranışına sessizce geri döner.
- Öznitelikleri virgülle ve boşluk bırakmadan ayırın; virgülden sonraki boşluk ayırıcı değerini bir karakter kaydırır (yukarıdaki uyarıya bakın).
- `arraydelimiter` değeri, doğrudan iki noktadan sonra yazılan tek karakter veya çift tırnak içine alınmış çok karakterli bir dize olabilir.
- `arraydelimiter` belirtilmediğinde öğeler virgülle birleştirilir.
- Dizi alanlarını `set_json_data_source` satır nesneleriyle sağlayın. `set_data_source` aracılığıyla geçirilen düz Python nesneleri ve sözlükler bu platformda bağlanmaz; sütunu bir Python listesi döndüren özel bir `ICellsDataTable` ise öğeleri birleştirmek yerine listenin ham metin gösterimini işler.
- JSON sayıları, birleştirilmiş çıktıda düz tam sayı biçimini korur.

## **İlgili Makaleler**
- [Aspose.Cells for Python via .NET'te PivotTable'a filtre alanları ekleme](/cells/tr/python-net/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via .NET ile Pivot Tablolarına Stil Uygulama](/cells/tr/python-net/apply-style-to-pivot-table/)
- [Pivot tablosunda sayfa alanı düzenini değiştirme](/cells/tr/python-net/change-page-field-layout/)
- [Aspose.Cells for Python via .NET ile Mini Grafikleri Görüntüye ve HTML'e Dönüştürme](/cells/tr/python-net/convert-sparkline-to-image-and-html/)
- [Excel'i OFD biçimine dönüştürme](/cells/tr/python-net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python-net" >}}