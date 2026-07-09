---
title: Aspose.Cells for Node.js via C++'da Mini Grafiği Görüntüye ve HTML'e Dönüştürme
linktitle: Convert Sparkline to Image and HTML
description: Aspose.Cells mini grafiklerini hücreye gömme için bağımsız görüntüler olarak işlemeyi ve HtmlSaveOptions kullanarak mini grafik açısından zengin çalışma sayfalarını HTML'ye aktarmayı öğrenin.
keywords: Aspose.Cells, Node.js via C++, mini grafik, Sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, mini grafik işleme, mini grafiği görüntüye dönüştürme, mini grafiği HTML'ye aktarma
type: docs
weight: 120
url: /tr/nodejs-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Mini grafikler (sparkline), çalışma sayfası hücrelerinin içine yerleştirilen küçük boyutlu grafiklerdir. Aspose.Cells, her bir mini grafiği bağımsız bir görüntü olarak çıkarmanıza (başka bir hücreye veya harici bir rapora gömmek için) ve ayrıca tüm mini grafik açısından zengin çalışma sayfasını tarayıcı tabanlı dağıtım için HTML olarak dışa aktarmanıza olanak tanır. Bu makalede kullanılan `cell.embeddedImage` özelliği **Aspose.Cells 26.5 ve sonrasında** kullanılabilir.
{{% /alert %}}

## **Giriş**

Mini grafikler, trendleri doğrudan bir çalışma sayfasının içinde görselleştirmenin kompakt bir yoludur. Excel kullanıcıları onları yerinde görse de, birçok gerçek dünya senaryosunda mini grafiğin hücreden çıkması gerekir — örneğin, statik bir resim olarak farklı bir hücreye gömülmesi, otomatik bir e-postaya eklenmesi veya web'de yayınlanan bir HTML raporunun parçası olarak işlenmesi gibi.

Aspose.Cells bu iki işlemi de destekler. `Sparkline.toImage` yöntemi, tek bir mini grafiği bir akışa işler ve elde edilen baytlar `cell.embeddedImage`'a atanabilir, böylece resim çalışma kitabının tek bir hücresinde saklanır. Ayrıca, `HtmlSaveOptions` tüm çalışma kitabını — mini grafikler dahil — kendi kendine yeterli bir HTML dosyasına dönüştürmenize olanak tanır. Bu makale her iki iş akışını da uçtan uca ele almaktadır.

## **İş Akışı 1 — Mini Grafikleri Görüntülere İşleme ve Hücrelere Gömme**

Bu iş akışında, küçük bir kaynak değer aralığı içeren bir çalışma sayfası oluşturacak, o aralığa üç farklı mini grafik grubu (Çizgi, Sütun ve Yığılmış/Kazanma-Kaybetme) ekleyecek, her grubu bir PNG olarak işleyecek ve bu PNG baytlarını bitişik hücrelere gömülü görüntüler olarak yazacaksınız. Nihai sonuç, hem canlı mini grafikleri hem de işlenmiş resim karşılıklarını içeren tek bir `.xlsx` dosyasıdır.

### **Adım Adım Talimatlar**

1. Bir çalışma dizini tanımlayın ve diskinizde mevcut olduğundan emin olun.
2. Yeni bir `Workbook` oluşturun ve ilk `Worksheet`'e bir başvuru elde edin.
3. `A1`'den `E1`'e kadar olan hücreleri beş adet örnek sayısal değerle doldurun (örneğin, günlük satışlar veya sıcaklık okumaları).
4. `worksheet.sparklineGroups.add(...)` çağrısı yaparak çalışma sayfasına üç `SparklineGroup` nesnesi ekleyin:
   - `A1:E1` veri aralığıyla `F1`'e sabitlenmiş bir `SparklineType.Line` grubu.
   - `A1:E1` veri aralığıyla `G1`'e sabitlenmiş bir `SparklineType.Column` grubu.
   - `A1:E1` veri aralığıyla `H1`'e sabitlenmiş bir `SparklineType.Stacked` (kazanma/kaybetme) grubu.
5. Bir `ImageOrPrintOptions` örneği oluşturun ve `ImageType` özelliğini `ImageType.Png` olarak ayarlayın, böylece her mini grafik şeffaf bir PNG olarak işlenir.
6. Üç grubun her biri için, `group.sparklines[0].toImage(memoryStream, imageOrPrintOptions)` kullanarak tek mini grafiği işleyin, akışı bir `Buffer`'a (veya `Uint8Array`'e) dönüştürün ve baytları sırasıyla `worksheet.cells["F2"].embeddedImage`, `worksheet.cells["G2"].embeddedImage` ve `worksheet.cells["H2"].embeddedImage` özelliklerine atayın.
7. Çalışma kitabını `output_with_sparklines.xlsx` olarak kaydedin.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// A1:E1 hücrelerine örnek verileri doldur
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// F1'e (sütun 5, satır 0) sabitlenmiş bir Çizgi sparkline grubu ekle
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// G1'e (sütun 6, satır 0) sabitlenmiş bir Sütun sparkline grubu ekle
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// H1'e (sütun 7, satır 0) sabitlenmiş bir Kazanma/Kaybetme (Yığılmış) sparkline grubu ekle
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
let linePath = "line_sparkline.png";
lineSp.toImage(linePath, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(fs.readFileSync(linePath));

// Sütun sparkline'ı görüntüye dönüştür ve G2 hücresine göm
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnPath = "column_sparkline.png";
columnSp.toImage(columnPath, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(fs.readFileSync(columnPath));

// Kazanma/Kaybetme sparkline'ı görüntüye dönüştür ve H2 hücresine göm
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedPath = "stacked_sparkline.png";
stackedSp.toImage(stackedPath, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(fs.readFileSync(stackedPath));

// Çalışma kitabını diske kaydet
workbook.save("output_with_sparklines.xlsx");
```

Yukarıdaki kod, bir mini grafiğin her görsel temsilinin iki biçimde çoğaltıldığı bir çalışma kitabı üretir: 1. satıra sabitlenmiş canlı, yerel mini grafik ve 2. satırdaki bitişik bir hücreye doğrudan gömülmüş statik bir PNG resmi. Resimler dosyanın kendi içinde yaşadığı için, çalışma kitabı gömülü görüntü referanslarını bozmadan e-posta ile gönderilebilen veya arşivlenebilen tek bir kendi kendine yeterli yapı olarak kalır. Her mini grafik grubunu bir PNG olarak işleyin, akışı bir `Buffer`'a dönüştürün ve diziyi hedef hücrenin `embeddedImage` özelliğine atayın — atama işlemi, resmi hücrenin saklanan içeriklerinin bir parçası yapan şeydir.

{{% alert color="primary" %}}
Her mini grafik grubu tek bir hücreye sabitlendiğinden, onu `forEach` ile numaralandırmak yerine `group.sparklines[0]` dizin oluşturucusu aracılığıyla adresleyebilirsiniz. Bu, işleme kodunu kısa tutar ve tipik "sabitlenmiş hücre başına bir mini grafik" deseniyle eşleşir. Resim baytlarını `cell.embeddedImage` aracılığıyla saklamak için Aspose.Cells 26.5 veya sonrası gereklidir.
{{% /alert %}}

## **İş Akışı 2 — Mini Grafik Çalışma Sayfasını HTML'ye Aktarma**

Çalışma kitabı canlı mini grafikleri (ve isteğe bağlı olarak gömülü resim karşılıklarını) içerdiğinde, tüm çalışma sayfası HTML olarak kaydedilerek web'de yayınlanabilir. `HtmlSaveOptions` sınıfı, bu dışa aktarımı kontrol etmek için ihtiyaç duyduğunuz düğmeleri sunar; bu iş akışında İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasını yeniden kullanacak ve onu temiz, tek sayfalık bir HTML belgesine dönüştüreceksiniz.

### **Adım Adım Talimatlar**

1. İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasının çalışma dizininizde mevcut olduğundan emin olun.
2. Bu dosyayı yeni bir `Workbook` örneğine yükleyin.
3. `HtmlSaveOptions`'ı örnekleyin ve `exportActiveWorksheetOnly` özelliğini `true` olarak ayarlayın, böylece ortaya çıkan HTML dosyası tüm çalışma kitabı yerine yalnızca etkin çalışma sayfasını içerir.
4. HTML çıktısını diske yazmak için `workbook.save("sparklines.html", htmlOptions)` çağrısı yapın.

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Yukarıdaki kod, İş Akışı 1'deki mini grafik açısından zengin çalışma kitabını alır ve onu taşınabilir bir HTML dosyasına dönüştürür. Mini grafikler, dışa aktarma moduna bağlı olarak, oluşturulan HTML içinde satır içi SVG veya PNG işlemeleri olarak korunur, böylece son kullanıcılar Excel yüklemeye gerek kalmadan trendleri herhangi bir modern tarayıcıda görüntüleyebilir. `exportActiveWorksheetOnly` özelliğini `true` olarak ayarlayarak, gizli sayfaları veya yardımcı verileri yanlışlıkla yayınlamaktan kaçınırsınız — yalnızca kullanıcı tarafından o anda görülebilen çalışma sayfası dışa aktarılır.

{{% alert color="primary" %}}
`HtmlSaveOptions` sınıfı, çıktıyı ince ayar yapmak için `exportHiddenWorksheet`, `exportImagesAsBase64` ve `encoding` gibi ek özellikler sunar. Bunları dağıtım hedefinize göre gerektiği gibi ayarlayın.
{{% /alert %}}

## **API Özeti**

Yukarıdaki iş akışları, birlikte çalışan küçük bir Aspose.Cells API setine dayanır.

- `SparklineGroup` ve koleksiyon erişimcisi `worksheet.sparklineGroups`, her mini grafik grubu için türü (Çizgi, Sütun, Yığılmış), veri aralığını ve sabitleme hücresini bildirmek için kullanılır. Bu makalede her grup tek bir hücreye sabitlendiğinden, gruba `worksheet.sparklineGroups[i]` aracılığıyla ulaşılır.
- `Sparkline` ve `group.sparklines[0]` dizin oluşturucusu, bir grup içindeki tek tek mini grafiği döndürür. Örnekteki her grup tam olarak bir mini grafik içerdiğinden, `forEach` döngüsü gerekli değildir.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)`, mini grafiğin resmini sağlanan `Stream`'e yazan işleme yöntemidir. Yöntem `void` döndürür; çağrıdan sonra baytları akıştan okursunuz.
- `cell.embeddedImage`, tek bir hücrenin içine bir resim saklayan bir `Buffer` (veya `Uint8Array`) özelliğidir. **Aspose.Cells 26.5 ve sonrasında** kullanılabilir ve `toImage` tarafından işlenen bir mini grafiği aynı çalışma kitabına geri yerleştirmenin önerilen yoludur.
- `htmlSaveOptions.exportActiveWorksheetOnly` (bir `bool`), HTML dışa aktarımını etkin çalışma sayfasıyla sınırlar. Tek sayfalık raporlar oluştururken `HtmlSaveOptions` üzerinde en sık kullanılan özelliklerden biridir.
- `imageOrPrintOptions.imageType`, `Aspose.Cells.Drawing` ad alanında yaşar ve `toImage` ile işleme ve çalışma sayfalarını görüntülere yazdırma sırasında kullanılan resim biçimini (örneğin, `ImageType.Png`) seçer.

## **İlgili Makaleler**

- [Aspose.Cells for Node.js via C++'da Aspose.Cells için Mini Grafikler](/cells/tr/nodejs-cpp/sparkline/)
- [Bir Hücreye Resim Ekleme](/cells/tr/nodejs-cpp/inserting-an-image-into-a-cell/)
- [SmartMarker Tek Hücre Dizi İşleme | Aspose.Cells Node.js via C++](/cells/tr/nodejs-cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}