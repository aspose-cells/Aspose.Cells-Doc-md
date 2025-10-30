---
title: JavaScript ile C++ kullanarak şekil veya grafik parlaklık efekti ile çalışma
linktitle: Şekil veya Grafik Gölgelendirme Efekti Çalışmak
type: docs
weight: 240
url: /tr/javascript-cpp/working-with-the-glow-effect-of-shape-or-chart/
description: Şekillerin veya grafiklerin parlaklık efektleriyle nasıl çalışacağınızı Aspose.Cells for JavaScript kullanarak C++ ile öğrenin.
---

## **Olası Kullanım Senaryoları**  
Aspose.Cells, şekil veya grafik parlaklık efektleriyle çalışmak için [Shape.glow](https://reference.aspose.com/cells/javascript-cpp/shape/#glow--) özelliği ve [GlowEffect](https://reference.aspose.com/cells/javascript-cpp/gloweffect/) sınıfı sağlar. [GlowEffect](https://reference.aspose.com/cells/javascript-cpp/gloweffect/) sınıfı, uygulama gereksinimlerine göre farklı sonuçlar elde etmek için ayarlanabilen aşağıdaki özellikleri içerir.  

- [GlowEffect.boyut](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#size--)  
- [GlowEffect şeffaflık](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#transparency--)  
- [GlowEffect renk](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#color--)  

## **Şekil veya Grafik Gölgelendirme Efekti Çalışmak**  
Aşağıdaki örnek kod, [kaynak excel dosyasını](5115407.xlsx) yükler, ilk çalışma sayfasındaki ilk şekle erişir ve [Shape.glow](https://reference.aspose.com/cells/javascript-cpp/shape/#glow--) özelliğinin alt özelliklerini ayarlar ve ardından çalışma kitabını [çıkış excel dosyasına](5115414.xlsx) kaydeder.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Glow Effect</title>
    </head>
    <body>
        <h1>Apply Glow Effect to First Shape</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Apply Glow Effect</button>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first shape
            const shape = worksheet.shapes.get(0);

            // Set the glow effect of the shape, Set its Size and Transparency properties
            const glowEffect = shape.glow;
            glowEffect.size = 30;
            glowEffect.transparency = 0.4;

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Glow effect applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
