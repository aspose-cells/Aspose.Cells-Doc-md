---
title: Node.js via C++ kullanarak XML Map in Kök Unsur Adını Bulma
linktitle: XML Haritasının Kök Öğe Adını Bul
type: docs
weight: 30
url: /tr/nodejs-cpp/find-the-root-element-name-of-xml-map/
description: Excel de XML haritasının kök unsur adını Aspose.Cells for Node.js via C++ kullanarak nasıl bulunacağını öğrenin.
---

## **Olası Kullanım Senaryoları**

XML Map'in kök unsur adını [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--) özelliği ile Aspose.Cells for Node.js via C++ kullanarak bulabilirsiniz. Aşağıdaki ekran görüntüsü, Microsoft Excel'de XML Haritasının kök unsur adını gösterir.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Örnek Kod**

Aşağıdaki örnek kod, [örnek Excel dosyasını](55541789.xlsx) yükler ve ilk XML Map'e erişir ve [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--) özelliğini yazdırır. Lütfen aşağıdaki örnek kodun konsol çıktısına bakın.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRootElementNameOfXmlMap.xlsx");

// Load sample Excel file having Xml Map
const wb = new AsposeCells.Workbook(filePath);

// Access first Xml Map inside the Workbook
const xmap = wb.getWorksheets().getXmlMaps().get(0);

// Print Root Element Name of Xml Map on Console
console.log("Root Element Name Of Xml Map: " + xmap.getRootElementName());
```

## **Konsol Çıktısı**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
