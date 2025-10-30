---
title: JavaScript ile C++ kullanarak Başlık veya Altbilgi Alma
linktitle: Başlık veya Altlık Alınması
type: docs
weight: 30
url: /tr/javascript-cpp/get-headers-or-footers/
description: Bu makale, JavaScript via C++ API kullanarak Excel veya OpenOffice dosyalarından programatik olarak başlık ve altbilgilerin nasıl alınacağını açıklamaktadır.
---

{{% alert color="primary" %}}

Başlıklar ve altlıklar yalnızca Sayfa Düzeni görünümünde, Baskı Önizleme'de ve yazdırılan sayfalarda gösterilir. 

Ayrıca, birden fazla çalışma sayfasında başlıkları veya altlıkları görüntülemek istiyorsanız, Sayfa Düzeni iletişim kutusunu da kullanabilirsiniz. 

Grafik sayfaları veya grafikler gibi diğer sayfa türleri için, başlık ve altyazıları yalnızca Sayfa Düzeni iletişim kutusunu kullanarak ekleyebilirsiniz.

{{% /alert %}}

## **MS Excel'de Başlık ve Altlıkların Alınması**
1. Başlık veya altyazıları görüntülemek veya değiştirmek istediğiniz çalışma sayfasına tıklayın.
2. Görünüm sekmesinde, Çalışma Kitabı Görünümleri grubunda, Sayfa Düzeni'ne tıklayın.
   Excel, çalışma sayfasını Sayfa Düzeni görünümünde gösterir.
3. Bir başlık veya altlık görüntülemek veya düzenlemek için, çalışma sayfasının üstünde veya altında (Üstbilgi altında) sol, orta veya sağ başlık veya altlık metin kutusuna tıklayın.


## **Aspose.Cells for JavaScript kullanarak C++ ile Başlık ve Altbilgi Alma**
[**PageSetup.header(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-) ve [**PageSetup.footer(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-) metodlarıyla, JavaScript geliştiricileri dosyadan kolayca başlık veya altbilgi alabilir.

1. Dosyayı açmak için Bir Çalışma Kitabı oluşturun.
2. Başlık veya altbilgiyi almak istediğiniz çalışma sayfasını alın.
3. Belirli bir bölüm kimliği ile başlık veya altbilgiyi alın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Header/Footer Reader Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

        function escapeHtml(str) {
            if (str === null || str === undefined) return '';
            return String(str)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Gets left section of header
            const headerLeft = sheet.pageSetup.header(0);
            // Gets center section of header
            const headerCenter = sheet.pageSetup.header(1);
            // Gets right section of header
            const headerRight = sheet.pageSetup.header(2);
            // Gets center section of footer
            const footerCenter = sheet.pageSetup.footer(1);

            const resultHtml = [
                `<p><strong>Left Header:</strong> ${escapeHtml(headerLeft)}</p>`,
                `<p><strong>Center Header:</strong> ${escapeHtml(headerCenter)}</p>`,
                `<p><strong>Right Header:</strong> ${escapeHtml(headerRight)}</p>`,
                `<p><strong>Center Footer:</strong> ${escapeHtml(footerCenter)}</p>`
            ].join('');

            document.getElementById('result').innerHTML = resultHtml;
        });
    </script>
</html>
```

## **Başlık ve Altlıkları Komut Listesine Ayrıştır**
Başlık veya altbilgi metni, sayfa numarası, geçerli tarih veya metin biçimlendirme özellikleri gibi özel komutlar içerebilir.

Özel komutlar, önünde ampersand ("&") ile gösterilen tek harf ile temsil edilir.

Başlık ve altbilgi dizeleri, ABNF grameri kullanılarak oluşturulur. Bir görüntüleyici olmadan anlaması kolay değildir.

Aspose.Cells for JavaScript via C++, başlık ve altbilgileri komut listesi olarak ayrıştırmak için [**PageSetup.commands(string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#commands-string-) metodunu sağlar.

Aşağıdaki kodlar, başlık veya altbilgiyi komut listesi olarak ayrıştırma ve komutları işleme nasıl gösterileceğini gözler önüne serer:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Header/Footer Commands Example</title>
    </head>
    <body>
        <h1>Header/Footer Commands Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Gets left section of header
            const headerSection = sheet.pageSetup.header(0);
            const commands = sheet.pageSetup.commands(headerSection) || [];

            const items = [];
            commands.forEach(c => {
                const type = c.type;
                switch (type) {
                    case AsposeCells.HeaderFooterCommandType.SheetName:
                        // embedded the name of the sheet to header or footer
                        items.push('<li>SheetName command found (embeds sheet name)</li>');
                        break;
                    default:
                        items.push(`<li>Command type: ${type}</li>`);
                        break;
                }
            });

            if (!items.length) {
                items.push('<li>No header/footer commands found.</li>');
            }

            resultDiv.innerHTML = `<ul>${items.join('')}</ul>`;

            // Save the (possibly unchanged) workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HeaderFooter_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Workbook';
        });
    </script>
</html>
```
