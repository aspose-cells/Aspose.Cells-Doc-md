---
title: Excel'i OFD Formatına Dönüştürme
linktitle: Excel'i OFD Formatına Dönüştürme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için OFD (Open Fixed-layout Document) formatına Excel çalışma kitaplarını dönüştürmeyi destekleyen bir C++ kütüphanesidir. Bu makale, Aspose.Cells kullanarak Excel içeriği oluşturmayı ve OFD olarak dışa aktarmayı, ayrıca mevcut Excel dosyalarını OFD'ye dönüştürmeyi göstermektedir.
keywords: Aspose.Cells, C++ kütüphanesi, elektronik tablo, Excel'ten OFD'ye, OFD dönüşümü, SaveFormat.Ofd, sabit düzen belge, çalışma kitabı dışa aktarma
type: docs
weight: 195
url: /tr/cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, `SaveFormat.Ofd` numaralandırma değerini kullanarak Excel çalışma kitaplarını doğrudan OFD (Open Fixed-layout Document) formatına dönüştürmeyi destekler. Ortaya çıkan OFD belgesi, çalışma kitabının görünür düzenini, içeriğini, birleştirilmiş hücrelerini, sütun genişliklerini, satır yüksekliklerini, yazı tiplerini, renklerini, kenarlıklarını ve sayı formatlarını korur. Bu, Aspose.Cells'i sabit düzenli bir çıktı gerektiren arşivleme, yazdırma, düzenleyici dosyalama ve hükümet başvurusu iş akışları için uygun hale getirir.

{{% /alert %}}
## **Giriş**
OFD (Open Fixed-layout Document), dijital belgeleri sabit, sayfa tabanlı bir düzende temsil etmek için Çin ulusal standardıdır (GB/T 33190-2016). Kaynak belgenin görsel görünümünün tam olarak yazıldığı şekliyle korunması gereken kullanım durumları için PDF'ye benzer bir rol üstlenir. OFD, Çin Halk Cumhuriyeti'nde hükümet başvuruları, düzenleyici dosyalama, elektronik faturalar ve uzun süreli arşivleme için yaygın olarak benimsenmiştir.

Excel çalışma kitaplarını OFD'ye dönüştürmek, elektronik tablo içeriğinin düzenlenebilir bir elektronik tablo olarak değil, salt okunur, düzeni kilitli bir yapıt olarak dağıtılması gereken senaryolarda yaygın bir gereksinimdir. Örnekler arasında, kesinleştirilmiş bir faturanın müşteriye gönderilmesi, üç aylık bir finansal raporun arşivlenmesi veya bir bütçe elektronik tablosunun düzenleyici bir makama sunulması yer alır. Aspose.Cells, çalışma kitabını doğrudan OFD'ye yazan ve ara bir dönüşüm adımı gerektirmeyen `SaveFormat.Ofd` numaralandırma değeri aracılığıyla bu gereksinimi karşılar. OFD çıktısı, çalışma kitabı üzerinde yapılandırılan hücre değerlerini, birleştirilmiş aralıkları, yazı tiplerini, renkleri, kenarlıkları, sayı formatlarını ve sayfa yapısı seçeneklerini korur.

{{% alert color="primary" %}}

Aspose.Cells tarafından oluşturulan OFD çıktısı, kaynak çalışma kitabının görünür düzenini, hücre içeriği, birleştirilmiş hücreler, sütun genişlikleri ve satır yükseklikleri dahil olmak üzere korur. Yazı tipleri, renkler, kenarlıklar, hizalama ve sayı formatları gibi hücre biçimlendirmesi de sabit düzen çıktısında işlenir. Çalışma sayfası üzerinde yapılandırılan kağıt boyutu, yönlendirme ve yazdırma alanı gibi sayfa yapısı seçenekleri, ortaya çıkan OFD belgesinin düzenini etkiler.

{{% /alert %}}
## **Excel Çalışma Kitabı Oluşturma ve OFD Olarak Kaydetme**
Aspose.Cells, bir çalışma kitabını programatik olarak oluşturmanıza, verilerle doldurmanıza ve ardından `SaveFormat.Ofd` numaralandırmasını kullanarak doğrudan OFD formatında kaydetmenize olanak tanır. Aşağıdaki örnek sıfırdan bir fatura oluşturur. Bir şirket logosu, başlık bilgileri, fatura alıcısı bölümü, kalemler ve hesaplanan toplamlar ekler, ardından çalışma kitabını bir OFD belgesine aktarır.
### **Logo ile Fatura Oluşturma**
Örnek, sol üst alana bir logo görüntüsü ekleyerek, şirket adı ve iletişim bilgilerini doldurarak, birleştirilmiş hücreler arasına "FATURA" başlığı ekleyerek, fatura numarasını ve tarihini kaydederek, fatura alıcısı müşterisini listeleyerek, açıklama, miktar, birim fiyat ve toplam sütunlarıyla bir kalem tablosu oluşturarak ve hücre formüllerini kullanarak ara toplam, vergi ve genel toplamı hesaplayarak bir fatura çalışma sayfası oluşturur. Kalın başlıklar, fiyatlar için para birimi formatı, kenarlıklar ve sütun genişlikleri gibi biçimlendirme `Style` ve `Font` nesneleri kullanılarak uygulanır. Son olarak, çalışma kitabı `SaveFormat.Ofd` kullanılarak `.ofd` uzantısıyla kaydedilir.

```cpp
// Aspose.Cells for C++ örneği
// Aspose.Cells 26.6.0 (veya üstü) ve C++17 (veya üstü) derleyici ile derleyin

#include "Aspose.Cells.h"
#include <string>
#include <ctime>

using namespace Aspose::Cells;

int main()
{
    // Aspose.Cells'i başlat
    Aspose::Cells::Startup();

    // Kaynaklar ve çıktı için dizin
    const char16_t* dataDir = u"C:\\Temp\\";

    // Yeni bir çalışma kitabı oluştur
    Workbook workbook;

    // İlk çalışma sayfasını al
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Sütun genişliklerini ayarla
    cells.SetColumnWidth(0, 5.0);
    cells.SetColumnWidth(1, 35.0);
    cells.SetColumnWidth(2, 12.0);
    cells.SetColumnWidth(3, 15.0);
    cells.SetColumnWidth(4, 15.0);
    cells.SetColumnWidth(5, 5.0);

    // Şirket logosunu ekle
    worksheet.GetPictures().Add(1, 1, U16String(dataDir) + u"logo.png");

    // Şirket adı ve iletişim bilgileri
    cells.Get(u"B3").PutValue(u"Acme Corporation");
    cells.Get(u"B4").PutValue(u"123 Business Street");
    cells.Get(u"B5").PutValue(u"City, State 12345");
    cells.Get(u"B6").PutValue(u"Phone: (555) 123-4567");

    // INVOICE başlığı - hücreleri birleştir
    cells.Merge(7, 1, 2, 4);
    Cell titleCell = cells.Get(u"B8");
    titleCell.PutValue(u"INVOICE");

    Style titleStyle = workbook.CreateStyle();
    titleStyle.GetFont().SetIsBold(true);
    titleStyle.GetFont().SetSize(20);
    titleStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    titleCell.SetStyle(titleStyle);

    // Fatura numarası ve tarih
    cells.Get(u"B11").PutValue(u"Invoice Number:");
    cells.Get(u"C11").PutValue(u"INV-2024-001");
    cells.Get(u"B12").PutValue(u"Date:");

    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char dateBuffer[11];
    std::strftime(dateBuffer, sizeof(dateBuffer), "%Y-%m-%d", now);
    cells.Get(u"C12").PutValue(U16String(dateBuffer));

    // Fatura alıcısı bölümü
    cells.Get(u"B14").PutValue(u"Bill To:");
    cells.Get(u"B15").PutValue(u"Client Name");
    cells.Get(u"B16").PutValue(u"Client Address");
    cells.Get(u"B17").PutValue(u"Client City, State");

    // Kalem başlıkları
    Cell headerDesc = cells.Get(u"B19");
    Cell headerQty = cells.Get(u"C19");
    Cell headerPrice = cells.Get(u"D19");
    Cell headerTotal = cells.Get(u"E19");

    headerDesc.PutValue(u"Description");
    headerQty.PutValue(u"Quantity");
    headerPrice.PutValue(u"Unit Price");
    headerTotal.PutValue(u"Total");

    Style headerStyle = workbook.CreateStyle();
    headerStyle.GetFont().SetIsBold(true);
    headerStyle.GetFont().SetColor(Color::White());
    headerStyle.SetForegroundColor(Color{0, 0, 128});
    headerStyle.SetPattern(BackgroundType::Solid);
    headerStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    headerStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    headerDesc.SetStyle(headerStyle);
    headerQty.SetStyle(headerStyle);
    headerPrice.SetStyle(headerStyle);
    headerTotal.SetStyle(headerStyle);

    // Kenarlıklı para birimi stili
    Style currencyStyle = workbook.CreateStyle();
    currencyStyle.SetCustom(u"\"$\"#,##0.00");
    currencyStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // Açıklama/miktar hücreleri için düz kenarlık stili
    Style borderStyle = workbook.CreateStyle();
    borderStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // Kalem satırları
    struct LineItem { const char16_t* desc; int qty; double price; };
    LineItem lineItems[] = {
        {u"Product A - Widget", 2, 50.00},
        {u"Product B - Gadget", 3, 75.00},
        {u"Product C - Service", 1, 100.00}
    };

    for (int i = 0; i < 3; i++)
    {
        int row = 20 + i;
        Cell descCell = cells.Get(row, 1);
        Cell qtyCell = cells.Get(row, 2);
        Cell priceCell = cells.Get(row, 3);
        Cell totalCell = cells.Get(row, 4);

        descCell.PutValue(lineItems[i].desc);
        qtyCell.PutValue(lineItems[i].qty);
        priceCell.PutValue(lineItems[i].price);

        std::string formula = "C" + std::to_string(row) + "*D" + std::to_string(row);
        totalCell.SetFormula(U16String(formula.c_str()));

        descCell.SetStyle(borderStyle);
        qtyCell.SetStyle(borderStyle);
        priceCell.SetStyle(currencyStyle);
        totalCell.SetStyle(currencyStyle);
    }

    // Ara toplam, vergi, genel toplam
    cells.Get(u"B24").PutValue(u"Subtotal:");
    Cell subtotalCell = cells.Get(u"E24");
    subtotalCell.SetFormula(u"SUM(E20:E22)");

    cells.Get(u"B25").PutValue(u"Tax (10%):");
    Cell taxCell = cells.Get(u"E25");
    taxCell.SetFormula(u"E24*0.1");

    cells.Get(u"B26").PutValue(u"Grand Total:");
    Cell grandTotalCell = cells.Get(u"E26");
    grandTotalCell.SetFormula(u"E24+E25");

    // Toplam değerler için kalın + para birimi stili
    Style totalStyle = workbook.CreateStyle();
    totalStyle.GetFont().SetIsBold(true);
    totalStyle.SetCustom(u"\"$\"#,##0.00");

    subtotalCell.SetStyle(totalStyle);
    taxCell.SetStyle(totalStyle);
    grandTotalCell.SetStyle(totalStyle);

    // Toplam etiketleri için kalın stil
    Style boldStyle = workbook.CreateStyle();
    boldStyle.GetFont().SetIsBold(true);

    cells.Get(u"B24").SetStyle(boldStyle);
    cells.Get(u"B25").SetStyle(boldStyle);
    cells.Get(u"B26").SetStyle(boldStyle);

    // Çalışma kitabını OFD dosyası olarak kaydet
    workbook.Save(U16String(dataDir) + u"Invoice.ofd", SaveFormat::Ofd);

    // Aspose.Cells kaynaklarını temizle
    Aspose::Cells::Cleanup();

    return 0;
}
```
## **Mevcut Bir Excel Dosyasını OFD'ye Dönüştürme**
Aspose.Cells ayrıca diskteki mevcut bir Excel çalışma kitabını yükleyebilir ve doğrudan OFD formatına aktarabilir. Bu, toplu dönüşüm hatları, arşivleme iş akışları ve kaynak çalışma kitabının başka bir araç tarafından üretildiği ve yalnızca sabit düzenli bir yapıt olarak yeniden yayınlanması gereken senaryolar için kullanışlıdır. Aşağıdaki örnek, mevcut bir `.xlsx` çalışma kitabını yükler, hücrelerinden veri okur, isteğe bağlı sayfa yapısı ayarlamaları uygular ve sonucu bir OFD belgesi olarak kaydeder.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <iostream>
#include <ctime>

using namespace Aspose::Cells;

std::string GetCurrentTimestamp() {
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char buffer[20];
    std::strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", now);
    return std::string(buffer);
}

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "C:\\Examples\\";

    // Mevcut bir Excel çalışma kitabını diskten aç
    Workbook workbook(U16String((dataDir + "SampleBook.xlsx").c_str()));

    // (1) Dosyanın yüklendiğini doğrulamak için seçili hücrelerdeki değerleri oku ve görüntüle
    Worksheet firstSheet = workbook.GetWorksheets().Get(0);
    U16String sheetName = firstSheet.GetName();
    Cell a1 = firstSheet.GetCells().Get(u"A1");
    Cell b1 = firstSheet.GetCells().Get(u"B1");
    Cell c1 = firstSheet.GetCells().Get(u"C1");

    std::cout << "First sheet name: " << sheetName.ToUtf8() << std::endl;
    std::cout << "Cell A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell B1: " << b1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell C1: " << c1.GetStringValue().ToUtf8() << std::endl;

    // (2) Mevcut sayfaları listelemek için Worksheets koleksiyonu üzerinde yineleme yap
    std::cout << "\nAvailable worksheets:" << std::endl;
    WorksheetCollection sheets = workbook.GetWorksheets();
    int sheetCount = sheets.GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet ws = sheets.Get(i);
        U16String wsName = ws.GetName();
        std::cout << "  [" << i << "] " << wsName.ToUtf8() << std::endl;
    }

    // (3) Dönüşümü yansıtmak için isteğe bağlı olarak bir zaman damgası hücresini güncelle
    std::string timestamp1 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A1").PutValue(U16String(("Converted on: " + timestamp1).c_str()));

    // Veri bloğunun üstüne bir özet başlık satırı ekle
    firstSheet.GetCells().InsertRow(0);
    firstSheet.GetCells().Get(u"A1").PutValue(u"Conversion Summary");

    std::string timestamp2 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A2").PutValue(U16String(("Generated: " + timestamp2).c_str()));

    // (4) Çalışma sayfasında PageSetup özelliklerini yapılandır
    PageSetup pageSetup = firstSheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    pageSetup.SetFitToPagesTall(1);
    pageSetup.SetFitToPagesWide(1);

    // (5) OFD çıktısı için yazdırma alanını isteğe bağlı olarak ayarla
    int lastRow = firstSheet.GetCells().GetMaxDataRow();
    int lastCol = firstSheet.GetCells().GetMaxDataColumn();
    U16String lastColLetter = CellsHelper::ColumnIndexToName(lastCol);
    std::string printArea = "A1:" + lastColLetter.ToUtf8() + std::to_string(lastRow + 1);
    firstSheet.GetPageSetup().SetPrintArea(U16String(printArea.c_str()));
    std::cout << "\nPrint area set to: " << printArea << std::endl;

    // (6) Çalışma kitabını OFD dosyası olarak kaydet
    workbook.Save(U16String((dataDir + "SampleBook.ofd").c_str()), SaveFormat::Ofd);
    std::cout << "\nFile successfully converted to OFD format: " << dataDir << "SampleBook.ofd" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **İlgili Makaleler**
- [Excel Dosyalarını Birden Çok Dosyaya Bölme](/cells/tr/cpp/splitting-excel-files-into-multiple-files/)
- [Bir Hücreye Görüntü Ekleme](/cells/tr/cpp/inserting-an-image-into-a-cell/)
- [DBF Dosyalarını Okuma ve Yazma](/cells/tr/cpp/dbf/)
- [Aspose.Cells for C++'da Mini Grafiği Görüntüye ve HTML'ye Dönüştürme](/cells/tr/cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="cpp" >}}