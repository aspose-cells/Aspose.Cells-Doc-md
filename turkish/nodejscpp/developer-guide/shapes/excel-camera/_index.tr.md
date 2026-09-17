---
title: Aspose.Cells for Node.js via C++'da Excel Camera
linktitle: Aspose.Cells for Node.js via C++'da Excel Camera
description: Aspose.Cells for Node.js via C++'da Excel Camera kullanarak, bir hücre aralığına bağlı, kaynak verilerle yenilenen ve tüm kaynak biçimlendirmesini koruyan dinamik bir resim oluşturmayı öğrenin.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, Excel Camera, dinamik resim, bağlı resim, Picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /tr/nodejs-cpp/excel-camera/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera, bir hücre aralığının canlı görüntüsünü oluşturan ve çizim katmanında sıradan bir resim gibi yüzen bir çalışma sayfası nesnesidir. Aspose.Cells iki oluşturma modunu destekler: kaynak veriler değiştiğinde otomatik olarak yenilenen dinamik bir resim ve bir aralığın tek seferlik anlık görüntüsünü yakalayan statik bir resim. Bu makale, düzeninize uygun olanı seçebilmeniz için her iki yaklaşımı da ele alır.

## Excel Camera Nedir?
Excel Camera, esasen çalışma sayfasının çizim katmanında belirli bir satır ve sütuna sabitlenmiş bir resim nesnesidir. Normal eklenmiş bir resmin aksine, Camera `"A1:F10"` gibi A1 tarzında bir formül aracılığıyla bir kaynak aralığa bağlanır. O aralıktaki herhangi bir hücre değiştiğinde, Camera'nın görüntüsü yeni içeriği yansıtacak şekilde otomatik olarak yenilenir. Camera, kaynak alanın tam biçimlendirmesini korur — kenarlıklar, arka plan renkleri, yazı tipleri ve sayı biçimleri — böylece hücrelerin içinde görünen her şey Camera'nın görüntüsünün içinde de görünür. Bu, Camera'yı uzak bir bölgenin kaydırma veya veri tekrarı yapmadan görünür bir önizlemesini istediğiniz panolar, özetler, yan paneller ve rapor düzenleri için özellikle kullanışlı kılar. İki uyarı geçerlidir: çalışma kitabını kaydetmeden önce `updateSelectedValue()` çağrısı yapmalısınız ve dosya HTML veya PDF'ye aktarılacaktır, çünkü bu formatlar canlı yeniden hesaplama yerine gömülü görüntü verilerine dayanır.

## Yöntem 1 — Dinamik Camera Resmi Ekleme
Dinamik Camera en yaygın yaklaşımdır ve Excel'in yerleşik Camera aracına en yakın eşleşmedir. Başlangıçta görüntü içeriği olmayan bir resim ekleyerek ve ardından kaynak aralığa referans veren bir `Formula` atayarak çalışır. Formül atandıktan sonra, `updateSelectedValue()` çağrısı gömülü görüntü verilerini yansıttığı hücrelerle senkronize olacak şekilde yeniler. Camera, özel bir sınıf aracılığıyla uygulanmaz — tamamen standart `Picture` türü üzerine kuruludur.
Temel API'ler şunlardır:
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — resmi belirtilen satır ve sütuna sabitler. `stream` parametresi için `null` geçmek, dinamik bir Camera için yer tutucu işlevi gören boş bir resim oluşturur. Yöntem, yeni resmin dizinini döndürür.
- `pictures.get(index)` — koleksiyondan dizine göre belirli bir `Picture` alır.
- `Picture.formula` — Camera'nın yansıttığı kaynak aralığa A1 tarzında referansı tutan bir dize özelliğidir (get/set), örneğin `"A1:F10"`.
- `Picture.updateSelectedValue()` — `formula` tarafından referans verilen hücrelerden gömülü görüntü verilerini yenileyen void bir yöntemdir.

{{% alert color="primary" %}}
`updateSelectedValue()` çağrısı, çıktı HTML veya PDF olduğunda kaydetmeden önce YAPILmalıdır; aksi takdirde dışa aktarılan dosya resim verilerini içermeyecek ve Camera işlenmiş çıktıda boş görünecektir.
{{% /alert %}}

Aşağıdaki kod bir çalışma kitabı oluşturur, satır 10 sütun 6'ya sabitlenmiş boş bir resim ekler, onu `Formula` özelliği aracılığıyla `A1:F10` kaynak aralığına bağlar, gömülü görüntü verilerini yeniler ve çalışma kitabını kaydeder.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Dinamik Kamera: boş bir resim ekleyin, Formül aracılığıyla A1:F10'a bağlayın, ardından yenileyin
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.Xlsx);
```

## Yöntem 2 — Statik Camera Resmi Ekleme
Statik Camera, esasen bir hücre aralığının tek seferlik işlenmiş önizlemesidir. Canlı bağlantıyı sürdürmek yerine, aralığı bir kez görüntü baytlarına işler, bu baytları bir `Buffer` içinde sarar ve normal bir resim olarak eklersiniz. Görüntü içeriği oluşturulduğu anda sabitlenir ve kaynak hücreler değiştiğinde otomatik olarak yenilenmez.
Temel API'ler şunlardır:
- `Cells.createRange(address)` — `A1:F10` gibi A1 tarzında bir adresten bir `Range` nesnesi oluşturur.
- `Range.toImage(ImageOrPrintOptions options)` — aralığı görüntü baytlarına işler. `null` geçmek varsayılan işleme seçeneklerini kullanır; çıktı üzerinde daha ayrıntılı kontrol için aşırı yüklemeler mevcuttur.
- `new Buffer(byte[] buffer)` — işlenmiş görüntü baytlarını `getPictures().add` öğesine beslenebilecek bir `Buffer` içinde sarar.
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — resmi belirtilen satır ve sütuna sabitler, bu sefer işleme tarafından üretilen `Buffer`'ı geçer.
Aşağıdaki kod bir çalışma kitabı oluşturur, `A1:F10` için bir `Range` oluşturur, onu `range.toImage(null)` aracılığıyla görüntü baytlarına işler, baytları bir `Buffer` içinde sarar, resmi satır 10 sütun 6'ya sabitler ve çalışma kitabını kaydeder.

```javascript
const aspose = require("aspose.cells");
const { MemoryStream } = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Statik Kamera: Aralık oluştur, bayt olarak işle, MemoryStream içine sar, resim olarak ekle
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let stream = new MemoryStream();
stream.write(imageBytes);
let pictures = worksheet.getPictures();
pictures.add(10, 6, stream);
workbook.save("output_static.xlsx", aspose.SaveFormat.Xlsx);
```

## Dinamik ve Statik Arasında Seçim Yapma
- **Dinamik Camera:** her yeniden hesaplamada güncellenir, `updateSelectedValue()` sonrasında HTML ve PDF dışa aktarımını destekler ve dosyanın ömrü boyunca canlı bağlantı davranışını korur.
- **Statik Camera:** hiçbir zaman güncellenmeyen tek seferlik bir işleme, canlı bir veri yansıması yerine derleme zamanında gömülü sabit bir görsel anlık görüntü istediğinizde kullanışlıdır.
Aspose.Cells hem `Picture.formula` artı `updateSelectedValue()` üzerine kurulu dinamik, otomatik yenilenen bir Camera'yı hem de `Range.toImage` artı bir `Buffer` üzerine kurulu statik, tek seferlik bir Camera'yı destekler. Çıktınızın kaynak hücrelerle senkronize kalması gerektiğinde dinamik yaklaşımı, derleme zamanında yalnızca sabit bir görsel anlık görüntüye ihtiyacınız olduğunda statik yaklaşımı seçin.

{{< app/cells/assistant language="nodejs-cpp" >}}