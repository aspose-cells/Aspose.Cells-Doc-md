---
title: JavaScript ve C++ ile Şekilleri Kilitlemek veya Kilidini Açmak
linktitle: Şekilleri kilitle veya kilidi aç
type: docs
weight: 200
url: /tr/javascript-cpp/lock-or-unlock-shapes/
description: Bu makale, Aspose.Cells kütüphanesi kullanarak JavaScript ve C++ ile şekilleri nasıl kilitleyip açacağınızı göstermek için kodlar içerir.
keywords: JavaScript ve C++ kullanarak şekilleri kilitleme veya kilidini açma, şekilleri korumak için nasıl kilitleneceği veya açılacağı hakkında bilgi.
---

## **Olası Kullanım Senaryoları**

Bazı durumlarda, istenmeyen durumlar tarafından yok edilmekten korumak için belirli çalışma sayfalarındaki tüm şekilleri korumanız gerekebilir. Bu durumda, belirtilen çalışma sayfasındaki tüm şekilleri kilitlemeniz gerekir. 

Bir elektronik tabloda veya dokümanda şekillerin kilitlenmesi çeşitli nedenlerle faydalı olabilir:
1. Kazara Değişiklikleri Önleme: Şekilleri kilitlemek, kullanıcıların bunları kazara taşımalarını, yeniden boyutlandırmalarını veya silmelerini engeller. Bu, şekillerin açıklama, çizim veya dokümanın tasarımının bir parçası olarak kullanıldığı karmaşık belgelerde özellikle önemlidir.
1. Düzeni ve Tasarımı Koru: Şekiller genellikle bir belgenin düzeninde ve görsel tasarımında önemli rol oynar. Bunları kilitlemek, istenen görünümü koruyarak, belgenin profesyonel ve görsel olarak çekici kalmasını sağlar.
1. Veri Bütünlüğü: Elektronik tablolarda, şekiller önemli veri noktalarını vurgulamak, yorum eklemek veya görsel açıklamalar yapmak için kullanılabilir. Bu şekillerin kilitlenmesi, sağladıkları bağlamsal bilginin doğru ve bütün kalmasını sağlar.
1. Paylaşılan Belgelerde Tutarlılık: Birlikte çalışırken, farklı kullanıcıların uzmanlık seviyeleri farklı olabilir. Şekillerin kilitlenmesi, beklenmedik değişiklikleri engelleyerek belgenin tutarlılığını korumaya yardımcı olur.
1. Güvenlik: Hassas belgelerde şekillerin kilitlenmesi, bilgileri korumak için daha geniş bir stratejinin parçası olabilir. Örneğin, finansal raporlarda veya yasal belgelerde, kilitli şekiller, kritik bağlam sağlayan açıklamaları veya vurguları korumak için kullanılabilir.

Bazen, belirli korumalı çalışma sayfalarında bazı şekilleri değiştirebilmeniz gerekebilir; bu durumda, bu şekilleri kilidini çözmeniz gerekir. Bu makale, belirli şekillerin nasıl kilitlenip kilidinin açılacağını ayrıntılı şekilde tanıtacaktır.

## **Excel'de Şekilleri Nasıl Kilitlersiniz ve Korursunuz**

İşte Microsoft Excel'de hücreleri kilitlemenin yolu:

1. Excel Dosyanızı Açın: Kilitlemek istediğiniz şekillerin bulunduğu Excel dosyasını açın.

1. Şekli Seçin: Kilitlemek istediğiniz şekle tıklayın. Ayrıca, Ctrl tuşunu basılı tutarak birden çok şekli de seçebilirsiniz.

1. Şekil Biçimlendirme Panelini Açın: Seçilen şekle sağ tıklayın ve "Boyut ve Özellikler"i seçin. Alternatif olarak, Şerit üzerindeki "Biçim" sekmesine gidip "Boyut" grubundan, küçük ok işaretine tıklayarak "Şekil Biçimi" panelini açabilirsiniz.
1. Şekli Kilitleyin: "Şekil Biçimi" panelinde, "Boyut ve Özellikler" sekmesine (kare ve ok işareti gibi görünen ikon) gidin. "Özellikler" bölümünde, "Kilitle" kutusunu işaretleyin.
<br>
<img src="1.png" width=60% />
1. Sayfayı Koruyun: Şerit üzerindeki "Gözden Geçir" sekmesine gidin. "Sayfayı Koru" seçeneğine tıklayın. Bir şifre belirleyin (isteğe bağlı) ve izin vermek istediğiniz işlemleri seçin (ör. kilitli hücreleri seçme, hücreleri biçimlendirme vb.). "Tamam" düğmesine tıklayın.
<br>
<img src="2.png" width=60% />

## **Belirli bir çalışma sayfasındaki tüm şekilleri nasıl kilitlersiniz**

Bütün şekilleri korunan bir çalışma sayfasında kilitlemek için, aşağıdaki örnek kodda gösterildiği gibi `worksheet.protect(ProtectionType.Objects)` metodunu kullanabilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Lock Shapes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const text = "This is a test";
            const worksheet = workbook.worksheets.get(0);

            let shape = worksheet.shapes.addTextBox(1, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addRectangle(5, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addButton(9, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addOval(13, 0, 1, 0, 50, 100);
            shape.text = text;

            // Protect all shapes in the specified worksheet
            shape.worksheet.protect(ProtectionType.Objects);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shapes locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Korunan bir çalışma sayfasında belirli şekillerin kilidini nasıl açarsınız**

Korunan bir çalışma sayfasında belirli bir şekli çözmek için, `shape.isLocked` kullanılır, aşağıdaki örnek kodda gösterildiği gibi.

Not: `shape.isLocked` yalnızca çalışma sayfası korunduğunda anlamlıdır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Unlock Shape</title>
    </head>
    <body>
        <h1>Unlock Shape Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get protected worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the specified shape to be unlocked
            const shape = worksheet.shapes.get("TextBox 1");

            if (!shape) {
                resultDiv.innerHTML = '<p style="color: red;">Shape "TextBox 1" not found.</p>';
                return;
            }

            // Unlock the specified shape
            if (!worksheet.protection.allowEditingObject && shape.isLocked) {
                shape.isLocked = false;
            }

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'UnLocked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape unlocked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
