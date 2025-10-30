---
title: Paylaşılan Çalışma Kitaplarında Revizyon Günlüklerini Korumak İçin Günleri Güncelleme ve Geçmişi Saklama ile ilgili JavaScript ve C++ kullanımı
linktitle: Paylaşılan Çalışma Kitabındaki Revizyon Günlüğü Tarihini Koruyan Günlük Günlerini Güncelleme Yöntemi
type: docs
weight: 80
url: /tr/javascript-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Paylaşılan çalışma kitaplarında revizyon günlükleriyle ilgili günleri güncellemek için Aspose.Cells for JavaScript ve C++ kullanmayı öğrenin.
---

## **Olası Kullanım Senaryoları**

Bir çalışma kitabını paylaştığınızda, aşağıdaki ekran görüntüsünde gösterildiği gibi ***N gün için değişiklik geçmişini tut*** seçeneği vardır. Geçmişi koruma gün sayısını Aspose.Cells for JavaScript ve C++ kullanarak [**WorksheetCollection.daysPreservingHistory**](https://reference.aspose.com/cells/javascript-cpp/revisionlogcollection/#daysPreservingHistory--) özelliği ile güncelleyebilirsiniz.

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Paylaşılan Çalışma Kitabındaki Revizyon Günlüğü Tarihini Güncelleme**

Aşağıdaki örnek kod boş bir çalışma kitabı oluşturur, sonra onu paylaşır ve revizyon günlüklerini koruyarak normalde 30 gün olan geçmişi 7 gün olarak günceller. Lütfen [Kod tarafından oluşturulan çıktı Excel dosyasına](60489773.xlsx) bir referans için bakınız.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Shared Workbook</title>
    </head>
    <body>
        <h1>Shared Workbook - DaysPreservingHistory Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Shared Workbook</button>
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
            // Create empty workbook
            const workbook = new Workbook();

            // Share the workbook
            workbook.settings.shared = true;

            // Update DaysPreservingHistory of RevisionLogs
            workbook.worksheets.revisionLogs.daysPreservingHistory = 7;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputShared_DaysPreservingHistory.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and configured. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
