---
title: C++ ile Yazdırma Başlıklarını Ayarlama Yöntemi
linktitle: Yazdırma Başlıklarını Nasıl Ayarlarsınız
type: docs
weight: 200
url: /tr/cpp/how-to-set-print-titles/
description: Bu makale, Aspose.Cells kütüphanesi kullanılarak C++ ile yazdırma başlıklarının nasıl ayarlanacağını açıklayan kodu gösterir.
keywords: Satırları ve sütunları tekrar tekrar yazdırma, C++ ta Yazdırma Başlıklarını Ayarlama, C++ kullanarak Yazdırma Başlıklarını Ayarla ve Temizle, C++ kullanarak Yazdırma Başlıklarını Kaldırma, Excel de Yazdırma Başlıklarını Ayarlama, Excel de Yazdırma Başlıklarını Temizleme.
---

## **Olası Kullanım Senaryoları**

Excel'de yazdırma başlıklarını ayarlamak, belirli satır veya kolonların her yazdırılan sayfada tekrarlanmasını sağlar, bu özellik büyük elektronik tablolar için özellikle faydalıdır. İşte birkaç neden:

1. Artırılmış Okunabilirlik: Yazdırma başlıkları, başlıkları tüm sayfalarda görünür tutarak veriyi anlamaya yardımcı olur, böylece her seferinde ilk sayfaya dönmeden bilgileri yorumlamak daha kolay hale gelir.

1. Profesyonel Sunum: Her sayfada tutarlı bir şekilde başlıklar veya etiketler göstermek, yazdırılmış belgeler için daha düzgün ve profesyonel bir görünüm sağlar.

1. Gelişmiş Navigasyon: Geniş veriler içeren belgelerde, her sayfada başlıkların tekrarlanması, daha hızlı gezinme ve referans sağlar, böylece sayfalar arasında geri dönüp gitme ihtiyacını azaltır.

1. Hata Azaltma: Her sayfada başlıklar olduğunda, yanlış anlamalar veya veri giriş hataları minimize edilir, kullanıcılar verilerin bağlamını kolayca görebilir.

1. Tutarlılık: Kolon başlıkları veya satır etiketleri gibi önemli bilgilerin her zaman görünür olması, belge genelinde tutarlılık ve açıklık sağlar.

## **Excel’de Yazdırma Başlıklarını Nasıl Ayarlarsınız**

Excel’de yazdırma başlıklarını ayarlamak için şu adımları izleyin:

1. Sayfa Düzeni Sekmesini Açın: Excel penceresinin üstündeki "Sayfa Düzeni" sekmesine tıklayın.
1. Yazdırma Başlıklarına Erişin: "Sayfa Ayarı" grubunda "Yazdırma Başlıkları"na tıklayın.
1. Satırları Tekrarlamak İçin Ayarlayın: "Sayfa Ayarı" iletişim kutusunda, "Sayfa" sekmesine gidin. "Yazdırma başlıkları" bölümünde, "Üstte tekrarlanacak satırlar" kutusuna tıklayın ve tekrarlanmasını istediğiniz satırları seçin.
1. Kolonları Tekrarlamak İçin Ayarlayın (gerekirse): Aynı şekilde, "Sol tarafta tekrarlanacak kolonlar" kutusuna tıklayın ve tekrarlanmasını istediğiniz kolonları seçin.
<br>
<img src="3.png" width=60% />

1. Onaylayın ve Yazdırın: "Tamam"a tıklayarak ayarları uygulayın. Çalışma sayfasını yazdırdığınızda, belirttiğiniz satırlar veya kolonlar her sayfada görünecektir.

## **Excel’de Yazdırma Başlıklarını Nasıl Temizlersiniz**

Excel’de yazdırma başlıklarını temizlemek için, her yazdırılan sayfada tekrarlanan satır veya kolonları kaldırmanız gerekir. İşte nasıl yapılır:

1. Sayfa Düzeni Sekmesini Açın: Excel penceresinin üstündeki "Sayfa Düzeni" sekmesine tıklayın.
1. Yazdırma Başlıklarına Erişin: "Sayfa Ayarı" grubunda "Yazdırma Başlıkları"na tıklayın.
1. Yazdırma Başlıklarını Temizle: "Sayfa Ayarı" iletişim kutusunda, "Sayfa" sekmesine gidin. "Üstte tekrarlanacak satırlar" ve "Sol tarafta tekrarlanacak kolonlar" metin kutularını temizleyin ve içlerindeki içerikleri silin.
<br>
<img src="4.png" width=60% />

1. Onaylayın ve Kapatın: Değişiklikleri uygulamak için "Tamam"a tıklayın.

## **Aspose.Cells kullanarak Yazdırma Başlıklarını Nasıl Ayarlarsınız**

Belirtilmiş bir çalışma sayfasında yazdırma başlıklarını ayarlamak için: İlk olarak, [örnek dosyayı](input.xlsx) yükleyin, ardından istenen çalışma sayfası için [**Worksheet.GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) ve [**Worksheet.GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) özelliklerini [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) nesnesinde değiştirmeniz gerekir. Bu özellikleri bir aralık dizesine ayarlamak, yazdırma başlıklarını belirler.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    Workbook workbook(u"input.xlsx");

    // Access the desired worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set rows to repeat at the top (e.g., rows 1 and 2)
    worksheet.GetPageSetup().SetPrintTitleRows(u"$1:$2");

    // Set columns to repeat at the left (e.g., columns A and B)
    worksheet.GetPageSetup().SetPrintTitleColumns(u"$A:$B");

    // Save the workbook
    workbook.Save(u"set_print_titles.pdf");

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Çıktı sonucu:
<br>
<img src="1.png" width=60% />

## **Aspose.Cells kullanarak Yazdırma Başlıklarını Temizleme**

Belirli bir çalışma sayfasında yazdırma başlıklarını temizlemek için: İlk olarak, [örnek dosyayı](input.xlsx) yükleyin, ardından istenen çalışma sayfası için [**Worksheet.GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) ve [**Worksheet.GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) özelliklerini [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) nesnesinde değiştirin. Bu özellikleri boş bir dizgeye ayarlamak, yazdırma başlıklarını temizler.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    U16String inputFilePath = u"input.xlsx";
    Workbook workbook(inputFilePath);

    // Access the desired worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Clear the rows and columns set to repeat
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintTitleRows(u"");
    pageSetup.SetPrintTitleColumns(u"");

    // Save the workbook
    U16String outputFilePath = u"clear_print_titles.pdf";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();
}
```

Çıktı sonucu:
<br>
<img src="2.png" width=60% />
