---
title: Shape veya Grafik in Yansıma Efekti ile çalışma
linktitle: Şekil veya Grafik Yansıma Efekti Çalışmak
type: docs
weight: 210
url: /tr/javascript-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Şekiller veya grafiklerin yansıma efektleriyle çalışmayı C++ aracılığıyla Aspose.Cells for JavaScript kullanarak öğrenin. İstenen sonuçları elde etmek için çeşitli yansıma özelliklerini ayarlayın.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells for JavaScript C++ aracılığıyla, [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) özelliği ve [ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect) sınıfı ile şekil veya grafiklerin yansıma efektleri üzerinde çalışabilir. [ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect) sınıfı, uygulama gereksinimlerine göre farklı sonuçlar elde etmek için ayarlanabilen aşağıdaki özellikleri içerir.

- [ReflectionEffect.blur](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#blur--)
- [ReflectionEffect.direction](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#direction--)
- [ReflectionEffect.distance](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#distance--)
- [ReflectionEffect.fadeDirection](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#fadeDirection--)
- [ReflectionEffect.rotWithShape](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#rotWithShape--)
- [ReflectionEffect.size](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#size--)
- [ReflectionEffect.transparency](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#transparency--)
- [ReflectionEffect.type](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#type--)

## **Şekil veya Grafik Yansıma Efekti Çalışmak**
Aşağıdaki örnek kod, [kaynak Excel dosyasını](5115424.xlsx) yükler ve varsayılan çalışma sayfasındaki ilk şekle erişir. [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) özelliklerini farklı şekilde ayarlar ve ardından çalışma kitabını [çıktı Excel dosyasına](5115423.xlsx) kaydeder.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Shape Reflection Effect Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first shape
            const shape = worksheet.shapes.get(0);

            // Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
            const reflectionEffect = shape.reflection;
            reflectionEffect.blur = 30;
            reflectionEffect.size = 90;
            reflectionEffect.transparency = 0;
            reflectionEffect.distance = 80;

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Reflection effect updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
