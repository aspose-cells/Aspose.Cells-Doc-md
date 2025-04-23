---  
title: 使用 C++ 在 Workbook 中添加 XML 映射 XmlMapCollection.Add 方法  
linktitle: 使用XmlMapCollection.Add方法在工作簿中添加XML映射  
type: docs  
weight: 10  
url: /zh/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 通过 XmlMapCollection.Add 方法在工作簿中添加 XML 映射。  
---  

## **可能的使用场景**  

Aspose.Cells 提供了 [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) 方法，您可以使用该方法将 XML 映射导入工作簿。  

## **使用XmlMapCollection.Add方法在工作簿中添加XML映射**  

以下示例代码使用 [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) 方法向工作簿中添加 XML 映射，并将其保存为 [输出 Excel 文件](5115434.xlsx)。屏幕截图显示了已从 [sample.xml](5115433.xml) 中导入的 XML 映射。  

![add-xml-map](add-xml-map.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Add xml map found inside the sample.xml inside the workbook
wb.getWorksheets().getXmlMaps().add(path.join(dataDir, "sample.xml"));

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```  

