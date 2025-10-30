---
title: HTML ile C++
linktitle: HTML
type: docs
weight: 230
url: /tr/cpp/convert-excel-to-html/
description: Aspose.Cells kullanarak Excel dosyasını HTML ve MHTML biçimine dönüştürün.
---

## **Excel Çalışma Kitabını HTML'ye Dönüştürme**
Aspose.Cells API, elektronik tabloyu HTML formatına aktarmayı destekler. Bu amaçla, Aspose.Cells [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions) sınıfını kullanarak çıktı HTML'sinin çeşitli yönlerini kontrol etme esnekliği sağlar.

Aşağıdaki kod örneği, C++ kullanarak bir çalışma kitabını HTML dosyası olarak nasıl kaydedeceğinizi gösterir:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"Book1.xlsx");

    // Save file to HTML format
    workbook.Save(u"out.html");

    std::cout << "Workbook saved to HTML format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excel Çalışma Kitabını MHTML Dosyalarına Dönüştürme**
MHTML, normal HTML'yi dış kaynaklar (örneğin, içerik bağlanan resimler, animasyonlar, sesler vb.) ile birleştirir ve tek bir dosyada tutar. .mht dosya uzantısına sahip e-postalar için kullanılır. Aspose.Cells, MHTML dosyalarını okuma ve yazmayı destekler.

Aşağıdaki kod örneği, C++ kullanarak bir çalışma kitabını MHTML dosyası olarak nasıl kaydedeceğinizi gösterir:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"Book1.xlsx");
    std::unique_ptr<Workbook> workbook = std::make_unique<Workbook>(inputFilePath);

    // Save file to mhtml format
    U16String outputFilePath(u"out.mht");
    workbook->Save(outputFilePath, SaveFormat::MHtml);

    std::cout << "Workbook saved to MHTML format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [HTML yüklenirken Sütunları ve Satırları Otomatik Uydurma](/cells/tr/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [HTML'den İçe Aktarırken Büyük Sayıların Üstel Görünümünü Engelle](/cells/tr/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/)
- [HTML Bağlantı Hedef Türünü Değiştirme](/cells/tr/cpp/change-the-html-link-target-type/)
- [Excel'i HTML'e dönüştür ve açıklama metni ekleyin](/cells/tr/cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/tr/cpp/create-transparent-image-of-excel-worksheet/)
- [HTML içe aktarırken satır sonrası gereksiz boşlukları silin](/cells/tr/cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [HTML'ye kaydederken Downlevel Açıklanan Yorumları Devre Dışı Bırak](/cells/tr/cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Çerçeve Betiklerini ve Belge Özelliklerini Dışa Aktarmayı Devre Dışı Bırak](/cells/tr/cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel'den HTML'ye - Daha İyi Düzen için PresentationPreference Seçeneğini Kullan](/cells/tr/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Excel dosyası oluşturan ve kullanılmayan isimli bir stil oluşturan aşağıdaki örnek kod. {0} **true** olarak ayarlandığından, bu kullanılmayan isimli stil [çıktı HTML'sine](61767778.zip) dışa aktarılmayacaktır. Ancak, **false**olarak ayarlarsanız, bu kullanılmayan stil çıktı HTML içinde bulunacaktır ve yukarıdaki ekran görüntüsünde HTML işaretleme dilinde görebilirsiniz.](/cells/tr/cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Excel dosyasını HTML'e dönüştüren aşağıdaki örnek kod. Bu ekran görüntüsü, örnek Excel dosyasının Microsoft Excel 2013'te nasıl göründüğünü göstermektedir.](/cells/tr/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Excel'den HTML'ye Databar, ColorScale ve IconSet Koşullu Biçimlendirmeyi Dışa Aktar](/cells/tr/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Excel Dosyasını HTML'ye Kaydederken Yorumları Dışa Aktar](/cells/tr/cpp/export-comments-while-saving-excel-file-to/)
- [Excel'de belge çalışma kitabı ve çalışma sayfası özelliklerini HTML dönüşümünde dışa aktar](/cells/tr/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Excel'den HTML'e Grid Çizgileri ile Dışa Aktar](/cells/tr/cpp/export-excel-to-html-with-gridlines/)
- [HTML'e Baskı Alanı Aralığını Dışa Aktar](/cells/tr/cpp/export-print-area-range-to/)
- [CrossHideRight ile Üzerine Binme Content'ini HTML'şe kaydederken Gizle](/cells/tr/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Çıktı HTML'sindeki Sayfa CSS'sini Ayrı Ayrı Dışa Aktarma](/cells/tr/cpp/export-worksheet-css-separately-in-output/)
- [Web Tarayıcıları tarafından desteklenmeyen Birleşik Stil'in benzerini dışa aktar](/cells/tr/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [HtmlSaveOptions.TableCssId özelliği ile Tablo Öğeleri Stillerini Ön Eklemek](/cells/tr/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [HTML'ye Kaydetme İşlemi Sırasında Gizli Çalışsayfa İçeriğinin Dışa Aktarılmasını Engelle](/cells/tr/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Kendini Kapatan Etiketleri Tanı](/cells/tr/cpp/recognise-self-closing-tags/)
- [Yayılan Elemanın Düzgünleşmiş Doldurmasını, Çalışma Kitaplarını HTML'e Dönüştürürken Renderle](/cells/tr/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Kolon genişliğini em veya yüzde gibi ölçeklenebilir birim olarak ayarlayın](/cells/tr/cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [HTML olarak elektronik tabloyu oluştururken varsayılan yazı tipini ayarlayın](/cells/tr/cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Çıkış HTML'sinde dizeyi nasıl geçeceğini HtmlCrossType kullanarak belirtin](/cells/tr/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [HTML'nin Excel elektronik tablosuna yüklenmesi sırasında DIV etiketlerinin düzenini destekle](/cells/tr/cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)
- [ HTML'ye Kaydederken CSS Özel Özelliklerini Etkinleştir](/cells/tr/cpp/enable-css-custom-properties-while-saving-to-html/)
{{< app/cells/assistant language="cpp" >}}
