---
title: Aspose.Cells ta özel XML Bölümlerini JavaScript ve C++ kullanarak kullanın
linktitle: Aspose.Cells te Özel XML Parçalarını Kullanma
type: docs
weight: 390
url: /tr/javascript-cpp/use-custom-xml-parts-in-aspose-cells/
description: C++ kullanarak Aspose.Cells for JavaScript ile özel XML bölümlerini kullanmayı öğrenin. Excel dosyalarına dış XML verilerini sorunsuz entegre edin.
---

## Aspose.Cells'te Özel XML Parçalarını Kullanma

Özel XML Parçaları, SharePoint gibi çeşitli uygulamalar tarafından Excel dosyası içinde saklanan XML verileridir. Bu veriyi ihtiyaç duyan çeşitli uygulamalar tarafından kullanılır. Microsoft Excel bu veriyi kullanmaz, bu yüzden ekleme için bir GUI yoktur. Bu veriyi görmek için **.xlsx** uzantısını **.zip**'e değiştirip **WinZip** kullanarak açabilirsiniz. Ayrıca herhangi bir üçüncü taraf Windows zip yardımcı programı (WinRAR veya WinZip gibi) kullanarak ZIP dosyasını açabilirsiniz. Veri, **customXml** klasörü içinde bulunur.

 [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/) yöntemi aracılığıyla C++ kullanarak Aspose.Cells for JavaScript ile özel XML bölümleri ekleyebilirsiniz.

Aşağıdaki örnek kod, [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/) yöntemini kullanmakta ve **Book Catalog XML**'i eklemekte ve ismi **BookStore**'dır. Aşağıdaki resim, bu kodun sonucunu göstermektedir. Görüntüde, Book Catalog XML'inin BookStore düğümünün içine eklendiği görülmektedir, bu da bu özelliğin adıdır.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Özel XML bölümlerini kullanmak için JavaScript kodu

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Custom XML to Workbook Example</h1>
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

        const booksXML = `<catalog>
<book>
<title>Complete C#</title>
<price>44</price>
</book>
<book>
<title>Complete Java</title>
<price>76</price>
</book>
<book>
<title>Complete SharePoint</title>
<price>55</price>
</book>
<book>
<title>Complete PHP</title>
<price>63</price>
</book>
<book>
<title>Complete VB.NET</title>
<price>72</price>
</book>
</catalog>`;

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create an instance of Workbook class
            const workbook = new Workbook();

            // Add Custom XML Part to ContentTypePropertyCollection
            workbook.contentTypeProperties.add("BookStore", booksXML);

            // Save the resultant spreadsheet
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom XML added and file prepared. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## İlgili Makale

- [Belge Bilgi Paneli içinde görülebilen Özel Özellikler eklemek](/cells/tr/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
