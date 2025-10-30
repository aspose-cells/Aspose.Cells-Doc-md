---
title: Doküman Bilgi Paneli içinde görünür özel özellikler ekleme ile Node.js ve C++
linktitle: Belge Bilgi Paneli içinde görülebilen Özel Özellikler eklemek
type: docs
weight: 300
url: /tr/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Aspose.Cells for Node.js via C++ kullanarak çalışma kitabı nesnesine özel özellikler eklemeyi öğrenin. Bu özellikler Belge Bilgi Paneli nde görüntülenebilir.
---

## **Belge Bilgi Paneli içinde görülebilen Özel Özellikler eklemek**

Aspose.Cells for Node.js via C++ içindeki özel özellikler çalışma kitabı nesnesine eklenebilir ve Belge Bilgi Paneli'nde görünür. Microsoft Excel'de Belge Bilgi Paneli'ni Dosya > Bilgi > Özellikler > Belge Panelini Göster menü komutlarını kullanarak açabilirsiniz.

Lütfen belge bilgisi panelinde görünür olacak özelleştirilmiş özellik eklemek için [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/#add-string-string-) yöntemini kullanın.

Aşağıdaki örnek kod, iki özelleştirilmiş özellik ekler. Birinci özellik herhangi bir tipe sahip değildir, ikinci özellik ise tarih/zaman tipi taşır. Bu kodla oluşturulan çıktı Excel dosyasını açtığınızda, bu iki özelliği Belge Bilgisi Panelinde göreceksiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Add simple property without any type
workbook.getContentTypeProperties().add("MK31", "Simple Data");

// Add date time property with type
workbook.getContentTypeProperties().add("MK32", "04-Mar-2015", "DateTime");

// Save the workbook
workbook.save(path.join(dataDir, "AddingCustomPropertiesVisible_out.xlsx"));
```

### **İlgili Makale**

{{% alert color="primary" %}}

- [Aspose.Cells'te Özel XML Parçalarını Kullanma](/cells/tr/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
