---
title: Aspose.Cells for Node.js via Java ile Sparkline'ı Görüntüye ve HTML'e Dönüştürme
linktitle: Convert Sparkline to Image and HTML
description: Aspose.Cells sparkline'larını hücreye gömme için bağımsız görüntüler olarak işlemeyi ve sparkline içeren çalışma sayfalarını HtmlSaveOptions kullanarak HTML'e aktarmayı öğrenin.
keywords: Aspose.Cells, Node.js via Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, sparkline işleme, sparkline'ı görüntüye dönüştürme, sparkline'ı HTML'e aktarma
type: docs
weight: 120
url: /tr/nodejs-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparkline'lar çalışma sayfası hücrelerinin içine yerleştirilen küçük grafiklerdir. Aspose.Cells her bir sparkline'ı bağımsız bir görüntü olarak çıkarmanıza (başka bir hücreye veya harici bir rapora gömmek için) ve ayrıca sparkline açısından zengin çalışma sayfasının tamamını tarayıcı tabanlı dağıtım için HTML olarak dışa aktarmanıza olanak tanır. Bu makalede kullanılan `Cell.EmbeddedImage` özelliği **Aspose.Cells 26.5 ve sonrasında** kullanılabilir.
{{% /alert %}}

## **Giriş**

Sparkline'lar, eğilimleri doğrudan bir çalışma sayfasının içinde görselleştirmenin kompakt bir yoludur. Excel kullanıcıları bunları yerinde görse de, birçok gerçek dünya senaryosunda bir sparkline'ın hücreden çıkması gerekir — örneğin, farklı bir hücreye statik resim olarak gömülmek, otomatik bir e-postaya eklenmek veya web'de yayınlanan bir HTML raporunun parçası olarak işlenmek için.

Aspose.Cells bu iki işlemi de destekler. `Sparkline.toImage` yöntemi, tek bir sparkline'ı bir akışa işler ve elde edilen baytlar `Cell.EmbeddedImage`'a atanabilir, böylece resim çalışma kitabının tek bir hücresinde saklanır. Ayrı olarak, `HtmlSaveOptions` tüm çalışma kitabını — sparkline'lar dahil — kendi kendine yeten bir HTML dosyasına dönüştürmenize olanak tanır. Bu makale her iki iş akışını uçtan uca ele almaktadır.

## **İş Akışı 1 — Sparkline'ları Görüntülere İşleme ve Hücrelere Gömme**

Bu iş akışında, küçük bir kaynak değer aralığı içeren bir çalışma sayfası oluşturacak, o aralığa üç farklı sparkline grubu (Çizgi, Sütun ve Yığılmış/Kazanma-Kaybetme) ekleyecek, her grubu PNG olarak işleyecek ve bu PNG baytlarını bitişik hücrelere gömülü görüntüler olarak yazacaksınız. Nihai sonuç, hem canlı sparkline'ları hem de bunların işlenmiş resim karşılıklarını içeren tek bir `.xlsx` dosyasıdır.

### **Adım Adım Talimatlar**

1. Bir çalışma dizini tanımlayın ve diskte mevcut olduğundan emin olun.
2. Yeni bir `Workbook` oluşturun ve ilk `Worksheet`'e bir referans elde edin.
3. `A1` ile `E1` arasındaki hücreleri beş örnek sayısal değerle (örneğin, günlük satışlar veya sıcaklık okumaları) doldurun.
4. `worksheet.sparklineGroups.add(...)` çağrısı yaparak çalışma sayfasına üç `SparklineGroup` nesnesi ekleyin:
   - Veri aralığı `A1:E1` olan, `F1`'de sabitlenmiş bir `SparklineType.Line` grubu.
   - Veri aralığı `A1:E1` olan, `G1`'de sabitlenmiş bir `SparklineType.Column` grubu.
   - Veri aralığı `A1:E1` olan, `H1`'de sabitlenmiş bir `SparklineType.Stacked` (kazanma/kaybetme) grubu.
5. Bir `ImageOrPrintOptions` örneği oluşturun ve her sparkline'ın şeffaf bir PNG olarak işlenmesi için `ImageType` özelliğini `ImageType.Png` olarak ayarlayın.
6. Üç grubun her biri için, `group.sparklines[0].toImage(outputStream, imageOptions)` kullanarak tek bir sparkline'ı işleyin, `ByteArrayOutputStream`'i bir `byte[]`'e dönüştürün ve diziyi sırasıyla `worksheet.cells.get("F2").setEmbeddedImage(...)`, `worksheet.cells.get("G2").setEmbeddedImage(...)` ve `worksheet.cells.get("H2").setEmbeddedImage(...)` öğelerine atayın.
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

// F1'de (sütun 5, satır 0) sabitlenmiş bir Çizgi mini grafik grubu ekle
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// G1'de (sütun 6, satır 0) sabitlenmiş bir Sütun mini grafik grubu ekle
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// H1'de (sütun 7, satır 0) sabitlenmiş bir Kazanma/Kaybetme (Yığılmış) mini grafik grubu ekle
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// PNG çıktısı için görüntü seçeneklerini yapılandır
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// Çizgi mini grafiğini görüntüye dönüştür ve F2 hücresine göm
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let lineMs = new java.io.ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// Sütun mini grafiğini görüntüye dönüştür ve G2 hücresine göm
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnMs = new java.io.ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// Kazanma/Kaybetme mini grafiğini görüntüye dönüştür ve H2 hücresine göm
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedMs = new java.io.ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// Çalışma kitabını diske kaydet
workbook.save("output_with_sparklines.xlsx");
```

Yukarıdaki kod, bir sparkline'ın her görsel temsilinin iki biçimde çoğaltıldığı bir çalışma kitabı üretir: 1. satıra sabitlenmiş canlı, yerel sparkline ve 2. satırdaki bitişik bir hücreye doğrudan gömülmüş statik bir PNG resmi. Resimler dosyanın kendisinde bulunduğundan, çalışma kitabı gömülü resim referanslarını bozmadan e-posta ile gönderilebilen veya arşivlenebilen tek bir kendi kendine yeten yapı olarak kalır. Her bir sparkline grubunu PNG olarak işleyin, `ByteArrayOutputStream`'i bir `byte[]`'e dönüştürün ve diziyi hedef hücrenin `setEmbeddedImage` özelliğine atayın — atama işlemi, resmi hücrenin saklanan içeriğinin bir parçası yapan şeydir.

{{% alert color="primary" %}}
Her sparkline grubu tek bir hücreye sabitlendiğinden, `forEach` ile numaralandırmak yerine `group.sparklines[0]` indeksleyicisi aracılığıyla erişebilirsiniz. Bu, işleme kodunu kısa tutar ve tipik "sabitleme hücresi başına bir sparkline" deseniyle eşleşir. Resim baytlarını `Cell.EmbeddedImage` aracılığıyla saklamak için Aspose.Cells 26.5 veya sonrası gereklidir.
{{% /alert %}}

## **İş Akışı 2 — Sparkline Çalışma Sayfasını HTML'e Aktarma**

Çalışma kitabı canlı sparkline'ları (ve isteğe bağlı olarak gömülü resim karşılıklarını) içerdiğinde, çalışma sayfasının tamamı HTML olarak kaydedilerek web'de yayınlanabilir. `HtmlSaveOptions` sınıfı, bu dışa aktarmayı kontrol etmek için ihtiyaç duyduğunuz ayar düğmelerini sunar; bu iş akışında İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasını yeniden kullanacak ve onu temiz, tek sayfalık bir HTML belgesine dönüştüreceksiniz.

### **Adım Adım Talimatlar**

1. İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasının çalışma dizininizde diskte mevcut olduğundan emin olun.
2. Bu dosyayı yeni bir `Workbook` örneğine yükleyin.
3. `HtmlSaveOptions`'ı örnekleyin ve ortaya çıkan HTML dosyasının yalnızca etkin çalışma sayfasını (tüm çalışma kitabı yerine) içermesi için `ExportActiveWorksheetOnly` özelliğini `true` olarak ayarlayın.
4. HTML çıktısını diske yazmak için `workbook.save("sparklines.html", htmlOptions)` çağırın.

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Yukarıdaki kod, İş Akışı 1'den alınan sparkline açısından zengin çalışma kitabını taşınabilir bir HTML dosyasına dönüştürür. Sparkline'lar, dışa aktarma moduna bağlı olarak, oluşturulan HTML içinde satır içi SVG veya PNG işlemeleri olarak korunur, böylece son kullanıcılar Excel yüklemeye gerek kalmadan eğilimleri herhangi bir modern tarayıcıda görüntüleyebilir. `ExportActiveWorksheetOnly`'i `true` olarak ayarlayarak, gizli sayfaları veya yardımcı verileri yanlışlıkla yayınlamaktan kaçınırsınız — yalnızca kullanıcı tarafından o anda görülebilen çalışma sayfası dışa aktarılır.

{{% alert color="primary" %}}
`HtmlSaveOptions` sınıfı, `ExportHiddenWorksheet`, `ExportImagesAsBase64` ve `Encoding` gibi çıktıda ince ayar yapmak için ek özellikler sunar. Bunları dağıtım hedefinize göre gerektiği gibi ayarlayın.
{{% /alert %}}

## **API Özeti**

Yukarıdaki iş akışları, birlikte çalışan küçük bir Aspose.Cells API kümesine dayanır.

- `SparklineGroup` ve koleksiyon erişimcisi `worksheet.sparklineGroups`, her sparkline grubu için türü (Çizgi, Sütun, Yığılmış), veri aralığını ve sabitleme hücresini bildirmek için kullanılır. Bu makalede her grup tek bir hücreye sabitlendiğinden, gruba `worksheet.sparklineGroups[i]` aracılığıyla erişilir.
- `Sparkline` ve indeksleyici `group.sparklines[0]`, grup içindeki tek tek sparkline'ı döndürür. Örnekteki her grup tam olarak bir sparkline içerdiğinden, `forEach` döngüsü gerekmez.
- `Sparkline.toImage(OutputStream, ImageOrPrintOptions)`, sparkline'ın bir resmini sağlanan `OutputStream`'e yazan işleme yöntemidir. Yöntem `void` döndürür; çağrıdan sonra baytları akıştan okursunuz.
- `Cell.EmbeddedImage`, tek bir hücrenin içine bir resim saklayan bir `byte[]` özelliğidir. **Aspose.Cells 26.5 ve sonrasında** kullanılabilir ve `toImage` tarafından işlenen bir sparkline'ı aynı çalışma kitabına geri yerleştirmenin önerilen yoludur.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (bir `boolean`), HTML dışa aktarımını etkin çalışma sayfasıyla sınırlar. Tek sayfalık raporlar oluştururken `HtmlSaveOptions`'ın en sık kullanılan özelliklerinden biridir.
- `ImageOrPrintOptions.ImageType`, `com.aspose.cells.drawing` ad alanında bulunur ve `toImage` ile işlenirken ve çalışma sayfaları görüntülere yazdırılırken kullanılan resim biçimini (örneğin, `ImageType.Png`) seçer.

## **İlgili Makaleler**

- [Aspose.Cells for Aspose.Cells for Node.js via Java'da Sparkline'lar](/cells/tr/nodejs-java/sparkline/)
- [Bir Hücreye Resim Ekleme](/cells/tr/nodejs-java/inserting-an-image-into-a-cell/)
- [SmartMarker Tek Hücre Dizi İşleme | Aspose.Cells for Aspose.Cells for Node.js via Java](/cells/tr/nodejs-java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}