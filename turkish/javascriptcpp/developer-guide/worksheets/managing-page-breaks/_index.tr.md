---
title: Sayfa Kesmesini Yönetme JavaScript ile C++
linktitle: Sayfa Kesmelerinin Yönetimi
type: docs
weight: 30
url: /tr/javascript-cpp/managing-page-breaks/
description: Bu makale, Aspose.Cells for JavaScript ile C++ kullanarak Excel çalışma sayfalarında sayfa kesmesini ekleme, temizleme veya silme gibi işlemleri yapmanın örnek kodlarını sağlar ve açıklar.
keywords: Sayfa kesmeleri JavaScript ile C++, Excel sayfa kesmeleri JavaScript ile C++, Sayfa kesmesini temizleme JavaScript ile C++, Belirli sayfa kesmesini silme JavaScript ile C++
---

{{% alert color="primary" %}}

Tanıma göre, bir sayfa kesmesi, metin akışının bir sayfanın bittiği ve diğerinin başladığı yeridir. Microsoft Excel kullanıcılarına herhangi bir seçili hücreye sayfa kesmeleri eklemelerine izin verir.

Sayfa kırığı eklenen hücrenin konumunda, sayfa biter ve sayfa kırığından sonraki veri bir sonraki sayfaya basılırken. Basitçe söylemek gerekirse, sayfa kırıkları çalışma sayfanızı istediğiniz özelliklere göre birden çok sayfaya böler. Ayrıca, Aspose.Cells kullanarak çalışma sayfalarınızda çalışma zamanında sayfa kırıkları ekleyebilirsiniz. Aspose.Cells, geliştiricilere iki tür sayfa kırığı ekleme olanağı sağlar:

- Yatay sayfa kesmesi
- Dikey sayfa kesmesi

Tartışmanın geri kalanında, Aspose.Cells kullanarak çalışma sayfalarınıza yatay veya dikey sayfa kesme nasıl ekleyebileceğinizi açıklayacağız.

{{% /alert %}}

## **Sayfa Sonları**

Aspose.Cells for JavaScript ile C++ kullanarak {0} sınıfını sağlar ve bu sınıf bir Excel dosyasını temsil eder. {1} sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir {2} koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, çalışma sayfasını yönetmek için kullanılan geniş bir özellik ve yöntem yelpazesi sağlar.

Sayfa kırıklarını eklemek için, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfının [**worksheet.horizontalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#horizontalPageBreaks--) ve [**worksheet.verticalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#verticalPageBreaks--) özelliklerini kullanın.

[**worksheet.horizontalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#horizontalPageBreaks--) ve [**worksheet.verticalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#verticalPageBreaks--) özellikleri, birkaç sayfa kırığı içerebilen koleksiyonlardır. Her koleksiyon, yatay ve dikey sayfa kırıklarını yönetmek için birçok yöntem içerir.

### **Sayfa Kesmeleri Eklemek**

Bir çalışma sayfasına sayfa kırması eklemek için, belirtilen hücreye dikey ve yatay sayfa kırmaları eklemek amacıyla [**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/horizontalpagebreakcollection/#add-number-number-number-) ve [**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/verticalpagebreakcollection/#add-number-number-number-) metodlarını çağırın. Her **add** yöntemi, kırmanın ekleneceği hücrenin adını alır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Page Breaks Example</h1>
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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a page break at cell Y30
            worksheet.horizontalPageBreaks.add("Y30");
            worksheet.verticalPageBreaks.add("Y30");

            // Save the Excel file (Excel 97-2003 format .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingPageBreaks_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page breaks added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Sayfa kesmeleri önizleme veya yazdırma önizleme modlarında, bu sayfa kesmelerinin nasıl çalıştığını görebilirsiniz.

{{% /alert %}}

### **Belirli Sayfa Kesmesini Kaldırma**

Belirli bir sayfa kırmasını kaldırmak için, [**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/horizontalpagebreakcollection/#removeAt-number-) ve [**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/verticalpagebreakcollection/#removeAt-number-) metodlarını çağırın. Her **removeAt** yöntemi, kaldırılacak olan sayfa kırmasının indeksini alır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Remove Specific Page Break Example</title>
    </head>
    <body>
        <h1>Remove Specific Page Break Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Removing a specific page break
            worksheet.horizontalPageBreaks.removeAt(0);
            worksheet.verticalPageBreaks.removeAt(0);

            // Saving the Excel file (Excel 97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RemoveSpecificPageBreak_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page breaks removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Bilinmesi Gerekenler**

Sayfa ayarları yapılandırılırken, **fitToPages** özellikleri ([**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--) ve [**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--)) ayarlandığında, sayfa kırma ayarları etkilenir, bu nedenle, çalışma sayfasını yazdırırken, ayarlar yine de yapılandırılmış olmasına rağmen dikkate alınmaz.
