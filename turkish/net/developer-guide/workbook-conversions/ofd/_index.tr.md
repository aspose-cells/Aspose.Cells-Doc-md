---
title: Excel'i OFD Biçimine Dönüştürme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışan ve Excel çalışma kitaplarını OFD (Açık Sabit Düzen Belgesi) biçimine dönüştürmeyi destekleyen bir .NET kitaplığıdır. Bu makale, Aspose.Cells kullanarak Excel içeriğinin nasıl oluşturulacağını ve OFD olarak dışa aktarılacağını ve mevcut Excel dosyalarının OFD biçimine nasıl dönüştürüleceğini gösterir.
linktitle: OFD
keywords: Aspose.Cells, .NET kitaplığı, elektronik tablo, Excel'den OFD'ye, OFD dönüşümü, SaveFormat.Ofd, sabit düzenli belge, çalışma kitabı dışa aktarma
type: docs
weight: 195
url: /tr/net/converting-excel-to-ofd-format/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, `SaveFormat.Ofd` numaralandırma değerini kullanarak Excel çalışma kitaplarını doğrudan OFD (Açık Sabit Düzen Belgesi) biçimine dönüştürmeyi destekler. Elde edilen OFD belgesi; çalışma kitabının görünür düzenini, içeriğini, birleştirilmiş hücrelerini, sütun genişliklerini, satır yüksekliklerini, yazı tiplerini, renklerini, kenarlıklarını ve sayı biçimlerini korur. Bu durum, Aspose.Cells'i sabit düzenli çıktı gerektiren arşivleme, yazdırma, mevzuata uygun dosya sunma ve kamu makamlarına gönderim iş akışları için uygun hâle getirir.

## **Giriş**
OFD (Açık Sabit Düzen Belgesi), dijital belgeleri sabit ve sayfa tabanlı bir düzende temsil etmeye yönelik Çin ulusal standardıdır (GB/T 33190-2016). Kaynak belgenin görsel görünümünün hazırlandığı biçimiyle tam olarak korunması gereken kullanım senaryolarında PDF'ye benzer bir rol üstlenir. OFD, Çin Halk Cumhuriyeti'nde kamu kurumlarına sunum, mevzuata uygun dosya sunma, elektronik faturalar ve uzun süreli arşivleme amacıyla yaygın olarak kullanılmaktadır.
Excel çalışma kitaplarını OFD biçimine dönüştürme; elektronik tablo içeriğinin düzenlenebilir bir elektronik tablo olarak değil, salt okunur ve düzeni kilitli bir çıktı olarak dağıtılması gereken senaryolarda sık karşılaşılan bir gereksinimdir. Örnekler arasında tamamlanmış bir faturanın müşteriye gönderilmesi, üç aylık finansal raporun arşivlenmesi veya bütçe elektronik tablosunun düzenleyici bir makama sunulması yer alır. Aspose.Cells bu gereksinimi, çalışma kitabını ara bir dönüştürme adımı gerektirmeden doğrudan OFD biçimine yazan `SaveFormat.Ofd` numaralandırma değeriyle karşılar. OFD çıktısı; hücre değerlerini, birleştirilmiş hücre aralıklarını, yazı tiplerini, renkleri, kenarlıkları, sayı biçimlerini ve çalışma kitabında yapılandırılan sayfa yapısı seçeneklerini korur.

{{% alert color="primary" %}}
Aspose.Cells tarafından oluşturulan OFD çıktısı, hücre içeriği, birleştirilmiş hücreler, sütun genişlikleri ve satır yükseklikleri dahil olmak üzere kaynak çalışma kitabının görünür düzenini korur. Yazı tipleri, renkler, kenarlıklar, hizalama ve sayı biçimleri gibi hücre biçimlendirmeleri de sabit düzenli çıktıda korunur. Kağıt boyutu, yönlendirme ve yazdırma alanı gibi çalışma sayfasında yapılandırılan sayfa yapısı seçenekleri, elde edilen OFD belgesinin düzenini etkiler.

## **Excel Çalışma Kitabı Oluşturma ve OFD Olarak Kaydetme**
Aspose.Cells, programlı olarak bir çalışma kitabı oluşturmanıza, verilerle doldurmanıza ve ardından `SaveFormat.Ofd` numaralandırmasını kullanarak doğrudan OFD biçiminde kaydetmenize olanak tanır. Aşağıdaki örnek sıfırdan bir fatura oluşturur. Şirket logosu, üstbilgi bilgileri, fatura edilecek taraf bölümü, kalemler ve hesaplanan toplamlar ekledikten sonra çalışma kitabını OFD belgesi olarak dışa aktarır.

### **Logolu Fatura Oluşturma**
Örnek; sol üst bölüme bir logo görüntüsü ekleyerek, şirket adını ve iletişim bilgilerini girerek, birleştirilmiş hücrelerin genişliğine bir "FATURA" başlığı yerleştirerek, fatura numarasını ve tarihi kaydederek, fatura edilecek müşteriyi belirterek, açıklama, miktar, birim fiyat ve toplam sütunlarından oluşan bir kalemler tablosu oluşturarak ve hücre formüllerini kullanarak ara toplam, vergi ve genel toplamı hesaplayarak bir fatura çalışma sayfası oluşturur. Kalın üstbilgiler, fiyatlar için para birimi biçimi, kenarlıklar ve sütun genişlikleri gibi biçimlendirmeler `Style` ve `Font` nesneleri kullanılarak uygulanır. Son olarak çalışma kitabı, `SaveFormat.Ofd` kullanılarak `.ofd` uzantısıyla kaydedilir.

```csharp
using System;
using Aspose.Cells;
using System.Drawing;
string dataDir = "C:\\Temp\\";
// Yeni bir Workbook oluştur
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
// Şirket logosunu ekle
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
// Faturalanacak kişi bölümü
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
// Toplam değerler için kalın + para birimi stili
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
// Workbook'u OFD dosyası olarak kaydet
workbook.Save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```

## **Mevcut Bir Excel Dosyasını OFD Biçimine Dönüştürme**
Aspose.Cells, diskte bulunan mevcut bir Excel çalışma kitabını da yükleyebilir ve doğrudan OFD biçimine aktarabilir. Bu özellik; toplu dönüştürme hatları, arşivleme iş akışları ve kaynak çalışma kitabının başka bir araçla oluşturulduğu ve yalnızca sabit düzenli bir çıktı olarak yeniden oluşturulması gereken senaryolar için kullanışlıdır. Aşağıdaki örnek mevcut bir `.xlsx` çalışma kitabını yükler, hücrelerindeki verileri okur, isteğe bağlı sayfa yapısı ayarları uygular ve sonucu OFD belgesi olarak kaydeder.

```csharp
using System;
using Aspose.Cells;
string dataDir = "C:\\Examples\\";
// Disk üzerinden mevcut bir Excel çalışma kitabını aç
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");
// (1) Dosyanın yüklendiğini onaylamak için seçili hücrelerden değerleri oku ve görüntüle
Worksheet firstSheet = workbook.Worksheets[0];
Console.WriteLine("First sheet name: " + firstSheet.Name);
Console.WriteLine("Cell A1: " + firstSheet.Cells["A1"].StringValue);
Console.WriteLine("Cell B1: " + firstSheet.Cells["B1"].StringValue);
Console.WriteLine("Cell C1: " + firstSheet.Cells["C1"].StringValue);
// (2) Kullanılabilir sayfaları numaralandırmak için Worksheets koleksiyonu üzerinde yineleme yap
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
// (5) OFD çıktısı için yazdırma alanını isteğe bağlı olarak ayarla
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

{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}