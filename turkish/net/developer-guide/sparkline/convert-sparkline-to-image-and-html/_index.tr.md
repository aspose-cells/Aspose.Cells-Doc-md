---
title: Aspose.Cells for .NET'te Mini Grafikleri Görüntüye ve HTML'ye Dönüştürme
linktitle: Convert Sparkline to Image and HTML
description: Aspose.Cells mini grafiklerini hücreye gömme için bağımsız görüntülere nasıl işleyeceğinizi ve HtmlSaveOptions kullanarak mini grafik açısından zengin çalışma sayfalarını HTML'ye nasıl dışa aktaracağınızı öğrenin.
keywords: Aspose.Cells, .NET, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, mini grafik işleme, mini grafiği görüntüye dönüştürme, mini grafiği HTML'ye dışa aktarma
type: docs
weight: 120
url: /tr/net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Mini grafikler, çalışma sayfası hücrelerinin içine yerleştirilen küçük grafiklerdir. Aspose.Cells, her bir mini grafiği bağımsız bir görüntü olarak (başka bir hücreye veya harici bir rapora gömmek için) çıkarmanıza ve ayrıca tüm mini grafik açısından zengin çalışma sayfasını tarayıcı tabanlı dağıtım için HTML olarak dışa aktarmanıza olanak tanır. Bu makalede kullanılan `Cell.EmbeddedImage` özelliği **Aspose.Cells 26.5 ve sonrasında** kullanılabilir.
{{% /alert %}}

## **Giriş**

Mini grafikler, trendleri doğrudan bir çalışma sayfasının içinde görselleştirmenin kompakt bir yoludur. Excel kullanıcıları onları yerinde görse de, birçok gerçek dünya senaryosunda bir mini grafiğin hücreden çıkması gerekir — örneğin, farklı bir hücreye statik bir resim olarak gömülmesi, otomatik bir e-postaya eklenmesi veya web'de yayınlanan bir HTML raporunun parçası olarak işlenmesi gibi.

Aspose.Cells bu işlemlerin her ikisini de destekler. `Sparkline.ToImage` yöntemi tek bir mini grafiği bir akışa işler ve elde edilen baytlar `Cell.EmbeddedImage` özelliğine atanabilir; böylece resim çalışma kitabının tek bir hücresinin içinde saklanır. Ayrı olarak, `HtmlSaveOptions` tüm çalışma kitabını — mini grafikler dahil — kendi kendine yeten bir HTML dosyasına dönüştürmenize olanak tanır. Bu makale her iki iş akışını da uçtan uca ele alır.

## **İş Akışı 1 — Mini Grafikleri Görüntülere İşleme ve Hücrelere Gömme**

Bu iş akışında, küçük bir kaynak değer aralığı içeren bir çalışma sayfası oluşturacak, bu aralığa üç farklı mini grafik grubu (Çizgi, Sütun ve Yığılmış/Kazanma-Kaybetme) ekleyecek, her grubu PNG olarak işleyecek ve bu PNG baytlarını bitişik hücrelere gömülü görüntüler olarak yazacaksınız. Nihai sonuç, hem canlı mini grafikleri hem de işlenmiş resim karşılıklarını içeren tek bir `.xlsx` dosyasıdır.

### **Adım Adım Talimatlar**

1. Bir çalışma dizini tanımlayın ve diskte mevcut olduğundan emin olun.
2. Yeni bir `Workbook` oluşturun ve ilk `Worksheet`'e bir başvuru edinin.
3. `A1` ile `E1` hücreleri arasına beş örnek sayısal değer doldurun (örneğin, günlük satışlar veya sıcaklık okumaları).
4. `worksheet.SparklineGroups.Add(...)` çağırarak çalışma sayfasına üç `SparklineGroup` nesnesi ekleyin:
   - `A1:E1` veri aralığıyla `F1` hücresine sabitlenmiş bir `SparklineType.Line` grubu.
   - `A1:E1` veri aralığıyla `G1` hücresine sabitlenmiş bir `SparklineType.Column` grubu.
   - `A1:E1` veri aralığıyla `H1` hücresine sabitlenmiş bir `SparklineType.Stacked` (kazanma/kaybetme) grubu.
5. Bir `ImageOrPrintOptions` örneği oluşturun ve her mini grafiğin şeffaf bir PNG olarak işlenmesi için `ImageType` özelliğini `ImageType.Png` olarak ayarlayın.
6. Üç grubun her biri için, `group.Sparklines[0].ToImage(memoryStream, imageOptions)` kullanarak tek mini grafiğini işleyin, `MemoryStream`'i `byte[]`'e dönüştürün ve diziyi sırasıyla `worksheet.Cells["F2"].EmbeddedImage`, `worksheet.Cells["G2"].EmbeddedImage` ve `worksheet.Cells["H2"].EmbeddedImage` özelliklerine atayın.
7. Çalışma kitabını `output_with_sparklines.xlsx` olarak kaydedin.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
using Aspose.Cells.Rendering;

// Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// A1:E1 hücrelerine örnek veri doldur
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// F1'de (sütun 5, satır 0) sabitlenmiş bir Çizgi mini grafik grubu ekle
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);

// G1'de (sütun 6, satır 0) sabitlenmiş bir Sütun mini grafik grubu ekle
CellArea columnArea = new CellArea();
columnArea.StartColumn = 6;
columnArea.EndColumn = 6;
columnArea.StartRow = 0;
columnArea.EndRow = 0;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);

// H1'de (sütun 7, satır 0) sabitlenmiş bir Kazanma/Kaybetme (Yığılmış) mini grafik grubu ekle
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 7;
stackedArea.EndColumn = 7;
stackedArea.StartRow = 0;
stackedArea.EndRow = 0;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);

// PNG çıktısı için görüntü seçeneklerini yapılandır
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.ImageType = ImageType.Png;

// Çizgi mini grafiğini görüntüye dönüştür ve F2 hücresine göm
Sparkline lineSp = worksheet.SparklineGroups[lineIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    lineSp.ToImage(ms, imageOptions);
    worksheet.Cells["F2"].EmbeddedImage = ms.ToArray();
}

// Sütun mini grafiğini görüntüye dönüştür ve G2 hücresine göm
Sparkline columnSp = worksheet.SparklineGroups[columnIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    columnSp.ToImage(ms, imageOptions);
    worksheet.Cells["G2"].EmbeddedImage = ms.ToArray();
}

// Kazanma/Kaybetme mini grafiğini görüntüye dönüştür ve H2 hücresine göm
Sparkline stackedSp = worksheet.SparklineGroups[stackedIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    stackedSp.ToImage(ms, imageOptions);
    worksheet.Cells["H2"].EmbeddedImage = ms.ToArray();
}

// Çalışma kitabını diske kaydet
workbook.Save("output_with_sparklines.xlsx");
```

Yukarıdaki kod, her bir mini grafiğin görsel temsilinin iki biçimde çoğaltıldığı bir çalışma kitabı üretir: 1. satıra sabitlenmiş canlı, yerel mini grafik ve 2. satırdaki bitişik bir hücreye doğrudan gömülmüş statik bir PNG resmi. Resimler dosyanın kendisinin içinde yaşadığından, çalışma kitabı gömülü görüntü başvurularını bozmadan e-postayla gönderilebilen veya arşivlenebilen tek bir kendi kendine yeten yapı olarak kalır. Her mini grafik grubunu PNG olarak işleyin, `MemoryStream`'i `byte[]`'e dönüştürün ve diziyi hedef hücrenin `EmbeddedImage` özelliğine atayın — atama işlemi, resmi hücrenin saklanan içeriğinin bir parçası yapan şeydir.

{{% alert color="primary" %}}
Her mini grafik grubu tek bir hücreye sabitlendiğinden, `foreach` ile numaralandırmak yerine `group.Sparklines[0]` dizinleyicisi aracılığıyla ona erişebilirsiniz. Bu, işleme kodunu kısa tutar ve tipik "çapa hücresi başına bir mini grafik" kalıbıyla eşleşir. Resim baytlarını `Cell.EmbeddedImage` aracılığıyla saklamak Aspose.Cells 26.5 veya sonrasını gerektirir.
{{% /alert %}}

## **İş Akışı 2 — Mini Grafik Çalışma Sayfasını HTML'ye Dışa Aktarma**

Çalışma kitabı canlı mini grafikleri (ve isteğe bağlı olarak gömülü resim karşılıklarını) içerdiğinde, tüm çalışma sayfası HTML olarak kaydedilerek web'de yayınlanabilir. `HtmlSaveOptions` sınıfı, bu dışa aktarımı kontrol etmek için ihtiyaç duyduğunuz ayar seçeneklerini sunar; bu iş akışında İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasını yeniden kullanacak ve onu temiz, tek sayfalık bir HTML belgesine dönüştüreceksiniz.

### **Adım Adım Talimatlar**

1. İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasının çalışma dizininizde diskte mevcut olduğundan emin olun.
2. Bu dosyayı yeni bir `Workbook` örneğine yükleyin.
3. `HtmlSaveOptions` örneğini oluşturun ve ortaya çıkan HTML dosyasının yalnızca aktif çalışma sayfasını içermesi için `ExportActiveWorksheetOnly` özelliğini `true` olarak ayarlayın; tüm çalışma kitabını değil.
4. HTML çıktısını diske yazmak için `workbook.Save("sparklines.html", htmlOptions)` çağırın.

```csharp
using System;
using System.IO;
using Aspose.Cells;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.ExportActiveWorksheetOnly = true;
workbook.Save("sparklines.html", htmlOptions);
```

Yukarıdaki kod, İş Akışı 1'den gelen mini grafik açısından zengin çalışma kitabını taşınabilir bir HTML dosyasına dönüştürür. Mini grafikler, dışa aktarma moduna bağlı olarak oluşturulan HTML içinde satır içi SVG veya PNG işlemeleri olarak korunur; böylece son kullanıcılar Excel yüklemeye gerek kalmadan trendleri herhangi bir modern tarayıcıda görüntüleyebilir. `ExportActiveWorksheetOnly`'i `true` olarak ayarlayarak, gizli sayfaları veya yardımcı verileri yanlışlıkla yayınlamaktan kaçınırsınız — yalnızca kullanıcının o anda görebildiği çalışma sayfası dışa aktarılır.

{{% alert color="primary" %}}
`HtmlSaveOptions` sınıfı, çıktıyı ince ayar yapmak için `ExportHiddenWorksheet`, `ExportImagesAsBase64` ve `Encoding` gibi ek özellikler sunar. Bunları dağıtım hedefinize göre gerektiği gibi ayarlayın.
{{% /alert %}}

## **API Özeti**

Yukarıdaki iş akışları, birlikte çalışan küçük bir Aspose.Cells API kümesine dayanır.

- `SparklineGroup` ve koleksiyon erişimcisi `worksheet.SparklineGroups`, her mini grafik grubu için türü (Line, Column, Stacked), veri aralığını ve çapa hücresini bildirmek amacıyla kullanılır. Bu makalede her grup tek bir hücreye sabitlenmiştir; dolayısıyla gruba `worksheet.SparklineGroups[i]` aracılığıyla erişilir.
- `Sparkline` ve `group.Sparklines[0]` dizinleyicisi, bir grup içindeki tek tek mini grafiği döndürür. Örnekteki her grup tam olarak bir mini grafik içerdiğinden, hiçbir `foreach` döngüsü gerekmez.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)`, sağlanan `Stream`'e mini grafiğin bir resmini yazan işleme yöntemidir. Yöntem `void` döndürür; çağrıdan sonra baytları akıştan okursunuz.
- `Cell.EmbeddedImage`, tek bir hücrenin içine bir resim saklayan bir `byte[]` özelliğidir. **Aspose.Cells 26.5 ve sonrasında** kullanılabilir ve `ToImage` tarafından işlenen bir mini grafiği aynı çalışma kitabına geri yüklemenin önerilen yoludur.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (bir `bool`), HTML dışa aktarımını aktif çalışma sayfasıyla sınırlar. Tek sayfalık raporlar oluştururken `HtmlSaveOptions` üzerinde en sık kullanılan özelliklerden biridir.
- `ImageOrPrintOptions.ImageType`, `Aspose.Cells.Drawing` ad alanında bulunur ve `ToImage` ile işleme ve çalışma sayfalarını görüntülere yazdırma sırasında kullanılan resim biçimini seçer (örneğin, `ImageType.Png`).

## **İlgili Makaleler**

- [Aspose.Cells for .NET'te Mini Grafikler](/cells/tr/net/sparkline/)
- [Bir Hücreye Görüntü Ekleme](/cells/tr/net/inserting-an-image-into-a-cell/)
- [SmartMarker Tek Hücreli Dizi İşleme | Aspose.Cells .NET](/cells/tr/net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="csharp" >}}