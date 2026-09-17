---
title: Sparkline'ı Aspose.Cells for C++'ta Görüntüye ve HTML'e Dönüştürme
linktitle: Sparkline'ı Aspose.Cells for C++'ta Görüntüye ve HTML'e Dönüştürme
description: Aspose.Cells sparkline'larını hücreye gömme için bağımsız görüntülere işlemeyi ve sparkline açısından zengin çalışma sayfalarını HtmlSaveOptions kullanarak HTML'e aktarmayı öğrenin.
keywords: Aspose.Cells, C++, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, sparkline işleme, sparkline'ı görüntüye dönüştürme, sparkline'ı HTML'e aktarma
type: docs
weight: 120
url: /tr/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparkline'lar, çalışma sayfası hücrelerinin içine yerleştirilmiş minyatür grafiklerdir. Aspose.Cells, her bir sparkline'ı bağımsız bir görüntü olarak ayıklamanıza (başka bir hücreye veya harici bir rapora yerleştirmek için) ve ayrıca sparkline açısından zengin tüm çalışma sayfasını tarayıcı tabanlı dağıtım için HTML olarak dışa aktarmanıza olanak tanır. Bu makalede kullanılan `Cell.EmbeddedImage` özelliği **Aspose.Cells 26.5 ve sonrasında** kullanılabilir.
{{% /alert %}}

## **Introduction**
Sparkline'lar, eğilimleri doğrudan bir çalışma sayfasının içinde görselleştirmenin kompakt bir yoludur. Excel kullanıcıları bunları yerinde görürken, birçok gerçek dünya senaryosu sparkline'ın hücreden çıkmasını gerektirir — örneğin, statik bir resim olarak farklı bir hücreye gömülmek, otomatik bir e-postaya eklenmek veya web'de yayınlanan bir HTML raporunun parçası olarak işlenmek.
Aspose.Cells bu işlemlerin her ikisini de destekler. `Sparkline.ToImage` yöntemi, tek bir sparkline'ı bir `Vector<uint8_t>` bayt dizisine işler ve ortaya çıkan baytlar `Cell.EmbeddedImage`'a atanabilir, böylece resim çalışma kitabının tek bir hücresinin içinde saklanır. Ayrı olarak, `HtmlSaveOptions` tüm çalışma kitabını — sparkline'lar dahil — kendi kendine yeten bir HTML dosyasına dönüştürmenize olanak tanır. Bu makale her iki iş akışını da uçtan uca ele almaktadır.

## **Workflow 1 — Render Sparklines to Images and Embed Them into Cells**
Bu iş akışında, küçük bir kaynak değer aralığı içeren bir çalışma sayfası oluşturacak, o aralığa üç farklı sparkline grubu (Çizgi, Sütun ve Yığılmış/Kazanç-Kayıp) ekleyecek, her grubu PNG olarak işleyecek ve bu PNG baytlarını bitişik hücrelere gömülü görüntüler olarak yazacaksınız. Son sonuç, hem canlı sparkline'ları hem de bunların işlenmiş resim karşılıklarını içeren tek bir `.xlsx` dosyasıdır.

### **Step-by-Step Instructions**
1. Bir çalışma dizini tanımlayın ve diskinizde var olduğundan emin olun.
2. Yeni bir `Workbook` oluşturun ve ilk `Worksheet`'e bir referans edinin.
3. `A1` ile `E1` hücreleri arasına beş örnek sayısal değer (örneğin, günlük satışlar veya sıcaklık okumaları) yerleştirin.
4. `worksheet.SparklineGroups.Add(...)` çağrısı yaparak çalışma sayfasına üç `SparklineGroup` nesnesi ekleyin:
   - `F1`'e ankrajlanmış, `A1:E1` veri aralığına sahip bir `SparklineType.Line` grubu.
   - `G1`'e ankrajlanmış, `A1:E1` veri aralığına sahip bir `SparklineType.Column` grubu.
   - `H1`'e ankrajlanmış, `A1:E1` veri aralığına sahip bir `SparklineType.Stacked` (kazanç/kayıp) grubu.
5. Bir `ImageOrPrintOptions` örneği oluşturun ve her sparkline'ın şeffaf bir PNG olarak işlenmesi için `ImageType` özelliğini `ImageType.Png` olarak ayarlayın.
6. Çalışma kitabını `output_with_sparklines.xlsx` olarak kaydedin.

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

Yukarıdaki kod, bir sparkline'ın her görsel temsilinin iki biçimde çoğaltıldığı bir çalışma kitabı üretir: 1. satıra ankrajlanmış canlı, yerel sparkline ve 2. satırdaki bitişik hücreye doğrudan gömülmüş statik bir PNG resmi. Resimler dosyanın kendisi içinde yaşadığı için, çalışma kitabı gömülü görüntü referanslarını bozmadan e-postalanabilen veya arşivlenebilen tek bir kendi kendine yeten yapı olarak kalır. Her sparkline grubunu PNG olarak işleyin — `Sparkline.ToImage(ImageOrPrintOptions)` resim baytlarını doğrudan bir `Vector<uint8_t>` olarak döndürür — ve diziyi hedef hücrenin `EmbeddedImage` özelliğine atayın — atama işlemi, resmi hücrenin saklanan içeriklerinin bir parçası yapan şeydir.

{{% alert color="primary" %}}
Her sparkline grubu tek bir hücreye ankrajlandığı için, `foreach` ile numaralandırmak yerine `group.Sparklines[0]` dizinleyicisi aracılığıyla ona erişebilirsiniz. Bu, işleme kodunu kısa tutar ve tipik "her ankraj hücresi için bir sparkline" deseniyle eşleşir. Resim baytlarının `Cell.EmbeddedImage` aracılığıyla saklanması Aspose.Cells 26.5 veya sonrasını gerektirir.
{{% /alert %}}

## **Workflow 2 — Export the Sparkline Worksheet to HTML**
Çalışma kitabı canlı sparkline'ları (ve isteğe bağlı olarak gömülü resim karşılıklarını) içerdiğinde, tüm çalışma sayfası HTML olarak kaydedilerek web'de yayınlanabilir. `HtmlSaveOptions` sınıfı, bu dışa aktarımı kontrol etmek için ihtiyacınız olan ayar düğmelerini sunar; bu iş akışında İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasını yeniden kullanacak ve bunu temiz, tek sayfalık bir HTML belgesine dönüştüreceksiniz.

### **Step-by-Step Instructions**
1. İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasının çalışma dizininizde disk üzerinde mevcut olduğundan emin olun.
2. Bu dosyayı yeni bir `Workbook` örneğine yükleyin.
3. `HtmlSaveOptions`'ı örnekleyin ve ortaya çıkan HTML dosyasının tüm çalışma kitabı yerine yalnızca etkin çalışma sayfasını içermesi için `ExportActiveWorksheetOnly` özelliğini `true` olarak ayarlayın.
4. HTML çıktısını diske yazmak için `workbook.Save("sparklines.html", htmlOptions)` çağrısını yapın.

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

Yukarıdaki kod, İş Akışı 1'den sparkline açısından zengin çalışma kitabını alır ve onu taşınabilir bir HTML dosyasına dönüştürür. Sparkline'lar, dışa aktarma moduna bağlı olarak, oluşturulan HTML içinde satır içi SVG veya PNG işlemeleri olarak korunur, böylece son kullanıcılar Excel yüklemeye gerek kalmadan eğilimleri herhangi bir modern tarayıcıda görüntüleyebilir. `ExportActiveWorksheetOnly`'i `true` olarak ayarlayarak, gizli sayfaları veya yardımcı verileri yanlışlıkla yayınlamaktan kaçınırsınız — yalnızca kullanıcı için o anda görünür olan çalışma sayfası dışa aktarılır.

{{% alert color="primary" %}}
`HtmlSaveOptions` sınıfı, çıktıyı ince ayar yapmak için `ExportHiddenWorksheet`, `ExportImagesAsBase64` ve `Encoding` gibi ek özellikler sunar. Bunları dağıtım hedefinize göre gerektiği gibi ayarlayın.

## **API Summary**
Yukarıdaki iş akışları, birlikte çalışan küçük bir Aspose.Cells API kümesine dayanmaktadır.
- `SparklineGroup` ve koleksiyon erişimcisi `worksheet.SparklineGroups`, her sparkline grubu için türü (Çizgi, Sütun, Yığılmış), veri aralığını ve ankraj hücresini bildirmek için kullanılır. Bu makalede her grup tek bir hücreye ankrajlandığından, gruba `worksheet.SparklineGroups[i]` aracılığıyla erişilir.
- `Sparkline` ve `group.Sparklines[0]` dizinleyicisi, bir grup içindeki tek tek sparkline'ı döndürür. Örnekteki her grup tam olarak bir sparkline içerdiğinden, `foreach` döngüsü gerekmez.
- `Sparkline.ToImage(ImageOrPrintOptions)`, sparkline'ın resmini doğrudan bir `Vector<uint8_t>` bayt dizisi olarak döndüren işleme yöntemidir.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (bir `bool`) HTML dışa aktarımını etkin çalışma sayfasıyla sınırlar. Tek sayfalık raporlar oluştururken `HtmlSaveOptions` üzerinde en sık kullanılan özelliklerden biridir.
- `ImageOrPrintOptions.ImageType`, `Aspose.Cells.Drawing` ad alanında bulunur ve `ToImage` ile işleme ve çalışma sayfalarını görüntülere yazdırma sırasında kullanılan resim biçimini (örneğin, `ImageType.Png`) seçer.

## **Related Articles**
- [Bir Hücreye Görüntü Ekleme](/cells/tr/cpp/inserting-an-image-into-a-cell/)
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}