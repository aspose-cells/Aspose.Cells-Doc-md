---
title: タイムラインのレンダリング
type: docs
weight: 40
url: /ja/javascript-cpp/rendering-timeline/
description: C++を使用してExcelファイルのタイムラインを管理
keywords: Office 2013、Office 2016、Office 2019、Office 365を使用せずにタイムラインをレンダリング
---

## **可能な使用シナリオ**
Aspose.Cells for JavaScriptはOffice 2013、2016、2019、365を使用せずにタイムラインシェイプのレンダリングをサポートします。ワークシートを画像に変換したり、ワークブックをPDFやHTML形式で保存すると、タイムラインは適切にレンダリングされます。

## **タイムラインのレンダリング**
以下のサンプルコードは、既存のタイムラインを含む[sample Excel file](input.xlsx) を読み込み、タイムラインの名前に応じてシェイプオブジェクトを取得し、それをShape.ToImage()メソッドで画像にレンダリングします。以下の画像はレンダリングされたタイムラインを示す[出力画像](out.png)です。タイムラインは正しくレンダリングされており、サンプルExcelファイルと同じ外観です。

![todo:image_alt_text](out.png)
### **サンプルコード**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Timeline Shape as Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, ImageType, Utils } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access second worksheet (index 1)
            const sheet = workbook.worksheets.get(1);

            // Add timeline relating to pivot table (access first timeline)
            const timeline = sheet.timelines.get(0);

            // Prepare image options
            const options = new ImageOrPrintOptions();
            options.imageType = ImageType.Png;

            // Get timeline shape object by timeline's name
            const timeLineShape = sheet.shapes.get(timeline.name);

            // Export shape to image (browser returns image bytes)
            const imageData = timeLineShape.toImage(options);

            // Create blob and provide download link
            const blob = new Blob([imageData], { type: 'image/png' });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Timeline Image';

            resultDiv.innerHTML = '<p style="color: green;">Timeline image generated successfully. Click the download link to save the image.</p>';
        });
    </script>
</html>
```
