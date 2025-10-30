---
title: JavaScript ile C++ kullanarak Sayfa Ayarları ve Yazdırma Seçenekleri
linktitle: Sayfa Düzeni ve Yazdırma Seçenekleri
type: docs
weight: 60
url: /tr/javascript-cpp/page-setup-and-printing-options/
---

{{% alert color="primary" %}}  
Bazı durumlarda, geliştiriciler yazdırma sürecini kontrol etmek için sayfa düzeni ve yazdırma ayarlarını yapılandırmak isteyebilir. Sayfa düzeni ve yazdırma ayarları çeşitli seçenekler sunar ve Aspose.Cells tarafından tamamen desteklenir.  

Bu makale, C++ ile JavaScript kullanarak bir konsol uygulaması oluşturmayı ve birkaç basit satır kodla Aspose.Cells API'si kullanarak bir sayfa öğesine sayfa ayarları ve yazdırma seçenekleri uygulamayı gösterir.  
{{% /alert %}}  

## **Sayfa ve Yazdırma Ayarları İle Çalışma**  

Bu örnekte, Microsoft Excel’de bir çalışma kitabı oluşturduk ve Aspose.Cells kullanarak sayfa ayarları ve yazdırma seçenekleri ayarladık.  

### **Aspose.Cells Kullanarak Sayfa Düzeni Seçenekleri Ayarlama**  

Öncelikle Microsoft Excel'de basit bir çalışma sayfası oluşturun. Sonra ona sayfa düzeni seçenekleri uygulayın. Kodu yürüttüğünüzde, aşağıdaki ekran görüntüsünde görülen gibi Sayfa Düzeni seçeneklerini değiştirir.  

|**Çıktı dosyası.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|  

1. Microsoft Excel'de bazı veriler içeren bir çalışma sayfası oluşturun:  
   1. Microsoft Excel'de yeni bir çalışma kitabı açın.  
   1. Bazı veriler ekleyin.  
1. Sayfa düzeni seçeneklerini ayarlayın:  
   Ayarları dosyaya uygulayın. Yeni ayarların uygulanmadan önceki varsayılan seçeneklerin ekran görüntüsü aşağıda verilmiştir.  

|**Varsayılan sayfa düzeni seçenekleri.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|  

1. Aspose.Cells'i indirin ve kurun:  
   1. [İndir](https://downloads.aspose.com/cells/javascript-cpp) C++ ile Aspose.Cells for JavaScript.  
   1. Geliştirme bilgisayarınıza kurun.  
      Kurulduğunda, tüm Aspose bileşenleri değerlendirme modunda çalışır. Değerlendirme modunun süresiz bir sınırlaması yoktur ve yalnızca üretilen belgelere filigran enjekte eder.  
1. Bir proje oluşturun:  
   1. JavaScript ortamınızı başlatın.  
   1. Yeni bir konsol uygulaması oluşturun.  
      Bu örnek bir JavaScript konsol uygulaması gösterecek, ancak C++ bağlamlarını da kullanabilirsiniz.  
1. Referanslar ekleyin:  
   1. Bu örnek Aspose.Cells kullanır, bu bileşene projeye bir referans ekleyin. Örneğin:  
      …\Program Files\Aspose\Aspose.Cells\Bin\JavaScript-Cpp\Aspose.Cells.node  
1. API'yi çağıran uygulamayı yazın:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PageOrientationType, PaperSizeType } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Access page setup as a property
            const pageSetup = worksheet.pageSetup;

            // Setting the orientation to Portrait
            pageSetup.orientation = PageOrientationType.Portrait;

            // Setting the number of pages to which the length of the worksheet will be spanned
            pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            pageSetup.fitToPagesWide = 1;

            // Setting the paper size to A4
            pageSetup.paperSize = PaperSizeType.PaperA4;

            // Setting the print quality of the worksheet to 1200 dpi
            pageSetup.printQuality = 1200;

            // Setting the first page number of the worksheet pages
            pageSetup.firstPageNumber = 2;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetup_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Yazdırma seçeneklerini ayarlama**  

Sayfa ayarı ayarları ayrıca kullanıcıların çalışma sayfalarının nasıl yazdırılacağını kontrol etmelerine olanak tanıyan birkaç yazdırma seçeneği (aynı zamanda sayfa seçenekleri de denir) sağlar. Kullanıcılara şunları yapma olanağı tanırlar:  

- Bir çalışma sayfasının belirli bir baskı alanını seçin.
- Başlıkları yazdırın.
- Izgaraları yazdırın.
- Satır/sütun başlıklarını yazdırın.
- Taslak kalitesine ulaşın.
- Yorumları yazdırın.
- Hücre hatalarını yazdırın.
- Sayfa sıralamasını tanımlayın.  

Aşağıdaki örnek yeni seçeneklerin uygulandığı dosyaya (Yukarıdaki örnekte oluşturulan PageSetup.xls) yazdırma seçeneklerini uygular. Aşağıdaki ekran görüntüsü, yeni seçenekler uygulanmadan önceki varsayılan yazdırma seçeneklerini gösterir.  

|**Giriş belgesi**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|  
Kodun çalıştırılması yazdırma seçeneklerini değiştirir.  

|**Çıktı dosyası**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Setup Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
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

            // Open the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            const pageSetup = worksheet.pageSetup;

            // Specifying the cells range (from A1 cell to E30 cell) of the print area
            pageSetup.printArea = "A1:E30";

            // Defining column numbers A & E as title columns
            pageSetup.printTitleColumns = "$A:$E";

            // Defining row numbers 1 as title rows
            pageSetup.printTitleRows = "$1:$2";

            // Allowing to print gridlines
            pageSetup.printGridlines = true;

            // Allowing to print row/column headings
            pageSetup.printHeadings = true;

            // Allowing to print worksheet in black & white mode
            pageSetup.blackAndWhite = true;

            // Allowing to print comments as displayed on worksheet
            pageSetup.printComments = AsposeCells.PrintCommentsType.PrintInPlace;

            // Allowing to print worksheet with draft quality
            pageSetup.printDraft = true;

            // Allowing to print cell errors as N/A
            pageSetup.printErrors = AsposeCells.PrintErrorsType.PrintErrorsNA;

            // Setting the printing order of the pages to over then down
            pageSetup.order = AsposeCells.PrintOrderType.OverThenDown;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetup_Print_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
