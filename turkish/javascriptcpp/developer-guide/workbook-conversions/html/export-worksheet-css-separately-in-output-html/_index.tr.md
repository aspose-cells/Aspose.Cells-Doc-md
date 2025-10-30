---
title: Çalışma Sayfası CSS sini Çıktı HTML sinde Ayrı Dışa Aktar JavaScript ve C++ aracılığıyla
linktitle: Çıktı HTML sindeki Sayfa CSS sini Ayrı Ayrı Dışa Aktarma
type: docs
weight: 80
url: /tr/javascript-cpp/export-worksheet-css-separately-in-output/
description: Çalışma sayfası CSS sini dışa aktarmayı öğrenin, Excel dosyasını HTML ye dönüştürürken Aspose.Cells for JavaScript aracılığıyla C++ kullanarak.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells for JavaScript C++ kullanarak, Excel dosyanızı HTML'ye dönüştürürken çalışma sayfası CSS'sini ayrı olarak dışa aktarma özelliği sağlar. Bu amaçla [**HtmlSaveOptions.exportWorksheetCSSSeparately**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetCSSSeparately--) özelliğini kullanın ve Excel dosyasını HTML'ye kaydederken değeri **true** yapın.

## **Çıktı HTML'sindeki Sayfa CSS'sini Ayrı Ayrı Dışa Aktarma**

Aşağıdaki örnek kod, bir Excel dosyası oluşturur, **B5** hücresine Kırmızı renkli metin ekler ve ardından [**HtmlSaveOptions.exportWorksheetCSSSeparately**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetCSSSeparately--) özelliği kullanarak HTML formatında kaydeder. Referans için kod tarafından oluşturulan [çıktı HTML](60489766.zip) dosyasına bakın. Örnekte **stylesheet.css** dosyasını bulacaksınız.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Worksheet CSS Separately Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Color, Utils } = AsposeCells;

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
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and put value inside it
            const cell = ws.cells.get("B5");
            cell.value = "This is some text.";

            // Set the style of the cell - font color is Red
            const st = cell.style;
            st.font.color = Color.Red;
            cell.style = st;

            // Specify html save options - export worksheet css separately
            const opts = new HtmlSaveOptions();
            opts.exportWorksheetCSSSeparately = true;

            // Save the workbook in html 
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportWorksheetCSSSeparately.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as HTML. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Tek Çalışsayı İş Kitabını HTML'ye Dışa Aktarma**

Birden fazla sayfaya sahip çalışma kitabı Aspose.Cells for JavaScript ve C++ ile HTML'ye dönüştürüldüğünde, birlikte CSS içeren bir HTML dosyası ve CSS'yi içeren bir klasör oluşturulur. Bu HTML dosyası tarayıcıda açıldığında sekmeler görünür. Aynı davranış, tek sayfadan oluşan çalışma kitapları içindir; önceki sürümler yalnızca bir HTML dosyası oluşturuyordu ve sekmeler görünmüyordu. Artık, tek sayfalık çalışma kitapları için de uygun klasör ve HTML oluşturulur ve bu davranış Aspose.Cells API'leri kullanılarak uygulanır. Aşağıdaki bağlantıdan örnek dosya indirilebilir ve aşağıdaki örnek kodda kullanılabilir:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Save Workbook as HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, EncodingType, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HTML save options
            const options = new HtmlSaveOptions();

            // Set optional settings (converted from setters to properties)
            options.encoding = EncodingType.UTF8;
            options.exportImagesAsBase64 = true;
            options.exportGridLines = true;
            options.exportSimilarBorderStyle = true;
            options.exportBogusRowData = true;
            options.excludeUnusedStyles = true;
            options.exportHiddenWorksheet = true;

            // Save the workbook in HTML format with specified HtmlSaveOptions
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSampleSingleSheet.htm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook saved to HTML. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
