---
title: Aspose.Cells for C++'ta Sparkline'ı Görüntüye ve HTML'ye Dönüştürme
linktitle: Convert Sparkline to Image and HTML
description: Aspose.Cells sparkline'larını hücreye gömme için bağımsız görüntüler olarak işlemeyi ve HtmlSaveOptions kullanarak sparkline açısından zengin çalışma sayfalarını HTML'ye aktarmayı öğrenin.
keywords: Aspose.Cells, C++, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, sparkline işleme, sparkline'ı görüntüye dönüştürme, sparkline'ı HTML'ye aktarma
type: docs
weight: 120
url: /tr/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparkline'lar, çalışma sayfası hücrelerinin içine yerleştirilen küçük grafiklerdir. Aspose.Cells, her bir sparkline'ı bağımsız bir görüntü olarak çıkarmanıza (başka bir hücreye veya harici bir rapora gömmek için) ve ayrıca sparkline açısından zengin çalışma sayfasının tamamını tarayıcı tabanlı dağıtım için HTML olarak dışa aktarmanıza olanak tanır. Bu makalede kullanılan `Cell.EmbeddedImage` özelliği **Aspose.Cells 26.5 ve sonrasında** kullanılabilir.
{{% /alert %}}

## **Giriş**

Sparkline'lar, trendleri doğrudan bir çalışma sayfasının içinde görselleştirmenin kompakt bir yoludur. Excel kullanıcıları onları yerinde görse de, birçok gerçek dünya senaryosunda bir sparkline'ın hücreden çıkması gerekir — örneğin, farklı bir hücreye statik resim olarak gömülmesi, otomatik bir e-postaya eklenmesi veya web'de yayınlanan bir HTML raporunun parçası olarak işlenmesi gerekir.

Aspose.Cells bu işlemlerin her ikisini de destekler. `Sparkline.ToImage` metodu, tek bir sparkline'ı bir akışa işler ve elde edilen baytlar `Cell.EmbeddedImage` özelliğine atanabilir, böylece resim çalışma kitabının tek bir hücresinde saklanır. Ayrı olarak, `HtmlSaveOptions` tüm çalışma kitabını — sparkline'lar dahil — kendi kendine yeterli bir HTML dosyasına dönüştürmenize olanak tanır. Bu makale her iki iş akışını da uçtan uca ele almaktadır.

## **İş Akışı 1 — Sparkline'ları Görüntülere Dönüştürün ve Hücrelere Gömün**

Bu iş akışında, küçük bir kaynak değer aralığı içeren bir çalışma sayfası oluşturacak, o aralığa üç farklı sparkline grubu (Çizgi, Sütun ve Yığılmış/Kazanma-Kaybetme) ekleyecek, her grubu PNG olarak işleyecek ve bu PNG baytlarını bitişik hücrelere gömülmüş görüntüler olarak yazacaksınız. Sonuç, hem canlı sparkline'ları hem de bunların işlenmiş resim karşılıklarını içeren tek bir `.xlsx` dosyasıdır.

### **Adım Adım Talimatlar**

1. Bir çalışma dizini tanımlayın ve diskte var olduğundan emin olun.
2. Yeni bir `Workbook` oluşturun ve ilk `Worksheet`'e bir referans alın.
3. `A1`'den `E1`'e kadar olan hücreleri beş örnek sayısal değerle doldurun (örneğin, günlük satışlar veya sıcaklık okumaları).
4. `worksheet.SparklineGroups.Add(...)` çağırarak çalışma sayfasına üç `SparklineGroup` nesnesi ekleyin:
   - Veri aralığı `A1:E1` olan, `F1`'e bağlantılı bir `SparklineType.Line` grubu.
   - Veri aralığı `A1:E1` olan, `G1`'e bağlantılı bir `SparklineType.Column` grubu.
   - Veri aralığı `A1:E1` olan, `H1`'e bağlantılı bir `SparklineType.Stacked` (kazanma/kaybetme) grubu.
5. Bir `ImageOrPrintOptions` örneği oluşturun ve her sparkline'ın şeffaf bir PNG olarak işlenmesi için `ImageType` özelliğini `ImageType.Png` olarak ayarlayın.
6. Üç grubun her biri için, `group.Sparklines[0].ToImage(memoryStream, imageOptions)` kullanarak tek sparkline'ı işleyin, `MemoryStream`'i bir `Vector<uint8_t>`'a dönüştürün ve diziyi sırasıyla `worksheet.Cells["F2"].EmbeddedImage`, `worksheet.Cells["G2"].EmbeddedImage` ve `worksheet.Cells["H2"].EmbeddedImage` öğelerine atayın.
7. Çalışma kitabını `output_with_sparklines.xlsx` olarak kaydedin.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, U16String("A1:E1"), false, lineArea);

    CellArea columnArea;
    columnArea.StartColumn = 6;
    columnArea.EndColumn = 6;
    columnArea.StartRow = 0;
    columnArea.EndRow = 0;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, U16String("A1:E1"), false, columnArea);

    CellArea stackedArea;
    stackedArea.StartColumn = 7;
    stackedArea.EndColumn = 7;
    stackedArea.StartRow = 0;
    stackedArea.EndRow = 0;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, U16String("A1:E1"), false, stackedArea);

    ImageOrPrintOptions imageOptions;
    imageOptions.SetImageType(ImageType::Png);

    Sparkline lineSp = worksheet.GetSparklineGroups().Get(lineIdx).GetSparklines().Get(0);
    Vector<uint8_t> lineImg = lineSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"F2").SetEmbeddedImage(lineImg);

    Sparkline columnSp = worksheet.GetSparklineGroups().Get(columnIdx).GetSparklines().Get(0);
    Vector<uint8_t> columnImg = columnSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"G2").SetEmbeddedImage(columnImg);

    Sparkline stackedSp = worksheet.GetSparklineGroups().Get(stackedIdx).GetSparklines().Get(0);
    Vector<uint8_t> stackedImg = stackedSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"H2").SetEmbeddedImage(stackedImg);

    workbook.Save(u"output_with_sparklines.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

Yukarıdaki kod, bir sparkline'ın her görsel temsilinin iki biçimde çoğaltıldığı bir çalışma kitabı üretir: 1. satıra bağlantılı canlı, yerel sparkline ve 2. satırdaki bitişik bir hücreye doğrudan gömülmüş statik bir PNG resmi. Resimler dosyanın kendisinde yaşadığı için, çalışma kitabı gömülü görüntü referanslarını kırmadan e-postalanabilen veya arşivlenebilen tek bir kendi kendine yeterli yapıt olmaya devam eder. Her sparkline grubunu PNG olarak işleyin, `MemoryStream`'i bir `Vector<uint8_t>`'a dönüştürün ve diziyi hedef hücrenin `EmbeddedImage` özelliğine atayın — atama işlemi, resmi hücrenin saklanan içeriğinin bir parçası yapan şeydir.

{{% alert color="primary" %}}
Her sparkline grubu tek bir hücreye bağlantılı olduğundan, `foreach` ile numaralandırmak yerine `group.Sparklines[0]` dizinleyicisi aracılığıyla ona erişebilirsiniz. Bu, işleme kodunu kısa tutar ve tipik "bağlantı hücresi başına bir sparkline" kalıbıyla eşleşir. Resim baytlarını `Cell.EmbeddedImage` aracılığıyla saklamak Aspose.Cells 26.5 veya sonrasını gerektirir.
{{% /alert %}}

## **İş Akışı 2 — Sparkline Çalışma Sayfasını HTML'ye Aktarın**

Çalışma kitabı canlı sparkline'ları (ve isteğe bağlı olarak gömülmüş resim karşılıklarını) içerdiğinde, çalışma sayfasının tamamı HTML olarak kaydedilerek web'de yayınlanabilir. `HtmlSaveOptions` sınıfı, bu dışa aktarmayı kontrol etmek için ihtiyacınız olan düğmeleri sunar; bu iş akışında İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasını yeniden kullanacak ve onu temiz, tek sayfalık bir HTML belgesine dönüştüreceksiniz.

### **Adım Adım Talimatlar**

1. İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasının çalışma dizininizde diskte mevcut olduğundan emin olun.
2. Bu dosyayı yeni bir `Workbook` örneğine yükleyin.
3. `HtmlSaveOptions`'ı örnekleyin ve sonuç HTML dosyasının tüm çalışma kitabı yerine yalnızca etkin çalışma sayfasını içermesi için `ExportActiveWorksheetOnly` özelliğini `true` olarak ayarlayın.
4. HTML çıktısını diske yazmak için `workbook.Save("sparklines.html", htmlOptions)` çağırın.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook(u"output_with_sparklines.xlsx");
    HtmlSaveOptions htmlOptions;
    htmlOptions.SetExportActiveWorksheetOnly(true);
    workbook.Save(u"sparklines.html", htmlOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

Yukarıdaki kod, İş Akışı 1'deki sparkline açısından zengin çalışma kitabını alır ve onu taşınabilir bir HTML dosyasına dönüştürür. Sparkline'lar, dışa aktarma moduna bağlı olarak, oluşturulan HTML içinde satır içi SVG veya PNG işlemeleri olarak korunur, böylece son kullanıcılar Excel yüklemeye gerek kalmadan trendleri herhangi bir modern tarayıcıda görüntüleyebilir. `ExportActiveWorksheetOnly`'i `true` olarak ayarlayarak, gizli sayfaları veya yardımcı verileri yanlışlıkla yayımlamaktan kaçınırsınız — yalnızca kullanıcı tarafından o anda görülebilen çalışma sayfası dışa aktarılır.

{{% alert color="primary" %}}
`HtmlSaveOptions` sınıfı, çıktıyı ince ayar yapmak için `ExportHiddenWorksheet`, `ExportImagesAsBase64` ve `Encoding` gibi ek özellikler sunar. Bunları dağıtım hedefinize göre gerektiği gibi ayarlayın.
{{% /alert %}}

## **API Özeti**

Yukarıdaki iş akışları, birlikte çalışan küçük bir Aspose.Cells API kümesine dayanır.

- `SparklineGroup` ve koleksiyon erişimcisi `worksheet.SparklineGroups`, her sparkline grubu için türü (Çizgi, Sütun, Yığılmış), veri aralığını ve bağlantı hücresini bildirmek için kullanılır. Bu makalede her grup tek bir hücreye bağlantılıdır, dolayısıyla gruba `worksheet.SparklineGroups[i]` aracılığıyla erişilir.
- `Sparkline` ve `group.Sparklines[0]` dizinleyicisi, bir grup içindeki tek tek sparkline'ı döndürür. Örnekteki her grup tam olarak bir sparkline içerdiğinden, `foreach` döngüsü gerekmez.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)`, sparkline'ın bir resmini sağlanan `Stream`'e yazan işleme metodudur. Metod `void` döndürür; çağrıdan sonra baytları akıştan okursunuz.
- `Cell.EmbeddedImage`, tek bir hücrenin içinde bir resim saklayan bir `Vector<uint8_t>` özelliğidir. **Aspose.Cells 26.5 ve sonrasında** kullanılabilir ve `ToImage` tarafından işlenen bir sparkline'ı aynı çalışma kitabına geri döndürmek için önerilen yoldur.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (bir `bool`), HTML dışa aktarımını etkin çalışma sayfasıyla sınırlar. Tek sayfalık raporlar oluştururken `HtmlSaveOptions` üzerinde en yaygın kullanılan özelliklerden biridir.
- `ImageOrPrintOptions.ImageType`, `Aspose.Cells.Drawing` ad alanında bulunur ve `ToImage` ile işlenirken ve çalışma sayfaları görüntülere yazdırılırken kullanılan resim biçimini (örneğin, `ImageType.Png`) seçer.

## **İlgili Makaleler**

- [Aspose.Cells for C++ için Aspose.Cells'te Sparkline'lar](/cells/tr/cpp/sparkline/)
- [Hücreye Görüntü Ekleme](/cells/tr/cpp/inserting-an-image-into-a-cell/)
- [SmartMarker Tek Hücre Dizi İşleme | Aspose.Cells for C++](/cells/tr/cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="cpp" >}}