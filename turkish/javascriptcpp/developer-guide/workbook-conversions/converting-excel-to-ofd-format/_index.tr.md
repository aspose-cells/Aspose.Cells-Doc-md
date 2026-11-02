---
title: Excel'i OFD Biçimine Dönüştürme
linktitle: Excel'i OFD Biçimine Dönüştürme
description: Aspose.Cells for JavaScript via C++, elektronik tablo dosyalarıyla çalışmayı ve Excel çalışma kitaplarını OFD (Açık Sabit Düzenli Belge) biçimine dönüştürmeyi destekleyen bir JavaScript kitaplığıdır. Bu makale, Aspose.Cells kullanarak Excel içeriği oluşturup OFD olarak dışa aktarmayı ve mevcut Excel dosyalarını OFD biçimine dönüştürmeyi gösterir.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, JavaScript kitaplığı, elektronik tablo, Excel'den OFD'ye, OFD dönüştürme, SaveFormat.Ofd, sabit düzenli belge, çalışma kitabı dışa aktarma
type: docs
weight: 195
url: /tr/javascript-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, `SaveFormat.Ofd` numaralandırma değerini kullanarak Excel çalışma kitaplarını doğrudan OFD (Açık Sabit Düzenli Belge) biçimine dönüştürmeyi destekler. Oluşturulan OFD belgesi, çalışma kitabının görünür yerleşimini, içeriğini, birleştirilmiş hücrelerini, sütun genişliklerini, satır yüksekliklerini, yazı tiplerini, renklerini, kenarlıklarını ve sayı biçimlerini korur. Bu özellik; sabit düzenli çıktı gerektiren arşivleme, yazdırma, düzenleyici makamlara yapılan başvurular ve devlet kurumlarına gönderim iş akışlarında Aspose.Cells'i uygun bir çözüm hâline getirir.
{{% /alert %}}

## **Giriş**
OFD (Açık Sabit Düzenli Belge), dijital belgeleri sabit ve sayfa tabanlı bir yerleşimde temsil etmek için kullanılan bir Çin ulusal standardıdır (GB/T 33190-2016). Kaynak belgenin görünümünün yazıldığı gibi birebir korunması gereken kullanım senaryolarında PDF'ye benzer bir işlev görür. OFD, Çin Halk Cumhuriyeti'nde devlet kurumlarına gönderimler, düzenleyici makamlara yapılan başvurular, elektronik faturalar ve uzun süreli arşivleme için yaygın olarak kullanılır.
Elektronik tablo içeriğinin düzenlenebilir bir elektronik tablo olarak değil, salt okunur ve düzeni kilitlenmiş bir çıktı belgesi olarak dağıtılması gereken senaryolarda Excel çalışma kitaplarını OFD biçimine dönüştürmek yaygın bir gerekliliktir. Bunlara örnek olarak nihai olarak düzenlenmiş bir faturayı müşteriye göndermek, üç aylık finansal raporu arşivlemek veya bütçe elektronik tablosunu bir düzenleyici makama sunmak verilebilir. Bu gereksinim, Aspose.Cells tarafından `SaveFormat.Ofd` numaralandırma değeriyle karşılanır. Bu değer, çalışma kitabını ara bir dönüştürme adımı gerektirmeden doğrudan OFD biçiminde yazar. OFD çıktısı, hücre değerlerini, birleştirilmiş aralıkları, yazı tiplerini, renkleri, kenarlıkları, sayı biçimlerini ve çalışma kitabında yapılandırılmış sayfa yapımı seçeneklerini korur.

{{% alert color="primary" %}}
Aspose.Cells tarafından oluşturulan OFD çıktısı, kaynak çalışma kitabının görünür yerleşimini korur. Bu yerleşim hücre içeriğini, birleştirilmiş hücreleri, sütun genişliklerini ve satır yüksekliklerini içerir. Yazı tipi, renk, kenarlık, hizalama ve sayı biçimi gibi hücre biçimlendirmeleri de sabit düzenli çıktıda uygulanır. Çalışma sayfasında yapılandırılan kağıt boyutu, sayfa yönü ve yazdırma alanı gibi sayfa yapımı seçenekleri, oluşturulan OFD belgesinin yerleşimini etkiler.
{{% /alert %}}

## **Excel Çalışma Kitabı Oluşturma ve OFD Olarak Kaydetme**
Aspose.Cells ile bir çalışma kitabını programatik olarak oluşturabilir, verilerle doldurabilir ve ardından `SaveFormat.Ofd` numaralandırma değerini kullanarak doğrudan OFD biçiminde kaydedebilirsiniz. Aşağıdaki örnek sıfırdan bir fatura oluşturur. Şirkete ait logoyu, üst bilgileri, fatura edilecek kişi bölümünü, kalem satırlarını ve hesaplanan toplamları ekler; ardından çalışma kitabını bir OFD belgesine dışa aktarır.

### **Logolu Fatura Oluşturma**
Örnek, bir logo görselini sol üst alana ekleyerek bir fatura çalışma sayfası oluşturur; şirket adını ve iletişim ayrıntılarını doldurur, birleştirilmiş hücrelere fatura başlığını ekler, fatura numarası ile tarihi kaydeder, fatura edilecek kişi bilgilerini ekler, açıklama, miktar, birim fiyat ve toplam sütunlarından oluşan kalem tablosu oluşturur ve hücre formülleriyle ara toplamı, vergiyi ve genel toplamı hesaplar. Kalın başlıklar, fiyatlar için para birimi biçimi, kenarlıklar ve sütun genişlikleri gibi biçimlendirmeler `Style` ve `Font` nesneleriyle uygulanır. Son olarak, çalışma kitabı `SaveFormat.Ofd` kullanılarak `.ofd` uzantısıyla kaydedilir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, Color } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                // Yeni bir Çalışma Kitabı oluştur
                const workbook = new Workbook();
                // İlk çalışma sayfasını al
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Sütun genişliklerini ayarla
                cells.setColumnWidth(0, 5);
                cells.setColumnWidth(1, 35);
                cells.setColumnWidth(2, 12);
                cells.setColumnWidth(3, 15);
                cells.setColumnWidth(4, 15);
                cells.setColumnWidth(5, 5);
                // Şirket logosunu ekle
                // Tarayıcının dosya sistemi yolu olmadığı için bellek içi bir PNG oluştur.
                const logoCanvas = document.createElement("canvas");
                logoCanvas.width = 100;
                logoCanvas.height = 30;
                const logoContext = logoCanvas.getContext("2d");
                logoContext.fillStyle = "#000080";
                logoContext.fillRect(0, 0, logoCanvas.width, logoCanvas.height);
                logoContext.fillStyle = "#FFFFFF";
                logoContext.font = "bold 18px Arial";
                logoContext.fillText("ACME", 16, 21);
                const logoBlob = await new Promise(resolve => logoCanvas.toBlob(resolve, "image/png"));
                if (!logoBlob) {
                    throw new Error("Unable to create the company logo.");
                }
                const logoData = new Uint8Array(await logoBlob.arrayBuffer());
                worksheet.pictures.add(1, 1, logoData);
                // Şirket adı ve iletişim bilgileri
                cells.get("B3").value = "Acme Corporation";
                cells.get("B4").value = "123 Business Street";
                cells.get("B5").value = "City, State 12345";
                cells.get("B6").value = "Phone: (555) 123-4567";
                // FATURA başlığı - hücreleri birleştir
                cells.merge(7, 1, 2, 4);
                const titleCell = cells.get("B8");
                titleCell.value = "INVOICE";
                const titleStyle = workbook.createStyle();
                titleStyle.font.isBold = true;
                titleStyle.font.size = 20;
                titleStyle.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
                titleCell.style = titleStyle;
                // Fatura numarası ve tarih
                cells.get("B11").value = "Invoice Number:";
                cells.get("C11").value = "INV-2024-001";
                cells.get("B12").value = "Date:";
                const now = new Date();
                const invoiceDate = [
                    now.getFullYear(),
                    String(now.getMonth() + 1).padStart(2, "0"),
                    String(now.getDate()).padStart(2, "0")
                ].join("-");
                cells.get("C12").value = invoiceDate;
                // Fatura edilecek kişi bölümü
                cells.get("B14").value = "Bill To:";
                cells.get("B15").value = "Client Name";
                cells.get("B16").value = "Client Address";
                cells.get("B17").value = "Client City, State";
                // Satır öğeleri başlığı
                const headerDesc = cells.get("B19");
                const headerQty = cells.get("C19");
                const headerPrice = cells.get("D19");
                const headerTotal = cells.get("E19");
                headerDesc.value = "Description";
                headerQty.value = "Quantity";
                headerPrice.value = "Unit Price";
                headerTotal.value = "Total";
                const headerStyle = workbook.createStyle();
                headerStyle.font.isBold = true;
                headerStyle.font.color = Color.fromArgb(255, 255, 255);
                headerStyle.foregroundColor = Color.fromArgb(0, 0, 128);
                headerStyle.pattern = AsposeCells.BackgroundType.Solid;
                headerStyle.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
                headerStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerDesc.style = headerStyle;
                headerQty.style = headerStyle;
                headerPrice.style = headerStyle;
                headerTotal.style = headerStyle;
                // Kenarlıklı para birimi stili
                const currencyStyle = workbook.createStyle();
                currencyStyle.custom = '"$"#,##0.00';
                currencyStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // Açıklama/miktar hücreleri için sade kenarlık stili
                const borderStyle = workbook.createStyle();
                borderStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // Satır öğeleri satırları
                const lineItems = [
                    ["Product A - Widget", 2, 50.00],
                    ["Product B - Gadget", 3, 75.00],
                    ["Product C - Service", 1, 100.00]
                ];
                for (let i = 0; i < lineItems.length; i++) {
                    const row = 20 + i;
                    const descCell = cells.get(row, 1);
                    const qtyCell = cells.get(row, 2);
                    const priceCell = cells.get(row, 3);
                    const totalCell = cells.get(row, 4);
                    descCell.value = lineItems[i][0];
                    qtyCell.value = lineItems[i][1];
                    priceCell.value = lineItems[i][2];
                    totalCell.formula = "C" + (row + 1) + "*D" + (row + 1);
                    descCell.style = borderStyle;
                    qtyCell.style = borderStyle;
                    priceCell.style = currencyStyle;
                    totalCell.style = currencyStyle;
                }
                // Ara toplam, vergi, genel toplam
                cells.get("B24").value = "Subtotal:";
                const subtotalCell = cells.get("E24");
                subtotalCell.formula = "SUM(E21:E23)";
                cells.get("B25").value = "Tax (10%):";
                const taxCell = cells.get("E25");
                taxCell.formula = "E24*0.1";
                cells.get("B26").value = "Grand Total:";
                const grandTotalCell = cells.get("E26");
                grandTotalCell.formula = "E24+E25";
                // Toplam değerler için kalın + para birimi stili
                const totalStyle = workbook.createStyle();
                totalStyle.font.isBold = true;
                totalStyle.custom = '"$"#,##0.00';
                subtotalCell.style = totalStyle;
                taxCell.style = totalStyle;
                grandTotalCell.style = totalStyle;
                // Toplam etiketleri için kalın stil
                const boldStyle = workbook.createStyle();
                boldStyle.font.isBold = true;
                cells.get("B24").style = boldStyle;
                cells.get("B25").style = boldStyle;
                cells.get("B26").style = boldStyle;
                // Çalışma kitabını OFD dosyası olarak kaydet
                const outputData = workbook.save(AsposeCells.SaveFormat.Ofd);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "Invoice.ofd";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
        </script>
    </body>
</html>
```

## **Mevcut Bir Excel Dosyasını OFD Biçimine Dönüştürme**
Aspose.Cells, diskte bulunan mevcut bir Excel çalışma kitabını yükleyebilir ve doğrudan OFD biçimine dışa aktarabilir. Bu özellik; toplu dönüştürme işlem hatları ve arşivleme iş akışlarında yararlıdır. Ayrıca, kaynak çalışma kitabının başka bir araçla oluşturulduğu ve yalnızca sabit düzenli bir belge olarak yeniden dışa aktarılması gereken senaryolarda kullanışlıdır. Aşağıdaki örnek, mevcut bir `.xlsx` çalışma kitabını yükler, hücrelerinden veri okur, isteğe bağlı sayfa yapımı ayarlamalarını uygular ve sonucu bir OFD belgesi olarak kaydeder.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, CellsHelper } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            function formatTimestamp(date) {
                const pad = value => String(value).padStart(2, "0");
                return date.getFullYear() + "-" +
                    pad(date.getMonth() + 1) + "-" +
                    pad(date.getDate()) + " " +
                    pad(date.getHours()) + ":" +
                    pad(date.getMinutes()) + ":" +
                    pad(date.getSeconds());
            }
            function escapeHtml(value) {
                const entities = {
                    "&": "&amp;",
                    "<": "&lt;",
                    ">": "&gt;",
                    '"': "&quot;",
                    "'": "&#39;"
                };
                return String(value).replace(/[&<>"']/g, character => entities[character]);
            }
            runButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an Excel file first.</p>';
                        return;
                    }
                    runButton.disabled = true;
                    downloadLink.style.display = "none";
                    downloadLink.removeAttribute("href");
                    // Diskte mevcut bir Excel çalışma kitabını aç
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // (1) Dosyanın yüklendiğini doğrulamak için seçili hücrelerdeki değerleri oku ve göster
                    const firstSheet = workbook.worksheets.get(0);
                    const cells = firstSheet.cells;
                    const output = [];
                    output.push("First sheet name: " + firstSheet.name);
                    output.push("Cell A1: " + cells.get("A1").stringValue);
                    output.push("Cell B1: " + cells.get("B1").stringValue);
                    output.push("Cell C1: " + cells.get("C1").stringValue);
                    // (2) Mevcut sayfaları listelemek için Worksheets koleksiyonu üzerinde yinele
                    output.push("");
                    output.push("Available worksheets:");
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const ws = workbook.worksheets.get(i);
                        output.push("  [" + i + "] " + ws.name);
                    }
                    // (3) İsteğe bağlı olarak dönüşümü yansıtmak için zaman damgası hücresini güncelle
                    cells.get("A1").value = "Converted on: " + formatTimestamp(new Date());
                    // Veri bloğunun üst kısmına özet başlık satırı ekle
                    cells.insertRow(0);
                    cells.get("A1").value = "Conversion Summary";
                    cells.get("A2").value = "Generated: " + formatTimestamp(new Date());
                    // (4) Çalışma sayfasında PageSetup özelliklerini yapılandır
                    const pageSetup = firstSheet.pageSetup;
                    pageSetup.orientation = AsposeCells.PageOrientationType.Landscape;
                    pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA4;
                    pageSetup.fitToPagesTall = 1;
                    pageSetup.fitToPagesWide = 1;
                    // (5) İsteğe bağlı olarak OFD çıktısı için yazdırma alanını ayarla
                    const lastRow = cells.maxDataRow;
                    const lastCol = cells.maxDataColumn;
                    const lastColLetter = CellsHelper.columnIndexToName(lastCol);
                    const printArea = "A1:" + lastColLetter + (lastRow + 1);
                    pageSetup.printArea = printArea;
                    output.push("");
                    output.push("Print area set to: " + printArea);
                    // (6) Çalışma kitabını OFD dosyası olarak kaydet
                    const outputData = workbook.save(AsposeCells.SaveFormat.Ofd);
                    const blob = new Blob([outputData]);
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "SampleBook.ofd";
                    downloadLink.textContent = "Download SampleBook.ofd";
                    downloadLink.style.display = "block";
                    output.push("");
                    output.push("File successfully converted to OFD format: SampleBook.ofd");
                    result.innerHTML =
                        '<pre style="white-space: pre-wrap;">' +
                        escapeHtml(output.join("\n")) +
                        "</pre>" +
                        '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    const message = error && error.message ? error.message : String(error);
                    result.innerHTML = '<p style="color: red;">Error: ' + escapeHtml(message) + "</p>";
                } finally {
                    runButton.disabled = false;
                }
            });
        </script>
    </body>
</html>
```

## **İlgili Makaleler**
- [Bir Hücreye Görsel Ekleme](/cells/tr/javascript-cpp/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="javascript-cpp" >}}