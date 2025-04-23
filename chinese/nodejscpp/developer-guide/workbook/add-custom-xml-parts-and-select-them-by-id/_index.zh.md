---  
title: 添加自定义XML部件并通过ID选择它们，使用Node.js和C++  
linktitle: 添加自定义XML部件并按ID选择  
type: docs  
weight: 70  
url: /zh/nodejs-cpp/add-custom-xml-parts-and-select-them-by-id/  
description: 学习如何向Excel文档添加自定义XML部件并通过ID进行选择，使用Aspose.Cells for Node.js via C++。  
---  

## **可能的使用场景**  

自定义XML部件是存储在Microsoft Excel文档中的XML数据，供处理它们的应用程序使用。目前没有直接通过Microsoft Excel UI添加它们的方法。但你可以通过编程方式添加，例如使用VSTO、Aspose.Cells等。如果你想用Aspose.Cells API添加自定义XML部件，请使用[**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--)方法。你还可以通过[**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--)属性设置其ID。同样，若要按ID选择自定义XML部件，可以使用[**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--)方法。  

## **添加自定义XML部件并按ID选择**  

下面的示例代码首先使用[**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--)方法添加四个自定义XML部件，然后用[**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--)属性设置它们的ID，最后用[**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--)方法找到或选择已添加的某个自定义XML部件。请参阅下面的控制台输出以获取参考。  

## **示例代码**  

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

## **控制台输出**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  

