---  
title: Node.js経由でC++を使用してカスタムXMLパーツを追加し、IDで選択する  
linktitle: カスタムXMLパーツの追加およびIDでの選択  
type: docs  
weight: 70  
url: /ja/nodejs-cpp/add-custom-xml-parts-and-select-them-by-id/  
description: ExcelドキュメントにカスタムXMLパーツを追加し、IDで選択する方法を学びます。Aspose.Cells for Node.js via C++を使用しています。  
---  

## **可能な使用シナリオ**  

カスタムXMLパーツはMicrosoft Excelドキュメント内に保存されるXMLデータで、これを扱うアプリケーションで使用されます。現時点ではMicrosoft ExcelのUIから直接追加する方法はありませんが、プログラム的に追加可能です。例えばVSTOやAspose.Cellsを使用します。[**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--)メソッドを使うとAspose.Cells APIでカスタムXMLパーツを追加できます。また、[**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--)プロパティを使ってIDを設定可能です。同様に、IDで選択する場合は[**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--)メソッドを使用します。  

## **カスタムXMLパーツの追加およびIDでの選択**  

以下のサンプルコードは、まず[**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--)メソッドを使って4つのカスタムXMLパーツを追加します。それらのIDを[**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--)プロパティで設定し、最後に[**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--)メソッドで追加したXMLパーツの一つを検索・選択します。参考のために下記のコンソール出力も参照してください。  

## **サンプルコード**  

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

## **コンソール出力**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  

