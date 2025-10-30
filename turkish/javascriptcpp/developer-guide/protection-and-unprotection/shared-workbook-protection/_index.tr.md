---
title: JavaScript kullanarak Paylaşılan Çalışma Kitabını Parola ile Koru veya Korumayı Kaldır
linktitle: Paylaşılan Çalışma Kitabını Koruma Altına Alma veya Korumasız Yapma
type: docs
weight: 10
url: /tr/javascript-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **Olası Kullanım Senaryoları**

Aşağıdaki ekran görüntüsünde gösterildiği gibi, Microsoft Excel kullanarak paylaşılan çalışma kitabını koruyabilir veya korumasını kaldırabilirsiniz. C++ ile Aspose.Cells for JavaScript bu özelliği [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#protectSharedWorkbook-string-) ve [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#unprotectSharedWorkbook-string-) metodlarıyla destekler.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Paylaşılan çalışma kitabını koruma altına alan ve paylaşımı etkinleştiren bir çalışma kitabı oluşturan aşağıdaki örnek kod ve bunu [çıktı Excel dosyası](55541777.xlsx) olarak kaydeden bir çalışma sayfasına şifre eklemesini göstermektedir. Ekran görüntüsü, korumasız yapmaya çalıştığınızda Microsoft Excel'in şifreyi girmenizi istediğini göstermektedir.**

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur, onu korur ve paylaşımı etkinleştirir ve [çıktı Excel dosyası](55541777.xlsx) olarak kaydeder. Ekran görüntüsü, açmak için denediğinizde, Microsoft Excel'in onu korumak için şifreyi girmenizi istediğini gösterir.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Shared Workbook Example</h1>
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
            // Creating an empty Workbook
            const workbook = new Workbook();

            // Protect the Shared Workbook with Password
            workbook.protectSharedWorkbook("1234");

            // Uncomment this line to Unprotect the Shared Workbook
            // workbook.unprotectSharedWorkbook("1234");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputProtectSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
