---
title: Aspose.Cells for Java'da Excel Kamera
linktitle: Aspose.Cells for Java'da Excel Kamera
description: Aspose.Cells for Java'da Excel Kamerası'nı kullanarak kaynak verilerle yenilenen ve tüm kaynak biçimlendirmesini koruyan bir hücre aralığına bağlı dinamik bir resim oluşturmayı öğrenin.
keywords: Aspose.Cells, Java, Excel Kamera, dinamik resim, bağlı resim, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, ByteArrayInputStream
type: docs
weight: 90
url: /tr/java/excel-camera/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Kamerası, bir hücre aralığının canlı bir görüntüsünü oluşturan ve sıradan bir resim gibi çizim katmanında yüzen bir çalışma sayfası nesnesidir. Aspose.Cells, kaynak veriler her değiştiğinde otomatik olarak yenilenen bir dinamik resim ve bir aralığın tek seferlik anlık görüntüsünü yakalayan bir statik resim olmak üzere iki oluşturma modunu destekler. Bu makale, her iki yaklaşımı da adım adım açıklayarak düzeninize uygun olanı seçmenize yardımcı olur.

## What Is Excel Camera?
Excel Kamerası, çalışma sayfasının çizim katmanında belirli bir satır ve sütuna sabitlenmiş temelde bir resim nesnesidir. Normal eklenmiş bir resmin aksine, Kamera, `"A1:F10"` gibi bir A1 tarzı formül aracılığıyla bir kaynak aralığına bağlıdır. Bu aralıktaki herhangi bir hücre değiştiğinde, Kameranın görüntüsü yeni içeriği yansıtacak şekilde otomatik olarak yenilenir. Kamera, kaynak alanın tüm biçimlendirmesini korur; kenarlıklar, arka plan renkleri, yazı tipleri ve sayı biçimleri dahil; hücrelerin içinde görünen her şey Kameranın görüntüsünde de görünür. Bu, Kamerayı uzaktaki bir bölgenin görünür önizlemesini kaydırma veya veri tekrarı yapmadan görmek istediğiniz panolar, özetler, yan paneller ve rapor düzenleri için özellikle kullanışlı hale getirir. İki önemli uyarı geçerlidir: çalışma kitabını kaydetmeden önce `updateSelectedValue()` çağrısı yapmalısınız ve dosya HTML veya PDF formatında dışa aktarılacaktır; çünkü bu formatlar canlı yeniden hesaplamaya değil, gömülü görüntü verilerine güvenir.

## Method 1 — Add a Dynamic Camera Picture
Dinamik Kamera en yaygın yaklaşımdır ve Excel'in yerleşik Kamera aracına en yakın eşleşmedir. Başlangıçta görüntü içeriği olmayan bir resim ekleyerek, ardından kaynak aralığına başvuran bir `Formula` atayarak çalışır. Formül atandıktan sonra, `updateSelectedValue()` çağrısı, gömülü görüntü verilerini yansıttığı hücrelerle senkronize olacak şekilde yeniler. Kamera, özel bir sınıf aracılığıyla uygulanmaz; tamamen standart `Picture` türü üzerine inşa edilmiştir.
Temel API'ler şunlardır:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — verilen satır ve sütuna sabitlenmiş bir resim ekler. `stream` parametresi için `null` geçmek, dinamik Kamera için yer tutucu görevi gören boş bir resim oluşturur. Yöntem, yeni resmin dizinini döndürür.
- `worksheet.getPictures().get(index)` — koleksiyondan belirli bir `Picture` öğesini almak için dizin erişimi.
- `Picture.setFormula(String value)` — Kameranın yansıttığı kaynak aralığa A1 tarzı başvuruyu ayarlar, örneğin `"A1:F10"`.
- `Picture.updateSelectedValue()` — `Formula` tarafından başvurulan hücrelerden gömülü görüntü verilerini yenileyen void bir yöntemdir.

{{% alert color="primary" %}}
Çıktı HTML veya PDF olduğunda `updateSelectedValue()` kaydetmeden önce çağrılmalıdır; aksi takdirde dışa aktarılan dosya resim verilerini içermeyecek ve Kamera, işlenmiş çıktıda boş görünecektir.
{{% /alert %}}

Aşağıdaki kod bir çalışma kitabı oluşturur, satır 10 sütun 6'ya sabitlenmiş boş bir resim ekler, `setFormula` aracılığıyla onu kaynak aralık `A1:F10`'a bağlar, gömülü görüntü verilerini yeniler ve çalışma kitabını kaydeder.

```java
import java.io.InputStream;
import com.aspose.cells.PictureCollection;
import com.aspose.cells.SaveFormat;
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
PictureCollection pictures = worksheet.getPictures();
int index = pictures.add(10, 6, (InputStream) null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX);
```

## Method 2 — Add a Static Camera Picture
Statik Kamera, esasen bir hücre aralığının tek seferlik işlenmiş önizlemesidir. Canlı bir bağlantıyı sürdürmek yerine, aralığı bir kez görüntü baytlarına dönüştürür, bu baytları bir `ByteArrayInputStream` içine sarar ve bunları sıradan bir resim olarak eklersiniz. Görüntü içeriği oluşturulma anında sabitlenir ve kaynak hücreler değiştiğinde otomatik olarak yenilenmez.
Temel API'ler şunlardır:
- `Cells.createRange(String address)` — `"A1:F10"` gibi bir A1 tarzı adresten bir `Range` nesnesi oluşturur.
- `Range.toImage(ImageOrPrintOptions options)` — aralığı görüntü baytlarına dönüştürür. `null` geçmek varsayılan işleme seçeneklerini kullanır; çıktı üzerinde daha ayrıntılı kontrol için aşırı yüklemeler mevcuttur.
- `new ByteArrayInputStream(byte[] buffer)` — işlenmiş görüntü baytlarını, `PictureCollection.add` içine beslenebilen bir `ByteArrayInputStream` içine sarar.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — resmi verilen satır ve sütuna sabitlenmiş olarak ekler, bu kez işleme tarafından üretilen `ByteArrayInputStream`'i geçer.
Aşağıdaki kod bir çalışma kitabı oluşturur, `A1:F10` için bir `Range` oluşturur, `Range.toImage(null)` aracılığıyla onu görüntü baytlarına dönüştürür, baytları bir `ByteArrayInputStream` içine sarar, resmi satır 10 sütun 6'ya sabitlenmiş olarak ekler ve çalışma kitabını kaydeder.

```java
import java.io.ByteArrayInputStream;
import com.aspose.cells.PictureCollection;
import com.aspose.cells.Range;
import com.aspose.cells.SaveFormat;
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Static Camera: build Range, render to bytes, wrap in ByteArrayInputStream, add as picture
Range range = worksheet.getCells().createRange("A1:F10");
PictureCollection pictures = worksheet.getPictures();
pictures.add(10, 6, new ByteArrayInputStream(range.toImage(null)));
workbook.save("output_static.xlsx", SaveFormat.XLSX);
```

## Choosing Between Dynamic and Static
- **Dinamik Kamera:** her yeniden hesaplamada güncellenir, `updateSelectedValue()` sonrasında HTML ve PDF dışa aktarımını destekler ve dosyanın ömrü boyunca canlı bağlantı davranışını korur.
- **Statik Kamera:** asla güncellenmeyen tek seferlik bir işleme; derleme zamanında gömülü sabit bir görsel anlık görüntü istediğinizde, verilerin canlı bir yansıması yerine kullanışlıdır.
Aspose.Cells hem `Picture.Formula` ve `updateSelectedValue()` üzerine inşa edilmiş dinamik, otomatik yenilenen bir Kamerayı hem de `Range.toImage` ve bir `ByteArrayInputStream` üzerine inşa edilmiş statik, tek seferlik bir Kamerayı destekler. Çıktınızın kaynak hücrelerle senkronize kalması gerektiğinde dinamik yaklaşımı, yalnızca derleme zamanında sabit bir görsel anlık görüntüye ihtiyacınız olduğunda statik yaklaşımı seçin.

## Related Articles
- [Aspose.Cells for Java'da Mini Grafiği Görüntüye ve HTML'ye Dönüştürme](/cells/tr/java/convert-sparkline-to-image-and-html/)
- [Bir Hücreye Resim Ekleme](/cells/tr/java/inserting-an-image-into-a-cell/)
- [Aspose.Cells for Java'da Pivot Tablosuna Filtre Alanları Ekleme](/cells/tr/java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Java'da Pivot Tablolarına Stil Uygulama](/cells/tr/java/apply-style-to-pivot-table/)
- [Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme](/cells/tr/java/change-page-field-layout/)

{{< app/cells/assistant language="java" >}}