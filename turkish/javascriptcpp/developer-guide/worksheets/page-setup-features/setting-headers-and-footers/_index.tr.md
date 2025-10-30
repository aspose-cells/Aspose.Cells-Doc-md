---
title: Başlık ve Altbilgi Ayarları JavaScript ile C++ kullanarak
linktitle: Başlık ve Altbilgileri Ayarlama
type: docs
weight: 30
url: /tr/javascript-cpp/setting-headers-and-footers/
description: Bu makale, Aspose.Cells for JavaScript kullanarak Excel çalışma sayfalarının başlık ve altbilgilerine programlı olarak görüntü eklemenin nasıl yapıldığını açıklamaktadır. 
keywords: excel başlık altbilgiye resim ekleme JavaScript ve C++ kullanımı, excel başlık ve altbilgi script komutları JavaScript ve C++
---

{{% alert color="primary" %}}

Başlık ve altbilgiler, üst kenar boşluğunun altında veya alt kenar boşluğunun üstünde gösterilen metin satırlarıdır. Çalışma sayfalarına da başlık ve altbilgi eklemek mümkündür. Başlıklar ve altbilgiler, sayfa numarası, yazar adı, konu adı veya tarih ve saat gibi yararlı bilgileri göstermek için kullanılabilir. Başlıklar ve altbilgiler, sayfa düzeni ayarları kullanılarak yönetilir.

{{% /alert %}}

## **Başlık ve Altbilgileri Ayarlama**

Aspose.Cells for JavaScript, C++ kullanarak çalışma sayfalarına başlık ve altbilgi eklemenize imkan verir, ancak baskı için önceden tasarlanmış bir dosyada manuel olarak başlık ve altbilgi ayarlamanızı öneririz. Microsoft Excel, başlık ve altbilgi ayarlamak için bir GUI aracı olarak kullanılabilir ve bu sayede zaman ve geliştirme maliyetlerinden tasarruf edebilirsiniz. Aspose.Cells dosyayı içe aktarabilir ve ayarları kaydedebilir.

Çalışma zamanında başlık ve altbilgiler eklemek için Aspose.Cells, özel API çağrıları ve betik komutları sağlar.

### **Betik Komutları**

Betik komutları, başlık ve altbilgi biçimlendirmesini ayarlamanıza olanak tanıyan özel komutlardır.

|**Betik Komutları**|**Açıklama**|
| :- | :- |
|&P| Geçerli sayfa numarası
|&G| Bir resim
|&N| Toplam sayfa sayısı
|&D| Geçerli tarih
|&T| Geçerli saat
|&A| Çalışma sayfası adı
|&F| Dosya adı ve yolu olmadan
|&&Yazı|&Yazıyı gösterir. Örneğin: &&WO &WO olarak görüntülenir|
|&"\<FontName>"| Yazı tipi adını temsil eder. Örneğin: &"Arial"|
|&"\<FontName>, \<FontStyle>"| Stil ile yazı tipi adını temsil eder. Örneğin: &"Arial,Kalın"|
|&\<FontSize>| Yazı tipi boyutunu temsil eder. Örneğin: “&14abc”. Ancak, bu komuttan sonra başlığa yazdırılacak düz bir sayı izlenecekse, bu, yazı tipi boyutundan bir boşluk karakteri ile ayrılmalıdır. Örneğin: “&14 123”.|

### **Başlık ve Altbilgileri Ayarlama**

[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) sınıfı, çalışma sayfasına başlık ve altbilgi eklemek için kullanılan [**header(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-string-) ve [**footer(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-string-) olmak üzere iki yöntem sağlar. Bu yöntemler yalnızca iki parametre alır:

- **Bölüm** – başlığın veya altbilginin yerleştirileceği bölüm. Sırasıyla sol, merkez ve sağ olmak üzere temsil edilen üç bölüm bulunmaktadır.
- **Betik** – başlık veya altbilgi için kullanılacak betik. Bu betik, başlıkları veya altbilgileri biçimlendirmek için betik komutları içerir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Set Headers and Footers Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;

            // Setting worksheet name at the left section of the header
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[0] = "&A";

            // Setting current date and current time at the central section of the header
            // and changing the font of the header
            pageSetup.header[1] = "&\"Times New Roman,Bold\"&D-&T";

            // Setting current file name at the right section of the header and changing the
            // font of the header
            pageSetup.header[2] = "&\"Times New Roman,Bold\"&12&F";

            // Setting a string at the left section of the footer and changing the font
            // of a part of this string ("123")
            pageSetup.footer = pageSetup.footer || [];
            pageSetup.footer[0] = "Hello World! &\"Courier New\"&14 123";

            // Setting the current page number at the central section of the footer
            pageSetup.footer[1] = "&P";

            // Setting page count at the right section of footer
            pageSetup.footer[2] = "&N";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetHeadersAndFooters_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Headers and footers set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Bir Resmi Başlık veya Altbilgiye Ekleyin**

[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) sınıfının, başlık ve altbilgiye görseller eklemek için kullanılan iki ek yöntemi, [**headerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#headerPicture-number-numberarray-) ve [**footerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footerPicture-number-numberarray-) bulunmaktadır. Bu yöntemler şu parametreleri alır:

- **Bölüm** – resmin yerleştirileceği başlık veya altbilgi bölümü. Sırasıyla sol, merkez ve sağ olmak üzere temsil edilen üç bölüm bulunmaktadır.
- **Bayt dizisi** – görsel veri (ikili veri bir byte dizisinin tamponuna yazılmalıdır).

Aşağıdaki kodu çalıştırdıktan sonra dosyayı açarak, çalışma sayfasının üstbilgisini kontrol edin:

1. **Dosya** menüsünde **Sayfa Düzeni**'ni seçin. Bir iletişim kutusu görüntülenecektir.
1. **Üst Bilgi/Alt Bilgi** sekmesini seçin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Image in Header/Footer Example</title>
    </head>
    <body>
        <h1>Insert Image in Header/Footer Example</h1>
        <p>Select an existing Excel file to modify (optional). If none is selected, a new workbook will be used.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>Select an image to insert into the header:</p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Insert Image into Header</button>
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert into the header.</p>';
                return;
            }

            // Read image bytes
            const imageFile = imageInput.files[0];
            const imageBuffer = await imageFile.arrayBuffer();
            const binaryData = new Uint8Array(imageBuffer);

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const excelBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(excelBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet's page setup
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Set the header picture and header scripts (converted from setters to properties)
            pageSetup.headerPicture = binaryData;
            pageSetup.header = "&G";
            pageSetup.header = "&A";

            // Save the workbook as Excel97-2003 (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertImageInHeaderFooter_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Image inserted into header successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
