---
title: SmartMarker Tek Hücre Dizi Oluşturma | Aspose.Cells for Node.js via Java
linktitle: SmartMarker Tek Hücre Dizi Oluşturma | Aspose.Cells
description: Aspose.Cells for Node.js via Java ile Smart Markers'da ArrayAsSingle ve ExtraDelimiter özniteliklerini kullanarak dizi verilerini tek bir hücreye nasıl aktaracağınızı öğrenin.
keywords: Aspose.Cells, Node.js via Java kütüphanesi, elektronik tablo, Smart Markers, ArrayAsSingle, ExtraDelimiter, tek hücre dizi, dizi oluşturma, şablon
type: docs
weight: 195
url: /tr/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, Smart Markers aracılığıyla dizi verilerini tek bir hücreye aktarmayı destekler. Geliştiriciler, `ArrayAsSingle` özniteliğini `ExtraDelimiter` özniteliği ile birlikte kullanarak dizi öğelerinin tek bir hücre içinde nasıl ayrılacağını kontrol edebilir ve raporlar ile şablonlar için esnek biçimlendirme sağlayabilir.

{{% /alert %}}

## **Giriş**

Aspose.Cells'teki Smart Markers, `&=DataSource.Field` gibi işaretçi ifadeleri kullanarak elektronik tablo verilerini dinamik olarak doldurmanıza olanak tanıyan güçlü, şablon tabanlı bir özelliktir. İşaretçi, tasarımcı çalışma kitabına yerleştirilir ve şablon `WorkbookDesigner` tarafından işlendiğinde, işaretçiler sağlanan veri kaynağındaki değerlerle değiştirilir.

Varsayılan olarak, bir Smart Marker bir dizi özelliğine başvurduğunda (örneğin, `&=DataSource.Numbers`), motor diziyi genişletir ve her öğeyi ayrı bir bitişik hücreye yerleştirir — yatay olarak bir satır boyunca veya dikey olarak bir sütun aşağı. Bu davranış birçok senaryoda kullanışlı olsa da, tüm diziyi öğeleri birleştirilmiş ve seçtiğiniz bir ayırıcı ile ayrılmış şekilde tek bir hücreye aktarmayı tercih edeceğiniz durumlar da vardır.

Bir Smart Marker etiketinin içinde birlikte kullanılan `ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri tam olarak bu gereksinimi karşılar. Rapor düzenlerini kompakt ve öngörülebilir tutarken, dizi veri kaynaklarıyla yerel olarak çalışmanıza olanak tanırlar.

## **Bu Özelliğe Neden İhtiyaç Duyulur**

### **Varsayılan Dizi Yayılma Davranışı**

Bir Smart Marker bir dizi özelliğine başvurduğunda, Aspose.Cells diziyi varsayılan olarak birden çok hücreye genişletir. Örneğin, dört değer içeren bir `string[]` karşısında `&=Product.Tags` gibi bir işaretçi, her değeri kendi hücresine yerleştirir, diğer şablon içeriklerini dışa doğru iter ve özenle tasarlanmış rapor düzenlerini potansiyel olarak bozar.

### **Kullanım Senaryosu Sınırlamaları**

Varsayılan yayılma davranışının istenmediği birçok pratik senaryo vardır:

- **Özet tarzı raporlar** — kompakt bir kayıt başına tek satır düzeni gerektiren.
- **Tag, etiket veya anahtar kelime listeleri** — tek bir hücre içinde virgülle veya boru ile ayrılmış değerler olarak görüntülenmesi gereken.
- **Filtre çipleri veya durum göstergeleri** — okunabilirlik için birden çok değeri tek bir yerde gruplayan.
- **Aşağı akış işlem hatları** (CSV dışa aktarma, PDF oluşturma, posta birleştirme) — genişletilmiş bir aralık yerine hücre başına tek bir birleşik değer bekleyen.
- **Platformlar arası uyumluluk** — bazı tüketicilerin birden çok hücreye yayılan dizilere tolerans gösteremediği durumlar.

### **Doldurduğu Boşluk**

Yerleşik bir mekanizma olmadan, geliştiriciler JavaScript'te verileri önceden işlemeye — dizileri çalışma kitabı tasarımcısına bağlamadan önce ayrılmış dizelere birleştirmeye — zorlanırdı. Bu, mantığı çoğaltır, veri modellerini karmaşıklaştırır ve hata olasılığını artırır. `ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, biçimlendirmeyi Smart Marker'ın kendisi içinde bildirimsel olarak işleyerek bu geçici çözümü ortadan kaldırır.

## **Özellik Avantajları**

Smart Marker'larınızda `ArrayAsSingle` ve `ExtraDelimiter` özniteliklerini kullanmak birkaç avantaj sağlar:

- **Tek hücre kapsama**: Tüm dizi öğeleri tam olarak tek bir hücreye aktarılır, düzenler kompakt ve öngörülebilir kalır.
- **Özel ayırıcı kontrolü**: Virgül, noktalı virgül, kısa çizgi, boru, yeni satır veya istediğiniz herhangi bir özel metin gibi herhangi bir ayırıcı dize belirtin.
- **Şablon odaklı biçimlendirme**: Verileri önceden işlemek için ek kod gerekmez; biçimlendirme kuralları Smart Marker etiketinin içinde bulunur.
- **Daha temiz raporlar**: Dizi verileri artık komşu şablon içeriklerini farklı satır veya sütunlara itmez.
- **Çok yönlü veri tipleri**: Dizeler, sayılar, tarihler ve ayırıcı ile birleştirilebilen diğer veri tipleri ile çalışır.
- **Geriye dönük uyumluluk**: Öznitelikler atlandığında, orijinal yayılma davranışı korunur, böylece mevcut şablonlar değişmeden çalışmaya devam eder.

## **Bu Özellik Nasıl Kullanılır**

### **Smart Marker Sözdizimi**

`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, standart bir Smart Marker'ın parantezleri içinde anahtar-değer çiftleri olarak iletilir. Genel sözdizimi şudur:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

İşaretçi aşağıdaki parçalardan oluşur:

- `&=DataSource.ArrayProperty` — bağlı veri kaynağındaki dizi özelliğine başvuran standart Smart Marker.
- `arrayasSingle=true` — motora tüm diziyi tek bir hücreye aktarması talimatını verir. Yalnızca `true` değeri tek hücre davranışını tetikler.
- `extraDelimiter=", "` — dizi öğeleri arasına yerleştirilecek ayırıcıyı tanımlar. Değer bir dize değişmezidir; boş, tek karakterli veya çok karakterli bir dize olabilir.

{{% alert color="primary" %}}

`extraDelimiter` özniteliği, çok karakterli ayırıcılar, özel metinler veya yeni satırla ayrılmış çıktı için `\n` gibi kaçış dizileri dahil herhangi bir dize değişmezini kabul eder. Dizi boşsa, sonuç hücresi boş bırakılır.

{{% /alert %}}

### **Adım Adım İş Akışı**

Aşağıdaki iş akışı, Smart Markers kullanarak bir dizinin tek bir hücreye nasıl aktarılacağını açıklar.

1. **Veri kaynağını hazırlayın**: Bir dizi döndüren bir özellik sunan bir sınıf (veya veri yapısı) oluşturun. Özellik `string[]`, `int[]` veya desteklenen herhangi bir dizi türünü döndürebilir.
2. **Tasarımcı çalışma kitabı oluşturun**: Yeni bir `Workbook` oluşturun, bir başlık satırı ekleyin ve dizi özelliğine `arrayasSingle` ve `extraDelimiter` öznitelikleriyle başvuran bir Smart Marker hücresi yerleştirin.
3. **WorkbookDesigner'ı örnekleyin**: Bir `WorkbookDesigner` nesnesi oluşturun, tasarımcı çalışma kitabını ona ekleyin ve `setDataSource` yöntemini kullanarak veri kaynağınızı bağlayın.
4. **İşaretçileri işleyin**: Smart Marker'ları genişletmek ve çalışma kitabını gerçek verilerle doldurmak için `workbookDesigner.process()` yöntemini çağırın.
5. **Sonucu kaydedin**: Ortaya çıkan çalışma kitabını XLSX veya desteklenen diğer herhangi bir dosya biçiminde diske kaydedin.

### **Kod Örneği 1 — Temel Dize Dizisi Oluşturma**

```javascript
class Product {
    constructor() {
        this.Tags = null;
    }
}

const product = new Product();
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

const designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Product", product);
designer.process();

workbook.save("output_arraySingle.xlsx");
```

### **Kod Örneği 2 — Özel Ayırıcılı Sayısal Dizi**

```javascript
class Student {
    constructor() {
        this.Scores = [];
    }
}

const student = new Student();
student.Scores = [95, 88, 76, 100, 67];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Scores");
worksheet.getCells().get("A2").putValue(student.Scores.join(" - "));

workbook.save("output_numericArray.xlsx");
```

### **Kod Örneği 3 — Varsayılan ve ArrayAsSingle Davranışlarını Karşılaştırma**

```javascript
const AsposeCells = require("aspose.cells");

function main() {
    const order = {
        Items: ["Apple", "Banana", "Cherry", "Date"]
    };

    const workbook = new AsposeCells.Workbook();
    const sheet = workbook.getWorksheets().get(0);
    const cells = sheet.getCells();

    // Bölüm 1: Varsayılan Akıllı İşaretleyici - değerler hücreler arasında yatay olarak yayılır
    cells.get("A1").putValue("Default Spreading Behavior:");
    cells.get("A2").putValue("&=Order.Items");

    // Bölüm 2: arrayasSingle ve extraDelimiter kullanarak yeni tek hücreli oluşturma
    cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):");
    cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // Veri kaynağını bağla ve Akıllı İşaretleyicileri işle
    const designer = new AsposeCells.WorkbookDesigner(workbook);
    designer.setDataSource("Order", order);
    designer.process();

    // Elde edilen çalışma kitabını kaydet
    workbook.save("output_comparison.xlsx");
}

main();
```

### **Notlar ve En İyi Uygulamalar**

`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleriyle çalışırken aşağıdaki noktaları aklınızda bulundurun:

- `extraDelimiter` değeri bir dize değişmezi olarak değerlendirilir; şablon işlemcinizin yorumlayabileceği özel karakterleri kaçışla belirtin.
- `arrayasSingle` özniteliği bir boolean değer kabul eder (`true` / `false`). Yalnızca `true` tek hücre davranışını tetikler; diğer herhangi bir değer varsayılan yayılma davranışına geri döner.
- Dizi boş veya null ise, hücre boş bırakılır (veya veri türüne bağlı olarak boş bir dize içerir).
- Özellik, nesne veri kaynaklarının yanı sıra bir sütunun dizilere bölünebileceği `DataSet` ve `DataTable` kaynaklarıyla da çalışır.
- Yeni satırla ayrılmış çıktı için, ayırıcı değeri olarak `\n` kullanabilirsiniz.
- Smart Marker'ı, ortaya çıkan birleştirilmiş dizeyi görüntülemek için yeterli genişliğe sahip bir hücreye yerleştirin; aksi takdirde, içerik biçime bağlı olarak görsel olarak bitişik hücrelere taşabilir.



{{< app/cells/assistant language="javascript" >}}