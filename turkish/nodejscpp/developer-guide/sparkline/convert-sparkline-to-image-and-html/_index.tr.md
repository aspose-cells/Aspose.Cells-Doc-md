---
title: Aspose.Cells for Node.js via C++'ta Sparkline'ı Görüntüye ve HTML'e Dönüştürme
linktitle: Aspose.Cells for Node.js via C++'ta Sparkline'ı Görüntüye ve HTML'e Dönüştürme
description: Aspose.Cells sparkline'larını hücreye gömmek için bağımsız görüntüler olarak işlemeyi ve sparkline açısından zengin çalışma sayfalarını HtmlSaveOptions kullanarak HTML'e aktarmayı öğrenin.
keywords: Aspose.Cells, Node.js via C++, sparkline, Sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, sparkline işleme, sparkline'ı görüntüye dönüştürme, sparkline'ı HTML'e aktarma
type: docs
weight: 120
url: /tr/nodejs-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparkline'lar çalışma sayfası hücrelerinin içine yerleştirilen minyatür grafiklerdir. Aspose.Cells, her bir sparkline'ı bağımsız bir görüntü olarak çıkarmanıza (başka bir hücreye veya harici bir rapora gömmek için) ve ayrıca sparkline açısından zengin tüm çalışma sayfasını tarayıcı tabanlı dağıtım için HTML'e aktarmanıza olanak tanır. Bu makalede kullanılan `cell.embeddedImage` özelliği **Aspose.Cells 26.5 ve sonrasında** kullanılabilir.
{{% /alert %}}

## **Introduction**
Sparkline'lar, trendleri doğrudan bir çalışma sayfasının içinde görselleştirmenin kompakt bir yoludur. Excel kullanıcıları onları yerinde görse de, birçok gerçek dünya senaryosu sparkline'ın hücreden çıkmasını gerektirir — örneğin, statik bir resim olarak farklı bir hücreye gömülmek, otomatik bir e-postaya eklenmek veya web'de yayınlanan bir HTML raporunun parçası olarak işlenmek üzere.
Aspose.Cells bu işlemlerin her ikisini de destekler. `Sparkline.toImage` yöntemi, tek bir sparkline'ı bir akışa işler ve elde edilen baytlar `cell.embeddedImage`'a atanabilir, böylece resim çalışma kitabının tek bir hücresinin içinde saklanır. Ayrı olarak `HtmlSaveOptions`, tüm çalışma kitabını — sparkline'lar dahil — kendi kendine yeterli bir HTML dosyasına dönüştürmenize olanak tanır. Bu makale her iki iş akışını da uçtan uca ele almaktadır.

## **Workflow 1 — Render Sparklines to Images and Embed Them into Cells**
Bu iş akışında, küçük bir kaynak değer aralığı içeren bir çalışma sayfası oluşturacak, o aralığa üç farklı sparkline grubu (Çizgi, Sütun ve Yığılmış/Kazanma-Kaybetme) ekleyecek, her grubu PNG olarak işleyecek ve bu PNG baytlarını bitişik hücrelere gömülü görüntüler olarak yazacaksınız. Nihai sonuç, hem canlı sparkline'ları hem de işlenmiş resim karşılıklarını içeren tek bir `.xlsx` dosyasıdır.

### **Step-by-Step Instructions**
1. Bir çalışma dizini tanımlayın ve diskte var olduğundan emin olun.
2. Yeni bir `Workbook` oluşturun ve ilk `Worksheet`'e bir referans elde edin.
3. `A1` ile `E1` hücreleri arasını beş örnek sayısal değerle doldurun (örneğin, günlük satışlar veya sıcaklık ölçümleri).
4. `worksheet.sparklineGroups.add(...)` çağrısı yaparak çalışma sayfasına üç `SparklineGroup` nesnesi ekleyin:
   - `A1:E1` veri aralığıyla `F1`'de sabitlenmiş bir `SparklineType.Line` grubu.
   - `A1:E1` veri aralığıyla `G1`'de sabitlenmiş bir `SparklineType.Column` grubu.
   - `A1:E1` veri aralığıyla `H1`'de sabitlenmiş bir `SparklineType.Stacked` (kazanma/kaybetme) grubu.
5. Bir `ImageOrPrintOptions` örneği oluşturun ve `ImageType` özelliğini `ImageType.Png` olarak ayarlayın, böylece her sparkline şeffaf bir PNG olarak işlenir.
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

Yukarıdaki kod, bir sparkline'ın her görsel temsilinin iki biçimde çoğaltıldığı bir çalışma kitabı üretir: 1. satıra sabitlenmiş canlı, yerel sparkline ve 2. satırdaki bitişik bir hücreye doğrudan gömülmüş statik bir PNG resmi. Resimler dosyanın kendisinin içinde yaşadığı için çalışma kitabı, gömülü görüntü referanslarını kırmadan e-postayla gönderilebilen veya arşivlenebilen tek bir kendi kendine yeterli yapı olarak kalır. Her sparkline grubunu PNG olarak işleyin, akışı bir `Buffer`'a dönüştürün ve diziyi hedef hücrenin `embeddedImage` özelliğine atayın — atama işlemi, resmi hücrenin saklanan içeriklerinin bir parçası yapan şeydir.

{{% alert color="primary" %}}
Her sparkline grubu tek bir hücreye sabitlendiği için, `forEach` ile numaralandırmak yerine `group.sparklines[0]` indeksleyicisi aracılığıyla ona erişebilirsiniz. Bu, işleme kodunu kısa tutar ve tipik "sabitlenen hücre başına bir sparkline" deseniyle eşleşir. Resim baytlarını `cell.embeddedImage` aracılığıyla saklamak Aspose.Cells 26.5 veya sonrasını gerektirir.

## **Workflow 2 — Export the Sparkline Worksheet to HTML**
Çalışma kitabı canlı sparkline'ları (ve isteğe bağlı olarak gömülü resim karşılıklarını) içerdiğinde, tüm çalışma sayfası HTML olarak kaydedilerek web'de yayınlanabilir. `HtmlSaveOptions` sınıfı, bu dışa aktarımı kontrol etmek için ihtiyacınız olan düğmeleri sunar; bu iş akışında İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasını yeniden kullanacak ve onu temiz, tek sayfalık bir HTML belgesine dönüştüreceksiniz.

### **Step-by-Step Instructions**
1. İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasının çalışma dizininizde diskte mevcut olduğundan emin olun.
2. Bu dosyayı yeni bir `Workbook` örneğine yükleyin.
3. `HtmlSaveOptions`'ı örnekleyin ve `exportActiveWorksheetOnly` özelliğini `true` olarak ayarlayın, böylece ortaya çıkan HTML dosyası tüm çalışma kitabı yerine yalnızca aktif çalışma sayfasını içerir.
4. HTML çıktısını diske yazmak için `workbook.save("sparklines.html", htmlOptions)` çağrısı yapın.

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Yukarıdaki kod, İş Akışı 1'deki sparkline açısından zengin çalışma kitabını alır ve onu taşınabilir bir HTML dosyasına dönüştürür. Sparkline'lar, dışa aktarma moduna bağlı olarak oluşturulan HTML içinde satır içi SVG veya PNG işlemeleri olarak korunur, böylece son kullanıcılar Excel yüklemeye gerek kalmadan trendleri herhangi bir modern tarayıcıda görüntüleyebilir. `exportActiveWorksheetOnly` öğesini `true` olarak ayarlayarak, yanlışlıkla gizli sayfaları veya yardımcı verileri yayınlamaktan kaçınırsınız — yalnızca kullanıcı tarafından o anda görülebilen çalışma sayfası dışa aktarılır.
{{% /alert %}}

{{% alert color="primary" %}}
`HtmlSaveOptions` sınıfı, çıktıyı ince ayarlamak için `exportHiddenWorksheet`, `exportImagesAsBase64` ve `encoding` gibi ek özellikler sunar. Bunları dağıtım hedefinize göre ayarlayın.

## **API Summary**
Yukarıdaki iş akışları, birlikte çalışan küçük bir Aspose.Cells API kümesine dayanır.
- `SparklineGroup` ve koleksiyon erişimcisi `worksheet.sparklineGroups`, her sparkline grubu için türü (Çizgi, Sütun, Yığılmış), veri aralığını ve sabitleme hücresini bildirmek için kullanılır. Bu makalede her grup tek bir hücreye sabitlendiğinden, gruba `worksheet.sparklineGroups[i]` aracılığıyla ulaşılır.
- `Sparkline` ve indeksleyici `group.sparklines[0]`, bir grubun içindeki tek tek sparkline'ı döndürür. Örnekteki her grup tam olarak bir sparkline içerdiğinden, `forEach` döngüsü gerekmez.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)`, sparkline'ın bir resmini sağlanan bir `Stream`'e yazan işleme yöntemidir. Yöntem `void` döndürür; çağrıdan sonra baytları akıştan okursunuz.
- `htmlSaveOptions.exportActiveWorksheetOnly` (bir `bool`), HTML dışa aktarımını aktif çalışma sayfasıyla sınırlar. Tek sayfalık raporlar oluştururken `HtmlSaveOptions` üzerinde en sık kullanılan özelliklerden biridir.
- `imageOrPrintOptions.imageType`, `Aspose.Cells.Drawing` ad alanında bulunur ve `toImage` ile işlerken ve çalışma sayfalarını görüntülere yazdırırken kullanılan resim biçimini (örneğin, `ImageType.Png`) seçer.

## **Related Articles**
- [Hücreye Resim Ekleme](/cells/tr/nodejs-cpp/inserting-an-image-into-a-cell/)
{{% /alert %}}

{{< app/cells/assistant language="javascript" >}}