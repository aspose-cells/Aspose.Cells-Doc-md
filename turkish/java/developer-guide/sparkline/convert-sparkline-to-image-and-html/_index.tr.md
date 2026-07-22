---
title: Aspose.Cells for Java'da Sparkline'ı Görüntüye ve HTML'ye Dönüştürme
linktitle: Convert Sparkline to Image and HTML
description: Aspose.Cells sparkline'larını hücreye gömme için bağımsız görüntüler olarak işlemeyi ve sparkline açısından zengin çalışma sayfalarını HtmlSaveOptions kullanarak HTML olarak dışa aktarmayı öğrenin.
keywords: Aspose.Cells, Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, sparkline işleme, sparkline'ı görüntüye dönüştürme, sparkline'ı HTML'ye aktarma
type: docs
weight: 120
url: /tr/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines (kıvılcım grafikler) çalışma sayfası hücrelerinin içine yerleştirilmiş mini grafiklerdir. Aspose.Cells, her bir sparkline'ı bağımsız bir görüntü olarak çıkarmanıza (başka bir hücreye veya harici bir rapora gömmek için) ve ayrıca sparkline açısından zengin çalışma sayfasının tamamını tarayıcı tabanlı dağıtım için HTML olarak dışa aktarmanıza olanak tanır. Bu makalede kullanılan `Cell.EmbeddedImage` özelliği **Aspose.Cells 26.5 ve sonrasında** kullanılabilir.
{{% /alert %}}

## **Giriş**

Sparklines, bir çalışma sayfasının içinde doğrudan eğilimleri görselleştirmenin kompakt bir yoludur. Excel kullanıcıları bunları yerinde görse de, birçok gerçek dünya senaryosunda sparkline'ın hücreden çıkması gerekir — örneğin, farklı bir hücreye statik resim olarak gömülmesi, otomatik bir e-postaya eklenmesi veya web'de yayınlanan bir HTML raporunun parçası olarak işlenmesi.

Aspose.Cells bu iki işlemi de destekler. `Sparkline.toImage` metodu, tek bir sparkline'ı bir akışa işler ve ortaya çıkan baytlar `Cell.EmbeddedImage` özelliğine (`setEmbeddedImage` aracılığıyla) atanabilir, böylece resim çalışma kitabının tek bir hücresinde saklanır. Ayrı olarak, `HtmlSaveOptions` tüm çalışma kitabını — sparkline'lar dahil — kendi kendine yeten bir HTML dosyasına dönüştürmenize olanak tanır. Bu makale her iki iş akışını da uçtan uca ele almaktadır.

## **İş Akışı 1 — Sparkline'ları Görüntülere İşleme ve Hücrelere Gömme**

Bu iş akışında, küçük bir kaynak değer aralığı içeren bir çalışma sayfası oluşturacak, o aralığa üç farklı sparkline grubu (Çizgi, Sütun ve Yığılmış/Kazanç-Kayıp) ekleyecek, her grubu PNG olarak işleyecek ve bu PNG baytlarını bitişik hücrelere gömülü görüntüler olarak yazacaksınız. Sonuç, hem canlı sparkline'ları hem de bunların işlenmiş resim karşılıklarını içeren tek bir `.xlsx` dosyasıdır.

### **Adım Adım Talimatlar**

1. Bir çalışma dizini tanımlayın ve diskte var olduğundan emin olun.
2. Yeni bir `Workbook` oluşturun ve ilk `Worksheet`'e bir referans elde edin.
3. `A1`'den `E1`'e kadar olan hücreleri beş örnek sayısal değerle doldurun (örneğin, günlük satışlar veya sıcaklık okumaları).
4. `worksheet.getSparklineGroups().add(...)` çağırarak çalışma sayfasına üç `SparklineGroup` nesnesi ekleyin:
   - Veri aralığı `A1:E1` olan, `F1`'e ankrajlanmış bir `SparklineType.LINE` grubu.
   - Veri aralığı `A1:E1` olan, `G1`'e ankrajlanmış bir `SparklineType.COLUMN` grubu.
   - Veri aralığı `A1:E1` olan, `H1`'e ankrajlanmış bir `SparklineType.STACKED` (kazanç/kayıp) grubu.
5. Bir `ImageOrPrintOptions` örneği oluşturun ve her sparkline'ın şeffaf bir PNG olarak işlenmesi için `setImageType(ImageType.PNG)` çağırın.
6. Üç grubun her biri için, `group.getSparklines().get(0).toImage(byteArrayOutputStream, imageOptions)` kullanarak tek sparkline'ı işleyin, `ByteArrayOutputStream`'i `byte[]`'e dönüştürün ve diziyi sırasıyla `worksheet.getCells().get("F2").setEmbeddedImage(...)`, `worksheet.getCells().get("G2").setEmbeddedImage(...)` ve `worksheet.getCells().get("H2").setEmbeddedImage(...)` aracılığıyla atayın.
7. Çalışma kitabını diske kaydetmek için `workbook.save("output_with_sparklines.xlsx")` çağırın.

```java
import com.aspose.cells.*;
import java.io.*;

// Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// A1:E1 hücrelerine örnek veri yerleştir
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// F1 hücresine (sütun 5, satır 0) sabitlenmiş bir Çizgi mini grafik grubu ekle
CellArea lineArea = CellArea.createCellArea(5, 0, 5, 0);
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);

// G1 hücresine (sütun 6, satır 0) sabitlenmiş bir Sütun mini grafik grubu ekle
CellArea columnArea = CellArea.createCellArea(6, 0, 6, 0);
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);

// H1 hücresine (sütun 7, satır 0) sabitlenmiş bir Kazanma/Kaybetme (Yığılmış) mini grafik grubu ekle
CellArea stackedArea = CellArea.createCellArea(7, 0, 7, 0);
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);

// PNG çıktısı için görüntü seçeneklerini yapılandır
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.setImageType(ImageType.PNG);

// Çizgi mini grafiğini görüntüye dönüştür ve F2 hücresine göm
Sparkline lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
ByteArrayOutputStream lineMs = new ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// Sütun mini grafiğini görüntüye dönüştür ve G2 hücresine göm
Sparkline columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
ByteArrayOutputStream columnMs = new ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// Kazanma/Kaybetme mini grafiğini görüntüye dönüştür ve H2 hücresine göm
Sparkline stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
ByteArrayOutputStream stackedMs = new ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// Çalışma kitabını diske kaydet
workbook.save("output_with_sparklines.xlsx");
```

Yukarıdaki kod, bir sparkline'ın her görsel temsilinin iki biçimde çoğaltıldığı bir çalışma kitabı üretir: 1. satıra ankrajlanmış canlı, yerel sparkline ve 2. satırdaki bitişik bir hücreye doğrudan gömülmüş statik bir PNG resmi. Resimler dosyanın kendisinde yaşadığından, çalışma kitabı gömülü görüntü referanslarını bozmadan e-postayla gönderilebilen veya arşivlenebilen tek bir kendi kendine yeten yapı olarak kalır. Her sparkline grubunu PNG olarak işleyin, `ByteArrayOutputStream`'i `byte[]`'e dönüştürün ve diziyi `setEmbeddedImage(byte[])` aracılığıyla hedef hücrenin `EmbeddedImage` özelliğine atayın — atama, resmi hücrenin saklanan içeriklerinin bir parçası yapan şeydir.

{{% alert color="primary" %}}
Her sparkline grubu tek bir hücreye ankrajlandığından, `for` döngüsü ile numaralandırmak yerine `group.getSparklines().get(0)` indeksleyicisi aracılığıyla ona erişebilirsiniz. Bu, işleme kodunu kısa tutar ve tipik "ankraj hücresi başına bir sparkline" kalıbıyla eşleşir. Resim baytlarının `Cell.EmbeddedImage` aracılığıyla saklanması (`setEmbeddedImage` ile ayarlanır) Aspose.Cells 26.5 veya üzerini gerektirir.
{{% /alert %}}

## **İş Akışı 2 — Sparkline Çalışma Sayfasını HTML'ye Aktarma**

Çalışma kitabı canlı sparkline'ları (ve isteğe bağlı olarak gömülü resim karşılıklarını) içerdiğinde, çalışma sayfasının tamamı HTML olarak kaydedilerek web'de yayınlanabilir. `HtmlSaveOptions` sınıfı, bu dışa aktarımı kontrol etmek için ihtiyacınız olan düğmeleri sunar; bu iş akışında İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasını yeniden kullanacak ve onu temiz, tek sayfalık bir HTML belgesine dönüştüreceksiniz.

### **Adım Adım Talimatlar**

1. İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasının çalışma dizininizde diskte mevcut olduğundan emin olun.
2. Bu dosyayı yeni bir `Workbook` örneğine yükleyin.
3. `HtmlSaveOptions` örneğini oluşturun ve ortaya çıkan HTML dosyasının tüm çalışma kitabı yerine yalnızca etkin çalışma sayfasını içermesi için `setExportActiveWorksheetOnly(true)` çağırın.
4. HTML çıktısını diske yazmak için `workbook.save("sparklines.html", htmlOptions)` çağırın.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Yukarıdaki kod, İş Akışı 1'den gelen sparkline açısından zengin çalışma kitabını alır ve onu taşınabilir bir HTML dosyasına dönüştürür. Sparklines, oluşturulan HTML içinde dışa aktarım moduna bağlı olarak satır içi SVG veya PNG işlemeleri olarak korunur, böylece son kullanıcılar Excel yüklemeye gerek kalmadan eğilimleri herhangi bir modern tarayıcıda görüntüleyebilir. `setExportActiveWorksheetOnly(true)` aracılığıyla `ExportActiveWorksheetOnly`'i `true` olarak ayarlayarak, gizli sayfaları veya yardımcı verileri yanlışlıkla yayınlamaktan kaçınırsınız — yalnızca kullanıcı tarafından o anda görülebilen çalışma sayfası dışa aktarılır.

{{% alert color="primary" %}}
`HtmlSaveOptions` sınıfı, çıktıyı ince ayar yapmak için `ExportHiddenWorksheet`, `ExportImagesAsBase64` ve `Encoding` gibi ek özellikler sunar. Bunları dağıtım hedefinize göre gerektiği gibi ayarlayın.
{{% /alert %}}

## **API Özeti**

Yukarıdaki iş akışları, birlikte çalışan küçük bir Aspose.Cells API kümesine dayanır.

- `SparklineGroup` ve koleksiyon erişimcisi `worksheet.getSparklineGroups()`, her sparkline grubu için türü (Çizgi, Sütun, Yığılmış), veri aralığını ve ankraj hücresini bildirmek için kullanılır. Bu makalede her grup tek bir hücreye ankrajlandığından, gruba `worksheet.getSparklineGroups().get(i)` aracılığıyla erişilir.
- `Sparkline` ve `group.getSparklines().get(0)` indeksleyicisi, bir grup içindeki tek tek sparkline'ı döndürür. Örnekteki her grup tam olarak bir sparkline içerdiğinden, `for` döngüsü gerekmez.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)`, sağlanan `Stream`'e sparkline'ın bir resmini yazan işleme metodudur. Metod `void` döndürür; baytları çağrıdan sonra akıştan okursunuz.
- `Cell.EmbeddedImage`, tek bir hücrenin içine bir resim saklayan bir `byte[]` özelliğidir (`cell.setEmbeddedImage(byte[])` ile atanır). **Aspose.Cells 26.5 ve sonrasında** kullanılabilir ve `toImage` ile işlenen bir sparkline'ı aynı çalışma kitabına geri yuvarlamanın önerilen yoludur.
- `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)`, HTML dışa aktarımını etkin çalışma sayfasıyla sınırlar. Tek sayfalık raporlar oluştururken `HtmlSaveOptions` üzerindeki en sık kullanılan özelliklerden biridir.
- `ImageOrPrintOptions.setImageType(ImageType)`, `com.aspose.cells.drawing` paketinde bulunur ve `toImage` ile işlenirken ve çalışma sayfaları görüntülere yazdırılırken kullanılan resim biçimini (örneğin, `ImageType.PNG`) seçer.

## **İlgili Makaleler**

- [Aspose.Cells for Java'da Sparklines](/cells/tr/java/sparkline/)
- [Bir Hücreye Resim Ekleme](/cells/tr/java/inserting-an-image-into-a-cell/)
- [SmartMarker Tek Hücre Dizi İşleme | Aspose.Cells Java](/cells/tr/java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="java" >}}