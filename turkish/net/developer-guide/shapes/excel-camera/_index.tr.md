---
title: Aspose.Cells for .NET'te Excel Kamera
linktitle: Aspose.Cells for .NET'te Excel Kamera
description: Aspose.Cells for .NET'te Excel Kamerayı kullanarak, kaynak verilerle yenilenen ve tüm kaynak biçimlendirmesini koruyan bir hücre aralığına bağlı dinamik bir resim oluşturmayı öğrenin.
keywords: Aspose.Cells, .NET, Excel Kamera, dinamik resim, bağlantılı resim, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, MemoryStream
type: docs
weight: 90
url: /tr/net/excel-camera/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Kamera, bir hücre aralığının canlı görüntüsünü oluşturan ve normal bir resim gibi çizim katmanında yüzen bir çalışma sayfası nesnesidir. Aspose.Cells iki oluşturma modunu destekler: kaynak veriler her değiştiğinde otomatik olarak yenilenen dinamik bir resim ve bir aralığın tek seferlik anlık görüntüsünü yakalayan statik bir resim. Bu makale, düzeninize uygun olanı seçebilmeniz için her iki yaklaşımı da ele alır.

## What Is Excel Camera?
Excel Kamera, esasen çalışma sayfasının çizim katmanında belirli bir satıra ve sütuna sabitlenmiş bir resim nesnesidir. Normal eklenmiş bir resmin aksine, Kamera, `"A1:F10"` gibi A1 stili bir formül aracılığıyla bir kaynak aralığa bağlıdır. Aralıktaki herhangi bir hücre her değiştiğinde, Kameranın görüntüsü yeni içeriği yansıtacak şekilde otomatik olarak yenilenir. Kamera, kaynak alanın tam biçimlendirmesini korur — kenarlıklar, arka plan renkleri, yazı tipleri ve sayı biçimleri — böylece hücrelerin içinde görünen her şey Kameranın görüntüsünün içinde de görünür. Bu, Kameranın özellikle panolar, özetler, yan paneller ve kaydırmadan veya verileri tekrarlamadan uzak bir bölgenin görünür önizlemesini istediğiniz rapor düzenleri için kullanışlı olmasını sağlar. İki uyarı geçerlidir: çalışma kitabını kaydetmeden önce `UpdateSelectedValue()` çağrısı yapmalısınız ve dosya, canlı yeniden hesaplamadan ziyade gömülü görüntü verilerine dayandıkları için HTML veya PDF olarak dışa aktarılacaktır.

## Method 1 — Add a Dynamic Camera Picture
Dinamik Kamera, en yaygın yaklaşımdır ve Excel'in yerleşik Kamera aracına en yakın eşleşmedir. İlk görüntü içeriği olmayan bir resim ekleyerek ve ardından ona kaynak aralığa başvuran bir `Formula` atayarak çalışır. Formül atandıktan sonra, `UpdateSelectedValue()` çağrısı gömülü görüntü verilerini yansıttığı hücrelerle senkronize olacak şekilde yeniler. Kamera, özel bir sınıf aracılığıyla uygulanmaz — tamamen standart `Picture` türü üzerine kuruludur.
Temel API'ler şunlardır:
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — verilen satır ve sütuna sabitlenmiş bir resim ekler. `stream` parametresi için `null` geçmek, dinamik Kamera için yer tutucu görevi gören boş bir resim oluşturur. Yöntem, yeni resmin dizinini döndürür.
- `worksheet.Pictures[index]` — koleksiyondan belirli bir `Picture` almak için dizinleyici erişimi.
- `Picture.Formula` — Kameranın yansıttığı kaynak aralığa A1 stili başvuruyu tutan bir dize özelliği (get/set), örneğin `"A1:F10"`.
- `Picture.UpdateSelectedValue()` — `Formula` tarafından başvurulan hücrelerden gömülü görüntü verilerini yenileyen void bir yöntem.

{{% alert color="primary" %}}
Çıktı HTML veya PDF olduğunda kaydetmeden önce `UpdateSelectedValue()` çağrılmalıdır; aksi takdirde dışa aktarılan dosya resim verilerini içermeyecek ve Kamera işlenmiş çıktıda boş görünecektir.
{{% /alert %}}

Aşağıdaki kod bir çalışma kitabı oluşturur, 10. satır 6. sütuna sabitlenmiş boş bir resim ekler, `Formula` özelliği aracılığıyla onu `A1:F10` kaynak aralığına bağlar, gömülü görüntü verilerini yeniler ve çalışma kitabını kaydeder.

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
var pictures = worksheet.Pictures;
int index = pictures.Add(10, 6, (Stream)null);
pictures[0].Formula = "A1:F10";
pictures[0].UpdateSelectedValue();
workbook.Save("output_dynamic.xlsx", SaveFormat.Xlsx);
```

## Method 2 — Add a Static Camera Picture
Statik Kamera, esasen bir hücre aralığının tek seferlik işlenmiş bir önizlemesidir. Canlı bir bağlantıyı sürdürmek yerine, aralığı bir kez görüntü baytlarına dönüştürür, bu baytları bir `MemoryStream` içine sarar ve bunları normal bir resim olarak eklersiniz. Görüntü içeriği daha sonra oluşturulma anında sabitlenir ve kaynak hücreler değiştiğinde otomatik olarak yenilenmez.
Temel API'ler şunlardır:
- `Cells.CreateRange(string address)` — `"A1:F10"` gibi A1 stili bir adresten bir `Range` nesnesi oluşturur.
- `Range.ToImage(ImageOrPrintOptions options)` — aralığı görüntü baytlarına dönüştürür. `null` geçmek varsayılan işleme seçeneklerini kullanır; çıktı üzerinde daha ayrıntılı kontrol için aşırı yüklemeler mevcuttur.
- `new MemoryStream(byte[] buffer)` — işlenmiş görüntü baytlarını `PictureCollection.Add`'a beslenebilecek bir `MemoryStream` içine sarar.
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — verilen satır ve sütuna sabitlenmiş resmi ekler, bu kez işleme tarafından üretilen `MemoryStream` geçirilir.
Aşağıdaki kod bir çalışma kitabı oluşturur, `A1:F10` için bir `Range` oluşturur, `Range.ToImage(null)` aracılığıyla onu görüntü baytlarına dönüştürür, baytları bir `MemoryStream` içine sarar, 10. satır 6. sütuna sabitlenmiş bir resim ekler ve çalışma kitabını kaydeder.

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Static Camera: build Range, render to bytes, wrap in MemoryStream, add as picture
var range = workbook.Worksheets[0].Cells.CreateRange("A1:F10");
var pictures = worksheet.Pictures;
pictures.Add(10, 6, new MemoryStream(range.ToImage(null)));
workbook.Save("output_static.xlsx", SaveFormat.Xlsx);
```

## Choosing Between Dynamic and Static
- **Dinamik Kamera:** her yeniden hesaplamada güncellenir, `UpdateSelectedValue()` sonrasında HTML ve PDF dışa aktarımını destekler ve dosyanın ömrü boyunca canlı bağlantı davranışını korur.
- **Statik Kamera:** asla güncellenmeyen tek seferlik bir işleme, verilerin canlı bir yansıması yerine derleme zamanında gömülü sabit bir görsel anlık görüntü istediğinizde kullanışlıdır.
Aspose.Cells, hem `Picture.Formula` ve `UpdateSelectedValue()` üzerine kurulu dinamik, otomatik yenilenen bir Kamerayı hem de `Range.ToImage` ve `MemoryStream` üzerine kurulu statik, tek seferlik bir Kamerayı destekler. Çıktınızın kaynak hücrelerle senkronize kalması gerektiğinde dinamik yaklaşımı seçin ve yalnızca derleme zamanında sabit bir görsel anlık görüntüye ihtiyacınız olduğunda statik yaklaşımı seçin.

## Related Articles
- [Aspose.Cells for .NET'te Mini Grafiği Görüntüye ve HTML'ye Dönüştürme](/cells/tr/net/convert-sparkline-to-image-and-html/)
- [Bir Hücreye Resim Ekleme](/cells/tr/net/inserting-an-image-into-a-cell/)
- [Aspose.Cells for .NET'te Pivot Tabloya Filtre Alanları Ekleme](/cells/tr/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .NET'te Pivot Tablolara Stil Uygulama](/cells/tr/net/apply-style-to-pivot-table/)
- [Pivot Tabloda Sayfa Alanı Düzenini Değiştirme](/cells/tr/net/change-page-field-layout/)

{{< app/cells/assistant language="csharp" >}}