---
title: Aspose.Cells for Node.js via Java ile Sparkline'ı Görüntüye ve HTML'ye Dönüştürme
linktitle: Aspose.Cells for Node.js via Java ile Sparkline'ı Görüntüye ve HTML'ye Dönüştürme
description: Aspose.Cells sparkline'larını bağımsız görüntülere dönüştürmeyi, hücrelere gömmek için ve HtmlSaveOptions kullanarak sparkline açısından zengin çalışma sayfalarını HTML'ye aktarmayı öğrenin.
keywords: Aspose.Cells, Node.js via Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, sparkline oluşturma, sparkline'ı görüntüye dönüştürme, sparkline'ı HTML'ye aktarma
type: docs
weight: 120
url: /tr/nodejs-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparkline'lar çalışma sayfası hücrelerinin içine yerleştirilmiş küçük grafiklerdir. Aspose.Cells her bir sparkline'ı bağımsız bir görüntü olarak çıkarmanıza (başka bir hücreye veya harici bir rapora gömmek için) ve ayrıca sparkline açısından zengin tüm çalışma sayfasını tarayıcı tabanlı dağıtım için HTML'ye aktarmanıza olanak tanır. Bu makalede kullanılan `Cell.EmbeddedImage` özelliği **Aspose.Cells 26.5 ve sonrasında** kullanılabilir.
{{% /alert %}}

## **Introduction**
Sparkline'lar, eğilimleri doğrudan bir çalışma sayfasının içinde görselleştirmenin kompakt bir yoludur. Excel kullanıcıları onları yerinde görse de, birçok gerçek dünya senaryosu bir sparkline'ın hücreden çıkmasını gerektirir; örneğin statik bir resim olarak farklı bir hücreye gömülmek, otomatik bir e-postaya eklenmek veya web'de yayınlanan bir HTML raporunun parçası olarak oluşturulmak.
Aspose.Cells bu işlemlerin her ikisini de destekler. `Sparkline.toImage` yöntemi tek bir sparkline'ı bir akışa dönüştürür ve elde edilen baytlar `Cell.EmbeddedImage`'a atanarak resim çalışma kitabının tek bir hücresinin içinde saklanabilir. Ayrı olarak, `HtmlSaveOptions` tüm çalışma kitabını — sparkline'lar dahil — kendi kendine yeten bir HTML dosyasına dönüştürmenize olanak tanır. Bu makale her iki iş akışını da uçtan uca ele almaktadır.

## **Workflow 1 — Render Sparklines to Images and Embed Them into Cells**
Bu iş akışında, kaynak değerlerin küçük bir aralığını içeren bir çalışma sayfası oluşturacak, o aralığa üç farklı sparkline grubu (Çizgi, Sütun ve Yığılmış/Kazanma-Kaybetme) ekleyecek, her grubu PNG olarak oluşturacak ve bu PNG baytlarını bitişik hücrelere gömülü görüntüler olarak yazacaksınız. Son sonuç, hem canlı sparkline'ları hem de oluşturulan resim karşılıklarını içeren tek bir `.xlsx` dosyasıdır.

### **Step-by-Step Instructions**
1. Bir çalışma dizini tanımlayın ve diskte mevcut olduğundan emin olun.
2. Yeni bir `Workbook` oluşturun ve ilk `Worksheet`'e bir referans edinin.
3. `A1`'den `E1`'e kadar olan hücreleri beş örnek sayısal değerle doldurun (örneğin, günlük satışlar veya sıcaklık okumaları).
4. Çalışma sayfasına `worksheet.sparklineGroups.add(...)` çağrısıyla üç `SparklineGroup` nesnesi ekleyin:
   - `F1`'e sabitlenmiş, veri aralığı `A1:E1` olan bir `SparklineType.Line` grubu.
   - `G1`'e sabitlenmiş, veri aralığı `A1:E1` olan bir `SparklineType.Column` grubu.
   - `H1`'e sabitlenmiş, veri aralığı `A1:E1` olan bir `SparklineType.Stacked` (kazanma/kaybetme) grubu.
5. Her sparkline'ın şeffaf bir PNG olarak oluşturulması için bir `ImageOrPrintOptions` örneği oluşturun ve `ImageType` özelliğini `ImageType.Png` olarak ayarlayın.
7. Çalışma kitabını `output_with_sparklines.xlsx` olarak kaydedin.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// A1:E1 hücrelerine örnek veri yerleştir
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// F1'de (sütun 5, satır 0) sabitlenmiş bir Çizgi sparkline grubu ekle
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
// G1'de (sütun 6, satır 0) sabitlenmiş bir Sütun sparkline grubu ekle
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
// H1'de (sütun 7, satır 0) sabitlenmiş bir Kazanma/Kaybetme (Yığılmış) sparkline grubu ekle
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
// PNG çıktısı için görüntü seçeneklerini yapılandır
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);
// Çizgi sparkline'ı görüntüye dönüştür ve F2 hücresine göm
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let lineMs = new java.io.ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());
// Sütun sparkline'ı görüntüye dönüştür ve G2 hücresine göm
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnMs = new java.io.ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());
// Kazanma/Kaybetme sparkline'ı görüntüye dönüştür ve H2 hücresine göm
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedMs = new java.io.ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());
// Çalışma kitabını diske kaydet
workbook.save("output_with_sparklines.xlsx");
```

Yukarıdaki kod, bir sparkline'ın her görsel temsilinin iki biçimde çoğaltıldığı bir çalışma kitabı üretir: 1. satıra sabitlenmiş canlı, yerel sparkline ve 2. satırdaki bitişik bir hücreye doğrudan gömülü statik bir PNG resmi. Resimler dosyanın kendisinin içinde bulunduğundan, çalışma kitabı gömülü görüntü referanslarını kırmadan e-postayla gönderilebilen veya arşivlenebilen tek bir kendi kendine yeten yapı olarak kalır. Her sparkline grubunu PNG olarak oluşturun, `ByteArrayOutputStream`'i `byte[]`'ye dönüştürün ve diziyi hedef hücrenin `setEmbeddedImage` özelliğine atayın — atama, resmin hücrenin saklanan içeriklerinin bir parçası olmasını sağlayan şeydir.

{{% alert color="primary" %}}
Her sparkline grubu tek bir hücreye sabitlendiğinden, `forEach` ile numaralandırmak yerine `group.sparklines[0]` dizin oluşturucusu aracılığıyla ona erişebilirsiniz. Bu, oluşturma kodunu kısa tutar ve tipik "sabitleme hücresi başına bir sparkline" kalıbıyla eşleşir. Resim baytlarını `Cell.EmbeddedImage` aracılığıyla saklamak Aspose.Cells 26.5 veya sonrasını gerektirir.

## **Workflow 2 — Export the Sparkline Worksheet to HTML**
Çalışma kitabı canlı sparkline'ları (ve isteğe bağlı olarak gömülü resim karşılıklarını) içerdiğinde, tüm çalışma sayfası HTML olarak kaydedilerek web'de yayınlanabilir. `HtmlSaveOptions` sınıfı bu dışa aktarmayı kontrol etmek için ihtiyaç duyduğunuz ayar düğmelerini sunar; bu iş akışında İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasını yeniden kullanacak ve onu temiz, tek sayfalık bir HTML belgesine dönüştüreceksiniz.

### **Step-by-Step Instructions**
1. İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasının çalışma dizininizde diskte mevcut olduğundan emin olun.
2. Bu dosyayı yeni bir `Workbook` örneğine yükleyin.
3. `HtmlSaveOptions`'ı örnekleyin ve `ExportActiveWorksheetOnly` özelliğini `true` olarak ayarlayın, böylece elde edilen HTML dosyası tüm çalışma kitabı yerine yalnızca etkin çalışma sayfasını içerir.
4. HTML çıktısını diske yazmak için `workbook.save("sparklines.html", htmlOptions)` çağrısını yapın.

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Yukarıdaki kod, İş Akışı 1'deki sparkline açısından zengin çalışma kitabını alır ve onu taşınabilir bir HTML dosyasına dönüştürür. Sparkline'lar, dışa aktarma moduna bağlı olarak üretilen HTML içinde satır içi SVG veya PNG oluşturmaları olarak korunur, böylece son kullanıcılar Excel yüklemeye gerek kalmadan eğilimleri herhangi bir modern tarayıcıda görüntüleyebilir. `ExportActiveWorksheetOnly`'i `true` olarak ayarlayarak, gizli sayfaları veya yardımcı verileri yanlışlıkla yayınlamaktan kaçınırsınız — yalnızca kullanıcının o anda gördüğü çalışma sayfası dışa aktarılır.
{{% /alert %}}

{{% alert color="primary" %}}
`HtmlSaveOptions` sınıfı, çıktıyı ince ayarlamak için `ExportHiddenWorksheet`, `ExportImagesAsBase64` ve `Encoding` gibi ek özellikler sunar. Bunları dağıtım hedefinize göre gerektiği şekilde ayarlayın.

## **API Summary**
Yukarıdaki iş akışları, birlikte çalışan küçük bir Aspose.Cells API setine dayanır.
- `SparklineGroup` ve koleksiyon erişimcisi `worksheet.sparklineGroups`, her sparkline grubu için türü (Çizgi, Sütun, Yığılmış), veri aralığını ve sabitleme hücresini bildirmek için kullanılır. Bu makalede her grup tek bir hücreye sabitlenmiştir, bu nedenle gruba `worksheet.sparklineGroups[i]` aracılığıyla erişilir.
- `Sparkline` ve dizin oluşturucu `group.sparklines[0]`, bir grup içindeki tek tek sparkline'ı döndürür. Örnekteki her grup tam olarak bir sparkline içerdiğinden, `forEach` döngüsü gerekmez.
- `Sparkline.toImage(OutputStream, ImageOrPrintOptions)`, sparkline'ın resmini sağlanan `OutputStream`'e yazan oluşturma yöntemidir. Yöntem `void` döndürür; çağrıdan sonra baytları akıştan okursunuz.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (bir `boolean`), HTML dışa aktarmasını etkin çalışma sayfasıyla sınırlar. Tek sayfalık raporlar oluştururken `HtmlSaveOptions` üzerinde en sık kullanılan özelliklerden biridir.
- `ImageOrPrintOptions.ImageType`, `com.aspose.cells.drawing` ad alanında bulunur ve `toImage` ile oluştururken ve çalışma sayfalarını görüntülere yazdırırken kullanılan resim biçimini (örneğin, `ImageType.Png`) seçer.

## **Related Articles**
- [Hücreye Görüntü Ekleme](/cells/tr/nodejs-java/inserting-an-image-into-a-cell/)
{{% /alert %}}

{{< app/cells/assistant language="javascript" >}}