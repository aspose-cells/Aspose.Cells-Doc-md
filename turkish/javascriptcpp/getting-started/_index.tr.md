---
title: Başlarken
type: docs
weight: 5
url: /tr/javascript-cpp/getting-started/
keywords: "Excel, Tarayıcı, Sunucusuz, XLS, XLSX, XLSB, CSV, PDF, JPG, PNG, HTML, ODS, XLSM, Elektronik Tablo, Markdown, XPS, DOCX, PPTX, MHTML, SVG, JSON, SQL, XML"
description: "JavaScript için Aspose.Cells kurulum ve kurulum yönergeleri."
---

## **Ürün Açıklaması**
Aspose.Cells for JavaScript C++ ile özel, özellik zengini ve yüksek performanslı bir kitaplık olup elektronik tablo dosyalarını (Excel, ODS, CSV, HTML) manipüle etme ve dönüştürme işlemleri için tasarlanmıştır. Tarayıcı ve Node.js ortamlarında elektronik tablolar oluşturma, düzenleme, dönüştürme ve görüntüleme için kapsamlı özellikler sağlar. Tüm büyük Excel formatlarını tam destekleyerek, Aspose.Cells for JavaScript C++ ile maksimum uyumluluk ve esneklik sağlar.
Tarayıcıda neredeyse yerel performansı açmak için WebAssembly ile geliştirilmiş olan Aspose.Cells for JavaScript C++ hızlı ve verimli elektronik tablo işlemesini, sunucu gerektirmeden gerçekleştirmeye imkan tanır. Hafif çalışma zamanı ayak izi, gelişmiş Excel fonksiyonelliği gerektiren sunucusuz web uygulamaları için mükemmeldir. Panel oluşturma, veri işleme hatları veya belge üretim araçları geliştirirken, Aspose.Cells for JavaScript C++ tam, güvenilir ve yüksek performanslı bir çözüm sunar. Aspose.Cells for JavaScript C++ çoğunlukla tarayıcıları ve Node.js destekler.

## **Ana özellikler**
1. **Dosya Oluşturma ve Düzenleme:** Sıfırdan yeni elektronik tablolar oluşturun veya mevcut olanları kolaylıkla düzenleyin. Bu, veri ekleme veya değiştirme, hücreleri biçimlendirme, çalışma sayfalarını yönetme ve daha fazlasını içerir.
1. **Veri İşleme:** Sıralama, filtreleme ve doğrulama gibi karmaşık veri manipülasyonları yapın. Kütüphane ayrıca gelişmiş formüller ve fonksiyonlar destekler, böylece veri analizi ve hesaplamalar kolaylaşır.
1. **Dosya Dönüştürme:** Excel dosyalarını PDF, HTML, ODS ve PNG, JPEG gibi resim formatlarına dönüştürün. Bu özellik, elektronik tablo verilerini farklı formatlarda paylaşma ve dağıtma için faydalıdır.
1. **Grafik ve Çizimler:** Verileri görsel olarak temsil etmek için çeşitli grafikler ve çizimler oluşturun ve özelleştirin. Kütüphane, çubuk grafikler, çizgi grafikler, pasta grafikler ve daha fazlasını destekler, tasarım ve düzenleme seçenekleriyle birlikte.
1. **Görselleştirme ve Yazdırma:** Excel sayfalarını yüksek çözünürlüklü görsellere ve PDF'lere dönüştürerek görsel temsilin doğru olmasını sağlayın. Kütüphane ayrıca sayfa düzeni ve format üzerinde hassas kontrol ile elektronik tablo yazdırma seçenekleri sunar.
1. **İleri Düzey Koruma ve Güvenlik:** Elektronik tabloları şifreyle koruyun, dosyaları şifreleyin ve erişim izinlerini yönetin, böylece veri güvenliği ve bütünlüğü sağlanır.
1. **Performans ve Ölçeklenebilirlik:** Büyük veri setleri ve karmaşık elektronik tabloları verimli şekilde yönetmek üzere tasarlanmış olan Aspose.Cells for JavaScript C++ yüksek performans ve kurumsal düzeyde ölçeklenebilirlik sağlar.


## **Önkoşullar**

Başlamadan önce, şunlara sahip olduğunuzdan emin olun:
- Sisteminizde Node.js kurulu olmalı (https://nodejs.org/ adresinden indiriniz)
- Geçerli bir Aspose lisans dosyası (örn. Aspose.Total.lic, Aspose.Cells.lic veya aspose.cells.js.lic) tam özellikli kullanım için
- HTML ve JavaScript temel bilgisi

## **Adım 1: Kurulum**

### Aspose.Cells for JavaScript Kurulumu

Yeni bir proje dizini oluşturun ve paketi yükleyin:

{{< highlight bash >}}
# Create a new project directory
mkdir my-excel-project
cd my-excel-project

# Install Aspose.Cells for JavaScript
npm install aspose.cells.js
{{< /highlight >}}

### HTTP Sunucusu Kurulumu (Lisans Ayarı için Gereklidir)

Basit bir HTTP sunucusunu küresel olarak yükleyin:

{{< highlight bash >}}
npm install -g http-server
{{< /highlight >}}

Veya Python'un yerleşik sunucusunu kullanın (Python yüklüyse):
{{< highlight bash >}}
# Python 3
python -m http.server

# Python 2
python -m SimpleHTTPServer
{{< /highlight >}}

## **Adım 2: Lisans Ayarı (Tüm Özellikler için Gereklidir)**

### Lisans Dosyanızı Şifreleyin

1. **HTTP sunucusunu başlatın** projeniz dizininde:
   {{< highlight bash >}}
   http-server -p 8080
   {{< /highlight >}}

2. **Lisans şifreleme aracını** tarayıcınızda açın:
   ```
   http://localhost:8080/node_modules/aspose.cells.js/encrypt_lic.html
   ```

3. **Lisans dosyanızı yükleyin**:
   - "Dosya Seç"e tıklayın ve lisans dosyanızı seçin (ör. `Aspose.Total.lic`, `Aspose.Cells.lic` veya `aspose.cells.js.lic`)
   - Şifreleme işlemi otomatik olarak tamamlanacaktır (çok hızlı)

4. **Şifrelenmiş lisansı indirin**:
   - "İşlenmiş Dosyayı İndir"e tıklayarak `aspose.cells.enc` dosyasını indirin
   - Bu dosyayı proje dizininize kaydedin

### Şifrelenmiş Lisansı Yerleştirin

`aspose.cells.enc` dosyasını proje kök dizinine veya uygulamanızın erişebileceği belirli bir klasöre taşıyın.

## **Adım 3: Kullanım Örnekleri**

### Tarayıcı Kullanımı

Proje dizininizde bir `index.html` dosyası oluşturun:

{{< highlight html >}}
<!DOCTYPE html>
<html>
<head>
    <title>Aspose.Cells Browser Example</title>
</head>
<body>
    <h1>Excel Processing with Aspose.Cells</h1>
    <button id="createExcel">Create Excel File</button>
    <div id="output"></div>

    <script src="./node_modules/aspose.cells.js/aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FileFormatType, SaveFormat } = AsposeCells;

        // Initialize with license (optional, remove for trial mode)
        AsposeCells.onReady({
            license: "aspose.cells.enc"  // Path to your encrypted license
        }).then(() => {
            console.log("Aspose.Cells is ready!");

            document.getElementById('createExcel').onclick = function() {
                // Create a new workbook
                var workbook = new Workbook(FileFormatType.Xlsx);

                // Get the first worksheet
                var worksheet = workbook.worksheets.get(0);

                // Add some data
                worksheet.cells.get("A1").putValue("Hello World");
                worksheet.cells.get("A2").putValue("Created with Aspose.Cells for JavaScript");
                worksheet.cells.get("B1").putValue(42);

                // Save as Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);

                // Create download link
                const blob = new Blob([outputData]);
                const downloadLink = document.createElement('a');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.textContent = 'Download Excel File';
                downloadLink.download = "my-excel-file.xlsx";
                downloadLink.style.display = 'block';

                const output = document.getElementById('output');
                output.innerHTML = '';
                output.appendChild(downloadLink);
            };
        }).catch(error => {
            console.error("Error initializing Aspose.Cells:", error);
        });
    </script>
</html>
{{< /highlight >}}

**Tarayıcı örneğini çalıştırmak için:**

{{< highlight bash >}}
# Start HTTP server
http-server -p 8080

# Open browser and visit:
# http://localhost:8080
{{< /highlight >}}

### Node.js Kullanımı

Bir `node-example.js` dosyası oluşturun:

{{< highlight javascript >}}
const { AsposeCells, Workbook, SaveFormat, FileFormatType } = require("aspose.cells.js");
const fs = require('fs');

// Initialize Aspose.Cells with license
AsposeCells.onReady({
    license: "aspose.cells.enc",  // Path to your encrypted license
    fontPath: "./fonts/"         // Optional: path to system fonts
}).then(() => {
    console.log("Aspose.Cells initialized successfully!");

    // Create a new workbook
    const workbook = new Workbook(FileFormatType.Xlsx);

    // Get the first worksheet
    const worksheet = workbook.worksheets.get(0);

    // Add data to cells
    worksheet.cells.get("A1").putValue("Product");
    worksheet.cells.get("B1").putValue("Price");
    worksheet.cells.get("A2").putValue("Apple");
    worksheet.cells.get("B2").putValue(1.99);
    worksheet.cells.get("A3").putValue("Orange");
    worksheet.cells.get("B3").putValue(2.49);

    // Save as Excel file
    const excelData = workbook.save(SaveFormat.Xlsx);
    fs.writeFileSync('output.xlsx', Buffer.from(excelData));
    console.log('Excel file saved as output.xlsx');

    // Save as PDF
    const pdfData = workbook.save(SaveFormat.Pdf);
    fs.writeFileSync('output.pdf', Buffer.from(pdfData));
    console.log('PDF file saved as output.pdf');

}).catch(error => {
    console.error("Error:", error);
});
{{< /highlight >}}

**Node.js örneğini çalıştırmak için:**

{{< highlight bash >}}
node node-example.js
{{< /highlight >}}

## **Yaygın Dosya İşlemleri**

### Varolan Bir Excel Dosyasını Okuma

{{< highlight javascript >}}
// Browser (using File input)
const fileInput = document.getElementById('fileInput');
fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    reader.onload = (e) => {
        const arrayBuffer = e.target.result;
        const workbook = new Workbook(new Uint8Array(arrayBuffer));
        // Process the workbook...
    };
    reader.readAsArrayBuffer(file);
});

// Node.js
const fs = require('fs');
const fileBuffer = fs.readFileSync('input.xlsx');
const workbook = new Workbook(fileBuffer);
{{< /highlight >}}

### Formatlar Arasında Dönüştürme

{{< highlight javascript >}}
// Convert Excel to PDF
const pdfData = workbook.save(SaveFormat.Pdf);

// Convert Excel to HTML
const htmlData = workbook.save(SaveFormat.Html);

// Convert Excel to CSV
const csvData = workbook.save(SaveFormat.Csv);

// Convert Excel to JSON
const jsonData = workbook.save(SaveFormat.Json);
{{< /highlight >}}

## **Sorun Giderme**

### Yaygın Problemler ve Çözümler

1. **"Modül bulunamadı" hatası**
   - HTTP sunucusunu doğru dizinden çalıştırdığınızdan emin olun
   - Komut dosyası src yolunun doğru konumu gösterdiğinden emin olun

2. **Lisans çalışmıyor**
   - `aspose.cells.enc` dosyasının doğru yerde olduğundan emin olun
   - Şifreli lisans dosyasının düzgün şekilde oluşturulduğunu kontrol edin
   - Orijinal lisans dosyasının geçerli ve süresi dolmamış olduğunu doğrulayın

3. **Tarayıcıda CORS sorunları**
   - Her zaman bir HTTP sunucusu kullanın, HTML dosyalarını doğrudan açmayın
   - Yerel geliştirme için `http-server` veya benzeri araçları kullanın

### Yardım Almak

Sorun yaşarsanız:
- [Aspose.Cells belgelerine](https://docs.aspose.com/cells/javascript-cpp/) bakın
- Topluluk desteği için [Aspose Forumları](https://forum.aspose.com/c/cells/9)’nu ziyaret edin
- Lisans bilgilerinizle Aspose Destek ile iletişime geçin

## **Sonraki Adımlar**

- Ayrıntılı belge için [API Referansı](https://reference.aspose.com/cells/javascript-cpp/)na göz atın
- Grafikler, formüller ve biçimlendirme gibi gelişmiş özellikleri öğrenin
- Belgede daha fazla örnek ve eğitimleri inceleyin
- Mevcut web uygulamalarınız veya yapı araçlarınız ile entegre etmeyi düşünün
