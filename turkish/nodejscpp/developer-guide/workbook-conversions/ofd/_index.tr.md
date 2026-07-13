---
title: Excel'i OFD Formatına Dönüştürme
linktitle: Excel'i OFD Formatına Dönüştürme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için Excel çalışma kitaplarını OFD (Open Fixed-layout Document) formatına dönüştürmeyi destekleyen bir Node.js kütüphanesidir. Bu makale, Aspose.Cells kullanarak Excel içeriği oluşturmayı ve OFD olarak dışa aktarmayı, ayrıca mevcut Excel dosyalarını OFD'ye dönüştürmeyi göstermektedir.
keywords: Aspose.Cells, Node.js kütüphanesi, elektronik tablo, Excel'den OFD'ye, OFD dönüşümü, SaveFormat.Ofd, sabit düzenli belge, çalışma kitabı dışa aktarma
type: docs
weight: 195
url: /tr/nodejs-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, Excel çalışma kitaplarını doğrudan `SaveFormat.Ofd` numaralandırma değerini kullanarak OFD (Open Fixed-layout Document) formatına dönüştürmeyi destekler. Ortaya çıkan OFD belgesi, çalışma kitabının görünür düzenini, içeriğini, birleştirilmiş hücrelerini, sütun genişliklerini, satır yüksekliklerini, yazı tiplerini, renkleri, kenarlıklarını ve sayı biçimlerini korur. Bu, Aspose.Cells'i arşivleme, yazdırma, düzenleyici dosyalama ve resmi kurumlara sunuş iş akışları için sabit düzenli çıktı gerektiren uygulamalar için uygun hale getirir.

{{% /alert %}}
## **Giriş**
OFD (Open Fixed-layout Document), dijital belgeleri sabit, sayfa tabanlı bir düzende temsil etmek için Çin ulusal standardıdır (GB/T 33190-2016). Kaynak belgenin görsel görünümünün tam olarak yazıldığı şekilde korunması gereken kullanım durumlarında PDF'ye benzer bir rol oynar. OFD, Çin Halk Cumhuriyeti'nde resmi kurumlara sunuşlar, düzenleyici dosyalamalar, elektronik faturalar ve uzun süreli arşivleme için yaygın olarak benimsenmiştir.

Excel çalışma kitaplarını OFD'ye dönüştürmek, elektronik tablo içeriğinin düzenlenebilir bir elektronik tablo olarak değil, salt okunur, düzeni kilitli bir eser olarak dağıtılması gereken senaryolarda yaygın bir gereksinimdir. Örnekler arasında, son haline getirilmiş bir faturanın müşteriye gönderilmesi, üç aylık bir finansal raporun arşivlenmesi veya bir bütçe elektronik tablosunun düzenleyici bir makama sunulması yer alır. Aspose.Cells bu gereksinimi, çalışma kitabını ara bir dönüşüm adımı gerektirmeden doğrudan OFD'ye yazan `SaveFormat.Ofd` numaralandırma değeri aracılığıyla ele alır. OFD çıktısı, hücre değerlerini, birleştirilmiş aralıkları, yazı tiplerini, renkleri, kenarlıkları, sayı biçimlerini ve çalışma kitabında yapılandırılan sayfa düzeni seçeneklerini korur.

{{% alert color="primary" %}}

Aspose.Cells tarafından oluşturulan OFD çıktısı, kaynak çalışma kitabının görünür düzenini, hücre içeriğini, birleştirilmiş hücreler, sütun genişlikleri ve satır yükseklikleri dahil olmak üzere korur. Yazı tipleri, renkler, kenarlıklar, hizalama ve sayı biçimleri gibi hücre biçimlendirmesi de sabit düzenli çıktıda işlenir. Çalışma sayfasında yapılandırılan kağıt boyutu, yönlendirme ve yazdırma alanı gibi sayfa düzeni seçenekleri, ortaya çıkan OFD belgesinin düzenini etkiler.

{{% /alert %}}
## **Excel Çalışma Kitabı Oluşturma ve OFD Olarak Kaydetme**
Aspose.Cells, bir çalışma kitabını programlı olarak oluşturmanıza, verilerle doldurmanıza ve ardından doğrudan OFD formatında kaydetmenize olanak tanır. Aşağıdaki örnek sıfırdan bir fatura oluşturur. Bir şirket logosu, başlık bilgileri, fatura alanı bilgileri, kalem satırları ve hesaplanan toplamlar ekler, ardından çalışma kitabını bir OFD belgesi olarak dışa aktarır.


```javascript
let dataDir = "C:\\Temp\\";

// Yeni bir Workbook oluştur
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
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
titleCell.setStyle(titleStyle);

// Fatura numarası ve tarihi
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
let now = new Date();
let dateStr = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
worksheet.getCells().get("C12").putValue(dateStr);

// Fatura kesilen kişi bölümü
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
headerStyle.getFont().setColor(AsposeCells.Color.White);
headerStyle.setBackgroundColor(AsposeCells.Color.Navy);
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Kenarlıklı para birimi stili
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

// Açıklama/miktar hücreleri için düz kenarlık stili
let borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

// Kalem satırları
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];

for (let i = 0; i < lineItems.length; i++) {
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

// Toplam değerleri için kalın + para birimi stili
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
### **Logolu Bir Fatura Oluşturma**
Örnek, sol üst alana bir logo görüntüsü ekleyerek bir fatura çalışma sayfası oluşturur, şirket adını ve iletişim bilgilerini doldurur, birleştirilmiş hücreler arasına "FATURA" başlığı ekler, fatura numarasını ve tarihini kaydeder, fatura alıcı müşterisini listeler, açıklama, miktar, birim fiyat ve toplam sütunlarıyla bir kalem satırları tablosu oluşturur ve hücre formülleri kullanarak ara toplam, vergi ve genel toplamı hesaplar. Kalın başlıklar, fiyatlar için para birimi biçimi, kenarlıklar ve sütun genişlikleri gibi biçimlendirmeler `Style` ve `Font` nesneleri kullanılarak uygulanır. Son olarak, çalışma kitabı `SaveFormat.Ofd` kullanılarak `.ofd` uzantısıyla kaydedilir.

## **Mevcut Bir Excel Dosyasını OFD'ye Dönüştürme**
Aspose.Cells ayrıca diskteki mevcut bir Excel çalışma kitabını yükleyebilir ve doğrudan OFD formatında dışa aktarabilir. Bu, toplu dönüştürme hatları, arşivleme iş akışları ve kaynak çalışma kitabının başka bir araç tarafından üretildiği ve yalnızca sabit düzenli bir eser olarak yeniden yayınlanması gereken senaryolar için kullanışlıdır. Aşağıdaki örnek, mevcut bir `.xlsx` çalışma kitabını yükler, hücrelerinden veri okur, isteğe bağlı sayfa düzeni ayarlamaları uygular ve sonucu bir OFD belgesi olarak kaydeder.


```javascript
let workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");

// (1) Dosyanın yüklendiğini doğrulamak için seçili hücrelerden değerleri okuyun ve görüntüleyin
let firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Çalışma sayfaları koleksiyonu üzerinde yineleyerek mevcut sayfaları listeleyin
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    let ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}

// İsteğe bağlı olarak, dönüşümü yansıtmak için bir zaman damgası hücresini güncelleyin
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));

// Veri bloğunun üstüne bir özet başlık satırı ekleyin
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));

// (4) Çalışma sayfasında PageSetup özelliklerini yapılandırın
let pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) İsteğe bağlı olarak OFD çıktısı için yazdırma alanını ayarlayın
let lastRow = firstSheet.getCells().getMaxDataRow();
let lastCol = firstSheet.getCells().getMaxDataColumn();
let lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
let printArea = "a1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);

// (6) Çalışma kitabını OFD dosyası olarak kaydedin
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **İlgili Makaleler**
- [Excel Dosyalarını Birden Çok Dosyaya Bölme](/cells/tr/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [Bir Hücreye Görüntü Ekleme](/cells/tr/nodejs-cpp/inserting-an-image-into-a-cell/)
- [DBF Dosyalarını Okuma ve Yazma](/cells/tr/nodejs-cpp/dbf/)
- [Aspose.Cells for Node.js via C++'da Sparkline'ı Görüntüye ve HTML'ye Dönüştürme](/cells/tr/nodejs-cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="javascript" >}}