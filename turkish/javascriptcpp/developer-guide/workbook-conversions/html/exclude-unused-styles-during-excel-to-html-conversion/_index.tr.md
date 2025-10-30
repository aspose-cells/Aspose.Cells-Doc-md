---
title: Excel den HTML ye dönüştürme sırasında kullanılmayan stilleri hariç tutun, JavaScript ile C++
linktitle: Excel den HTML ye Dönüşüm Sırasında Kullanılmayan Stilleri Hariç Tut
type: docs
weight: 30
url: /tr/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Kullanılmayan stilleri hariç tutmayı nasıl öğrenirim, Excel yi HTML ye dönüştürürken, Aspose.Cells for JavaScript kullanarak C++ ile.
---

## **Olası Kullanım Senaryoları**  

Microsoft Excel dosyaları birçok kullanılmayan stili içerebilir. Excel dosyasını HTML'ye dışa aktardığınızda, bu kullanılmayan stiller de aktarılır. Bu, HTML'nin boyutunu artırabilir. Excel dosyalarını HTML'ye dönüştürürken [**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--) özelliğini kullanarak kullanılmayan stilleri hariç tutabilirsiniz. Bunu **true** olarak ayarladığınızda, tüm kullanılmayan stiller çıktı HTML'den hariç edilir. Aşağıdaki ekran görüntüsü, çıktı HTML içinde bulunan örnek kullanılmayan stil örneğini gösterir.  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **Excel dosyası oluşturan ve kullanılmayan isimli bir stil oluşturan aşağıdaki örnek kod. {0} **true** olarak ayarlandığından, bu kullanılmayan isimli stil [çıktı HTML'sine](61767778.zip) dışa aktarılmayacaktır. Ancak, **false**olarak ayarlarsanız, bu kullanılmayan stil çıktı HTML içinde bulunacaktır ve yukarıdaki ekran görüntüsünde HTML işaretleme dilinde görebilirsiniz.**  

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve ayrıca kullanılmayan bir ad stil oluşturur. [**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--) **true** olarak ayarlandığı için, bu kullanılmayan ad stili [çıktı HTML'sine](61767778.zip) aktarılmaz. Ancak, onu **false** yaparsanız, bu kullanılmayan stil çıktı HTML'si içinde bulunur ve yukarıdaki ekran görüntüsünde gösterildiği gibi HTML biçiminde görebilirsiniz.  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Exclude Unused Styles</title>
    </head>
    <body>
        <h1>Exclude Unused Styles from Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');

            if (fileInput.files.length > 0 && fileInput.files[0].size === 0) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a valid Excel file.</p>';
                return;
            }

            // Instantiate workbook from selected file or create a new one
            let wb;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Create an unused named style
            const style = wb.createStyle();
            style.name = "UnusedStyle_XXXXXXXXXXXXXX";

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some value in cell C7
            const cell = ws.cells.get("C7");
            cell.value = "This is sample text.";

            // Specify html save options, we want to exclude unused styles
            const opts = new HtmlSaveOptions();
            // Comment this line to include unused styles
            opts.excludeUnusedStyles = true;

            // Save the workbook in html format
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExcludeUnusedStylesInExcelToHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML generated successfully. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
