---
title: JavaScript kullanarak Çalışma Kitabı Render Edilmesi için Bireysel veya Özel Yazı Tipleri Seti Belirtin
linktitle: Çalışma Kitabı Rendeleme için Bireysel veya Özel Font Kümesini Belirtin
type: docs
weight: 40
url: /tr/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: C++ ile Aspose.Cells for JavaScript kullanarak çalışma kitabı render edilmesi için bireysel veya özel yazı tipi setleri belirtmeyi öğrenin.
---

## **Olası Kullanım Senaryoları**  

Genellikle, çalışma kitaplarınız için yazı tipleri dizini veya yazı tipi listesi belirtirsiniz, ancak bazen bireysel veya özel yazı tipi setleri belirtmeniz gerekebilir. C++ ile Aspose.Cells for JavaScript, çalışma kitabınız için bireysel veya özel yazı tipi setleri belirtmek için kullanılabilen [**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs) sınıfını sağlar.  

## **Çalışma Kitabı Rendeleme İçin Bireysel veya Özel Font Kümesini Belirtin**  

Aşağıdaki örnek kod, belirtilen bireysel veya özel yazı tipi setleriyle [örnek Excel dosyasını](67338268.xlsx) yükler. Kod içindeki [örnek font](67338271.zip) ve üretilen [çıktı PDF'si](67338269.pdf) ile ilgili bilgileri görebilirsiniz. Bu ekran görüntüsü, yazı tipi başarıyla bulunduğunda çıktı PDF'sinin nasıl göründüğünü gösterir.  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Individual Or Private Fonts Example</title>
    </head>
    <body>
        <h1>Specify Individual Or Private Fonts Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, IndividualFontConfigs } = AsposeCells;

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

            // Path of your custom font directory.
            const customFontsDir = "C:\\TempDir\\CustomFonts";

            // Specify individual font configs custom font directory.
            const fontConfigs = new IndividualFontConfigs();

            // If you comment this line or if custom font directory is wrong or 
            // if it does not contain required font then output pdf will not be rendered correctly.
            // Converted setFontFolder -> property assignment (first argument used)
            fontConfigs.fontFolder = customFontsDir;

            // Specify load options with font configs.
            const opts = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
            // Converted setFontConfigs -> property assignment
            opts.fontConfigs = fontConfigs;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file with individual font configs.
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save to PDF format.
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
