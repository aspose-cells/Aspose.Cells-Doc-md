---
title: JavaScript ile C++ kullanarak Elektronik Tablo biçimlerini yapılandırma
linktitle: Yayınlanan İşlenmiş Elektronik Tablolar için Yazı Tiplerini Yapılandırma
type: docs
weight: 10
url: /tr/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Aspose.Cells for JavaC++ betiği kullanarak elektronik tabloların yazı tiplerini nasıl yapılandıracağınızı öğrenin. En iyi dönüştürme doğruluğu için yazı tiplerinin mevcut olduğundan emin olun.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells API’leri, elektronik tabloları görüntü biçiminde render etme ve PDF & XPS formatlarına dönüştürme özelliği sağlar. Dönüşüm doğruluğunu artırmak için, elektrik tablosunda kullanılan yazı tiplerinin işletim sisteminin varsayılan yazı tipi dizininde bulunması gerekir. Gerekli yazı tipleri yoksa, Aspose.Cells API'leri gerekli yazı tiplerini kullanılabilir olanlarla değiştirmeye çalışacaktır.

## **Yazı Tiplerinin Seçimi**

Aspose.Cells API'ları tarafından perde arkasında izlenen süreç aşağıda belirtilmiştir.

1. API, elektronik tabloda kullanılan tam olarak eşleşen yazı tipini dosya sistemi üzerinde bulmaya çalışır.
2. API, aynı ebeveyn düğümü altında kullanılan varsayılan yazı tipini belirleyebilecek olan [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) özelliği altında belirtilen varsayılan yazı tipini kullanmaya çalışır.
3. API, yazı tipini belirleyemiyorsa, [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) veya [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) özelliği altında belirtilen yazı tipini kullanmaya çalışır.
4. API, yazı tipini belirleyemiyorsa, [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) özelliği altında belirtilen yazı tipini kullanmaya çalışır.
1. API, [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--) özelliği altında tanımlanan yazı tipi bulunamazsa, mevcut yazı tiplerinden en uygun olanını seçmeye çalışır.
1. Son olarak, API dosya sisteminde herhangi bir yazı tipi bulamazsa, çalışsayı Arial kullanarak elektronik tabloyu oluşturur.

## **Özel Yazı Tipi Klasörlerini Ayarlayın**

Aspose.Cells API’leri, işletim sisteminin varsayılan yazı tipi dizininde gerekli yazı tiplerini arar. Gerekli yazı tipleri mevcut değilse, API’ler özel (kullanıcı tanımlı) dizinlerde arama yapar. [**FontConfigs**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs) sınıfı, özel yazı tipi dizinleri ayarlamak için çeşitli yollar sunar.

1. [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-): Bu yöntem, sadece bir klasör ayarlanacaksa kullanışlıdır.
1. [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-): Bu yöntem, yazı tiplerinin birden fazla klasörde bulunduğu durumda ve kullanıcı tüm klasörleri tek tek birleştirmek yerine ayrı ayrı ayarlamak istediğinde kullanışlıdır.
1. [**FontConfigs.fontSources(FontSourceBase[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources-fontsourcebasearray-): Bu mekanizma, kullanıcının birden fazla klasörden veya tek bir yazı tipi dosyasından veya bayt dizisinden yazı tiplerini yüklemek istemesi durumunda kullanışlıdır.

{{% alert color="primary" %}}

[**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-) ve [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-) yöntemleri her ikisi de ikinci olarak gelen Boolean türünde bir parametre kabul eder. İkinci parametre olarak **true** geçmek, Aspose.Cells API'lerini yazı tipleri dosyalarını aramak için alt klasörlere yönlendirir.

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Font Configuration Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Font Configuration Example</h1>
        <p>Select an Excel file (optional) and font resources to configure Aspose.Cells font sources in the browser.</p>

        <label>Excel File (optional):</label>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>

        <label>Font File (.ttf/.otf) (optional):</label>
        <input type="file" id="fontFileInput" accept=".ttf,.otf" />
        <br/><br/>

        <label>Font Folder (optional, select a folder):</label>
        <input type="file" id="fontFolderInput" webkitdirectory directory multiple />
        <br/><br/>

        <button id="runExample">Configure Fonts</button>
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
            const fontFileInput = document.getElementById('fontFileInput');
            const fontFolderInput = document.getElementById('fontFolderInput');
            const resultDiv = document.getElementById('result');

            // Basic validation: ensure at least one font resource is provided (file or folder)
            if (!fontFileInput.files.length && !fontFolderInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select at least one font file or a font folder.</p>';
                return;
            }

            // Defining string variables to store paths/names to font folders & font file
            // (In browser environment we use simple names or uploaded file names)
            const fontFolder1 = "Arial";
            const fontFolder2 = "Calibri";
            const fontFile = "arial.ttf";

            // Setting first font folder (converted from setFontFolder)
            AsposeCells.FontConfigs.fontFolder = fontFolder1;
            // Preserve the subfolder-search flag from original API call as a separate property
            AsposeCells.FontConfigs.fontFolderSearchSubFolders = true;

            // Setting both font folders (converted from setFontFolders)
            AsposeCells.FontConfigs.fontFolders = [fontFolder1, fontFolder2];
            // Preserve the subfolder-search flag as a separate property
            AsposeCells.FontConfigs.fontFoldersSearchSubFolders = false;

            // Defining FolderFontSource
            const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

            // Defining FileFontSource
            const sourceFile = new AsposeCells.FileFontSource(fontFile);

            // Defining MemoryFontSource
            let memoryFontBytes = new Uint8Array([]);
            if (fontFileInput.files.length) {
                const ff = fontFileInput.files[0];
                const arrayBuffer = await ff.arrayBuffer();
                memoryFontBytes = new Uint8Array(arrayBuffer);
            } else if (fontFolderInput.files.length) {
                // If a folder was provided, try to find a .ttf/.otf inside it and use the first found
                const files = Array.from(fontFolderInput.files);
                const fontCandidate = files.find(f => f.name.toLowerCase().endsWith('.ttf') || f.name.toLowerCase().endsWith('.otf'));
                if (fontCandidate) {
                    const arrayBuffer = await fontCandidate.arrayBuffer();
                    memoryFontBytes = new Uint8Array(arrayBuffer);
                }
            }
            const sourceMemory = new AsposeCells.MemoryFontSource(memoryFontBytes);

            // Setting font sources (converted from setFontSources)
            AsposeCells.FontConfigs.fontSources = [sourceFolder, sourceFile, sourceMemory];

            // Provide feedback to the user
            resultDiv.innerHTML = '<p style="color: green;">Font configuration applied successfully.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Lütfen uygulamanın başlangıcında yukarıda belirtilen yöntemlerden herhangi birini kullanın; diğer Aspose.Cells API nesnelerini çağırmadan önce.

{{% /alert %}} {{% alert color="primary" %}}

Yukarıda bahsedilen tüm yöntemler, yazı tiplerini ayarlamak için kullanıldığında, sadece son ayarlamalar etkili olacaktır.

{{% /alert %}}

## **Yazı Tipi Yedekleme Mekanizması**

Aspose.Cells API’leri ayrıca, render işlemi için yer değiştiren yazı tipi belirleme imkanını da sağlar. Bu mekanizma, dönüşüm sırasında gereken yazı tipi sistemde mevcut değilse faydalıdır. Kullanıcılar, orijinal gerekli yazı tipi yerine kullanılacak font adlarının listesini sağlayabilir. Bunu başarmak için, Aspose.Cells API'leri, 2 parametre kabul eden [**FontConfigs.fontSubstitutes(string, string[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-stringarray-) yöntemini açığa çıkarmıştır. Birinci parametre, **string** türünde olmalı ve değiştirilmesi gereken yazı tipinin adını temsil etmelidir. İkinci parametre ise, **string** türünde bir dizidir. Kullanıcılar, orijinal font adı yerine kullanılacak font isimlerinin listesini sağlayabilir.

İşte basit bir kullanım senaryosu.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Substituting the Arial font with Times New Roman & Calibri
            // Converted from: AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
            AsposeCells.FontConfigs.fontSubstitutes = { "Arial": ["Times New Roman", "Calibri"] };

            // Saving the (possibly modified) workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the processed file.</p>';
        });
    </script>
</html>
```

## **Bilgi Toplama**

Yukarıda bahsedilen yöntemlere ek olarak, Aspose.Cells API’leri, hangi kaynakların ve yer değiştirmelerin ayarlandığını gösteren bilgiler toplamaya da imkan sağlar.

1. [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) metodu, belirtilen font kaynaklarının listesini içeren [**FontSourceBase**](https://reference.aspose.com/cells/javascript-cpp/fontsourcebase) türünde bir dizi döndürür. Hiç kaynak ayarlanmadıysa, [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) metodu boş bir dizi döndürür.
1. [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) metodu, yerine koyma işlemi yapılmış yazı tipi adını belirtmek için **string** türünde bir parametre kabul eder. Belirtilen yazı tipi için yer değiştirme ayarlanmadıysa, [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) metodu null döner.

## **Gelişmiş Konular**
- [Yaygın Olarak Kullanılan Yazı tipini Resimlere Dönüştürürken Belirleme](/cells/tr/javascript-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [PdfSaveOptions ve ImageOrPrintOptions'ın DefaultFont özelliğini öncelikli şekilde ayarlayın](/cells/tr/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Desteklenen Yazı Tipi Biçimleri](/cells/tr/javascript-cpp/supported-font-formats/)
- [Elektronik Tabloyu Görüntüye - Görüntülenen Görüntü İçin Pixel Biçimini Ayarlama](/cells/tr/javascript-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
