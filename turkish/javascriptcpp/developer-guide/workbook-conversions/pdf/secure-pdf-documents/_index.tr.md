---
title: JavaScript aracılığıyla C++ kullanarak Güvenli PDF Belgeleri
linktitle: Güvenli PDF Belgeleri
type: docs
weight: 120
url: /tr/javascript-cpp/secure-pdf-documents/
description: PDF belgelerini sahibi ve kullanıcı şifreleri kullanarak güvenli hale getirmeyi ve PDF dosyaları için izinleri ayarlamayı öğrenin, Aspose.Cells for JavaScript kullanarak C++ aracılığıyla.
---

{{% alert color="primary" %}}

Bazı durumlarda, geliştiriciler şifrelenmiş PDF dosyalarıyla çalışmak zorunda kalabilir. Örneğin:

- Belgeleri sahip ve kullanıcı şifreleri ile güvence altına almak, böylece herkes tarafından açılamamasını sağlamak.
- Doküman açıldıktan sonra kısıtlamalar veya izinler belirlemek. Örneğin: doküman içeriğinin yazdırılabilir veya çıkarılabilir olup olmadığını sınırlamak.

Bu makale, elektronik tabloları PDF'ye kaydederken PDF güvenlik seçeneklerini nasıl geçireceğinizi açıklar.

{{% /alert %}}

 Aspose.Cells, güvenlikle ilgili işler için [**PdfSecurityOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsecurityoptions/) sağlar. PDF'ye kaydederken sahibi ve kullanıcı şifreleri ayarlayabilirsiniz. Şifreler, şifreli PDF dosyasını görüntülemek için gerekli olacaktır.

- Kullanıcı şifresi boş veya null olabilir; bu durumda, PDF dosyasını açarken kullanıcıdan şifre istenmez.
Doğru sahip şifresi ile PDF belgeyi açmak belgeye tam erişim sağlar (belirtilen herhangi bir erişim kısıtlaması olmadan).
- Doğru kullanıcı parolasıyla PDF belgesinin doğru şekilde açılması (veya herhangi bir kullanıcı parolası olmayan bir belgenin açılması) belirtilen izinlerle sınırlı erişim sağlar.

Aşağıdaki örnek kod, Aspose.Cells ile PDF'leri güvence altına alma işlemi hakkında bilgi verir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Secure PDF Example</title>
    </head>
    <body>
        <h1>Secure PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfSecurityOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PDF save options and security options
            const saveOption = new PdfSaveOptions();
            saveOption.securityOptions = new PdfSecurityOptions();

            // Set security options (converted from getters/setters to properties)
            saveOption.securityOptions.userPassword = "user";
            saveOption.securityOptions.ownerPassword = "owner";
            saveOption.securityOptions.extractContentPermission = false;
            saveOption.securityOptions.printPermission = false;

            // Save the workbook to PDF with security options
            const outputData = workbook.save(SaveFormat.Pdf, saveOption);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'securepdf_test.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Secure PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the secured PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Eğer elektronik tablo formüller içeriyorsa, PDF olarak dışa aktarmadan hemen önce [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)çağrısı yapmak en iyisidir. Böylece formüle bağlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
