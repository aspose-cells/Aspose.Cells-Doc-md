---
title: Aspose.Cells for Node.js via Java'da Excel Camera
linktitle: Aspose.Cells for Node.js via Java'da Excel Camera
description: Aspose.Cells for Node.js via Java'da Excel Camera kullanarak, kaynak verilerle yenilenen ve tüm kaynak biçimlendirmesini koruyan bir hücre aralığına bağlı dinamik bir resim oluşturmayı öğrenin.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, Excel Camera, dinamik resim, bağlantılı resim, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Buffer
type: docs
weight: 90
url: /tr/nodejs-java/excel-camera/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera, bir hücre aralığının canlı bir görüntüsünü oluşturan ve çizim katmanında sıradan bir resim gibi duran bir çalışma sayfası nesnesidir. Aspose.Cells iki oluşturma modunu destekler: kaynak veriler her değiştiğinde otomatik olarak yenilenen dinamik bir resim ve bir aralığın tek seferlik anlık görüntüsünü yakalayan statik bir resim. Bu makale, düzeninize uygun olanı seçebilmeniz için her iki yaklaşımı da açıklar.

## Excel Camera Nedir?
Excel Camera, çalışma sayfasının çizim katmanında belirli bir satır ve sütuna sabitlenmiş özünde bir resim nesnesidir. Normal eklenmiş bir resimden farklı olarak, Camera, `"A1:F10"` gibi bir A1 tarzı formül aracılığıyla bir kaynak aralığına bağlıdır. Aralıktaki herhangi bir hücre değiştiğinde, Camera'nın görüntüsü yeni içeriği yansıtacak şekilde otomatik olarak yenilenir. Camera, kaynak alanın tüm biçimlendirmesini korur — kenarlıklar, arka plan renkleri, yazı tipleri ve sayı biçimleri — böylece hücrelerin içinde görünen her şey Camera'nın görüntüsünde de görünür. Bu, Camera'yı uzak bir bölgenin kaydırma veya veri tekrarı yapmadan görünür bir önizlemesini istediğiniz panolar, özetler, yan paneller ve rapor düzenleri için özellikle kullanışlı hale getirir. İki uyarı geçerlidir: çalışma kitabını kaydetmeden önce `updateSelectedValue()` çağrısı yapmalısınız ve dosya HTML veya PDF olarak dışa aktarılacaktır, çünkü bu biçimler canlı yeniden hesaplama yerine gömülü görüntü verilerine dayanır.

## Yöntem 1 — Dinamik Bir Camera Resmi Ekleme
Dinamik Camera, en yaygın yaklaşımdır ve Excel'in yerleşik Camera aracına en yakın eşleşmedir. Başlangıçta görüntü içeriği olmayan bir resim ekleyerek, ardından kaynak aralığına başvuran bir `Formula` atayarak çalışır. Formül atandıktan sonra, `updateSelectedValue()` çağrısı, gömülü görüntü verilerini yansıttığı hücrelerle senkronize olacak şekilde yeniler. Camera özel bir sınıf aracılığıyla uygulanmaz — tamamen standart `Picture` türü üzerine kuruludur.
Anahtar API'ler şunlardır:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — verilen satır ve sütuna sabitlenmiş bir resim ekler. `stream` parametresi için `null` geçirilmesi, dinamik bir Camera için yer tutucu olarak işlev gören boş bir resim oluşturur. Yöntem, yeni resmin dizinini döndürür.
- `worksheet.getPictures().get(index)` — koleksiyondan belirli bir `Picture` öğesini almak için dizin erişimi.
- `Picture.Formula` — Camera'nın yansıttığı kaynak aralığına A1 tarzı başvuruyu tutan bir dize özelliği (`getFormula()`/`setFormula()`), örneğin `"A1:F10"`.
- `Picture.updateSelectedValue()` — `Formula` tarafından başvurulan hücrelerden gömülü görüntü verilerini yenileyen void bir yöntem.

{{% alert color="primary" %}}
Çıktı HTML veya PDF olduğunda, kaydetmeden önce `updateSelectedValue()` çağrısı yapılmalıdır; aksi takdirde dışa aktarılan dosya resim verilerini içermez ve Camera işlenmiş çıktıda boş görünür.
{{% /alert %}}

Aşağıdaki kod bir çalışma kitabı oluşturur, satır 10 sütun 6'ya sabitlenmiş boş bir resim ekler, `Formula` özelliği aracılığıyla onu kaynak aralığı `A1:F10`'a bağlar, gömülü görüntü verilerini yeniler ve çalışma kitabını kaydeder.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Dinamik Kamera: boş bir resim ekleyin, A1:F10'a Formül ile bağlayın, ardından yenileyin
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.XLSX);
```

## Yöntem 2 — Statik Bir Camera Resmi Ekleme
Statik Camera, esasen bir hücre aralığının tek seferlik işlenmiş bir önizlemesidir. Canlı bir bağlantıyı sürdürmek yerine, aralığı bir kez görüntü baytlarına işler, bu baytları bir `ByteArrayInputStream` içine sarar ve bunları normal bir resim olarak eklersiniz. Görüntü içeriği oluşturulma anında sabitlenir ve kaynak hücreler değiştiğinde otomatik olarak yenilenmez.
Anahtar API'ler şunlardır:
- `Cells.createRange(String address)` — `"A1:F10"` gibi bir A1 tarzı adresten bir `Range` nesnesi oluşturur.
- `Range.toImage(ImageOrPrintOptions options)` — aralığı görüntü baytlarına işler. `null` geçirilmesi varsayılan işleme seçeneklerini kullanır; çıktı üzerinde daha ayrıntılı kontrol için aşırı yüklemeler mevcuttur.
- `new ByteArrayInputStream(byte[] buffer)` — işlenmiş görüntü baytlarını, `PictureCollection.add`'a beslenebilen bir `ByteArrayInputStream` içine sarar.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — resmi verilen satır ve sütuna sabitlenmiş olarak ekler, bu kez işleme tarafından üretilen `ByteArrayInputStream`'i geçirir.
Aşağıdaki kod bir çalışma kitabı oluşturur, `A1:F10` için bir `Range` oluşturur, `range.toImage(null)` aracılığıyla onu görüntü baytlarına işler, baytları bir `ByteArrayInputStream` içine sarar, resmi satır 10 sütun 6'ya sabitlenmiş olarak ekler ve çalışma kitabını kaydeder.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Statik Kamera: Aralık oluştur, baytlara dönüştür, ByteArrayInputStream içine sar ve resim olarak ekle
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let pictures = worksheet.getPictures();
pictures.add(10, 6, new aspose.ByteArrayInputStream(imageBytes));
workbook.save("output_static.xlsx", aspose.SaveFormat.XLSX);
```

## Dinamik ve Statik Arasında Seçim Yapma
- **Dinamik Camera:** her yeniden hesaplamada güncellenir, `updateSelectedValue()` sonrasında HTML ve PDF dışa aktarımını destekler ve dosyanın ömrü boyunca canlı bağlantı davranışını korur.
- **Statik Camera:** asla güncellenmeyen tek seferlik bir işleme, oluşturma zamanında gömülü sabit bir görsel anlık görüntü istediğinizde, verinin canlı bir yansıması yerine kullanışlıdır.
Aspose.Cells, hem `Picture.Formula` ve `updateSelectedValue()` üzerine kurulu dinamik, otomatik yenilenen bir Camera'yı hem de `Range.toImage` ve `ByteArrayInputStream` üzerine kurulu statik, tek seferlik bir Camera'yı destekler. Çıktınızın kaynak hücrelerle senkronize kalması gerektiğinde dinamik yaklaşımı, yalnızca oluşturma zamanında sabit bir görsel anlık görüntüye ihtiyaç duyduğunuzda statik yaklaşımı seçin.

{{< app/cells/assistant language="nodejs-java" >}}