---
title: Aspose.Cells for .NET'te Sparkline'ı Görüntüye ve HTML'e Dönüştürme
linktitle: Aspose.Cells for .NET'te Sparkline'ı Görüntüye ve HTML'e Dönüştürme
description: Aspose.Cells sparkline'larını hücre içine gömülmek üzere tek başına görüntüler olarak işlemeyi ve HtmlSaveOptions kullanarak sparkline açısından zengin çalışma sayfalarını HTML'ye aktarmayı öğrenin.
keywords: Aspose.Cells, .NET, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, sparkline işleme, sparkline'ı görüntüye dönüştürme, sparkline'ı HTML'ye aktarma
type: docs
weight: 120
url: /tr/net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparkline'lar çalışma sayfası hücrelerinin içine yerleştirilen küçük grafiklerdir. Aspose.Cells, her bir sparkline'ı tek başına bir görüntü olarak çıkarmanıza (başka bir hücreye veya harici bir rapora gömülmek üzere) ve ayrıca sparkline açısından zengin tüm çalışma sayfasını tarayıcı tabanlı dağıtım için HTML'ye aktarmanıza olanak tanır. Bu makalede kullanılan `Cell.EmbeddedImage` özelliği **Aspose.Cells 26.5 ve sonrasında** kullanılabilir.
{{% /alert %}}

## **Introduction**
Sparkline'lar, çalışma sayfasının içinde doğrudan trendleri görselleştirmenin kompakt bir yoludur. Excel kullanıcıları bunları yerinde görse de, birçok gerçek dünya senaryosunda bir sparkline'ın hücreden ayrılması gerekir; örneğin, başka bir hücreye statik bir resim olarak gömülmek, otomatik bir e-postaya eklenmek veya web'de yayınlanan bir HTML raporunun parçası olarak işlenmek üzere.
Aspose.Cells bu işlemlerin her ikisini de destekler. `Sparkline.ToImage` yöntemi, tek bir sparkline'ı bir akışa işler ve elde edilen baytlar `Cell.EmbeddedImage`'a atanabilir, böylece resim çalışma kitabının tek bir hücresinin içinde saklanır. Ayrı olarak, `HtmlSaveOptions` tüm çalışma kitabını — sparkline'lar dahil — kendi kendine yeten bir HTML dosyasına dönüştürmenize olanak tanır. Bu makale her iki iş akışını da uçtan uca ele almaktadır.

## **Workflow 1 — Render Sparklines to Images and Embed Them into Cells**
Bu iş akışında, küçük bir kaynak değer aralığı içeren bir çalışma sayfası oluşturacak, o aralığa üç farklı sparkline grubu (Çizgi, Sütun ve Yığılmış/Kazanç-Kayıp) ekleyecek, her grubu PNG olarak işleyecek ve bu PNG baytlarını bitişik hücrelere gömülü görüntüler olarak yazacaksınız. Nihai sonuç, hem canlı sparkline'ları hem de işlenmiş resim karşılıklarını içeren tek bir `.xlsx` dosyasıdır.

### **Step-by-Step Instructions**
1. Yeni bir `Workbook` oluşturun ve ilk `Worksheet`'e bir referans elde edin.
2. `A1`'den `E1`'e kadar olan hücreleri beş örnek sayısal değerle doldurun (örneğin, günlük satışlar veya sıcaklık okumaları).
3. `worksheet.SparklineGroups.Add(...)` çağırarak çalışma sayfasına üç `SparklineGroup` nesnesi ekleyin:
   - `A1:E1` veri aralığıyla `F1`'de sabitlenmiş bir `SparklineType.Line` grubu.
   - `A1:E1` veri aralığıyla `G1`'de sabitlenmiş bir `SparklineType.Column` grubu.
   - `A1:E1` veri aralığıyla `H1`'de sabitlenmiş bir `SparklineType.Stacked` (kazanç/kayıp) grubu.
4. Bir `ImageOrPrintOptions` örneği oluşturun ve her sparkline'ın PNG resmi olarak işlenmesi için `ImageType` özelliğini `ImageType.Png` olarak ayarlayın.
6. Çalışma kitabını `output_with_sparklines.xlsx` olarak kaydedin.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
using Aspose.Cells.Rendering;
// Create a new workbook and access the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Populate sample data in cells A1:E1
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// Add a Line sparkline group anchored at F1 (column 5, row 0)
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
// Add a Column sparkline group anchored at G1 (column 6, row 0)
CellArea columnArea = new CellArea();
columnArea.StartColumn = 6;
columnArea.EndColumn = 6;
columnArea.StartRow = 0;
columnArea.EndRow = 0;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
// Add a Win/Loss (Stacked) sparkline group anchored at H1 (column 7, row 0)
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 7;
stackedArea.EndColumn = 7;
stackedArea.StartRow = 0;
stackedArea.EndRow = 0;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
// Configure image options for PNG output
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.ImageType = ImageType.Png;
// Convert the Line sparkline to image and embed it in cell F2
Sparkline lineSp = worksheet.SparklineGroups[lineIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    lineSp.ToImage(ms, imageOptions);
    worksheet.Cells["F2"].EmbeddedImage = ms.ToArray();
}
// Convert the Column sparkline to image and embed it in cell G2
Sparkline columnSp = worksheet.SparklineGroups[columnIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    columnSp.ToImage(ms, imageOptions);
    worksheet.Cells["G2"].EmbeddedImage = ms.ToArray();
}
// Convert the Win/Loss sparkline to image and embed it in cell H2
Sparkline stackedSp = worksheet.SparklineGroups[stackedIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    stackedSp.ToImage(ms, imageOptions);
    worksheet.Cells["H2"].EmbeddedImage = ms.ToArray();
}
// Save the workbook to disk
workbook.Save("output_with_sparklines.xlsx");
```

Yukarıdaki kod, her sparkline'ın görsel temsilinin iki biçimde var olduğu bir çalışma kitabı üretir: 1. satırda sabitlenmiş canlı, yerel sparkline ve 2. satırdaki bitişik bir hücreye doğrudan gömülmüş statik bir PNG resmi. Resimler dosyanın kendisinin içinde yer aldığından, çalışma kitabı gömülü görüntü referanslarını bozmadan e-postayla gönderilebilen veya arşivlenebilen tek bir kendi kendine yeten yapı olarak kalır.

{{% alert color="primary" %}}
Her sparkline grubu tek bir hücreye sabitlendiğinden, `foreach` ile numaralandırmak yerine `group.Sparklines[0]` indeksleyicisi aracılığıyla erişebilirsiniz. Bu, işleme kodunu kısa tutar ve tipik "sabitleme hücresi başına bir sparkline" kalıbıyla eşleşir. Resim baytlarının `Cell.EmbeddedImage` aracılığıyla saklanması Aspose.Cells 26.5 veya sonrasını gerektirir.

## **Workflow 2 — Export the Sparkline Worksheet to HTML**
Çalışma kitabı canlı sparkline'ları (ve isteğe bağlı olarak gömülü resim karşılıklarını) içerdiğinde, tüm çalışma sayfası HTML olarak kaydedilerek web'de yayınlanabilir. `HtmlSaveOptions` sınıfı, bu dışa aktarımı kontrol etmek için ihtiyaç duyduğunuz düğmeleri sunar; bu iş akışında İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasını yeniden kullanacak ve onu temiz, tek sayfalık bir HTML belgesine dönüştüreceksiniz.

### **Step-by-Step Instructions**
1. İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasının çalışma dizininizde diskte mevcut olduğundan emin olun.
2. Bu dosyayı yeni bir `Workbook` örneğine yükleyin.
3. `HtmlSaveOptions`'ı örnekleyin ve sonuç HTML dosyasının tüm çalışma kitabı yerine yalnızca etkin çalışma sayfasını içermesi için `ExportActiveWorksheetOnly` özelliğini `true` olarak ayarlayın.
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

Yukarıdaki kod, İş Akışı 1'den gelen sparkline açısından zengin çalışma kitabını alır ve onu taşınabilir bir HTML dosyasına dönüştürür. Sparkline grupları, oluşturulan HTML tablosunun içinde satır içi görüntüler olarak işlenir, böylece son kullanıcılar Excel'in yüklü olmasına gerek kalmadan trendleri herhangi bir modern tarayıcıda görüntüleyebilir. `ExportActiveWorksheetOnly` özelliğini `true` olarak ayarlayarak, gizli sayfaları veya yardımcı verileri yanlışlıkla yayınlamaktan kaçınırsınız — yalnızca kullanıcının o anda görebildiği çalışma sayfası dışa aktarılır.
{{% /alert %}}

{{% alert color="primary" %}}
`HtmlSaveOptions` sınıfı, çıktının ince ayarını yapmak için `ExportHiddenWorksheet`, `ExportImagesAsBase64` ve `Encoding` gibi ek özellikler sunar. Bunları dağıtım hedefinize göre gerektiği şekilde ayarlayın.

## **API Summary**
Yukarıdaki iş akışları, birlikte çalışan küçük bir Aspose.Cells API kümesine dayanır.
- `SparklineGroup` ve koleksiyon erişimcisi `worksheet.SparklineGroups`, her sparkline grubu için türü (Çizgi, Sütun, Yığılmış), veri aralığını ve sabitleme hücresini bildirmek için kullanılır. Bu makalede her grup tek bir hücreye sabitlenmiştir, dolayısıyla gruba `worksheet.SparklineGroups[i]` aracılığıyla erişilir.
- `Sparkline` ve indeksleyici `group.Sparklines[0]`, bir grup içindeki tek tek sparkline'ı döndürür. Örnekteki her grup tam olarak bir sparkline içerdiğinden, `foreach` döngüsü gerekmez.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)`, sparkline'ın resmini sağlanan `Stream`'e yazan işleme yöntemidir. Yöntem `void` döndürür; baytları çağrıdan sonra akıştan okursunuz.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (bir `bool`), HTML dışa aktarımını etkin çalışma sayfasıyla sınırlar. Tek sayfalık raporlar oluştururken `HtmlSaveOptions` üzerinde en sık kullanılan özelliklerden biridir.
- `ImageOrPrintOptions.ImageType`, `Aspose.Cells.Drawing` ad alanında yer alır ve `ToImage` ile işlenirken ve çalışma sayfaları görüntülere yazdırılırken kullanılan resim biçimini (örneğin, `ImageType.Png`) seçer.

## **Related Articles**
{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}