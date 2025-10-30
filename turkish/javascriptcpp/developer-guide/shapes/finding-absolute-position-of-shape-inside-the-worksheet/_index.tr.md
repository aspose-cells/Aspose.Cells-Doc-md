---
title: JavaScript ve C++ ile Çalışma Sayfası İçinde Şeklin Mutlak Pozisyonunu Bulma
linktitle: Çalışma sayfasının içindeki Şeklin Mutlak Konumunu Bulma
type: docs
weight: 8000
url: /tr/javascript-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: C++ ile Aspose.Cells for JavaScript kullanarak bir şeklin çalışma sayfası içindeki mutlak konumunu nasıl bulacağınızı öğrenin. 
---

{{% alert color="primary" %}}

Bazen, bir şeklin çalışma sayfasındaki mutlak konumunu bilmeniz gerekir. C++ ile Aspose.Cells for JavaScript bu amaçla [**Shape.leftToCorner**](https://reference.aspose.com/cells/javascript-cpp/shape/#leftToCorner--) ve [**Shape.topToCorner**](https://reference.aspose.com/cells/javascript-cpp/shape/#topToCorner--) özelliklerini sağlar. Bu özellikler, şeklin çalışma sayfası içindeki mutlak konumunu piksel cinsinden döndürür.

{{% /alert %}}

Aşağıdaki örnek kod çalışsayfadaki ilk şeklin mutlak konumunu pikseller cinsinden gösterir. Örnek kod aşağıdaki konsol çıktısını görüntüler:

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Shape Position</title>
    </head>
    <body>
        <h1>Get Shape Absolute Position</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file inside the workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first shape inside the worksheet
            const shape = worksheet.shapes.get(0);

            // Displays the absolute position of the shape
            const left = shape.leftToCorner;
            const top = shape.topToCorner;
            const message = `Absolute Position of this Shape is (${left} , ${top})`;
            console.log(message);
            resultDiv.innerHTML = `<p>${message}</p>`;
        });
    </script>
</html>
```
