---
title: JavaScript ve C++ kullanarak sütun genişliğini em veya yüzde gibi ölçeklenebilir bir birime ayarlayın
linktitle: Sütun Genişliğini Em veya Yüzde gibi Ölçeklenebilir Birim Olarak Ayarlama
type: docs
weight: 130
url: /tr/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Aspose.Cells for JavaScript kullanarak C++ ile sütun genişliğini em veya yüzde gibi ölçeklenebilir birime ayarlamayı öğrenin. Oluşturulan HTML tablolarının sunumunu iyileştirin.
---

Bir elektronik tabloyu HTML dosyasına dönüştürmek çok yaygındır. Sütunların boyutu "pt" cinsinden tanımlanır, bu birçok durumda işe yarar. Ancak, bu sabit boyut gerekmeyebilir. Örneğin, bir konteyner panel genişliği 600px ise ve bu HTML sayfası gösteriliyorsa, oluşturulan tablonun genişliği büyükse yatay kaydırıcı alabilirsiniz. Bu sabit boyutun em veya yüzde gibi ölçeklenebilir bir birime değiştirilmesi gerekebilir. Aşağıdaki örnek kod, [**HtmlSaveOptions.widthScalable**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#widthScalable--) değeri **true** olarak ayarlandığında ölçeklenebilir genişlik oluşturmak için kullanılabilir.

Örnek kaynak dosyası ve çıktı dosyalarını aşağıdaki bağlantılardan indirebilirsiniz:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Scalable Columns to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions, SaveFormat } = AsposeCells;

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

            // Specify Html Save Options
            const options = new HtmlSaveOptions();

            // Set the property for scalable width (converted from setWidthScalable)
            options.widthScalable = true;

            // Specify image save format (converted from setExportImagesAsBase64)
            options.exportImagesAsBase64 = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outsampleForScalableColumns.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted to HTML successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
