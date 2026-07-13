---
title: Excel'i OFD Formatına Dönüştürme
linktitle: Excel'i OFD Formatına Dönüştürme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmaya uygun, Excel çalışma kitaplarını OFD (Open Fixed-layout Document) formatına dönüştürmeyi destekleyen bir Java kütüphanesidir. Bu makale, Aspose.Cells kullanarak Excel içeriği oluşturmayı ve OFD olarak dışa aktarmayı, ayrıca mevcut Excel dosyalarını OFD'ye dönüştürmeyi göstermektedir.
keywords: Aspose.Cells, Java kütüphanesi, elektronik tablo, Excel'den OFD'ye, OFD dönüşümü, SaveFormat.Ofd, sabit düzenli belge, çalışma kitabı dışa aktarma
type: docs
weight: 195
url: /tr/java/converting-excel-to-ofd-format/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, Excel çalışma kitaplarını doğrudan OFD (Open Fixed-layout Document) formatına dönüştürmeyi `SaveFormat.Ofd` numaralandırma değerini kullanarak destekler. Elde edilen OFD belgesi, çalışma kitabının görünür düzenini, içeriğini, birleştirilmiş hücrelerini, sütun genişliklerini, satır yüksekliklerini, yazı tiplerini, renklerini, kenarlıklarını ve sayı formatlarını korur. Bu, Aspose.Cells'i arşivleme, yazdırma, düzenleyici dosyalama ve sabit düzenli çıktı gerektiren hükümet başvuru iş akışları için uygun hale getirir.

{{% /alert %}}
## **Giriş**
OFD (Open Fixed-layout Document), dijital belgeleri sabit, sayfa tabanlı bir düzende temsil etmek için kullanılan bir Çin ulusal standardıdır (GB/T 33190-2016). Kaynak belgenin görsel görünümünün tam olarak yazıldığı şekliyle korunması gereken kullanım durumları için PDF'ye benzer bir rol üstlenir. OFD, Çin Halk Cumhuriyeti'nde hükümet başvuruları, düzenleyici dosyalamalar, elektronik faturalar ve uzun süreli arşivleme için yaygın olarak benimsenmiştir.

Excel çalışma kitaplarını OFD'ye dönüştürmek, elektronik tablo içeriğinin düzenlenebilir bir elektronik tablo olarak değil, salt okunur, düzeni kilitli bir yapı olarak dağıtılması gereken senaryolarda yaygın bir gereksinimdir. Örnekler arasında son hali verilmiş bir faturanın müşteriye gönderilmesi, üç aylık bir finansal raporun arşivlenmesi veya bütçe elektronik tablosunun düzenleyici bir makama sunulması yer alır. Aspose.Cells bu gereksinimi, çalışma kitabını ara bir dönüşüm adımı gerektirmeden doğrudan OFD'ye yazan `SaveFormat.Ofd` numaralandırma değeri aracılığıyla karşılar. OFD çıktısı, hücre değerlerini, birleştirilmiş aralıkları, yazı tiplerini, renkleri, kenarlıkları, sayı formatlarını ve çalışma kitabında yapılandırılan sayfa yapısı seçeneklerini korur.

{{% alert color="primary" %}}

Aspose.Cells tarafından oluşturulan OFD çıktısı, kaynak çalışma kitabının görünür düzenini, hücre içeriğini, birleştirilmiş hücreleri, sütun genişliklerini ve satır yüksekliklerini dahil olmak üzere korur. Yazı tipleri, renkler, kenarlıklar, hizalama ve sayı formatları gibi hücre biçimlendirmeleri de sabit düzenli çıktıda işlenir. Çalışma sayfasında yapılandırılan kağıt boyutu, yönlendirme ve yazdırma alanı gibi sayfa yapısı seçenekleri, ortaya çıkan OFD belgesinin düzenini etkiler.

{{% /alert %}}
## **Excel Çalışma Kitabı Oluşturma ve OFD Olarak Kaydetme**
Aspose.Cells, bir çalışma kitabını programlı olarak oluşturmanıza, verilerle doldurmanıza ve ardından `SaveFormat.Ofd` numaralandırmasını kullanarak doğrudan OFD formatında kaydetmenize olanak tanır. Aşağıdaki örnek sıfırdan bir fatura oluşturur. Bir şirket logosu, başlık bilgileri, fatura kime bölümü, kalem satırları ve hesaplanmış toplamlar ekler, ardından çalışma kitabını bir OFD belgesi olarak dışa aktarır.
### **Logolu Bir Fatura Oluşturma**
Örnek, sol üst köşeye bir logo görseli ekleyerek, şirket adı ve iletişim bilgilerini doldurarak, birleştirilmiş hücreler arasına bir "FATURA" başlığı ekleyerek, fatura numarasını ve tarihini kaydederek, fatura alıcı müşterisini listeleyerek, açıklama, miktar, birim fiyat ve toplam sütunlarıyla bir kalem satırları tablosu oluşturarak ve hücre formülleri kullanarak alt toplam, vergi ve genel toplamı hesaplayarak bir fatura çalışma sayfası oluşturur. Kalın başlıklar, fiyatlar için para birimi formatı, kenarlıklar ve sütun genişlikleri gibi biçimlendirmeler `Style` ve `Font` nesneleri kullanılarak uygulanır. Son olarak, çalışma kitabı `SaveFormat.Ofd` kullanılarak `.ofd` uzantısıyla kaydedilir.

```java
import com.aspose.cells.*;
import java.text.SimpleDateFormat;
import java.util.Date;

String dataDir = "C:\\Temp\\";

// Yeni bir Çalışma Kitabı oluştur
Workbook workbook = new Workbook();

// İlk çalışma sayfasını al
Worksheet worksheet = workbook.getWorksheets().get(0);

// Sütun genişliklerini ayarla
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);

// Şirket logosunu ekle
worksheet.getPictures().add(1, 1, dataDir + "logo.png");

// Şirket adı ve iletişim bilgileri
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");

// FATURA başlığı - hücreleri birleştir
worksheet.getCells().merge(7, 1, 2, 4);
Cell titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

Style titleStyle = workbook.createStyle();
titleStyle.getFont().setBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);

// Fatura numarası ve tarih
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new SimpleDateFormat("yyyy-MM-dd").format(new Date()));

// Fatura kime bölümü
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// Satır öğeleri başlığı
Cell headerDesc = worksheet.getCells().get("B19");
Cell headerQty = worksheet.getCells().get("C19");
Cell headerPrice = worksheet.getCells().get("D19");
Cell headerTotal = worksheet.getCells().get("E19");

headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");

Style headerStyle = workbook.createStyle();
headerStyle.getFont().setBold(true);
headerStyle.getFont().setColor(Color.getWhite());
headerStyle.setBackgroundColor(Color.getNavy());
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
headerStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Kenarlıklı para birimi stili
Style currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

// Açıklama/miktar hücreleri için düz kenarlık stili
Style borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

// Satır öğeleri satırları
Object[][] lineItems = new Object[][] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};

for (int i = 0; i < lineItems.length; i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.getCells().get(row, 1);
    Cell qtyCell = worksheet.getCells().get(row, 2);
    Cell priceCell = worksheet.getCells().get(row, 3);
    Cell totalCell = worksheet.getCells().get(row, 4);

    descCell.putValue(lineItems[i][0]);
    qtyCell.putValue(lineItems[i][1]);
    priceCell.putValue(lineItems[i][2]);
    totalCell.setFormula("C" + row + "*D" + row);

    descCell.setStyle(borderStyle);
    qtyCell.setStyle(borderStyle);
    priceCell.setStyle(currencyStyle);
    totalCell.setStyle(currencyStyle);
}

// Ara toplam, vergi, genel toplam
worksheet.getCells().get("B24").putValue("Subtotal:");
Cell subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
Cell taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
Cell grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// Toplam değerler için kalın + para birimi stili
Style totalStyle = workbook.createStyle();
totalStyle.getFont().setBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// Toplam etiketleri için kalın stil
Style boldStyle = workbook.createStyle();
boldStyle.getFont().setBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// Çalışma kitabını OFD dosyası olarak kaydet
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```
## **Mevcut Bir Excel Dosyasını OFD'ye Dönüştürme**
Aspose.Cells ayrıca disk üzerindeki mevcut bir Excel çalışma kitabını yükleyebilir ve doğrudan OFD formatında dışa aktarabilir. Bu, toplu dönüştürme işlem hatları, arşivleme iş akışları ve kaynak çalışma kitabının başka bir araç tarafından üretildiği ve yalnızca sabit düzenli bir yapı olarak yeniden yayınlanması gereken senaryolar için kullanışlıdır. Aşağıdaki örnek, mevcut bir `.xlsx` çalışma kitabını yükler, hücrelerinden veri okur, isteğe bağlı sayfa yapısı ayarlamaları uygular ve sonucu bir OFD belgesi olarak kaydeder.

```java
import com.aspose.cells.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

String dataDir = "C:\\Examples\\";

// Diskten mevcut bir Excel çalışma kitabı aç
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");

// (1) Dosyanın yüklendiğini doğrulamak için seçili hücrelerden değerleri oku ve görüntüle
Worksheet firstSheet = workbook.getWorksheets().get(0);
System.out.println("First sheet name: " + firstSheet.getName());
System.out.println("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
System.out.println("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
System.out.println("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Mevcut sayfaları listelemek için Worksheets koleksiyonu üzerinde yineleme yap
System.out.println("\nAvailable worksheets:");
for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet ws = workbook.getWorksheets().get(i);
    System.out.println("  [" + i + "] " + ws.getName());
}

// (3) Dönüşümü yansıtmak için isteğe bağlı olarak bir zaman damgası hücresini güncelle
String timestamp1 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A1").putValue("Converted on: " + timestamp1);

// Veri bloğunun en üstüne bir özet başlık satırı ekle
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");

String timestamp2 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A2").putValue("Generated: " + timestamp2);

// (4) Sayfadaki PageSetup özelliklerini yapılandır
PageSetup pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(PageOrientationType.LANDSCAPE);
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) OFD çıktısı için isteğe bağlı olarak yazdırma alanını ayarla
int lastRow = firstSheet.getCells().getMaxDataRow();
int lastCol = firstSheet.getCells().getMaxDataColumn();
String lastColLetter = CellsHelper.columnIndexToName(lastCol);
String printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
System.out.println("\nPrint area set to: " + printArea);

// (6) Çalışma kitabını OFD dosyası olarak kaydet
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
System.out.println("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **İlgili Makaleler**
- [Excel Dosyalarını Birden Çok Dosyaya Bölme](/cells/tr/java/splitting-excel-files-into-multiple-files/)
- [Bir Hücreye Görsel Ekleme](/cells/tr/java/inserting-an-image-into-a-cell/)
- [DBF Dosyalarını Okuma ve Yazma](/cells/tr/java/dbf/)
- [Aspose.Cells for Java'da Sparkline'ı Görsel ve HTML'ye Dönüştürme](/cells/tr/java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="java" >}}