---
title: JavaScript kullanarak BuiltIn Document Properties ile Excel Dosyasının Sürümünü C++ ile belirtin
linktitle: Aspose.Cells ile Yerleşik Belge Özelliklerini Kullanarak Excel Dosyasının Belge Sürümünü Belirtme
type: docs
weight: 20
url: /tr/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Built in belge özellikleri kullanarak programlamalı olarak bir Excel dosyasının sürümünü JavaScript ile C++ kullanarak nasıl belirleyeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**  

Bir Excel dosyasının **Sürüm numarası**nı sağ tıklayarak ve sonra Özellikler > Ayrıntılar seçerek değiştirebilirsiniz. Programlı olarak değiştirmek için lütfen [**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--) özelliğini Aspose.Cells API'leri ile kullanın.  

## **Aspose.Cells kullanarak Excel Dosyasının Belge Sürümünü Belirtme**  

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve bu kitabın Title, Yazarlar ve Sürüm numarası gibi dahili belge özelliklerini değiştirir. Bu kod tarafından oluşturulan [çıktı Excel dosyasını](64716811.xlsx) ve modifiye edilen Sürüm numarasını gösteren ekran görüntüsünü inceleyin.  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Document Version Example</h1>
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
            // Create workbook object
            const wb = new Workbook();

            // Access built-in document property collection
            const bdpc = wb.builtInDocumentProperties;

            // Set the title
            bdpc.title = "Aspose File Format APIs";

            // Set the author
            bdpc.author = "Aspose APIs Developers";

            // Set the document version
            bdpc.documentVersion = "Aspose.Cells Version - 18.3";

            // Save the workbook in xlsx format
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyDocumentVersionOfExcelFile.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and prepared for download. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
