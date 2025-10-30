---
title: Aspose.Cells for JavaScript kullanarak Paylaşılan Çalışma Kitabı Oluşturun
linktitle: Aspose.Cells ile Paylaşılan Çalışma Kitabı Oluşturma
type: docs
weight: 40
url: /tr/javascript-cpp/create-shared-workbook-with-aspose-cells/
description: Aspose.Cells for JavaScript kullanarak paylaşılan çalışma kitabı nasıl oluşturulur öğrenin.
---

## **Olası Kullanım Senaryoları**  

Microsoft Excel, aşağıdaki ekran görüntüsünde gösterildiği gibi çalışma kitabını paylaşmanıza izin verir. Çalışma kitabını paylaştığınızda, birden fazla kullanıcı ağ üzerinde çalışma kitabını düzenleyebilir. Aspose.Cells for JavaScript kullanarak C++, paylaşılmış bir çalışma kitabı oluşturmak için [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--) özelliğini kullanır.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Aspose.Cells ile Paylaşılan Çalışma Kitabı Oluşturma**  

Aşağıdaki örnek kod, [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--) özelliğini **true** olarak ayarlayarak paylaşılan bir çalışma kitabı oluşturur. [Çıktı Excel dosyasını](55541786.xlsx) Microsoft Excel'de açtığınızda, bu ekran görüntüsüyle gösterildiği gibi **Paylaşılan** olarak göreceksiniz.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Shared Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="createShared" disabled>Create Shared Workbook</button>
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
            document.getElementById('createShared').disabled = false;
        });

        document.getElementById('createShared').addEventListener('click', async () => {
            const wb = new Workbook();

            // Share the Workbook (converted getter/setter to property)
            wb.settings.shared = true;

            // Save the Shared Workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Shared Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared workbook created successfully! Click the download link to save the file.</p>';
        });
    </script>
</html>
```
