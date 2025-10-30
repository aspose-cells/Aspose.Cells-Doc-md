---
title: Aspose.Cells ile Node.js kullanarak C++ üzerinden Özel XML Parçaları Kullanımı
linktitle: Aspose.Cells te Özel XML Parçalarını Kullanma
type: docs
weight: 390
url: /tr/nodejs-cpp/use-custom-xml-parts-in-aspose-cells/
description: Aspose.Cells for Node.js via C++ kullanarak özel XML parçalarını nasıl kullanacağınızı öğrenin. Dış XML verilerini Excel dosyalarına sorunsuzca entegre edin.
--- 

## Aspose.Cells'te Özel XML Parçalarını Kullanma

Özel XML Parçaları, SharePoint gibi çeşitli uygulamalar tarafından Excel dosyası içinde saklanan XML verileridir. Bu veriyi ihtiyaç duyan çeşitli uygulamalar tarafından kullanılır. Microsoft Excel bu veriyi kullanmaz, bu yüzden ekleme için bir GUI yoktur. Bu veriyi görmek için **.xlsx** uzantısını **.zip**'e değiştirip **WinZip** kullanarak açabilirsiniz. Ayrıca herhangi bir üçüncü taraf Windows zip yardımcı programı (WinRAR veya WinZip gibi) kullanarak ZIP dosyasını açabilirsiniz. Veri, **customXml** klasörü içinde bulunur.

Aspose.Cells kullanarak [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/) yöntemiyle özel XML parçaları ekleyebilirsiniz.

Aşağıdaki örnek kod, [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/) yöntemini kullanmakta ve **Book Catalog XML**'i eklemekte ve ismi **BookStore**'dır. Aşağıdaki resim, bu kodun sonucunu göstermektedir. Görüntüde, Book Catalog XML'inin BookStore düğümünün içine eklendiği görülmektedir, bu da bu özelliğin adıdır.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Node.js kullanarak özel XML parçalarını kullanma kodu

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "output.xlsx");

// The sample XML that will be injected to Workbook
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

// Create an instance of Workbook class
const workbook = new AsposeCells.Workbook();

// Add Custom XML Part to ContentTypePropertyCollection
workbook.getContentTypeProperties().add("BookStore", booksXML);

// Save the resultant spreadsheet
workbook.save(filePath);
```

## İlgili Makale

- [Belge Bilgi Paneli içinde görülebilen Özel Özellikler eklemek](/cells/tr/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="nodejs-cpp" >}}
