---
title: SmartMarker Tek Hücre Dizi Oluşturma | Aspose.Cells for Node.js via C++
linktitle: SmartMarker Tek Hücre Dizi Oluşturma | Aspose.Cells
description: Aspose.Cells for Node.js via C++ ile Akıllı İşaretçiler'de ArrayAsSingle ve ExtraDelimiter özniteliklerini kullanarak dizi verilerini tek bir hücreye nasıl oluşturacağınızı öğrenin.
keywords: Aspose.Cells, Node.js kütüphanesi, elektronik tablo, Akıllı İşaretçiler, ArrayAsSingle, ExtraDelimiter, tek hücre dizisi, dizi oluşturma, şablon
type: docs
weight: 195
url: /tr/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, Akıllı İşaretçiler aracılığıyla dizi verilerini tek bir hücreye oluşturmayı destekler. Geliştiriciler, `ArrayAsSingle` özniteliğini `ExtraDelimiter` özniteliği ile birlikte kullanarak dizi öğelerinin tek bir hücre içinde nasıl ayrılacağını kontrol edebilir ve raporlar ile şablonlar için esnek biçimlendirme sağlayabilir.

{{% /alert %}}

## **Giriş**

Aspose.Cells'teki Akıllı İşaretçiler, `&=DataSource.Field` gibi işaretçi ifadelerini kullanarak elektronik tablo verilerini dinamik olarak doldurmanıza olanak tanıyan güçlü, şablon tabanlı bir özelliktir. İşaretçi, tasarımcı çalışma kitabına yerleştirilir ve şablon `WorkbookDesigner` tarafından işlendiğinde, işaretçiler sağlanan veri kaynağından gelen değerlerle değiştirilir.

Varsayılan olarak, bir Akıllı İşaretçi bir dizi özelliğine başvurduğunda (örneğin, `&=DataSource.Numbers`), motor diziyi genişletir ve her öğeyi ayrı bir bitişik hücreye yerleştirir — ya bir satır boyunca yatay olarak ya da bir sütun boyunca dikey olarak. Bu davranış birçok senaryoda kullanışlı olsa da, tüm diziyi öğeleri birleştirilmiş ve seçtiğiniz bir sınırlayıcı ile ayrılmış şekilde tek bir hücreye oluşturmayı tercih edeceğiniz durumlar vardır.

Bir Akıllı İşaretçi etiketi içinde birlikte kullanılan `ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri tam olarak bu gereksinimi karşılar. Rapor düzenlerini kompakt ve öngörülebilir tutarken, dizi veri kaynaklarıyla yerel olarak çalışmanıza olanak tanır.

## **Bu Özelliğe Neden İhtiyaç Duyuluyor**

### **Varsayılan Dizi Yayılma Davranışı**

Bir Akıllı İşaretçi bir dizi özelliğine başvurduğunda, Aspose.Cells diziyi varsayılan olarak birden fazla hücreye genişletir. Örneğin, dört değer içeren bir `string[]` karşısında `&=Product.Tags` gibi bir işaretçi, her değeri kendi hücresine yerleştirir, diğer şablon içeriğini dışa doğru iter ve özenle tasarlanmış rapor düzenlerini potansiyel olarak bozar.

### **Kullanım Durumu Sınırlamaları**

Varsayılan yayılma davranışının istenmediği birçok pratik senaryo vardır:

- **Özet tarzı raporlar** için kompakt bir kayıt başına tek satır düzeni gerekir.
- **Etiket, açıklama veya anahtar kelime listeleri** tek bir hücre içinde virgülle veya boru ile ayrılmış değerler olarak görüntülenmelidir.
- **Filtre çipleri veya durum göstergeleri** okunabilirlik için birden fazla değeri tek bir yerde gruplandırır.
- **Aşağı yöndeki işlem hatları** (CSV dışa aktarma, PDF oluşturma, posta birleştirme) genişletilmiş bir aralık yerine hücre başına tek bir birleşik değer bekler.
- **Çapraz platform uyumluluğu** için bazı tüketiciler birden fazla hücreye yayılan dizilere tolerans göstermez.

### **Doldurduğu Boşluk**

Yerleşik bir mekanizma olmadan, geliştiriciler JavaScript'te verileri önceden işlemeye — dizileri çalışma kitabı tasarımcısına bağlamadan önce sınırlayıcı dizelere birleştirmeye zorlanırdı. Bu durum mantığı çoğaltır, veri modellerini karmaşıklaştırır ve hata olasılığını artırır. `ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, biçimlendirmeyi Akıllı İşaretçi içinde bildirimsel olarak işleyerek bu geçici çözümü ortadan kaldırır.

## **Özellik Avantajları**

Akıllı İşaretçilerinizde `ArrayAsSingle` ve `ExtraDelimiter` özniteliklerini kullanmak birkaç avantaj sağlar:

- **Tek hücre içerme**: Tüm dizi öğeleri tam olarak bir hücreye oluşturulur, düzenler kompakt ve öngörülebilir kalır.
- **Özel sınırlayıcı kontrolü**: İstediğiniz herhangi bir ayırıcı dizeyi belirtin — virgül, noktalı virgül, kısa çizgi, boru, yeni satır veya herhangi bir özel metin.
- **Şablon tabanlı biçimlendirme**: Verileri önceden işlemek için ek kod gerekmez; biçimlendirme kuralları Akıllı İşaretçi etiketinin içinde yaşar.
- **Daha temiz raporlar**: Dizi verileri artık komşu şablon içeriğini farklı satırlara veya sütunlara itmez.
- **Çok yönlü veri türleri**: Dizeler, sayılar, tarihler ve sınırlayıcı ile birleştirilebilen diğer veri türleriyle çalışır.
- **Geriye dönük uyumluluk**: Öznitelikler atlandığında, orijinal yayılma davranışı korunur, böylece mevcut şablonlar değişiklik yapılmadan çalışmaya devam eder.

## **Bu Özellik Nasıl Kullanılır**

### **Akıllı İşaretçi Sözdizimi**

`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, standart bir Akıllı İşaretçi'nin parantezleri içinde anahtar-değer çiftleri olarak iletilir. Genel sözdizimi şudur:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

İşaretçi aşağıdaki parçalardan oluşur:

- `&=DataSource.ArrayProperty` — bağlı veri kaynağındaki dizi özelliğine başvuran standart Akıllı İşaretçi.
- `arrayasSingle=true` — motora tüm diziyi tek bir hücreye oluşturması talimatını verir. Yalnızca `true` değeri tek hücre davranışını tetikler.
- `extraDelimiter=", "` — dizi öğeleri arasına yerleştirilen ayırıcıyı tanımlar. Değer bir dize değişmezidir; boş, tek karakterli veya çok karakterli bir dize olabilir.

{{% alert color="primary" %}}

`extraDelimiter` özniteliği, çok karakterli sınırlayıcılar, özel metinler veya yeni satırla ayrılmış çıktı için `\n` gibi kaçış dizileri dahil herhangi bir dize değişmezini kabul eder. Dizi boşsa, sonuç hücresi boş bırakılır.

{{% /alert %}}

### **Adım Adım İş Akışı**

Aşağıdaki iş akışı, Akıllı İşaretçileri kullanarak bir dizinin tek bir hücreye nasıl oluşturulacağını açıklar.

1. **Veri kaynağını hazırlayın**: Bir dizi döndüren bir özelliği açığa çıkaran bir sınıf (veya veri yapısı) oluşturun. Özellik `string[]`, `int[]` veya desteklenen başka bir dizi türü döndürebilir.
2. **Tasarımcı çalışma kitabı oluşturun**: Yeni bir `Workbook` oluşturun, bir başlık satırı ekleyin ve `arrayasSingle` ve `extraDelimiter` öznitelikleriyle dizi özelliğine başvuran bir Akıllı İşaretçi hücresi yerleştirin.
3. **WorkbookDesigner'ı örnekleyin**: Bir `WorkbookDesigner` nesnesi oluşturun, tasarımcı çalışma kitabını ona ekleyin ve `setDataSource` yöntemini kullanarak veri kaynağınızı bağlayın.
4. **İşaretçileri işleyin**: Akıllı İşaretçileri genişletmek ve çalışma kitabını gerçek verilerle doldurmak için `workbookDesigner.process()` yöntemini çağırın.
5. **Sonucu kaydedin**: Sonuç çalışma kitabını XLSX veya desteklenen başka bir dosya biçiminde diske kaydedin.

### **Kod Örneği 1 — Temel Dize Dizisi Oluşturma**

```javascript
let product = {
    Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
};

let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue('&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")');

let designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Product", product);
designer.process();

workbook.save("output_arraySingle.xlsx");
```

### **Kod Örneği 2 — Özel Sınırlayıcı ile Sayısal Dizi**

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

### **Kod Örneği 3 — Varsayılan ve ArrayAsSingle Davranışının Karşılaştırılması**

```javascript
var order = {
    Items: ["Apple", "Banana", "Cherry", "Date"]
};

var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Bölüm 1: Varsayılan Akıllı İşaretleyici - değerler hücreler arasında yatay olarak yayılır
cells.get("A1").putValue("Default Spreading Behavior:");
cells.get("A2").putValue("&=Order.Items");

// Bölüm 2: arrayasSingle ve extraDelimiter kullanılarak yeni tek hücreli işleme
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):");
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

// Veri kaynağını bağla ve Akıllı İşaretleyicileri işle
var designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setDataSource("Order", order);
designer.process();

// Ortaya çıkan çalışma kitabını kaydet
workbook.save("output_comparison.xlsx");
```

### **Notlar ve En İyi Uygulamalar**

`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleriyle çalışırken aşağıdaki noktaları aklınızda bulundurun:

- `extraDelimiter` değeri bir dize değişmezi olarak değerlendirilir; şablon işlemcinizin yorumlayabileceği özel karakterlerden kaçış yapın.
- `arrayasSingle` özniteliği bir boole değeri (`true` / `false`) kabul eder. Yalnızca `true` tek hücre davranışını tetikler; diğer herhangi bir değer varsayılan yayılma davranışına geri döner.
- Dizi boş veya null ise, hücre boş bırakılır (veya veri türüne bağlı olarak boş bir dize içerir).
- Özellik, bir sütunun dizilere bölünebileceği `DataSet` ve `DataTable` kaynaklarının yanı sıra nesne veri kaynaklarıyla da çalışır.
- Yeni satırla ayrılmış çıktı için, sınırlayıcı değeri olarak `\n` veya `os.EOL` kullanabilirsiniz.
- Akıllı İşaretçiyi, sonuçta birleştirilmiş dizeyi görüntülemek için yeterli genişliğe sahip bir hücreye yerleştirin; aksi takdirde, içerik biçime bağlı olarak bitişik hücrelere görsel olarak taşabilir.

## **İlgili Makaleler**

- [Hücreleri Birleştirme ve Ayırma](/cells/tr/nodejs-cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="javascript" >}}