---
title: Aspose.Cells for Python via Java'da Sparkline'ı Görüntüye ve HTML'e Dönüştürme
linktitle: Aspose.Cells for Python via Java'da Sparkline'ı Görüntüye ve HTML'e Dönüştürme
description: Aspose.Cells sparkline'larını hücre gömme için bağımsız görüntüler olarak işlemeyi ve sparkline açısından zengin çalışma sayfalarını HtmlSaveOptions kullanarak HTML'e aktarmayı öğrenin.
keywords: Aspose.Cells, Python via Java, sparkline, Sparkline.toImage, Cell.embeddedImage, HtmlSaveOptions, sparkline işleme, sparkline'ı görüntüye dönüştürme, sparkline'ı HTML'e aktarma
type: docs
weight: 120
url: /tr/python-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparkline'lar çalışma sayfası hücrelerinin içine yerleştirilen küçük grafiklerdir. Aspose.Cells her bir sparkline'ı bağımsız bir görüntü olarak çıkarmanıza (başka bir hücreye veya harici bir rapora gömmek için) ve ayrıca sparkline açısından zengin çalışma sayfasının tamamını tarayıcı tabanlı dağıtım için HTML olarak dışa aktarmanıza olanak tanır. Bu makalede kullanılan `Cell.embedded_image` özelliği **Aspose.Cells 26.5 ve sonrasında** kullanılabilir.
{{% /alert %}}

## **Giriş**
Sparkline'lar, eğilimleri doğrudan bir çalışma sayfasının içinde görselleştirmenin kompakt bir yoludur. Excel kullanıcıları onları yerinde görse de, birçok gerçek dünya senaryosunda bir sparkline'ın hücreden çıkması gerekir — örneğin, başka bir hücreye statik bir resim olarak gömülmek, otomatik bir e-postaya eklenmek veya web'de yayınlanan bir HTML raporunun parçası olarak işlenmek.
Aspose.Cells bu işlemlerin her ikisini de destekler. `Sparkline.to_image` metodu, tek bir sparkline'ı bir akışa işler ve ortaya çıkan baytlar, resmin çalışma kitabının tek bir hücresinin içinde saklanması için `Cell.embedded_image`'a atanabilir. Ayrı olarak, `HtmlSaveOptions` tüm çalışma kitabını — sparkline'lar dahil — kendi kendine yeten bir HTML dosyasına dönüştürmenize olanak tanır. Bu makale her iki iş akışını da uçtan uca ele almaktadır.

## **İş Akışı 1 — Sparkline'ları Görüntülere İşleme ve Hücrelere Gömme**
Bu iş akışında, küçük bir kaynak değer aralığı içeren bir çalışma sayfası oluşturacak, o aralığa üç farklı sparkline grubu (Çizgi, Sütun ve Yığılmış/Kazanç-Kayıp) ekleyecek, her grubu PNG olarak işleyecek ve bu PNG baytlarını bitişik hücrelere gömülü görüntüler olarak yazacaksınız. Nihai sonuç, hem canlı sparkline'ları hem de işlenmiş resim karşılıklarını içeren tek bir `.xlsx` dosyasıdır.

### **Adım Adım Talimatlar**
1. Bir çalışma dizini tanımlayın ve diskte var olduğundan emin olun.
2. Yeni bir `Workbook` oluşturun ve ilk `Worksheet`'e bir referans edinin.
3. `A1` ile `E1` hücreleri arasına beş örnek sayısal değer (örneğin, günlük satışlar veya sıcaklık okumaları) yerleştirin.
4. `worksheet.sparkline_groups.add(...)` çağırarak çalışma sayfasına üç `SparklineGroup` nesnesi ekleyin:
   - `F1`'e sabitlenmiş ve veri aralığı `A1:E1` olan bir `SparklineType.LINE` grubu.
   - `G1`'e sabitlenmiş ve veri aralığı `A1:E1` olan bir `SparklineType.COLUMN` grubu.
   - `H1`'e sabitlenmiş ve veri aralığı `A1:E1` olan bir `SparklineType.STACKED` (kazanç/kayıp) grubu.
5. Bir `ImageOrPrintOptions` örneği oluşturun ve `image_type` özelliğini `ImageType.PNG` olarak ayarlayın, böylece her sparkline şeffaf bir PNG olarak işlenir.
7. Çalışma kitabını `output_with_sparklines.xlsx` olarak kaydedin.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, ImageType, ImageOrPrintOptions, Sparkline
from jpype import JClass
ByteArrayOutputStream = JClass('java.io.ByteArrayOutputStream')
# Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# A1:E1 hücrelerine örnek veri yerleştir
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# F1'de (sütun 5, satır 0) sabitlenmiş bir Çizgi mini grafik grubu ekle
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, lineArea)
# G1'de (sütun 6, satır 0) sabitlenmiş bir Sütun mini grafik grubu ekle
columnArea = CellArea()
columnArea.setStartColumn(6)
columnArea.setEndColumn(6)
columnArea.setStartRow(0)
columnArea.setEndRow(0)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.Column, "A1:E1", False, columnArea)
# H1'de (sütun 7, satır 0) sabitlenmiş bir Kazanma/Kaybetme (Yığılmış) mini grafik grubu ekle
stackedArea = CellArea()
stackedArea.setStartColumn(7)
stackedArea.setEndColumn(7)
stackedArea.setStartRow(0)
stackedArea.setEndRow(0)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.Stacked, "A1:E1", False, stackedArea)
# PNG çıktısı için görüntü seçeneklerini yapılandır
imageOptions = ImageOrPrintOptions()
imageOptions.setImageType(ImageType.Png)
# Çizgi mini grafiğini görüntüye dönüştür ve F2 hücresine göm
lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
lineSp.toImage(ms, imageOptions)
worksheet.getCells().get("F2").setEmbeddedImage(ms.toByteArray())
# Sütun mini grafiğini görüntüye dönüştür ve G2 hücresine göm
columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
columnSp.toImage(ms, imageOptions)
worksheet.getCells().get("G2").setEmbeddedImage(ms.toByteArray())
# Kazanma/Kaybetme mini grafiğini görüntüye dönüştür ve H2 hücresine göm
stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
stackedSp.toImage(ms, imageOptions)
worksheet.getCells().get("H2").setEmbeddedImage(ms.toByteArray())
# Çalışma kitabını diske kaydet
workbook.save("output_with_sparklines.xlsx")
jpype.shutdownJVM()
```

Yukarıdaki kod, bir sparkline'ın her görsel temsilinin iki biçimde çoğaltıldığı bir çalışma kitabı üretir: 1. satıra sabitlenmiş canlı, yerel sparkline ve 2. satırdaki bitişik bir hücreye doğrudan gömülmüş statik bir PNG resmi. Resimler dosyanın kendisinin içinde yaşadığı için, çalışma kitabı gömülü görüntü referanslarını kırmadan e-postalanabilen veya arşivlenebilen tek bir kendi kendine yeten yapı olarak kalır. Her sparkline grubunu PNG olarak işleyin, `ByteArrayOutputStream`'i bir `byte[]`'e dönüştürün (veya Python `bytes` nesnesi elde etmek için `to_byte_array()` kullanın) ve diziyi hedef hücrenin `embedded_image` özelliğine atayın — atama işlemi, resmi hücrenin saklanan içeriklerinin bir parçası yapan şeydir.

{{% alert color="primary" %}}
Her sparkline grubu tek bir hücreye sabitlendiğinden, onu bir `for` döngüsü ile numaralandırmak yerine `group.sparklines[0]` dizin oluşturucusu aracılığıyla adresleyebilirsiniz. Bu, işleme kodunu kısa tutar ve tipik "sabit hücre başına bir sparkline" kalıbıyla eşleşir. Resim baytlarını `Cell.embedded_image` aracılığıyla saklamak Aspose.Cells 26.5 veya sonrasını gerektirir.

## **İş Akışı 2 — Sparkline Çalışma Sayfasını HTML'e Aktarma**
Çalışma kitabı canlı sparkline'ları (ve isteğe bağlı olarak gömülü resim karşılıklarını) içerdiğinde, tüm çalışma sayfası HTML olarak kaydedilerek web'de yayınlanabilir. `HtmlSaveOptions` sınıfı, bu dışa aktarımı kontrol etmek için ihtiyacınız olan düğmeleri sunar; bu iş akışında İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasını yeniden kullanacak ve onu temiz, tek sayfalık bir HTML belgesine dönüştüreceksiniz.

### **Adım Adım Talimatlar**
1. İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasının çalışma dizininizde diskte mevcut olduğundan emin olun.
2. Bu dosyayı yeni bir `Workbook` örneğine yükleyin.
3. `HtmlSaveOptions`'ı örnekleyin ve `export_active_worksheet_only` özelliğini `True` olarak ayarlayın, böylece ortaya çıkan HTML dosyası tüm çalışma kitabı yerine yalnızca aktif çalışma sayfasını içerir.
4. HTML çıktısını diske yazmak için `workbook.save("sparklines.html", html_options)` çağırın.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, HtmlSaveOptions
workbook = Workbook("output_with_sparklines.xlsx")
htmlOptions = HtmlSaveOptions()
htmlOptions.setExportActiveWorksheetOnly(True)
workbook.save("sparklines.html", htmlOptions)
jpype.shutdownJVM()
```

Yukarıdaki kod, İş Akışı 1'den gelen sparkline açısından zengin çalışma kitabını alır ve onu taşınabilir bir HTML dosyasına dönüştürür. Sparkline'lar, dışa aktarma moduna bağlı olarak oluşturulan HTML içinde satır içi SVG veya PNG işlemeleri olarak korunur, böylece son kullanıcılar Excel yüklemeye gerek kalmadan trendleri herhangi bir modern tarayıcıda görüntüleyebilir. `export_active_worksheet_only`'ı `True` olarak ayarlayarak, gizli sayfaları veya yardımcı verileri yanlışlıkla yayınlamaktan kaçınırsınız — yalnızca kullanıcı tarafından o anda görülebilen çalışma sayfası dışa aktarılır.
{{% /alert %}}

{{% alert color="primary" %}}
`HtmlSaveOptions` sınıfı, çıktıyı ince ayar yapmak için `export_hidden_worksheet`, `export_images_as_base64` ve `encoding` gibi ek özellikler sunar. Bunları dağıtım hedefinize göre gerektiği gibi ayarlayın.

## **API Özeti**
Yukarıdaki iş akışları, birlikte çalışan küçük bir Aspose.Cells API kümesine dayanır.
- Her sparkline grubu için türü (Çizgi, Sütun, Yığılmış), veri aralığını ve sabitleme hücresini bildirmek için `SparklineGroup` ve koleksiyon erişimcisi `worksheet.sparkline_groups` kullanılır. Bu makalede her grup tek bir hücreye sabitlendiğinden, gruba `worksheet.sparkline_groups[i]` aracılığıyla erişilir.
- `Sparkline` ve `group.sparklines[0]` dizin oluşturucusu, grup içindeki tek tek sparkline'ı döndürür. Örnekteki her grup tam olarak bir sparkline içerdiğinden, `for` döngüsü gerekmez.
- `Sparkline.to_image(OutputStream, ImageOrPrintOptions)`, sparkline'ın resmini sağlanan bir `OutputStream`'e (örneğin bir `ByteArrayOutputStream`) yazan işleme yöntemidir. Yöntem `void` döndürür; baytları çağrıdan sonra akıştan okursunuz.
- `HtmlSaveOptions.export_active_worksheet_only` (bir `bool`) HTML dışa aktarımını aktif çalışma sayfasıyla sınırlar. Tek sayfalık raporlar oluştururken `HtmlSaveOptions`'ın en sık kullanılan özelliklerinden biridir.
- `ImageOrPrintOptions.image_type`, `com.aspose.cells.drawing` namespace'inde yaşar ve `to_image` ile işlerken ve çalışma sayfalarını görüntülere yazdırırken kullanılan resim biçimini (örneğin, `ImageType.PNG`) seçer.
- [Aspose.Cells for Python via Java'da Sparkline'lar](/cells/tr/python-java/sparkline/)
{{% /alert %}}

{{< app/cells/assistant language="python" >}}