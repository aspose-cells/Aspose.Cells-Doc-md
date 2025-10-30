---
title: Hücreleri Kilitleyerek Korumak için Nasıl Yapılır
type: docs
weight: 130
url: /tr/javascript-cpp/how-to-lock-cells-to-protect-them/
description: Bu makale, Aspose.Cells for JavaScript kullanarak hücreleri kilitleme ve koruma nasıl yapılır gösteren kodları içermektedir.
keywords: Javascript ile Hücreleri Kilitle ve Koruma, Javascript kullanarak Hücreleri Nasıl Kilitlerim, Javascript te Hücreleri Korumak için Kilitle.
---

## **Olası Kullanım Senaryoları**
Hücreleri korumak için kilitlemek, Microsoft Excel veya Google Sheets gibi elektronik tablo uygulamalarında sık kullanılan önemli bir uygulamadır çünkü birçok önemli nedeni vardır:

1. Kazara Değişiklikleri Önleme: Hücreleri kilitlemek, kullanıcıların önemli veri veya formülleri kazara değiştirmesini önleyebilir. Bu, karmaşık tablolarda istenmeyen değişikliklerin ciddi hatalara yol açabileceği durumlarda özellikle faydalıdır.

1. Veri Bütünlüğünü Sağlama: Hücreleri kilitleyerek, kritik verilerin tutarlığını ve doğruluğunu koruyabilirsiniz. Bu, finansal belgeler, raporlar ve veri bütünlüğünün önemli olduğu diğer belgeler için çok önemlidir.

1. Kontrollü Erişim: İşbirliği ortamlarında, hücreleri kilitlemek, belirli alanlara kimlerin erişebileceğini kontrol etmenize olanak sağlar. Örneğin, yalnızca belirli ekip üyelerinin belirli hücreleri düzenlemesine izin verirken, diğer bütün sayfayı koruyabilirsiniz.

1. Formülleri Korumak: Formüller hesaplamalar ve veri analizi için genellikle kritiktir. Formülleri içeren hücreleri kilitlemek, bu formüllerin kazara değiştirilmesini veya silinmesini engeller; bu, bütün sayfa üzerindeki fonksiyonelliği bozabilir.

1. İş Kurallarını Zorunlu Kılmak: Bazı durumlarda, belirli iş kuralları veya mevzuatlar, verilerin değiştirilmesinin engellenmesini gerektirebilir. Hücreleri kilitlemek, bu gereksinimlere uyumu sağlar.

1. Kullanıcıları Yönlendirme: Hücreleri kilitleyerek ve hangi hücrelerin düzenlenebileceğine dair net talimatlar sağlayarak kullanıcıların tabloyla etkileşimde nasıl bulunacaklarını yönlendirebilirsiniz, bu da karışıklığı ve hataları azaltır.

## **Excel'de Hücreleri Kilitleyerek Nasıl Korumak Yapılır**
İşte Microsoft Excel'de hücreleri kilitlemenin yolu:

1. Kilitlemek İstediğiniz Hücreleri Seçin: Kilitlemek istediğiniz hücreleri seçin. Bütün sayfayı kilitlemek istiyorsanız, bu adımı atlayabilirsiniz.
1. Hücreleri Biçimlendirme Diyaloğunu Açın: Seçilen hücrelere sağ tıklayın ve "Hücreleri Biçimlendir" seçeneğini seçin veya Ctrl+1 tuşlarına basın.
<br>
<img src="1.png" width=60% />
1. Hücreleri Kilitleyin: Hücreleri biçimlendirme diyaloğunda, "Koruma" sekmesine gidin. "Kilitle" kutusunu işaretleyin. "Tamam" düğmesine tıklayın.
1. Sayfayı Koruyun: Şerit üzerindeki "Gözden Geçir" sekmesine gidin. "Sayfayı Koru" seçeneğine tıklayın. Bir şifre belirleyin (isteğe bağlı) ve izin vermek istediğiniz işlemleri seçin (ör. kilitli hücreleri seçme, hücreleri biçimlendirme vb.). "Tamam" düğmesine tıklayın.
<br>
<img src="2.png" width=60% />

## **Javascript kullanarak Hücreleri Korumak İçin Nasıl Kilitlerim**

Aspose.Cells, Excel dosyalarıyla programatik olarak çalışmak için güçlü bir kitaplıktır. Aspose.Cells for JavaScript kullanarak hücreleri kilitlemek için şu adımları izleyin: [örnek dosyayı](sample.xlsx) yükleyin, önce tüm hücreleri kilidini açın (varsayılan olarak tüm hücreler kilitlidir ancak koruma yapılmadıkça zorunlu değildir), ardından korumak istediğiniz özel hücreleri kilitleyin ve son olarak çalışma sayfasını koruyarak kilitleri uygulayın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Protect Worksheet Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unlock all cells first
            const unlockStyle = workbook.createStyle();
            unlockStyle.isLocked = false;

            const styleFlag = new StyleFlag();
            styleFlag.locked = true;
            sheet.cells.applyStyle(unlockStyle, styleFlag);

            // Lock specific cells (e.g., A1 and B2)
            const lockStyle = workbook.createStyle();
            lockStyle.isLocked = true;

            sheet.cells.get("A1").style = lockStyle;
            sheet.cells.get("B2").style = lockStyle;

            // Protect the worksheet to enforce the locking
            sheet.protect(ProtectionType.All);

            // Save the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet protected and cells locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Sonuç Çıktısı**
Bu kod, sadece belirtilen hücrelerin (örneğin A1 ve B2) kilitlendiğinden emin olur ve bu ayarların uygulanması için sayfa korumasını sağlar. Sayfanın diğer tüm hücreleri kilitsiz ve düzenlenebilir kalır.

<br>
<img src="3.png" width=60% />
