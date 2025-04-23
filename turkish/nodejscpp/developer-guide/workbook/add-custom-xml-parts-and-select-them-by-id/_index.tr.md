---  
title: Node.js üzerinden C++ kullanarak Özel XML Parçalarını ekleyin ve ID ile seçin  
linktitle: Özel XML Parçalarını Ekleyin ve ID leri ile Seçin  
type: docs  
weight: 70  
url: /tr/nodejs-cpp/add-custom-xml-parts-and-select-them-by-id/  
description: Excel belgelerine özel XML parçalarını nasıl ekleyeceğinizi ve bunları ID ile nasıl seçeceğinizi Aspose.Cells for Node.js via C++ kullanarak öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Özel XML Parçaları, Microsoft Excel belgelerinin içinde saklanan XML verileridir ve bunlarla ilgilenen uygulamalar tarafından kullanılır. Şu anda Microsoft Excel kullanıcı arayüzü kullanarak bunları doğrudan eklemenin bir yolu yoktur. Ancak, bunları programatik olarak çeşitli yollarla ekleyebilirsiniz, örneğin VSTO kullanarak, Aspose.Cells kullanarak vb. Lütfen Aspose.Cells API'sini kullanarak Özel XML Parçası eklemek istiyorsanız [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--) metodunu kullanın. Ayrıca, [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--) özelliği ile ID'sini ayarlayabilirsiniz. Benzer şekilde, ID ile özel XML Parçasını seçmek istiyorsanız [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--) metodunu kullanabilirsiniz.  

## **Özel XML Parçalarını ekleyin ve ID'leri ile seçin**  

Aşağıdaki örnek kod ilk olarak [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--) yöntemiyle dört adet Özel XML Parçası ekler. Ardından, bunların ID'lerini [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--) özelliği kullanarak ayarlar. Son olarak, eklenen Özel XML Parçası'ndan birini [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--) yöntemiyle bulur veya seçer. Ayrıca, aşağıda verilen kodun konsol çıktısına da göz atın.  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Some data in the form of byte array.
// Please use correct XML and Schema instead.
const btsData = new Uint8Array([1, 2, 3]);
const btsSchema = new Uint8Array([1, 2, 3]);

// Create four custom xml parts.
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);

// Assign ids to custom xml parts.
wb.getCustomXmlParts().get(0).setID("Fruit");
wb.getCustomXmlParts().get(1).setID("Color");
wb.getCustomXmlParts().get(2).setID("Sport");
wb.getCustomXmlParts().get(3).setID("Shape");

// Specify search custom xml part id.
let srchID = "Fruit";
srchID = "Color";
srchID = "Sport";

// Search custom xml part by the search id.
const cxp = wb.getCustomXmlParts().selectByID(srchID);

// Print the found or not found message on console.
if (cxp.isNull()) {
console.log(`Not Found: CustomXmlPart ID ${srchID}`);
} else {
console.log(`Found: CustomXmlPart ID ${srchID}`);
}

console.log("AddCustomXMLPartsAndSelectThemByID executed successfully.");
```  

## **Konsol Çıktısı**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  

