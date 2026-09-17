---
title: Aspose.Cells for Java'da Sparkline'ı Görüntüye ve HTML'e Dönüştürme
linktitle: Aspose.Cells for Java'da Sparkline'ı Görüntüye ve HTML'e Dönüştürme
description: Aspose.Cells sparkline'larını hücreye gömme için bağımsız görüntülere nasıl işleyeceğinizi ve HtmlSaveOptions kullanarak sparkline açısından zengin çalışma sayfalarını HTML'e nasıl aktaracağınızı öğrenin.
keywords: Aspose.Cells, Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, sparkline işleme, sparkline'ı görüntüye dönüştürme, sparkline'ı HTML'e aktarma
type: docs
weight: 120
url: /tr/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparkline'lar, çalışma sayfası hücrelerinin içine yerleştirilen küçük grafiklerdir. Aspose.Cells, her sparkline'ı bağımsız bir görüntü olarak çıkarmanıza (başka bir hücreye veya harici bir rapora gömmek için) ve ayrıca sparkline açısından zengin tüm çalışma sayfasını tarayıcı tabanlı dağıtım için HTML olarak dışa aktarmanıza olanak tanır. Bu makalede kullanılan `Cell.EmbeddedImage` özelliği **Aspose.Cells 26.5 ve sonrasında** kullanılabilir.
{{% /alert %}}

## **Introduction**
Sparkline'lar, eğilimleri doğrudan bir çalışma sayfası içinde görselleştirmenin kompakt bir yoludur. Excel kullanıcıları bunları yerinde görse de, birçok gerçek dünya senaryosunda bir sparkline'ın hücreden çıkması gerekir; örneğin, statik bir resim olarak farklı bir hücreye gömülmek, otomatik bir e-postaya eklenmek veya web'de yayınlanan bir HTML raporunun parçası olarak işlenmek için.
Aspose.Cells bu iki işlemi de destekler. `Sparkline.toImage` yöntemi, tek bir sparkline'ı bir akışa işler ve ortaya çıkan baytlar `Cell.EmbeddedImage`'a (`setEmbeddedImage` aracılığıyla) atanabilir, böylece resim çalışma kitabının tek bir hücresinin içinde saklanır. Ayrı olarak, `HtmlSaveOptions` tüm çalışma kitabını — sparkline'lar dahil — kendi kendine yeten bir HTML dosyasına dönüştürmenize olanak tanır. Bu makale, her iki iş akışını da uçtan uca ele almaktadır.

## **Workflow 1 — Render Sparklines to Images and Embed Them into Cells**
Bu iş akışında, kaynak değerlerden oluşan küçük bir aralık içeren bir çalışma sayfası oluşturacak, o aralığa üç farklı sparkline grubu (Çizgi, Sütun ve Yığılmış/Kazanma-Kaybetme) ekleyecek, her grubu PNG olarak işleyecek ve bu PNG baytlarını bitişik hücrelere gömülü görüntüler olarak yazacaksınız. Sonuç, hem canlı sparkline'ları hem de bunların işlenmiş resim karşılıklarını içeren tek bir `.xlsx` dosyasıdır.

### **Step-by-Step Instructions**
1. Bir çalışma dizini tanımlayın ve diskte var olduğundan emin olun.
2. Yeni bir `Workbook` oluşturun ve ilk `Worksheet`'e bir referans elde edin.
3. `A1`'den `E1`'e kadar olan hücreleri beş örnek sayısal değerle doldurun (örneğin, günlük satışlar veya sıcaklık okumaları).
4. `worksheet.getSparklineGroups().add(...)` çağrısı yaparak çalışma sayfasına üç `SparklineGroup` nesnesi ekleyin:
   - `F1`'e sabitlenmiş ve veri aralığı `A1:E1` olan bir `SparklineType.LINE` grubu.
   - `G1`'e sabitlenmiş ve veri aralığı `A1:E1` olan bir `SparklineType.COLUMN` grubu.
   - `H1`'e sabitlenmiş ve veri aralığı `A1:E1` olan bir `SparklineType.STACKED` (kazanma/kaybetme) grubu.
5. Bir `ImageOrPrintOptions` örneği oluşturun ve her sparkline'ın şeffaf bir PNG olarak işlenmesi için `setImageType(ImageType.PNG)` çağrısı yapın.
7. Çalışma kitabını diske kaydetmek için `workbook.save("output_with_sparklines.xlsx")` çağrısı yapın.

```java
import com.aspose.cells.*;
import java.io.*;
// Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// A1:E1 hücrelerine örnek veri doldur
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

Yukarıdaki kod, bir sparkline'ın her görsel temsilinin iki biçimde çoğaltıldığı bir çalışma kitabı üretir: 1. satıra sabitlenmiş canlı, yerel sparkline ve 2. satırdaki bitişik bir hücreye doğrudan gömülü statik bir PNG resmi. Resimler dosyanın kendisi içinde yer aldığından, çalışma kitabı gömülü görüntü referanslarını bozmadan e-postayla gönderilebilen veya arşivlenebilen tek bir kendi kendine yeten yapı olarak kalır. Her sparkline grubunu bir PNG olarak işleyin, `ByteArrayOutputStream`'i `byte[]`'e dönüştürün ve diziyi `setEmbeddedImage(byte[])` aracılığıyla hedef hücrenin `EmbeddedImage` özelliğine atayın — atama, resmin hücrenin saklanan içeriğinin bir parçası olmasını sağlayan şeydir.

{{% alert color="primary" %}}
Her sparkline grubu tek bir hücreye sabitlendiğinden, `for` döngüsü ile numaralandırmak yerine `group.getSparklines().get(0)` indeksleyicisi aracılığıyla ona erişebilirsiniz. Bu, işleme kodunu kısa tutar ve tipik "sabitlenen hücre başına bir sparkline" kalıbıyla eşleşir. Resim baytlarını `Cell.EmbeddedImage` (`setEmbeddedImage` aracılığıyla ayarlanır) üzerinden saklamak Aspose.Cells 26.5 veya üstünü gerektirir.

## **Workflow 2 — Export the Sparkline Worksheet to HTML**
Çalışma kitabı canlı sparkline'lar (ve isteğe bağlı olarak gömülü resim karşılıkları) içerdiğinde, tüm çalışma sayfası HTML olarak kaydedilerek web'de yayınlanabilir. `HtmlSaveOptions` sınıfı, bu dışa aktarımı kontrol etmek için ihtiyacınız olan düğmeleri sunar; bu iş akışında İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasını yeniden kullanacak ve onu temiz, tek sayfalık bir HTML belgesine dönüştüreceksiniz.

### **Step-by-Step Instructions**
1. İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasının çalışma dizininizde diskte mevcut olduğundan emin olun.
2. Bu dosyayı yeni bir `Workbook` örneğine yükleyin.
3. `HtmlSaveOptions`'ı örnekleyin ve ortaya çıkan HTML dosyasının tüm çalışma kitabı yerine yalnızca etkin çalışma sayfasını içermesi için `setExportActiveWorksheetOnly(true)` çağrısı yapın.
4. HTML çıktısını diske yazmak için `workbook.save("sparklines.html", htmlOptions)` çağrısı yapın.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Yukarıdaki kod, İş Akışı 1'den gelen sparkline açısından zengin çalışma kitabını alır ve onu taşınabilir bir HTML dosyasına dönüştürür. Sparkline'lar, dışa aktarım moduna bağlı olarak, oluşturulan HTML içinde satır içi SVG veya PNG işlemeleri olarak korunur, böylece son kullanıcılar Excel yüklemeye gerek kalmadan eğilimleri herhangi bir modern tarayıcıda görüntüleyebilir. `ExportActiveWorksheetOnly` öğesini `setExportActiveWorksheetOnly(true)` aracılığıyla `true` olarak ayarlayarak, yanlışlıkla gizli sayfaları veya yardımcı verileri yayınlamaktan kaçınırsınız — yalnızca kullanıcı tarafından o anda görülebilen çalışma sayfası dışa aktarılır.
{{% /alert %}}

{{% alert color="primary" %}}
`HtmlSaveOptions` sınıfı, `ExportHiddenWorksheet`, `ExportImagesAsBase64` ve `Encoding` gibi çıktıyı ince ayar yapmak için ek özellikler sunar. Bunları dağıtım hedefinize göre gerektiği gibi ayarlayın.

## **API Summary**
Yukarıdaki iş akışları, birlikte çalışan küçük bir Aspose.Cells API setine dayanır.
- `SparklineGroup` ve koleksiyon erişimcisi `worksheet.getSparklineGroups()`, her sparkline grubu için türü (Çizgi, Sütun, Yığılmış), veri aralığını ve sabitleme hücresini bildirmek için kullanılır. Bu makalede her grup tek bir hücreye sabitlenmiştir, bu nedenle gruba `worksheet.getSparklineGroups().get(i)` aracılığıyla erişilir.
- `Sparkline` ve indeksleyici `group.getSparklines().get(0)`, bir grup içindeki tek tek sparkline'ı döndürür. Örnekteki her grup tam olarak bir sparkline içerdiğinden, `for` döngüsü gerekmez.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)`, sparkline'ın bir resmini sağlanan `Stream`'e yazan işleme yöntemidir. Yöntem `void` döndürür; çağrıdan sonra baytları akıştan okursunuz.
- `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)`, HTML dışa aktarımını etkin çalışma sayfasıyla sınırlar. Tek sayfalık raporlar oluştururken `HtmlSaveOptions` üzerinde en sık kullanılan özelliklerden biridir.
- `ImageOrPrintOptions.setImageType(ImageType)`, `com.aspose.cells.drawing` paketinde bulunur ve `toImage` ile işlerken ve çalışma sayfalarını görüntülere yazdırırken kullanılan resim biçimini (örneğin, `ImageType.PNG`) seçer.

## **Related Articles**
- [Bir Hücreye Resim Ekleme](/cells/tr/java/inserting-an-image-into-a-cell/)
{{% /alert %}}

{{< app/cells/assistant language="java" >}}