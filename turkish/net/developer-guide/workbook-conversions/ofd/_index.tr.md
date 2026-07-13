---
title: Excel'i OFD Formatına Dönüştürme
linktitle: Excel'i OFD Formatına Dönüştürme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için Excel çalışma kitaplarını OFD (Open Fixed-layout Document) formatına dönüştürmeyi destekleyen bir .NET kütüphanesidir. Bu makale, Aspose.Cells kullanarak Excel içeriği oluşturmayı ve OFD olarak dışa aktarmayı, ayrıca mevcut Excel dosyalarını OFD'ye dönüştürmeyi gösterir.
keywords: Aspose.Cells, .NET kütüphanesi, elektronik tablo, Excel'den OFD'ye, OFD dönüşümü, SaveFormat.Ofd, sabit düzenli belge, çalışma kitabı dışa aktarma
type: docs
weight: 195
url: /tr/net/converting-excel-to-ofd-format/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, Excel çalışma kitaplarını doğrudan OFD (Open Fixed-layout Document) formatına dönüştürmeyi `SaveFormat.Ofd` numaralandırma değerini kullanarak destekler. Elde edilen OFD belgesi, çalışma kitabının görünür düzenini, içeriğini, birleştirilmiş hücrelerini, sütun genişliklerini, satır yüksekliklerini, yazı tiplerini, renklerini, kenarlıklarını ve sayı formatlarını korur. Bu, Aspose.Cells'i arşivleme, yazdırma, düzenleyici dosyalama ve sabit düzenli çıktı gerektiren hükümet başvuru iş akışları için uygun hale getirir.

{{% /alert %}}
## **Giriş**
OFD (Open Fixed-layout Document), dijital belgeleri sabit, sayfa tabanlı bir düzende temsil etmek için Çin ulusal standardıdır (GB/T 33190-2016). Kaynak belgenin görsel görünümünün tam olarak yazıldığı şekliyle korunması gereken kullanım durumlarında PDF'ye benzer bir rol oynar. OFD, Çin Halk Cumhuriyeti'nde hükümet başvuruları, düzenleyici dosyalamalar, elektronik faturalar ve uzun süreli arşivleme için yaygın olarak benimsenmiştir.

Excel çalışma kitaplarını OFD'ye dönüştürmek, elektronik tablo içeriğinin düzenlenebilir bir elektronik tablo olarak değil, salt okunur, düzeni kilitli bir eser olarak dağıtılması gereken senaryolarda yaygın bir gereksinimdir. Örnekler arasında, sonlandırılmış bir faturanın müşteriye gönderilmesi, üç aylık bir mali raporun arşivlenmesi veya bir bütçe elektronik tablosunun düzenleyici bir makama sunulması yer alır. Aspose.Cells bu gereksinimi, çalışma kitabını ara bir dönüşüm adımı gerektirmeden doğrudan OFD'ye yazan `SaveFormat.Ofd` numaralandırma değeri aracılığıyla ele alır. OFD çıktısı, hücre değerlerini, birleştirilmiş aralıkları, yazı tiplerini, renkleri, kenarlıkları, sayı formatlarını ve çalışma kitabı üzerinde yapılandırılan sayfa yapısı seçeneklerini korur.

{{% alert color="primary" %}}

Aspose.Cells tarafından oluşturulan OFD çıktısı, kaynak çalışma kitabının görünür düzenini korur; buna hücre içeriği, birleştirilmiş hücreler, sütun genişlikleri ve satır yükseklikleri dahildir. Yazı tipleri, renkler, kenarlıklar, hizalama ve sayı formatları gibi hücre biçimlendirmeleri de sabit düzenli çıktıda işlenir. Çalışma sayfası üzerinde yapılandırılan kağıt boyutu, yönlendirme ve yazdırma alanı gibi sayfa yapısı seçenekleri, ortaya çıkan OFD belgesinin düzenini etkiler.

{{% /alert %}}
## **Bir Excel Çalışma Kitabı Oluşturma ve OFD Olarak Kaydetme**
Aspose.Cells, bir çalışma kitabını programlı olarak oluşturmanıza, verilerle doldurmanıza ve ardından `SaveFormat.Ofd` numaralandırmasını kullanarak doğrudan OFD formatında kaydetmenize olanak tanır. Aşağıdaki örnek sıfırdan bir fatura oluşturur. Bir şirket logosu, başlık bilgileri, fatura kime bölümü, satır öğeleri ve hesaplanan toplamlar ekler, ardından çalışma kitabını bir OFD belgesi olarak dışa aktarır.
### **Logo İçeren Bir Fatura Oluşturma**
Örnek, sol üst alana bir logo görüntüsü ekleyerek, şirket adını ve iletişim bilgilerini doldurarak, birleştirilmiş hücreler arasına "FATURA" başlığı ekleyerek, fatura numarasını ve tarihini kaydederek, fatura kime müşterisini listeleyerek, açıklama, miktar, birim fiyat ve toplam sütunlarıyla bir satır öğeleri tablosu oluşturarak ve hücre formülleri kullanarak alt toplam, vergi ve genel toplamı hesaplayarak bir fatura çalışma sayfası oluşturur. Kalın başlıklar, fiyatlar için para birimi formatı, kenarlıklar ve sütun genişlikleri gibi biçimlendirmeler `Style` ve `Font` nesneleri kullanılarak uygulanır. Son olarak, çalışma kitabı `SaveFormat.Ofd` kullanılarak `.ofd` uzantısıyla kaydedilir.

```csharp
using System;
using Aspose.Cells;
using System.Drawing;

string dataDir = "C:\\Temp\\";

// Yeni bir Çalışma Kitabı oluştur
Workbook workbook = new Workbook();

// İlk çalışma sayfasını al
Worksheet worksheet = workbook.Worksheets[0];

// Sütun genişliklerini ayarla
worksheet.Cells.SetColumnWidth(0, 5);
worksheet.Cells.SetColumnWidth(1, 35);
worksheet.Cells.SetColumnWidth(2, 12);
worksheet.Cells.SetColumnWidth(3, 15);
worksheet.Cells.SetColumnWidth(4, 15);
worksheet.Cells.SetColumnWidth(5, 5);

// Şirket logosu ekle
worksheet.Pictures.Add(1, 1, dataDir + "logo.png");

// Şirket adı ve iletişim bilgileri
worksheet.Cells["B3"].PutValue("Acme Corporation");
worksheet.Cells["B4"].PutValue("123 Business Street");
worksheet.Cells["B5"].PutValue("City, State 12345");
worksheet.Cells["B6"].PutValue("Phone: (555) 123-4567");

// FATURA başlığı - hücreleri birleştir
worksheet.Cells.Merge(7, 1, 2, 4);
Cell titleCell = worksheet.Cells["B8"];
titleCell.PutValue("INVOICE");

Style titleStyle = workbook.CreateStyle();
titleStyle.Font.IsBold = true;
titleStyle.Font.Size = 20;
titleStyle.HorizontalAlignment = TextAlignmentType.Center;
titleCell.SetStyle(titleStyle);

// Fatura numarası ve tarih
worksheet.Cells["B11"].PutValue("Invoice Number:");
worksheet.Cells["C11"].PutValue("INV-2024-001");
worksheet.Cells["B12"].PutValue("Date:");
worksheet.Cells["C12"].PutValue(DateTime.Now.ToString("yyyy-MM-dd"));

// Fatura kime bölümü
worksheet.Cells["B14"].PutValue("Bill To:");
worksheet.Cells["B15"].PutValue("Client Name");
worksheet.Cells["B16"].PutValue("Client Address");
worksheet.Cells["B17"].PutValue("Client City, State");

// Kalem başlıkları
Cell headerDesc = worksheet.Cells["B19"];
Cell headerQty = worksheet.Cells["C19"];
Cell headerPrice = worksheet.Cells["D19"];
Cell headerTotal = worksheet.Cells["E19"];

headerDesc.PutValue("Description");
headerQty.PutValue("Quantity");
headerPrice.PutValue("Unit Price");
headerTotal.PutValue("Total");

Style headerStyle = workbook.CreateStyle();
headerStyle.Font.IsBold = true;
headerStyle.Font.Color = Color.White;
headerStyle.BackgroundColor = Color.Navy;
headerStyle.HorizontalAlignment = TextAlignmentType.Center;
headerStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

headerDesc.SetStyle(headerStyle);
headerQty.SetStyle(headerStyle);
headerPrice.SetStyle(headerStyle);
headerTotal.SetStyle(headerStyle);

// Kenarlıklı para birimi stili
Style currencyStyle = workbook.CreateStyle();
currencyStyle.Custom = "\"$\"#,##0.00";
currencyStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// Açıklama/miktar hücreleri için düz kenarlık stili
Style borderStyle = workbook.CreateStyle();
borderStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// Kalem satırları
object[,] lineItems = new object[,] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};

for (int i = 0; i < lineItems.GetLength(0); i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.Cells[row, 1];
    Cell qtyCell = worksheet.Cells[row, 2];
    Cell priceCell = worksheet.Cells[row, 3];
    Cell totalCell = worksheet.Cells[row, 4];

    descCell.PutValue(lineItems[i, 0]);
    qtyCell.PutValue(lineItems[i, 1]);
    priceCell.PutValue(lineItems[i, 2]);
    totalCell.Formula = "C" + row + "*D" + row;

    descCell.SetStyle(borderStyle);
    qtyCell.SetStyle(borderStyle);
    priceCell.SetStyle(currencyStyle);
    totalCell.SetStyle(currencyStyle);
}

// Ara toplam, vergi, genel toplam
worksheet.Cells["B24"].PutValue("Subtotal:");
Cell subtotalCell = worksheet.Cells["E24"];
subtotalCell.Formula = "SUM(E20:E22)";

worksheet.Cells["B25"].PutValue("Tax (10%):");
Cell taxCell = worksheet.Cells["E25"];
taxCell.Formula = "E24*0.1";

worksheet.Cells["B26"].PutValue("Grand Total:");
Cell grandTotalCell = worksheet.Cells["E26"];
grandTotalCell.Formula = "E24+E25";

// Toplam değerleri için kalın + para birimi stili
Style totalStyle = workbook.CreateStyle();
totalStyle.Font.IsBold = true;
totalStyle.Custom = "\"$\"#,##0.00";

subtotalCell.SetStyle(totalStyle);
taxCell.SetStyle(totalStyle);
grandTotalCell.SetStyle(totalStyle);

// Toplam etiketleri için kalın stil
Style boldStyle = workbook.CreateStyle();
boldStyle.Font.IsBold = true;

worksheet.Cells["B24"].SetStyle(boldStyle);
worksheet.Cells["B25"].SetStyle(boldStyle);
worksheet.Cells["B26"].SetStyle(boldStyle);

// Çalışma kitabını OFD dosyası olarak kaydet
workbook.Save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```
## **Mevcut Bir Excel Dosyasını OFD'ye Dönüştürme**
Aspose.Cells ayrıca diskteki mevcut bir Excel çalışma kitabını da yükleyebilir ve doğrudan OFD formatına dışa aktarabilir. Bu, toplu dönüşüm işlem hatları, arşivleme iş akışları ve kaynak çalışma kitabının başka bir araç tarafından üretildiği ve yalnızca sabit düzenli bir eser olarak yeniden yayınlanması gereken senaryolar için kullanışlıdır. Aşağıdaki örnek, mevcut bir `.xlsx` çalışma kitabını yükler, hücrelerinden veri okur, isteğe bağlı sayfa yapısı ayarlamaları uygular ve sonucu bir OFD belgesi olarak kaydeder.

```csharp
using System;
using Aspose.Cells;

string dataDir = "C:\\Examples\\";

// Diskteki mevcut bir Excel çalışma kitabını aç
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");

// (1) Dosyanın yüklendiğini doğrulamak için seçili hücrelerdeki değerleri oku ve görüntüle
Worksheet firstSheet = workbook.Worksheets[0];
Console.WriteLine("First sheet name: " + firstSheet.Name);
Console.WriteLine("Cell A1: " + firstSheet.Cells["A1"].StringValue);
Console.WriteLine("Cell B1: " + firstSheet.Cells["B1"].StringValue);
Console.WriteLine("Cell C1: " + firstSheet.Cells["C1"].StringValue);

// (2) Mevcut sayfaları listelemek için Worksheets koleksiyonu üzerinde yineleme yap
Console.WriteLine("\nAvailable worksheets:");
for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet ws = workbook.Worksheets[i];
    Console.WriteLine("  [" + i + "] " + ws.Name);
}

// (3) Dönüşümü yansıtmak için isteğe bağlı olarak bir zaman damgası hücresini güncelle
firstSheet.Cells["A1"].PutValue("Converted on: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// Veri bloğunun üstüne bir özet başlık satırı ekle
firstSheet.Cells.InsertRow(0);
firstSheet.Cells["A1"].PutValue("Conversion Summary");
firstSheet.Cells["A2"].PutValue("Generated: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// (4) Çalışma sayfasında PageSetup özelliklerini yapılandır
PageSetup pageSetup = firstSheet.PageSetup;
pageSetup.Orientation = PageOrientationType.Landscape;
pageSetup.PaperSize = PaperSizeType.PaperA4;
pageSetup.FitToPagesTall = 1;
pageSetup.FitToPagesWide = 1;

// (5) OFD çıktısı için isteğe bağlı olarak yazdırma alanını ayarla
int lastRow = firstSheet.Cells.MaxDataRow;
int lastCol = firstSheet.Cells.MaxDataColumn;
string lastColLetter = CellsHelper.ColumnIndexToName(lastCol);
string printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.PageSetup.PrintArea = printArea;
Console.WriteLine("\nPrint area set to: " + printArea);

// (6) Çalışma kitabını OFD dosyası olarak kaydet
workbook.Save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
Console.WriteLine("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **İlgili Makaleler**
- [Excel Dosyalarını Birden Fazla Dosyaya Bölme](/cells/tr/net/splitting-excel-files-into-multiple-files/)
- [Bir Hücreye Görüntü Ekleme](/cells/tr/net/inserting-an-image-into-a-cell/)
- [DBF Dosyalarını Okuma ve Yazma](/cells/tr/net/dbf/)
- [Aspose.Cells for .NET'te Sparkline'ı Görüntüye ve HTML'ye Dönüştürme](/cells/tr/net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="csharp" >}}