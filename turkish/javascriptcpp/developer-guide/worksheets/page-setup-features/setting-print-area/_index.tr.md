---
title: JavaScript ve C++ kullanarak Yazdırma Alanını Nasıl Ayarlarsınız
linktitle: Yazdırma Alanı Nasıl Ayarlanır
type: docs
weight: 200
url: /tr/javascript-cpp/how-to-set-print-area/
description: Bu makale, Aspose.Cells kütüphanesini kullanarak JavaScript ve C++ ile yazdırma alanını nasıl ayarlayacağınızı gösteren kodlar sunmaktadır.
keywords: Yazdırma aralığını sınırlandırma, Yazdırma Aralığını Ayarla, Yazdırma Aralığını Temizle, JavaScript ve C++ kullanarak Yazdırma Aralığını ayarlama ve temizleme, Yazdırma alanını ayarlama ve temizleme, JavaScript ve C++ ile Yazdırma Alanını nasıl ayarlarsınız, C++ ve JavaScript kullanarak Yazdırma Alanını Nasıl Temizlersiniz, Excel de Yazdırma Alanını Nasıl Ayarlarsınız, Excel de Yazdırma Alanını Temizleyin.
---

## **Olası Kullanım Senaryoları**

Bir belge, örneğin bir Excel sayfası, içinde yer alan içeriği kontrol etmek için yazdırma alanı ayarlamak faydalıdır. İşte yazdırma alanı ayarlamanın bazı nedenleri:

1. Belirli Verilere Odaklanma: Sadece en önemli bölümleri yazdırabilir, gereksiz içeriği engelleyebilirsiniz.
1. Gelişmiş Düzen: İçeriğin düzenlenmesine ve düzgün şekilde sığdırılmasına yardımcı olur, bölünmeleri veya istenmeyen sayfa sonlarını önler.
1. Kaynak Tasarrufu: Yazdırma alanını sınırlandırarak kağıt ve mürekkep kullanımını azaltabilirsiniz.
1. Profesyonel Sunum: Yalnızca verilerin düzgün ve son halini yazdırdığınızdan emin olur, bu özellikle raporlar veya sunumlar için önemlidir.
1. Tutarlılık: Aynı belgeyi birden fazla kez yazdırırken, belirli bir yazdırma alanı kullanmak, çıktıdaki tutarlılığı sağlar.

<br>
Yazdırma alanı ayarlamak, özellikle büyük belgelerde, yalnızca bir kısmının paylaşılması veya yazdırılmak üzere gözden geçirilmesi gerektiğinde çok kullanışlıdır.

## **Excel'de Yazdırma Alanı Nasıl Ayarlanır**

Excel'de yazdırma alanı belirlemek için şu adımları izleyin:

1. Hücreleri Seçin: Yazdırma alanı olarak ayarlamak istediğiniz hücre aralığını tıklayıp sürükleyerek seçin.
1. Sayfa Düzeni Sekmesini Açın: Excel penceresinin üstündeki şeritteki "Sayfa Düzeni" sekmesine gidin.
1. Yazdırma Alanını Ayarla: "Sayfa Kurulum" grubunda, "Yazdırma Alanı"na tıklayın. Açılan menüden "Yazdırma Alanını Ayarla"yı seçin.
<br>
<img src="3.png" width=60% />

1. Yazdırma Alanına Ekleyin: Mevcut yazdırma alanına başka hücreler ekmek istiyorsanız, ek hücreleri seçin, "Sayfa Düzeni" sekmesinde "Yazdırma Alanı"na gidin ve "Yazdırma Alanına Ekle"yi seçin.

<br>
Bu işlem, seçilen hücreleri yazdırma alanı olarak tanımlar. Çalışma sayfasını yazdırdığınızda, yalnızca bu tanımlı alan yazdırılır.

## **Excel'de Yazdırma Alanını Temizle Nasıl Yapılır**

Excel'de yazdırma alanını temizlemek için şu adımları izleyin:

1. Sayfa Düzeni Sekmesini Açın: Excel penceresinin üstündeki "Sayfa Düzeni" sekmesine tıklayın.
1. Yazdırma Alanını Temizle: "Sayfa Kurulum" grubunda, "Yazdırma Alanı"na tıklayın. Açılan menüden "Yazdırma Alanını Temizle"yi seçin.
<br>
<img src="4.png" width=60% />

<br>
Bu işlem, önceden ayarlanmış yazdırma alanını kaldırır ve tüm çalışma sayfasının yazdırılmasına izin verir.

## **Yazdırma Alanını Temizledikten Sonra Neler Olur**

Excel gibi elektronik tablo uygulamasında Aspose.Cells kullanarak yazdırma alanını temizlemek, belgenin tamamını yazdırmak anlamına gelir. Yazdırma alanı ayarlandıysa, yalnızca belirli hücre aralığı yazdırılır. Yazdırma alanı temizlendiğinde, herhangi bir belirli aralık tanımlanmaz ve varsayılan yazdırma davranışı devreye girer, bu da tüm sayfayı içerir.

1. Varsayılan Yazdırma Davranışı: Tüm çalışma sayfası yazdırılmak üzere değerlendirilir. Bu, tüm hücrelerin verileri veya biçimlendirmeleri kabul eder.
1. Yazdırma Alanı Sınırları Kalmadı: Önceden belirlenmiş yazdırma alanı sınırları kaldırılır. Önceden belirlenen satır ve sütunlar artık bu sınırlar içinde kalmaz.
1. Tüm İçeriğin Yazdırılması: Başlıklar, altbilgiler ve çalışma sayfasındaki diğer tüm veriler yazdırma işlemine dahil edilir.

## **Aspose.Cells for JavaScript kullanarak Yazdırma Alanını Nasıl Ayarlarsınız**

Belirli bir çalışma sayfasında yazdırma alanını ayarlamak için: İlk olarak, [örnek dosyayı](input.xlsx) yükleyin ve daha sonra [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) nesnesinin [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) özelliğini istediğiniz çalışma sayfası için değiştirin. Bu özelliği bir aralık dizisi olarak ayarlamak, yazdırma alanını belirler.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Area</title>
    </head>
    <body>
        <h1>Set Print Area Example</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet (first worksheet)
            const worksheet = workbook.worksheets.get(0);

            // Set the print area - specify the range you want to print
            worksheet.pageSetup.printArea = "A1:D10";

            // Save the workbook as PDF and provide a download link
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'set_print_area.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Print area set successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

Çıktı sonucu:
<br>
<img src="1.png" width=60% />

## **C++ ile Aspose.Cells for JavaScript Kullanarak Yazdırma Alanını Temizleme Nasıl Yapılır**

Belirtilmiş bir çalışma sayfasında yazdırma alanını temizlemek için: Önce [örnek dosyayı](input.xlsx) yükleyin, ardından istenen çalışma sayfası için [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) nesnesinin [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) özelliğini değiştirmeniz gerekir. Bu özelliği boş bir dize olarak ayarlamak yazdırma alanını temizler.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Clear Print Area</title>
    </head>
    <body>
        <h1>Clear Print Area Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Clear the print area
            worksheet.pageSetup.printArea = "";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'clear_print_area.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultEl.innerHTML = '<p style="color: green;">Print area cleared successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

Çıktı sonucu:
<br>
<img src="2.png" width=60% />
