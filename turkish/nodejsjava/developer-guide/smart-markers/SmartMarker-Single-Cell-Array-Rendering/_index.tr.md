---
title: SmartMarker Tek Hücre Dizisi Oluşturma | Aspose.Cells for Node.js via Java
description: arrayassingle ve arraydelimiter Smart Marker özniteliklerini kullanarak Aspose.Cells for Node.js via Java ile dizi verisini tek hücreye nasıl oluşturacağınızı öğrenin.
linktitle: SmartMarker Tek Hücre Dizisi Oluşturma | Aspose.Cells for Node.js via Java
url: /tr/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Node.js via Java kitaplığı, elektronik tablo, Smart Markers, arrayassingle, arraydelimiter, tek hücreli dizi, dizi oluşturma, şablon
type: docs
weight: 195
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, Smart Markers aracılığıyla bir dizi veri kaynağını tek bir hücreye oluşturabilir. `arrayassingle` özniteliği, öğeleri tek tek yayma varsayılan davranışını devre dışı bırakır ve `arraydelimiter` özniteliği, birleştirilen öğelerin arasına yerleştirilecek ayırıcıyı belirler — varsayılan olarak virgül veya belirttiğiniz herhangi bir tek karakter ya da tırnak içinde çok karakterli dize.
{{% /alert %}}

## **Giriş**

Aspose.Cells içindeki Smart Markers, `&=DataSource.Field` gibi işaretçi ifadeleri kullanarak elektronik tablo verilerini dinamik olarak dolduran, şablona dayalı bir özelliktir. İşaretçi, tasarımcı çalışma kitabına yerleştirilir ve şablon `WorkbookDesigner` tarafından işlendiğinde işaretçiler, sağlanan veri kaynağındaki değerlerle değiştirilir.
Varsayılan olarak, bir Smart Marker bir dizi alanına başvurduğunda (örneğin, dört değerlik bir diziye bağlı `&=Product.Tags` gibi), motor diziyi genişletir ve her öğeyi kendi hücresine yerleştirerek değerleri işaretçinin altındaki sütunda dikey olarak yayar. Bu davranış birçok senaryoda kullanışlı olsa da, dizinin tamamını öğeleri birleştirilmiş ve tercih ettiğiniz bir ayırıcıyla ayrılmış şekilde tek bir hücreye oluşturmak istediğiniz durumlar vardır.
`arrayassingle` ve `arraydelimiter` öznitelikleri, bir Smart Marker'ın parantezleri içinde `name:value` biçiminde yazılarak tam olarak bu ihtiyaca yanıt verir. Bu öznitelikler, dizi veri kaynaklarıyla doğal bir şekilde çalışmaya devam ederken rapor düzenlerini kompakt ve öngörülebilir tutmanıza olanak tanır.

## **Bu Özelliğe Neden İhtiyaç Duyulur**

### **Varsayılan Dizi Yayma Davranışı**

Bir Smart Marker bir dizi alanına başvurduğunda Aspose.Cells, varsayılan olarak diziyi birden fazla hücreye yayma davranışını uygular. Örneğin, dört değer içeren bir diziye karşılık `&=Product.Tags` gibi bir işaretçi, her değeri işaretçinin altındaki kendi hücresine yerleştirir; bu da diğer şablon içeriğini dışarı doğru iterek özenle tasarlanmış rapor düzenlerini bozabilir.

### **Kullanım Senaryosu Sınırları**

Varsayılan yayma davranışının istenmediği birçok pratik senaryo bulunmaktadır:
- **Özet tarzı raporlar**: her kayıt için kompakt, tek satırlık bir düzen gerektiren.
- **Etiket, etiketleme veya anahtar sözcük listeleri**: virgülle veya boru ile ayrılmış değerler olarak tek bir hücre içinde gösterilmesi gereken.
- **Filtre çipleri veya durum göstergeleri**: okunabilirlik için birden çok değeri tek yerde gruplayan.
- **Sonraki işlem hatları** (CSV dışa aktarma, PDF oluşturma, posta birleştirme): genişletilmiş bir aralık yerine hücre başına tek birleşik değer bekleyen.
- **Platformlar arası uyumluluk**: bazı tüketicilerin, birden fazla hücreye yayılan dizileri kabul edememesi durumu.

### **Doldurduğu Boşluk**

Yerleşik bir mekanizma olmadan, geliştiricilerin verileri JavaScript'te önceden işlemesi gerekirdi — dizileri çalışma kitabı tasarımcısına bağlamadan önce ayraçlı dizelere dönüştürmek. Bu durum mantığı tekrarlar, veri modellerini karmaşıklaştırır ve hata olasılığını artırır. `arrayassingle` ve `arraydelimiter` öznitelikleri, biçimlendirmeyi doğrudan Smart Marker'ın içinde bildirimsel olarak ele alarak bu geçici çözümü ortadan kaldırır.

## **Özellik Avantajları**

Smart Markers'ınızda `arrayassingle` ve `arraydelimiter` özniteliklerini kullanmak çeşitli avantajlar sağlar:
- **Tek hücrede toplama**: Tüm dizi öğeleri tam olarak tek bir hücreye oluşturulur ve düzenler kompakt ve öngörülebilir kalır.
- **Özel ayırıcı denetimi**: İstediğiniz ayırıcıyı belirtin — varsayılan virgül, noktalı virgül, tire, boru veya `" | "` gibi tırnak içinde çok karakterli bir dize.
- **Şablona dayalı biçimlendirme**: Verileri önceden işlemek için ek kod gerekmez; biçimlendirme kuralları Smart Marker etiketinin içinde yer alır.
- **Daha temiz raporlar**: Dizi verisi artık komşu şablon içeriğini farklı satırlara veya sütunlara itmez.
- **Esnek veri türleri**: JSON satırları olarak sağlanan dize dizileriyle çalışır; dize olarak oluşturulan sayısal değerler de buna dâhildir.
- **Geriye uyumluluk**: Öznitelikler atlandığında özgün yayma davranışı korunur, dolayısıyla mevcut şablonlar değişmeden çalışmaya devam eder.

## **Bu Özelliği Nasıl Kullanılır**

### **Smart Marker Sözdizimi**

`arrayassingle` ve `arraydelimiter` öznitelikleri, standart bir Smart Marker'ın parantezleri içinde Aspose.Cells'in `name:value` öznitelik sözdizimini kullanır. Genel sözdizim şöyledir:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

İşaretçi aşağıdaki bölümlerden oluşur:
- `&=DataSource.ArrayField` — bağlı veri kaynağındaki dizi alanına başvuran standart Smart Marker.
- `arrayassingle:true` — motorun, öğeleri yaymak yerine dizinin tamamını tek bir hücreye oluşturmasını sağlar.
- `arraydelimiter:;` — isteğe bağlıdır; dizi öğeleri arasına yerleştirilecek ayırıcıyı tanımlar. Atlandığında virgül kullanılır.

{{% alert color="warning" %}}
Öznitelikleri `name:value` biçiminde (eşittir işareti değil, iki nokta) yazın ve birden fazla özniteliği **boşluksuz** virgülle ayırın. Virgülden sonra gelen boşluk, ayrıştırılan değeri bir karakter kaydırır — `(arrayassingle:true, arraydelimiter:;)` hatalı ayırıcı olarak `:;` ile birleştirir.
{{% /alert %}}

### **Ayırıcı Biçimleri**

- Tek bir karakter, iki noktadan hemen sonra gelir: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Çok karakterli ayırıcı çift tırnak içinde yazılır: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Adım Adım İş Akışı**

Aşağıdaki iş akışı, Smart Markers kullanarak bir dizinin tek bir hücreye nasıl oluşturulacağını açıklar.
1. **Veri kaynağını hazırlayın**: Her kaydı, alanı bir dizi tutan bir JSON nesnesi olarak düzenleyin, örneğin `{"Tags": ["C#", "Aspose"]}`. Bu platformda `setDataSource` ile geçirilen düz JavaScript nesneleri ve dizileri bağlanmaz — JSON satırları desteklenen tablo biçimidir.
2. **Bir tasarımcı çalışma kitabı oluşturun**: Yeni bir `Workbook` oluşturun, bir başlık satırı ekleyin ve dizi alanına başvuran, `arrayassingle` özniteliğini içeren (özel bir ayırıcı gerektiğinde `arraydelimiter` ile) bir Smart Marker hücresi yerleştirin.
3. **WorkbookDesigner'ı örnekleyin**: Çalışma kitabının etrafında bir `WorkbookDesigner` oluşturun ve JSON satırlarınızı `setJsonDataSource` ile bağlayın.
4. **İşaretçileri işleyin**: Smart Markers'ı genişletmek ve çalışma kitabını gerçek verilerle doldurmak için `workbookDesigner.process()` yöntemini çağırın.
5. **Sonucu kaydedin**: Ortaya çıkan çalışma kitabını XLSX veya desteklenen diğer bir dosya biçiminde diske kaydedin.

### **Kod Örneği 1 — Temel Dize Dizisi Oluşturma**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Tags");
// No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-single.xlsx");
```

Örnek, dizinin tamamının birleştirilmiş değerini yazdırır. Dört etiket, varsayılan virgülle ayrılarak tek bir hücreye yerleşir:

```
C#,Aspose,SmartMarker,Excel
```

### **Kod Örneği 2 — Özel Ayırıcı ile Sayısal Değerler**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Scores");
// arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-numeric.xlsx");
```

Puanlar JSON dizesi olarak sağlandığında, birleştirilmiş çıktı düz sayıları korur:

```
95-88-76-100-67
```

{{% alert color="note" %}}
Java motoru üzerinden aktarılan JSON sayıları ondalık (double) olarak geldiği için, `[95, 88]` `95.0-88.0` olarak birleşir. Birleştirilmiş hücrede tam tamsayı metnini istediğinizde JSON satırlarındaki sayıları tırnak içine alın.
{{% /alert %}}

### **Kod Örneği 3 — Varsayılan ile Tek Hücreli Oluşturmayı Karşılaştırma**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const cells = workbook.getWorksheets().get(0).getCells();
// Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default");
cells.get("B2").putValue("&=Order.Items");
// Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell");
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]');
designer.process();
for (let row = 1; row <= 5; row++) {
    const b = cells.get(row, 1).getStringValue() || "";
    const c = cells.get(row, 2).getStringValue() || "";
    if (b || c) console.log(`B${row + 1}=[${b}]  C${row + 1}=[${c}]`);
}
workbook.save("output-array-comparison.xlsx");
```

Varsayılan işaretçi, B sütunu boyunca her öğe için bir hücreyi doldururken, `arrayassingle` işaretçisi aynı diziyi C sütunundaki tek bir hücrede birleştirir:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Notlar ve En İyi Uygulamalar**

`arrayassingle` ve `arraydelimiter` öznitelikleriyle çalışırken aşağıdaki noktaları göz önünde bulundurun:
- Öznitelik değerleri `name:value` biçimini kullanır. `arrayassingle=true` gibi eşittir işareti biçimi tanınmaz ve sessizce varsayılan yayma davranışına geri döner.
- Öznitelikleri virgülle ve boşluksuz ayırın; virgülden sonraki boşluk, ayırıcı değerini bir karakter kaydırır (yukarıdaki uyarıya bakın).
- `arraydelimiter` değeri, iki noktadan hemen sonra doğrudan yazılan tek bir karakter veya çift tırnak içine alınmış çok karakterli bir dize olabilir.
- `arraydelimiter` atlandığında, öğeler virgülle birleştirilir.
- Dizi alanlarını `setJsonDataSource` satır nesneleriyle sağlayın; `setDataSource` ile geçirilen düz JavaScript nesneleri ve dizileri bu platformda bağlanmaz.
- JSON sayıları Java motoru üzerinden ondalık (double) olarak gelir (`95`, `95.0` olarak birleşir); tam tamsayı metni önemliyse JSON satırlarındaki sayısal değerleri tırnak içine alın.
- Smart Marker'ı, ortaya çıkan birleştirilmiş dizeyi görüntüleyebileceği kadar geniş bir hücreye yerleştirin; aksi halde içerik, biçime bağlı olarak bitişik hücrelere görsel olarak taşabilir.

## **İlgili Makaleler**
- [Aspose.Cells for Node.js via Java'te PivotTable'a filtre alanları ekleme](/cells/tr/nodejs-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via Java'da Pivot Tablolarına Stil Uygulama](/cells/tr/nodejs-java/apply-style-to-pivot-table/)
- [Pivot tablosunda sayfa alanı düzenini değiştirme](/cells/tr/nodejs-java/change-page-field-layout/)
- [Aspose.Cells for Node.js via Java ile Sparkline'ı Görüntüye ve HTML'ye Dönüştürme](/cells/tr/nodejs-java/convert-sparkline-to-image-and-html/)
- [Excel'i OFD biçimine dönüştürme](/cells/tr/nodejs-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="nodejs-java" >}}