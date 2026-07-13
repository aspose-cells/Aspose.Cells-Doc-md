---
title: Excel'i OFD Formatına Dönüştürme
linktitle: Excel'i OFD Formatına Dönüştürme
description: Aspose.Cells for Node.js via Java, elektronik tablo dosyalarıyla çalışmak için Excel çalışma kitaplarını OFD (Open Fixed-layout Document) formatına dönüştürmeyi destekleyen bir elektronik tablo kütüphanesidir. Bu makale, Aspose.Cells kullanarak Excel içeriği oluşturmayı ve OFD olarak dışa aktarmayı, ayrıca mevcut Excel dosyalarını OFD'ye dönüştürmeyi göstermektedir.
keywords: Aspose.Cells, Node.js via Java kütüphanesi, elektronik tablo, Excel'den OFD'ye, OFD dönüşümü, SaveFormat.Ofd, sabit düzenli belge, çalışma kitabı dışa aktarma
type: docs
weight: 195
url: /tr/nodejs-java/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, `SaveFormat.Ofd` numaralandırma değerini kullanarak Excel çalışma kitaplarını doğrudan OFD (Open Fixed-layout Document) formatına dönüştürmeyi destekler. Elde edilen OFD belgesi, çalışma kitabının görünür düzenini, içeriğini, birleştirilmiş hücrelerini, sütun genişliklerini, satır yüksekliklerini, yazı tiplerini, renklerini, kenarlıklarını ve sayı formatlarını korur. Bu, Aspose.Cells'i sabit düzenli çıktı gerektiren arşivleme, yazdırma, düzenleyici dosyalama ve hükümet sunumu iş akışları için uygun hale getirir.

{{% /alert %}}
## **Giriş**
OFD (Open Fixed-layout Document), dijital belgeleri sabit, sayfa tabanlı bir düzende temsil etmek için Çin ulusal standardıdır (GB/T 33190-2016). Kaynak belgenin görsel görünümünün tam olarak yazıldığı şekilde korunması gereken kullanım durumlarında PDF'ye benzer bir rol üstlenir. OFD, Çin Halk Cumhuriyeti'nde hükümet sunumları, düzenleyici dosyalamalar, elektronik faturalar ve uzun süreli arşivleme için yaygın olarak benimsenmiştir.

Excel çalışma kitaplarını OFD'ye dönüştürmek, elektronik tablo içeriğinin düzenlenebilir bir elektronik tablo olarak değil, salt okunur, düzeni kilitli bir yapıt olarak dağıtılması gereken senaryolarda yaygın bir gereksinimdir. Örnekler arasında sonlandırılmış bir faturanın müşteriye gönderilmesi, üç aylık bir mali raporun arşivlenmesi veya bütçe elektronik tablosunun düzenleyici bir makama sunulması yer alır. Aspose.Cells bu gereksinimi, çalışma kitabını ara bir dönüşüm adımı gerektirmeden doğrudan OFD'ye yazan `SaveFormat.Ofd` numaralandırma değeri aracılığıyla ele alır. OFD çıktısı, hücre değerlerini, birleştirilmiş aralıkları, yazı tiplerini, renkleri, kenarlıkları, sayı formatlarını ve çalışma kitabında yapılandırılan sayfa yapısı seçeneklerini korur.

{{% alert color="primary" %}}

Aspose.Cells tarafından oluşturulan OFD çıktısı, kaynak çalışma kitabının görünür düzenini, hücre içeriği, birleştirilmiş hücreler, sütun genişlikleri ve satır yükseklikleri dahil olmak üzere korur. Yazı tipleri, renkler, kenarlıklar, hizalama ve sayı formatları gibi hücre biçimlendirmesi de sabit düzenli çıktıda işlenir. Çalışma sayfasında yapılandırılan kağıt boyutu, yönlendirme ve yazdırma alanı gibi sayfa yapısı seçenekleri, ortaya çıkan OFD belgesinin düzenini etkiler.

{{% /alert %}}
## **Excel Çalışma Kitabı Oluşturma ve OFD Olarak Kaydetme**
Aspose.Cells, bir çalışma kitabını programatik olarak oluşturmanıza, verilerle doldurmanıza ve ardından `SaveFormat.Ofd` numaralandırmasını kullanarak doğrudan OFD formatında kaydetmenize olanak tanır. Aşağıdaki örnek sıfırdan bir fatura oluşturur. Bir şirket logosu, başlık bilgileri, fatura alıcısı bölümü, kalem satırları ve hesaplanan toplamlar ekler, ardından çalışma kitabını bir OFD belgesi olarak dışa aktarır.
### **Logo İçeren Bir Fatura Oluşturma**
Örnek, sol üst alana bir logo görüntüsü ekleyerek, şirket adı ve iletişim bilgilerini doldurarak, birleştirilmiş hücreler arasına bir "FATURA" başlığı ekleyerek, fatura numarasını ve tarihini kaydederek, fatura alıcısı müşterisini listeleyerek, açıklama, miktar, birim fiyat ve toplam sütunlarıyla bir kalem satırları tablosu oluşturarak ve hücre formülleri kullanarak ara toplam, vergi ve genel toplamı hesaplayarak bir fatura çalışma sayfası oluşturur. Kalın başlıklar, fiyatlar için para birimi formatı, kenarlıklar ve sütun genişlikleri gibi biçimlendirmeler `Style` ve `Font` nesneleri kullanılarak uygulanır. Son olarak, çalışma kitabı `SaveFormat.Ofd` kullanılarak `.ofd` uzantısıyla kaydedilir.

```javascript
let dataDir = "C:\\Temp\\";

// Yeni bir Çalışma Kitabı oluştur
let workbook = new AsposeCells.Workbook();

// İlk çalışma sayfasını al
let worksheet = workbook.getWorksheets().get(0);

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
let titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

let titleStyle = workbook.createStyle();
titleStyle.getFont().setIsBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);

// Fatura numarası ve tarihi
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new Date().toISOString().slice(0, 10));

// Faturalanacak kişi bölümü
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// Kalem başlıkları
let headerDesc = worksheet.getCells().get("B19");
let headerQty = worksheet.getCells().get("C19");
let headerPrice = worksheet.getCells().get("D19");
let headerTotal = worksheet.getCells().get("E19");

headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");

let headerStyle = workbook.createStyle();
headerStyle.getFont().setIsBold(true);
headerStyle.getFont().setColor(AsposeCells.Color.getWhite());
headerStyle.setBackgroundColor(AsposeCells.Color.getNavy());
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.CENTER);
headerStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Kenarlıklı para birimi stili
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

// Açıklama/miktar hücreleri için düz kenarlık stili
let borderStyle = workbook.createStyle();
borderStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

// Kalem satırları
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];

for (let i = 0; i < lineItems.length; i++)
{
    let row = 20 + i;
    let descCell = worksheet.getCells().get(row, 1);
    let qtyCell = worksheet.getCells().get(row, 2);
    let priceCell = worksheet.getCells().get(row, 3);
    let totalCell = worksheet.getCells().get(row, 4);

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
let subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
let taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
let grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// Toplam değerler için kalın + para birimi stili
let totalStyle = workbook.createStyle();
totalStyle.getFont().setIsBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// Toplam etiketleri için kalın stil
let boldStyle = workbook.createStyle();
boldStyle.getFont().setIsBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// Çalışma kitabını OFD dosyası olarak kaydet
workbook.save(dataDir + "Invoice.ofd", AsposeCells.SaveFormat.Ofd);
```
## **Mevcut Bir Excel Dosyasını OFD'ye Dönüştürme**
Aspose.Cells ayrıca disk üzerindeki mevcut bir Excel çalışma kitabını yükleyebilir ve doğrudan OFD formatına dışa aktarabilir. Bu, toplu dönüştürme hatları, arşivleme iş akışları ve kaynak çalışma kitabının başka bir araç tarafından üretildiği ve yalnızca sabit düzenli bir yapıt olarak yeniden yayınlanması gereken senaryolar için kullanışlıdır. Aşağıdaki örnek, mevcut bir `.xlsx` çalışma kitabını yükler, hücrelerinden veri okur, isteğe bağlı sayfa yapısı düzenlemeleri uygular ve sonucu bir OFD belgesi olarak kaydeder.

```javascript
const AsposeCells = require("aspose.cells");

const dataDir = "C:\\Examples\\";

// Mevcut bir Excel çalışma kitabını diskten aç
const workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");

// (1) Dosyanın yüklendiğini onaylamak için seçili hücrelerden değerleri oku ve görüntüle
const firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Mevcut sayfaları numaralandırmak için Worksheets koleksiyonu üzerinde yineleme yap
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    const ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}

// (3) İsteğe bağlı olarak dönüşümü yansıtmak için bir zaman damgası hücresini güncelle
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));

// Veri bloğunun üstüne bir özet başlık satırı ekle
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));

// (4) Çalışma sayfasında PageSetup özelliklerini yapılandır
const pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) OFD çıktısı için yazdırma alanını isteğe bağlı olarak ayarla
const lastRow = firstSheet.getCells().getMaxDataRow();
const lastCol = firstSheet.getCells().getMaxDataColumn();
const lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
const printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);

// (6) Çalışma kitabını OFD dosyası olarak kaydet
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");

function formatDate(date) {
    const pad = (n) => n.toString().padStart(2, '0');
    return date.getFullYear() + "-" + pad(date.getMonth() + 1) + "-" + pad(date.getDate()) + " " + pad(date.getHours()) + ":" + pad(date.getMinutes()) + ":" + pad(date.getSeconds());
}
```

## **İlgili Makaleler**
- [Excel Dosyalarını Birden Çok Dosyaya Bölme](/cells/tr/nodejs-java/splitting-excel-files-into-multiple-files/)
- [Bir Hücreye Görüntü Ekleme](/cells/tr/nodejs-java/inserting-an-image-into-a-cell/)
- [DBF Dosyalarını Okuma ve Yazma](/cells/tr/nodejs-java/dbf/)
- [Aspose.Cells for Node.js via Java'da Sparkline'ı Görüntüye ve HTML'ye Dönüştürme](/cells/tr/nodejs-java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="javascript" >}}