---
title: JavaScript kullanarak C++ ile IFilePathProvider arayüzü üzerinden ihracat edilen çalışma sayfası HTML dosya yolunu sağlayın
linktitle: IFilePathProvider arayüzü aracılığıyla dışa aktarılan çalışma sayfası HTML dosyası yolunu sağlayın
type: docs
weight: 70
url: /tr/javascript-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Olası Kullanım Senaryoları**
Birden fazla sayfaya sahip bir Excel dosyanız olduğunu ve her sayfayı ayrı ayrı HTML dosyasına dışa aktarmak istediğinizi varsayın. Sayfalarınızdan herhangi birinde diğer sayfalara bağlantılar varsa, bu bağlantılar dışa aktarılan HTML'de kopacaktır. Bu sorunu çözmek için Aspose.Cells for JavaScript kullanarak C++ ile [IFilePathProvider](https://reference.aspose.com/cells/javascript-cpp/ifilepathprovider) arayüzü sağlar, bu arayüzü uygulayarak kopan bağlantıları düzeltebilirsiniz.

## **IFilePathProvider arayüzü aracılığıyla dışa aktarılan çalışma sayfası HTML dosya yolunu sağlayın**
Aşağıdaki kodda kullanılan örnek Excel dosyasını [indirin](5115213.zip) ve dışa aktarılmış HTML dosyalarını alın. Tüm dosyalar geçici dizin içerisindedir. Bunu C: sürücüsüne çıkartın. Bu durumda C:\Temp dizini olur. Ardından, Sheet1.html dosyasını tarayıcıda açın ve içindeki iki bağlantıya tıklayın. Bu bağlantılar, C:\Temp\OtherSheets dizini içindeki bu iki dışa aktarılmış HTML çalışma sayfasına işaret eder.

{{< highlight javascript >}}
 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
{{< /highlight >}}

Aşağıdaki ekran görüntüsü, C:\Temp\Sheet1.html ve bağlantılarının nasıl göründüğünü göstermektedir

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

Aşağıdaki ekran görüntüsü HTML kaynağını göstermektedir. Gördüğünüz gibi, bağlantılar artık C:\Temp\OtherSheets dizinine atıfta bulunmaktadır. Bu, [IFilePathProvider](https://reference.aspose.com/cells/javascript-cpp/ifilepathprovider) arayüzü kullanılarak gerçekleştirildi.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **Örnek Kod**
Lütfen C:\Temp dizininin sadece örnekleme amaçlı olduğunu unutmayın. İstediğiniz herhangi bir dizini kullanabilir ve içerisine [örnek Excel dosyasını](5115211.xlsx) koyabilirsiniz. Ardından, sağlanan örnek kodu çalıştırın. Bu, diziniz içinde bir OtherSheets alt dizini oluşturacak ve içindeki ikinci ve üçüncü çalışma sayfalarını HTML olarak dışa aktaracaktır. Lütfen kodda bulunan dirPath değişkenini değiştirerek kendi tercih ettiğiniz dizine göre ayarlayın.

{{% alert color="primary" %}} 

Örnek kod, yalnızca Aspose.Cells lisansı ayarlandığında çalışacaktır. Lisansı ayarlamadan kodu çalıştırmaya çalışırsanız, sonsuz döngüye girer. Bu yüzden, lisansın ayarlandığını kontrol eden ve ayarlanmadığında mesaj yazdırıp durduracak bir kod ekledik. Lisans satın alabilir veya Aspose.Purchase takımıyla 30 günlük geçici lisans talep edebilirsiniz.

{{% /alert %}} 

Lütfen, bu satırları kodda yorum satırı haline getirirseniz, Sheet1.html içindeki bağlantılar bozulur ve tıklandığında Sheet2.html veya Sheet3.html açılmaz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Worksheet to HTML with FilePathProvider Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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

        // Implementation of IFilePathProvider for browser
        class FilePathProvider extends AsposeCells.IFilePathProvider {
            constructor() {
                super();
            }

            // Converted method name from getFullName -> fullName per universal getter/setter conversion rule
            fullName(sheetName) {
                if (sheetName === "Sheet2") {
                    return "file:///OtherSheets/Sheet2.html";
                } else if (sheetName === "Sheet3") {
                    return "file:///OtherSheets/Sheet3.html";
                }
                return "";
            }
        }

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

            // Create HtmlSaveOptions and assign FilePathProvider (converted setter to property assignment)
            const options = new HtmlSaveOptions();
            options.filePathProvider = new FilePathProvider();

            // Save workbook to HTML using options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - IFilePathProvider</title>
    </head>
    <body>
        <h1>Aspose.Cells IFilePathProvider Example (Browser)</h1>
        <p>Select the Sample_filepath.xlsx file to export worksheets to separate HTML files.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <div id="links"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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

        // Implementation of IFilePathProvider interface for browser
        class FilePathProvider extends AsposeCells.IFilePathProvider {
            constructor() {
                super();
            }

            // Gets the full path of the file by worksheet name when exporting worksheet to html separately.
            // So the references among the worksheets could be exported correctly.
            getFullName(sheetName) {
                if (sheetName === "Sheet2") {
                    return "file:///OtherSheets/Sheet2.html";
                } else if (sheetName === "Sheet3") {
                    return "file:///OtherSheets/Sheet3.html";
                }
                return "";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const linksDiv = document.getElementById('links');
            linksDiv.innerHTML = '';
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select the Sample_filepath.xlsx file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Check license
            if (!workbook.isLicensed()) {
                resultDiv.innerHTML = '<p style="color: red;">You must set the license to execute this code successfully.</p>';
                return;
            }

            // Export each worksheet to separate HTML using HtmlSaveOptions and FilePathProvider
            const sheetCount = workbook.worksheets.count;

            for (let i = 0; i < sheetCount; i++) {
                // Set the active worksheet to current index
                workbook.worksheets.activeSheetIndex = i;

                // Create html save option
                const options = new HtmlSaveOptions();
                options.exportActiveWorksheetOnly = true;
                // Provide file path provider so hyperlinks among sheets are preserved correctly
                options.filePathProvider = new FilePathProvider();

                // Save the active worksheet to HTML (returns Uint8Array)
                const outputData = workbook.save(SaveFormat.Html, options);

                // Create downloadable blob for the HTML
                const blob = new Blob([outputData], { type: 'text/html' });

                // Determine filename similar to original logic
                const sheetIndex = i + 1;
                let filename = '';
                if (i === 0) {
                    filename = 'Sheet1.html';
                } else {
                    filename = `OtherSheets_Sheet${sheetIndex}_out.html`;
                }

                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = filename;
                link.textContent = 'Download ' + filename;
                link.style.display = 'block';
                linksDiv.appendChild(link);
            }

            resultDiv.innerHTML = '<p style="color: green;">Worksheets exported successfully! Use the links below to download each HTML file.</p>';
        });
    </script>
</html>
```
