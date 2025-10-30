---
title: Kaynak Çalışma Sayfasından Hedef Çalışma Sayfasına Sayfa Kurulumu Ayarlarını Kopyala JavaScript ve C++ ile
linktitle: Kaynak Çalışma Sayfasından Hedef Çalışma Sayfasına Sayfa Ayarı Ayarlarını Kopyala
type: docs
weight: 80
url: /tr/javascript-cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Bu makale, JavaScript API veya C++ Kütüphanesi örnek kodları kullanarak kaynak çalışma sayfasından hedef çalışma sayfasına Sayfa Kurulumu ayarlarını programlı olarak nasıl kopyalayacağınızı açıklar.
keywords: Sayfa kurulum ayarlarını kopyala JavaScript ve C++ ile, hedef çalışma sayfasına sayfa kurulum ayarlarını kopyala JavaScript ve C++ ile
---

## **Olası Kullanım Senaryoları**

Bir çalışma kitabına yeni bir sayfa eklediğinizde, varsayılan *Sayfa Kurulumu ayarları* bulunur. Bazen bu ayarları ([**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)) bir çalışma sayfasından diğerine aktarmanız gerekebilir. Bu belge, C++ API'leri kullanarak bir çalışma sayfasından diğerine Sayfa Kurulumu ayarlarını kopyalamanın nasıl yapılacağını açıklar.

## **Kaynak Çalışma Sayfasından Hedef Çalışma Sayfasına Sayfa Ayarı Ayarlarını Kopyala**

Aşağıdaki örnek kod, [**PageSetup.copy(PageSetup, CopyOptions)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#copy-pagesetup-copyoptions-) yöntemini kullanarak bir çalışma sayfasındaki *Sayfa Ayarı ayarlarını* diğerine kopyalamanın örneklerini göstermektedir. Lütfen örnek kodu ve konsol çıktısını referans için inceleyin.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup Copy</title>
    </head>
    <body>
        <h1>PageSetup Copy Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CopyOptions, PaperSizeType, Utils } = AsposeCells;

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
            // Create workbook
            const wb = new Workbook();

            // Add two test worksheets
            wb.worksheets.add("TestSheet1");
            wb.worksheets.add("TestSheet2");

            // Access both worksheets as TestSheet1 and TestSheet2
            const TestSheet1 = wb.worksheets.get("TestSheet1");
            const TestSheet2 = wb.worksheets.get("TestSheet2");

            // Set the Paper Size of TestSheet1 to PaperA3ExtraTransverse
            TestSheet1.pageSetup.paperSize = PaperSizeType.PaperA3ExtraTransverse;

            // Print the Paper Size of both worksheets (before copy)
            const before1 = TestSheet1.pageSetup.paperSize;
            const before2 = TestSheet2.pageSetup.paperSize;

            // Copy the PageSetup from TestSheet1 to TestSheet2
            TestSheet2.pageSetup.copy(TestSheet1.pageSetup, new CopyOptions());

            // Print the Paper Size of both worksheets (after copy)
            const after1 = TestSheet1.pageSetup.paperSize;
            const after2 = TestSheet2.pageSetup.paperSize;

            // Display results
            document.getElementById('result').innerHTML =
                '<pre>' +
                'Before Paper Size (TestSheet1): ' + before1 + '\n' +
                'Before Paper Size (TestSheet2): ' + before2 + '\n\n' +
                'After Paper Size (TestSheet1): ' + after1 + '\n' +
                'After Paper Size (TestSheet2): ' + after2 +
                '</pre>';

            // Saving the modified Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

## **Konsol Çıktısı**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
