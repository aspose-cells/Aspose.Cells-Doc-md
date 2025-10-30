---
title: Excel elektronik tablo dosyalarının ayarlarını JavaScript ile C++ kullanarak yönetin.
linktitle: Çalışma Kitabı Ayarları
type: docs
weight: 185
url: /tr/javascript-cpp/workbook-settings/
description: Aspose.Cells for JavaScript kullanarak C++ ile Excel dosyalarının ayarlarını yönetin.
---

## **Çalışma Kitabı Ayarları Genel Bakış**
Excel dosyalarıyla çalışma, programatik olarak çeşitli ayarların yönetilmesini içerir ve Aspose.Cells for JavaScript kullanılarak C++ ile yapılabilir. Bu belge, bu ayarları etkili bir şekilde yönetmenin yollarını özetler.

## **Olası Kullanım Senaryoları**
Aşağıdaki senaryolar, çalışma kitabı ayarlarını yönetmenizi gerektirebilecek durumları göstermektedir:
- Görünüm seçeneklerini ayarlama
- Hesaplama modunu ayarlama
- Sayfa düzeni parametrelerini yapılandırma

## **Aspose.Cells for JavaScript kullanarak C++ ile Çalışma Kitabı Ayarlarını Yönetmek**
Bu örnek, hesaplama seçenekleri ve görüntü ayarları gibi çalışma kitabı ayarlarını nasıl yöneteceğinizi gösterir.

1. Yeni bir çalışma kitabı oluşturun veya mevcut bir tane yükleyin.
2. Gereksinimlerinize göre çalışma kitabı ayarlarını değiştirin.
3. Değişiklikleri kalıcı kılmak için çalışma kitabını kaydedin.

### **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Workbook Settings Example</h1>
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
            // Create a new workbook
            const workbook = new Workbook();

            // Access the settings of the workbook
            const settings = workbook.settings;
            settings.calculationMode = 1; // Manual calculation

            // Display options
            settings.showGridLines = false; // Disable gridlines

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkbookSettingsExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Anahtar Çalışma Kitabı Ayarları Özellikleri ve Yöntemleri**
Aspose.Cells for JavaScript ile C++ çeşitli özellikler ve metodlar sağlayarak çalışma kitabı ayarlarını ayarlamayı kolaylaştırır:
- **Workbook.settings**: Çalışma kitabının ayarlarını erişin.
- **Settings.calculationMode**: Çalışma kitabı için hesaplama modunu ayarlayın.
- **Settings.showGridLines**: Ekranda ızgara çizgilerini etkinleştir veya devre dışı bırakın.

## **Sonuç**
C++ ile Aspose.Cells for JavaScript kullanarak çalışma kitabı ayarlarını yönetmek kolaydır ve Excel dosyası davranışlarını özelleştirmek için birçok seçenek sunar. Mevcut ayarları kullanarak, çalışma kitabını ihtiyaçlarınıza göre uyarlayabilirsiniz.
