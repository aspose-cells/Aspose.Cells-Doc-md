---
title: Sayı Biçimlendirme Nasıl Yapılır, Para Birimi Olarak Formatlama
type: docs
weight: 10
url: /tr/javascript-cpp/format-number-to-currency/
description: Bu makale, Aspose.Cells for JavaScript C++ API kullanarak sayı biçimini para birimine nasıl biçimlendireceğinizi tanıtacaktır.
keywords: sayı biçimini para birimi olarak ayarla, hücre sayı ayarları, sayıyı para birimine biçimlendir, para birimi ayarları, para birimi biçimi.
---

## **Olası Kullanım Senaryoları**
Excel’de sayıları para birimine biçimlendirmek, özellikle finansal verilerle çalışırken, birkaç nedenle önemlidir. İşte para birimi biçimlendirmesinin avantajları:

1. Finansal Değerleri Netleştirir: bir sayıyı para birimi olarak biçimlendirmek, değerin para olduğunu açıklar. Örneğin, 1000 yerine, $1,000 açıkça bir maddi tutarı gösterir.
1. Para Birimi Sembolleri Dahil Edilir: uluslararası veya çoklu para birimlerini işlerken, uygun para birimi sembolüyle (örn., $, €, £) sayıları biçimlendirmek, kullanılan para birimi türünü netleştirir, çok uluslu finansal rapor veya işlemlerde karışıklığı azaltır.
1. Profesyonel Sunumu Artırır: iyi biçimlendirilmiş para birimi değerleri, raporlar, sunumlar ve iş belgeleri için daha düzgün ve profesyonel görünür. $10,000.00, basit 10000’den daha inandırıcı ve düzenlidir.
1. Okunabilirliği Artırır: para birimi biçimlendirmesi, binlik ayırıcılar ve ondalık basamaklar ekler, böylece büyük sayılar daha kolay okunabilir hale gelir. Örneğin, 1000000, $1,000,000.00 olur, bu da daha okunaklı ve hızlı anlaşılır.
1. Tutarlılığı Sağlar: süreklilik gösteren para birimi biçimlendirmesiyle, bir veri kümesindeki tüm parasal değerlerin aynı formatta görüntülendiğinden emin olursunuz. Bu tutarlılık, finansal doğruluk ve büyük elektronik tablolar içindeki sayılar için profesyonel iletişim açısından önemlidir.
1. Kesinlik Gösterir: para birimi biçimlendirmesi genellikle iki ondalık basamağı içerir, böylece kesin parasal tutarları görebilirsiniz. Örneğin, $100.50, $100.00’dan açıkça farklıdır; bu, kesinlik önemli olduğunda finansal raporlarda önemlidir.
1. Finansal Hesaplamaları Basitleştirir: toplamları toplama veya maliyetleri ortalama alma gibi finansal hesaplamalar yaparken, para birimi biçimlendirmesi Excel ve kullanıcılara verilerin parasal olduğunu anlamalarına yardımcı olur. Excel’in formüllerde ve fonksiyonlarda uygun biçimlendirmeyi uygulamasını sağlar ve sonuçların tutarlı kalmasını temin eder.
1. Yanlış Anlamayı Azaltır: para birimi biçimlendirmesi olmadan, sayılar genel sayısal değerler olarak yanlış anlaşılabilir, yani para miktarı olarak değil. Örneğin, 500, nesne sayısı veya birim olarak karıştırılabilir, oysa $500.00 açıkça finansal bir tutarı temsil eder.
1. Muhasebe Özellikleriyle Çalışır: para birimi biçimlendirmesi, Excel’deki muhasebe fonksiyonlarıyla iyi uyum sağlar, örneğin bilanço veya nakit akış raporları gibi. Değerleri, para biriminin ana odak olduğu finansal tablolarda daha kullanışlı hale getirir.
<br>
Özetle, numaraları para birimi olarak biçimlendirmek, parasal değerleri diğer sayı türlerinden ayırmaya yardımcı olur, açıklığı artırır ve verilerin yorumlanmasını kolaylaştırır, özellikle finansal bağlamlarda.

## **Excel'de Sayı Nasıl Para Birimi Olarak Biçimlendirilir**
Excel'de sayıları para birimi olarak biçimlendirmek için şu adımları izleyin:

### **Para Birimi Biçim Seçeneğinin Kullanılması**
1. Para birimi olarak biçimlendirmek istediğiniz hücreleri seçin.
1. Şeritteki Giriş sekmesine gidin.
1. Sayı grubunda, sayı biçimi kutusunun yanındaki aşağı açılır oka tıklayın (varsayılan olarak "Genel" görüntülenebilir).
<br>
<img src="1.png" width=60% />
1. Listeden Para Birimi seçeneğini seçin.

### **Hücreleri Biçimlendir Diyalog Kutusunu Kullanarak**
1. Biçimlendirmek istediğiniz hücreleri seçin.
1. Seçili hücrelere sağ tıklayın ve Biçimlendir seçeneğini seçin, böylece Hücreleri Biçimlendir iletişim kutusu açılır.
1. Sayı sekmesinde, sol taraftaki listeden Para Birimi seçin.
<br>
<img src="2.png" width=60% />
1. Aşağıdaki ayarları özelleştirebilirsiniz: Ondalık basamaklar, Sembol, Negatif sayılar.
1. Tamam düğmesine tıklayarak biçimlendirmeyi uygulayın.

## **Aspose.Cells'de Sayı Nasıl Para Birimi Olarak Biçimlendirilir**

Excel dosyalarıyla çalışmak için Aspose.Cells for JavaScript C++ kütüphanesinde sayıların para birimi olarak biçimlendirilmesi, hücrelere programatik olarak para birimi biçimi uygulayarak yapılabilir. İşte bunu yapmanın yolu Aspose.Cells for JavaScript C++ kullanımıyla.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Currency Formatting Example</h1>
        <p>Optionally select an Excel file to modify. If no file is selected, a new workbook will be created.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell you want to format
            const a1 = worksheet.cells.get("A1");

            // Set a numeric value to the cell
            a1.value = 1234.56;

            // Create a style object to apply the currency format
            const a1Style = a1.style;
            // "7" is the currency format in Excel
            a1Style.number = 7;

            // Apply the style to the cell
            a1.style = a1Style;

            // Access the cell where you want to apply the currency format
            const a2 = worksheet.cells.get("A2");

            // Set a numeric value to the cell
            a2.value = 3456.78;

            // Create a style object to apply the currency format
            const a2Style = a2.style;
            // Custom format for dollar currency
            a2Style.custom = "$#,##0.00";

            // Apply the style to the cell
            a2.style = a2Style;

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CurrencyFormatted.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CurrencyFormatted.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook formatted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
