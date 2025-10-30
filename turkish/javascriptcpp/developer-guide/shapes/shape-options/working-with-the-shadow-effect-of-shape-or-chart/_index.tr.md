---
title: C++ aracılığıyla JavaScript kullanarak Shape veya Grafiklerin Gölge Efekti ile çalışma
linktitle: Şekil veya Grafik Gölgelendirme Efekti Çalışmak
type: docs
weight: 220
url: /tr/javascript-cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: Aspose.Cells for JavaScript aracılığıyla şekil veya grafiklerin gölge efektleriyle çalışmayı öğrenin.
---

## **Olası Kullanım Senaryoları**  
Aspose.Cells for JavaScript C++ aracılığıyla, [Shape.shadowEffect](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) özelliği ve [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) sınıfı ile şekil veya grafiklerin gölge efektleri üzerinde çalışabilir. [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) sınıfı, uygulama gereksinimlerine göre farklı sonuçlar elde etmek için ayarlanabilen aşağıdaki özellikleri içerir.  

- [ShadowEffect.angle](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#angle--)  
- [ShadowEffect.blur](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#blur--)  
- [ShadowEffect.color](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#color--)  
- [ShadowEffect.distance](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#distance--)  
- [ShadowEffect.presetType](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--)  
- [ShadowEffect.size](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#size--)  
- [GölgeEtki.saydamlık](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#transparency--)  

## **Şekil veya Grafik Gölgelenme Efekti ile Çalışma**  
Aşağıdaki örnek kod, [kaynak excel dosyasını](5115425.xlsx) yükler ve ilk çalışma sayfasındaki ilk şekle erişir ve [Şekil.gölgeEtki](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) özelliğinin alt özelliklerini ayarlar ve ardından çalışma kitabını [çıkış excel dosyasına](5115411.xlsx) kaydeder.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Shape Shadow Effect Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const shape = worksheet.shapes.get(0);

            const shadowEffect = shape.shadowEffect;
            shadowEffect.angle = 150;
            shadowEffect.blur = 4;
            shadowEffect.distance = 45;
            shadowEffect.transparency = 0.3;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shadow effect applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
