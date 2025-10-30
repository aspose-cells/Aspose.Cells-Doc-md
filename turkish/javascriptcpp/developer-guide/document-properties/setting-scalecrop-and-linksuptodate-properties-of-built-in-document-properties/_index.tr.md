---
title: Yerleşik Belge Özelliklerinin ÖlçekKosculuk ve BağlantılarGüncellemeli özelliklerini JavaScript ile C++ kullanarak ayarlama
linktitle: Yerleşik Belge Özellikleri için ScaleCrop ve LinksUpToDate özelliklerini ayarlama
type: docs
weight: 320
url: /tr/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Yerleşik belge özelliklerinin ÖlçekKosculuk ve BağlantılarGüncellemeli özelliklerini Aspose.Cells for JavaScript C++ kullanarak nasıl ayarlayacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**
[BuiltInDocumentPropertyCollection.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) ve [BuiltInDocumentPropertyCollection.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) OpenXml formatı içinde tanımlanmış iki gelişmiş yerleşik belge özelliğidir. Bu özelliklerin amacı aşağıdaki gibidir.

## **1) ScaleCrop**
Bu öğe, belge küçüğünün görüntüleme modunu gösterir. Belge küçüğünü ekranın uygun şekilde ölçeklendirmesi için bu öğeyi **TRUE** olarak ayarlayın. Yalnızca ekranın sığabileceği bölümleri göstermek için bu öğeyi **FALSE** olarak ayarlayın.

Bu öğe için olası değerler, W3C XML Şema boolean veri türü tarafından tanımlanır.

## **2) LinksUpToDate**
Bu öğe, bir belgedeki hiperbağlantıların güncel olup olmadığını gösterir. Hiperbağlantıların güncellendiğini belirtmek için bu öğeyi **TRUE** olarak ayarlayın. Hiperbağlantıların güncel olmadığını belirtmek için bu öğeyi **FALSE** olarak ayarlayın.

Bu öğe için olası değerler, W3C XML Şema boolean veri türü tarafından tanımlanır.

## **Bu özellikleri app.xml dosyası içinde gösteren ekran görüntüsü**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Yerleşik Belge Özellikleri için ScaleCrop ve LinksUpToDate özelliklerini ayarlama**
Aşağıdaki örnek kod, çalışma kitabının [BuiltInDocumentPropertyCollection.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) ve [BuiltInDocumentPropertyCollection.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) gelişmiş yerleşik belge özelliklerini ayarlar. Lütfen bu kodla oluşturulan [çıktı excel dosyasını](5115500.xlsx) kontrol edin, uzantısını .zip olarak değiştirin, içeriğini çıkarın ve yukarıdaki ekran görüntüsünde gösterildiği gibi app.xml dosyasını görüntüleyin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set BuiltIn Document Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Accessing BuiltIn Document Properties and setting properties
            const builtInDocumentProperties = workbook.builtInDocumentProperties;
            // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
            builtInDocumentProperties.scaleCrop = true;
            builtInDocumentProperties.linksUpToDate = true;

            // Saving the Excel file.
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
