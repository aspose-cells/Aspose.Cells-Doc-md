---
title: Excel den HTML ye dönüştürürken DataBar, ColorScale ve IconSet Koşullu Biçimlendirme i dışa aktarın, JavaScript ile C++
linktitle: DataBar, ColorScale ve IconSet Koşullu Biçimlendirmeyi Excel den HTML e Dönüşüm Sırasında Dışa Aktarın
type: docs
weight: 30
url: /tr/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
---

{{% alert color="primary" %}} 

 Excel dosyanızı HTML'ye dönüştürürken DataBar, ColorScale ve IconSet Koşullu Biçimlendirme'i dışa aktarabilirsiniz. Bu özellik Microsoft Excel tarafından kısmen desteklenmektedir, ancak Aspose.Cells for JavaScript tam desteği sağlar.

{{% /alert %}}  

## **Excel'den HTML'ye Databar, ColorScale ve IconSet Koşullu Biçimlendirmeyi Dışa Aktar**  
Aşağıdaki ekran görüntüsü, VeriÇubuğu, RenkÖlçeği ve SimgeSeti Koşullu Biçimlendirme ile [örnek excel dosyasını](5115558.xlsx) göstermektedir. Verilen bağlantıdan [örnek excel dosyasını](5115558.xlsx) indirebilirsiniz.  

![todo:image_alt_text](conversion_1.png)  

Aşağıdaki ekran görüntüsü, Aspose.Cells çıktı HTML dosyasını VeriÇubuğu, RenkÖlçeği ve SimgeSeti Koşullu Biçimlendirme göstermektedir. Gördüğünüz gibi, [örnek excel dosyası](5115558.xlsx)'yle tamamen aynı görünüyor.  

![todo:image_alt_text](conversion_2.png)  

### **Örnek Kod**  
 Aşağıdaki örnek kod, örnek Excel dosyasını HTML'ye dönüştürür; bu, sadece normal bir [Excel'den HTML'ye dönüştürme](/cells/tr/javascript-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml) işlevidir.  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Converting Excel to HTML Example</h1>
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

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in HTML format
            const outputData = workbook.save(SaveFormat.Html);

            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToHTMLFiles_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
