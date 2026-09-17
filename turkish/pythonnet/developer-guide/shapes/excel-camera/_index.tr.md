---
title: Aspose.Cells for Python via .NET'te Excel Camera
linktitle: Aspose.Cells for Python via .NET'te Excel Camera
description: Hücre aralığına bağlı, kaynak verilerle yenilenen ve tüm kaynak biçimlendirmesini koruyan dinamik bir resim oluşturmak için Aspose.Cells for Python via .NET'te Excel Camera'nın nasıl kullanılacağını öğrenin.
keywords: Aspose.Cells, Python, Excel Camera, dinamik resim, bağlı resim, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, BytesIO
type: docs
weight: 90
url: /tr/python-net/excel-camera/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera, bir hücre aralığının canlı görüntüsünü oluşturan ve çizim katmanında sıradan bir resim gibi yüzen bir çalışma sayfası nesnesidir. Aspose.Cells iki oluşturma modunu destekler: kaynak veriler değiştiğinde otomatik olarak yenilenen dinamik bir resim ve bir aralığın tek seferlik anlık görüntüsünü yakalayan statik bir resim. Bu makale, yerleşiminize uygun olan yaklaşımı seçebilmeniz için her iki yaklaşımı da ele alır.

## Excel Camera Nedir?
Excel Camera, esasen çalışma sayfasının çizim katmanında belirli bir satır ve sütuna sabitlenmiş bir resim nesnesidir. Sıradan eklenmiş bir resmin aksine, Camera, `"A1:F10"` gibi A1 stili bir formül aracılığıyla bir kaynak aralığına bağlıdır. O aralıktaki herhangi bir hücre her değiştiğinde, yeni içeriği yansıtacak şekilde Camera'nın görüntüsü otomatik olarak yenilenir. Camera, kaynak alanın tam biçimlendirmesini korur — kenarlıklar, arka plan renkleri, yazı tipleri ve sayı biçimleri — hücrelerin içinde görünen her şey Camera'nın görüntüsünde de görünür. Bu, Camera'yı kaydırmadan veya verileri tekrarlamadan uzak bir bölgenin görünür önizlemesini istediğiniz panolar, özetler, yan paneller ve rapor düzenleri için özellikle kullanışlı hale getirir. İki uyarı geçerlidir: çalışma kitabını kaydetmeden önce `update_selected_value()` çağrısı yapmalısınız ve dosya HTML veya PDF olarak dışa aktarılacaktır, çünkü bu formatlar canlı yeniden hesaplamadan ziyade gömülü görüntü verilerine dayanır.

## Yöntem 1 — Dinamik Camera Resmi Eklemek
Dinamik Camera en yaygın yaklaşımdır ve Excel'in yerleşik Camera aracına en yakın eşleşmedir. Hiçbir başlangıç görüntü içeriği olmayan bir resim ekleyerek çalışır, ardından kaynak aralığına referans veren bir `formula` atar. Formül atandıktan sonra, `update_selected_value()` çağrısı, gömülü görüntü verilerini yansıttığı hücrelerle senkronize olacak şekilde yeniler. Camera özel bir sınıf aracılığıyla uygulanmaz — tamamen standart `Picture` türü üzerine kuruludur.
Anahtar API'ler şunlardır:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — verilen satır ve sütuna sabitlenmiş bir resim ekler. `stream` parametresi için `None` geçmek, dinamik Camera için yer tutucu olarak işlev gören boş bir resim oluşturur. Yöntem, yeni resmin dizinini döndürür.
- `worksheet.pictures[index]` — koleksiyondan belirli bir `Picture` almak için dizinleyici erişimi.
- `picture.formula` — Camera'nın yansıttığı kaynak aralığa A1 stili referansı tutan bir dize özelliği (get/set), örneğin `"A1:F10"`.
- `picture.update_selected_value()` — `formula` tarafından başvurulan hücrelerden gömülü görüntü verilerini yenileyen void bir yöntemdir.

{{% alert color="primary" %}}
Çıktı HTML veya PDF olduğunda kaydetmeden önce `update_selected_value()` çağrılmalıdır; aksi takdirde dışa aktarılan dosya resim verilerini içermez ve Camera işlenmiş çıktıda boş görünür.
{{% /alert %}}

Aşağıdaki kod bir çalışma kitabı oluşturur, 10. satır 6. sütuna sabitlenmiş boş bir resim ekler, `formula` özelliği aracılığıyla onu kaynak aralığı `A1:F10`'a bağlar, gömülü görüntü verilerini yeniler ve çalışma kitabını kaydeder.

```python
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Dinamik Kamera: boş bir resim ekleyin, formül aracılığıyla A1:F10'a bağlayın, ardından yenileyin
pictures = worksheet.pictures
index = pictures.add(10, 6, None)
pictures[index].formula = "A1:F10"
pictures[index].update_selected_value()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## Yöntem 2 — Statik Camera Resmi Eklemek
Statik Camera, esasen bir hücre aralığının tek seferlik işlenmiş önizlemesidir. Canlı bağlantıyı sürdürmek yerine, aralığı bir kez görüntü baytlarına dönüştürürsünüz, bu baytları bir `BytesIO` içine sarar ve bunları sıradan bir resim olarak eklersiniz. Görüntü içeriği, oluşturulma anında sabitlenir ve kaynak hücreler değiştiğinde otomatik olarak yenilenmez.
Anahtar API'ler şunlardır:
- `Cells.create_range(string address)` — `"A1:F10"` gibi A1 stili bir adresten bir `Range` nesnesi oluşturur.
- `Range.to_image(ImageOrPrintOptions options)` — aralığı görüntü baytlarına dönüştürür. `None` geçmek varsayılan işleme seçeneklerini kullanır; çıktı üzerinde daha ayrıntılı kontrol için aşırı yüklemeler mevcuttur.
- `BytesIO(byte[] buffer)` — işlenen görüntü baytlarını `PictureCollection.add` öğesine beslenebilecek bir `BytesIO` içine sarar.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — verilen satır ve sütuna resmi sabitler, bu sefer işleme tarafından üretilen `BytesIO`'yu geçer.
Aşağıdaki kod bir çalışma kitabı oluşturur, `A1:F10` için bir `Range` oluşturur, `Range.to_image(null)` aracılığıyla onu görüntü baytlarına dönüştürür, baytları bir `BytesIO` içine sarar, 10. satır 6. sütuna sabitlenmiş resmi ekler ve çalışma kitabını kaydeder.

```python
from io import BytesIO
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Statik Kamera: Aralık oluştur, bayt olarak işle, BytesIO içine sar, resim olarak ekle
range_ = worksheet.cells.create_range("A1:F10")
pictures = worksheet.pictures
pictures.add(10, 6, BytesIO(range_.to_image(None)))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## Dinamik ve Statik Arasında Seçim Yapmak
- **Dinamik Camera:** her yeniden hesaplamada güncellenir, `update_selected_value()` sonrasında HTML ve PDF dışa aktarmayı destekler ve dosyanın ömrü boyunca canlı bağlantı davranışını korur.
- **Statik Camera:** asla güncellenmeyen tek seferlik bir işleme; canlı veri yansıması yerine derleme zamanında gömülü sabit bir görsel anlık görüntü istediğinizde kullanışlıdır.
Aspose.Cells hem `picture.formula` ve `update_selected_value()` üzerine kurulu dinamik, otomatik yenilenen bir Camera'yı hem de `Range.to_image` ve bir `BytesIO` üzerine kurulu statik, tek seferlik bir Camera'yı destekler. Çıktınızın kaynak hücrelerle senkronize kalması gerektiğinde dinamik yaklaşımı seçin ve yalnızca derleme zamanında sabit bir görsel anlık görüntüye ihtiyacınız olduğunda statik yaklaşımı seçin.

{{< app/cells/assistant language="python-net" >}}