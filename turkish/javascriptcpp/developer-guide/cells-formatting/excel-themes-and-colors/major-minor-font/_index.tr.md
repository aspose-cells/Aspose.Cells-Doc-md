---
title: Başlık ve Metin Tema Yazı Tipi
linktitle: Başlık ve Metin Tema Yazı Tipi
description: Aspose.Cells, C++ ile JavaScript kitaplığıdır ve elektronik tablo dosyalarıyla çalışmayı sağlar. Excel belgelerinde başlık ve gövde tema fontlarını ayarlamayı destekler, böylece kullanıcıların belgenin görünüm ve stilini özelleştirmesine olanak tanır. Bu makale, Aspose.Cells kitaplığını kullanarak Excel belgelerinde başlık ve gövde tema fontlarıyla nasıl çalışılacağını tanıtacaktır.
keywords: Aspose.Cells, Excel Belgesi, Başlık, Gövde, Tema Fontu, Görünüm, Stil, JavaScript C++ ile
type: docs
weight: 120
url: /tr/javascript-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Varsayılan yazı tipi, bölge ayarı değiştirildiğinde otomatik olarak değişecektir.

Varsayılan yazı tipinin değişmesine ne sebep oldu?

Varsayılan yazı tipinin değişmesine ne sebep oldu?

Excel tema yazı tipi ayarlandığında, Excel mevcut dil ortamına göre farklı yazı tipleri arasında otomatik olarak geçiş yapacaktır.

{{% /alert %}}

## **Excel'de, Ana Menü sekmesini seçin, yazı tipi açılır kutusuna tıklayın, İngilizce bölge ayarıyla en üstte iki tema yazı tipi : Üstbilgi (Calibri Light) ve Metin (Calibri) göreceksiniz.**

Excel'de, Ana Sayfa sekmesini seçin, yazı tipi açılır kutusuna tıklayın, "Tema Yazı Tipleri" göreceksiniz; üstte İngiliz bölge ayarına sahip olarak Kalibri Hafif (Başlıklar) ve Kalibri (Gövde) iki tema yazı tipi bulunur.

**![Tema Yazı Tipleri](Theme-Fonts.png)**

Eğer Tema Yazı Tipi seçilirse, font adı farklı bölgelerde farklı görünebilir. Yazı tipinin farklı bölgelerde otomatik değişmesini istemiyorsanız, iki Tema Yazı Tipi seçmeyin.

## **Başlıklar Ve Gövde Yazı Tiplerini Programatik Olarak Değiştirme**
C++ ile Aspose.Cells for JavaScript'i kullanarak varsayılan fontun tema fontu olup olmadığını kontrol edebilir veya [**Font.schemeType**](https://reference.aspose.com/cells/javascript-cpp/font/#schemeType-fontschemetype-) yöntemi ile tema fontu ayarlayabiliriz.

Aşağıdaki örnek kod, tema yazı tiplerini nasıl manipüle edeceğinizi gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Theme Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FontSchemeType, Utils } = AsposeCells;

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

            // Accessing and modifying the default style and its font scheme
            let defaultStyle = workbook.defaultStyle;
            let font = defaultStyle.font;
            let schemeType = font.schemeType;

            if (schemeType === FontSchemeType.Major || schemeType === FontSchemeType.Minor) {
                console.log("It's theme font");
            }

            // Change theme font to normal font
            font.schemeType = FontSchemeType.None;

            // Assign the modified default style back to the workbook
            workbook.defaultStyle = defaultStyle;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Theme font changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **Dinamik olarak, Yerel Tema Yazı Tipini Programatik Olarak Almak**
Bazı durumlarda, sunucularımız ve kullanıcı makineleri aynı bölgede değildir. Kullanıcıların dosya işleme için istediği aynı yazı tipini nasıl elde edebiliriz?

Çalıştırmadan önce, sistem bölge ayarlarını [**LoadOptions.region**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#region-countrycode-) metoduyla ayarlamalısınız.

Aşağıdaki örnek kod, yerel tema yazı tipini nasıl alacağımızı göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Default Style Local Font Example</h1>
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

            // Instantiate a new LoadOptions.
            const options = new AsposeCells.LoadOptions();
            // Sets the customer's region
            options.region = AsposeCells.CountryCode.Japan;

            // Instantiate a new Workbook using the uploaded file and load options.
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Get the default style
            const defaultStyle = workbook.defaultStyle;

            // Gets customer's local font.
            const localFontName = defaultStyle.font.name;

            resultDiv.innerHTML = `<p style="color: green;">Local font name: ${localFontName}</p>`;
        });
    </script>
</html>
```
