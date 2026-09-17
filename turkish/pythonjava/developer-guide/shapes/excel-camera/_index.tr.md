---
title: Aspose.Cells for Python via Java'da Excel Camera
linktitle: Aspose.Cells for Python via Java'da Excel Camera
description: Aspose.Cells for Python via Java'da Excel Camera'yı nasıl kullanacağınızı öğrenin; kaynak verilerle yenilenen ve tüm kaynak biçimlendirmesini koruyan bir hücre aralığına bağlı dinamik bir resim oluşturun.
keywords: Aspose.Cells, Python via Java, Excel Camera, dinamik resim, bağlı resim, Picture.formula, updateSelectedValue, createRange, toImage, byte[] dizisi
type: docs
weight: 90
url: /tr/python-java/excel-camera/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera, bir hücre aralığının canlı görüntüsünü oluşturan ve normal bir resim gibi çizim katmanında yüzen bir çalışma sayfası nesnesidir. Aspose.Cells for Python via Java iki oluşturma modunu destekler: kaynak veriler her değiştiğinde otomatik olarak yenilenen dinamik bir resim ve bir aralığın tek seferlik anlık görüntüsünü yakalayan statik bir resim. Bu makale, düzeninize uygun olanı seçebilmeniz için her iki yaklaşımı da adım adım açıklar.

## Excel Camera Nedir?
Excel Camera, temelde çalışma sayfasının çizim katmanında belirli bir satır ve sütuna sabitlenmiş bir resim nesnesidir. Normal eklenmiş bir resmin aksine, Camera `"A1:F10"` gibi bir A1 tarzı formül aracılığıyla bir kaynak aralığına bağlıdır. Aralıktaki herhangi bir hücre değiştiğinde, Camera'nın görüntüsü yeni içeriği yansıtacak şekilde otomatik olarak yenilenir. Camera, kaynak alanın tüm biçimlendirmesini korur — kenarlıklar, arka plan renkleri, yazı tipleri ve sayı biçimleri — böylece hücreler içinde görünen her şey Camera'nın görüntüsünde de görünür. Bu, Camera'yı uzaktaki bir bölgenin kaydırma veya verileri tekrarlamadan görünür bir önizlemesini istediğiniz panolar, özetler, yan paneller ve rapor düzenleri için özellikle kullanışlı kılar. İki uyarı geçerlidir: çalışma kitabını kaydetmeden önce `updateSelectedValue()` çağrısı yapmalısınız ve dosya HTML veya PDF olarak dışa aktarılacaktır, çünkü bu formatlar canlı yeniden hesaplama yerine gömülü görüntü verilerine dayanır.

## Yöntem 1 — Dinamik Camera Resmi Ekleme
Dinamik Camera en yaygın yaklaşımdır ve Excel'in yerleşik Camera aracına en yakın eşleşmedir. Başlangıçta görüntü içeriği olmayan bir resim ekleyip ardından ona kaynak aralığına başvuran bir formül atayarak çalışır. Formül atandıktan sonra, `updateSelectedValue()` çağrısı gömülü görüntü verilerini yansıttığı hücrelerle senkronize olacak şekilde yeniler. Camera, özel bir sınıf aracılığıyla uygulanmaz — tamamen standart `Picture` türü üzerine kuruludur.
Temel API'ler şunlardır:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — belirtilen satır ve sütunda sabitlenmiş bir resim ekler. `stream` parametresi için `None` geçmek, dinamik Camera için yer tutucu görevi gören boş bir resim oluşturur. Metot, yeni resmin dizinini döndürür.
- `worksheet.getPictures().get(index)` — koleksiyondan belirli bir `Picture` öğesini almak için erişimci.
- `Picture.getFormula()` / `Picture.setFormula()` — Camera'nın yansıttığı kaynak aralığa A1 tarzı başvuruyu alır/ayarlar, örneğin `"A1:F10"`.
- `Picture.updateSelectedValue()` — gömülü görüntü verilerini formülün başvurduğu hücrelerden yenileyen void bir metot.

{{% alert color="primary" %}}
Çıktı HTML veya PDF olduğunda kaydetmeden önce `updateSelectedValue()` çağrılmalıdır; aksi takdirde dışa aktarılan dosya resim verilerini içermeyecek ve Camera işlenmiş çıktıda boş görünecektir.
{{% /alert %}}

Aşağıdaki kod bir çalışma kitabı oluşturur, satır 10 sütun 6'da sabitlenmiş boş bir resim ekler, `setFormula` metodu aracılığıyla onu kaynak aralığı `A1:F10`'a bağlar, gömülü görüntü verilerini yeniler ve çalışma kitabını kaydeder.

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# Dinamik Kamera: boş bir resim ekle, Formül aracılığıyla A1:F10'a bağla, ardından yenile
pictures = worksheet.getPictures()
index = pictures.add(10, 6, None)
pictures.get(index).setFormula("A1:F10")
pictures.get(index).updateSelectedValue()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## Yöntem 2 — Statik Camera Resmi Ekleme
Statik Camera, temelde bir hücre aralığının tek seferlik oluşturulmuş bir önizlemesidir. Canlı bağlantıyı sürdürmek yerine, aralığı bir kez görüntü baytlarına dönüştürürsünüz, bu baytları bir `byte[]` dizisine sararsınız ve bunları normal bir resim olarak eklersiniz. Görüntü içeriği oluşturulma anında sabitlenir ve kaynak hücreler değiştiğinde otomatik olarak yenilenmez.
Temel API'ler şunlardır:
- `Cells.createRange(String address)` — `"A1:F10"` gibi A1 tarzı bir adresten bir `Range` nesnesi oluşturur.
- `Range.toImage(ImageOrPrintOptions options)` — aralığı görüntü baytlarına dönüştürür. `None` geçmek varsayılan işleme seçeneklerini kullanır; çıktı üzerinde daha ayrıntılı kontrol için aşırı yüklemeler mevcuttur.
- `byte[] array(byte[] buffer)` — işlenmiş görüntü baytlarını `PictureCollection.add` öğesine beslenebilecek bir `byte[] array` içine sarar.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — resmi belirtilen satır ve sütunda sabitler, bu kez işleme tarafından üretilen `byte[] array` öğesini geçirir.
Aşağıdaki kod bir çalışma kitabı oluşturur, `A1:F10` için bir `Range` oluşturur, `Range.toImage(None)` aracılığıyla onu görüntü baytlarına dönüştürür, baytları bir `byte[]` dizisine sarar, satır 10 sütun 6'da sabitlenmiş resmi ekler ve çalışma kitabını kaydeder.

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# Statik Kamera: Aralık oluştur, baytlara dönüştür, ByteArrayInputStream içine sar, resim olarak ekle
range_ = worksheet.getCells().createRange("A1:F10")
image_bytes = range_.toImage(None)
pictures = worksheet.getPictures()
pictures.add(10, 6, jpype.JArray(jpype.JByte)(image_bytes))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## Dinamik ve Statik Arasında Seçim Yapma
- **Dinamik Camera:** her yeniden hesaplamada güncellenir, `updateSelectedValue()` sonrasında HTML ve PDF dışa aktarmayı destekler ve dosyanın ömrü boyunca canlı bağlantı davranışını korur.
- **Statik Camera:** asla güncellenmeyen tek seferlik bir işleme, canlı bir veri yansıması yerine oluşturma zamanında gömülü sabit bir görsel anlık görüntü istediğiniz durumlarda kullanışlıdır.
Aspose.Cells for Python via Java hem `setFormula` ve `updateSelectedValue()` üzerine kurulu dinamik, otomatik yenilenen bir Camera'yı hem de `toImage` ve `byte[] array` üzerine kurulu statik, tek seferlik bir Camera'yı destekler. Çıktınızın kaynak hücrelerle senkronize kalması gerektiğinde dinamik yaklaşımı, yalnızca oluşturma zamanında sabit bir görsel anlık görüntüye ihtiyacınız olduğunda statik yaklaşımı seçin.

{{< app/cells/assistant language="python" >}}