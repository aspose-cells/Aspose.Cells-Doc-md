---
title: Node.js ve C++ kullanarak Dahili Belge Özellikleri nin ScaleCrop ve LinksUpToDate özelliklerini ayarlama
linktitle: Yerleşik Belge Özellikleri için ScaleCrop ve LinksUpToDate özelliklerini ayarlama
type: docs
weight: 320
url: /tr/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Aspose.Cells for Node.js via C++ kullanarak dahili belge özelliklerinin ScaleCrop ve LinksUpToDate özelliklerini nasıl ayarlayacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**
[BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--) ve [BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--) OpenXml formatı içerisinde tanımlanmış iki genişletilmiş dahili belge özelliğidir. Bu özelliklerin amacı şöyledir.

## **1) ScaleCrop**
Bu öğe, belge küçüğünün görüntüleme modunu gösterir. Belge küçüğünü ekranın uygun şekilde ölçeklendirmesi için bu öğeyi **TRUE** olarak ayarlayın. Yalnızca ekranın sığabileceği bölümleri göstermek için bu öğeyi **FALSE** olarak ayarlayın.

Bu öğe için olası değerler, W3C XML Şema boolean veri türü tarafından tanımlanır.

## **2) LinksUpToDate**
Bu öğe, bir belgedeki hiperbağlantıların güncel olup olmadığını gösterir. Hiperbağlantıların güncellendiğini belirtmek için bu öğeyi **TRUE** olarak ayarlayın. Hiperbağlantıların güncel olmadığını belirtmek için bu öğeyi **FALSE** olarak ayarlayın.

Bu öğe için olası değerler, W3C XML Şema boolean veri türü tarafından tanımlanır.

## **Bu özellikleri app.xml dosyası içinde gösteren ekran görüntüsü**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Yerleşik Belge Özellikleri için ScaleCrop ve LinksUpToDate özelliklerini ayarlama**
Aşağıdaki örnek kod, çalışma kitabının [BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--) ve [BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--) genişletilmiş dahili belge özelliklerini ayarlar. Bu kod ile oluşturulan [çıktı excel dosyasını](5115500.xlsx) kontrol edin, uzantısını .zip yapın ve içeriğini çıkartın, app.xml dosyasını yukarıdaki ekran görüntüsü gibi görüntüleyin.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object.
const workbook = new AsposeCells.Workbook();

// Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
workbook.getBuiltInDocumentProperties().getScaleCrop(true);
workbook.getBuiltInDocumentProperties().setLinksUpToDate(true);

// Saving the Excel file.
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Auto);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
