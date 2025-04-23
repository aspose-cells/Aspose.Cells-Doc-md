---  
title: 用Node.js和C++从网页地址插入链接图片  
linktitle: 从Web地址插入链接图片  
type: docs  
weight: 450  
url: /zh/nodejs-cpp/insert-a-linked-picture-from-web-address/  
description: 学习如何使用Aspose.Cells for Node.js via C++将网页地址中的链接图片插入到工作表中。  
---  

{{% alert color="primary" %}}  
有时候你需要从网页(http://)插入一张图片到工作表中。只需指定图片的URL，每次在Excel中打开电子表格时，图片将被下载。图片不会被实际嵌入到Excel文件中，而是指向一个网页资源。  
{{% /alert %}}  

## **使用Microsoft Excel**  

在Microsoft Excel中（例如2007）：  

1. 单击**插入**菜单，然后选择**图片**。  
1. 在插入图片对话框中指定图片的Web地址。  

## **使用 Aspose.Cells for Node.js via C++**  

Aspose.Cells for Node.js via C++支持使用[**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-)添加链接的图片。该方法返回一个[**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture)对象。  

以下示例展示了如何将来自Web地址的链接图片添加到工作表中。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();
// Insert a linked picture (from Web Address) to B2 Cell.
const pic = workbook.getWorksheets().get(0).getShapes().addLinkedPicture(1, 1, 100, 100, "http://www.aspose.com/Images/aspose-logo.jpg");
// Set the height and width of the inserted image.
pic.setHeightInch(1.04);
pic.setWidthInch(2.6);
// Save the Excel file.
workbook.save(path.join(dataDir, "outLinkedPicture.out.xlsx"));
```  

