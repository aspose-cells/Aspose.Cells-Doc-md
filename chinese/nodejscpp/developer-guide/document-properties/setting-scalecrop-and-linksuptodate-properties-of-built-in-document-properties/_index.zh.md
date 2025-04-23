---
title: 使用Node.js via C++设置内置文档属性的ScaleCrop和LinksUpToDate属性
linktitle: 设置内置文档属性的ScaleCrop和LinksUpToDate属性
type: docs
weight: 320
url: /zh/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: 学习如何使用Aspose.Cells for Node.js via C++设置内置文档属性的ScaleCrop和LinksUpToDate属性。
---

## **可能的使用场景**
[BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--) 和 [BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--)是由OpenXml格式定义的两个扩展的内置文档属性。这些属性的作用如下。

## **1) ScaleCrop**
此元素指示文档缩略图的显示模式。将此元素设置为**TRUE**以启用文档缩略图的缩放以进行显示。将此元素设置为**FALSE**以启用文档缩略图的裁剪，以仅显示适合显示器的部分。

此元素的可能值由W3C XML Schema布尔数据类型定义。

## **2) LinksUpToDate**
此元素指示文档中的超链接是否为最新状态。将此元素设置为**TRUE**表示超链接已更新。将此元素设置为**FALSE**表示超链接已过时。

此元素的可能值由W3C XML Schema布尔数据类型定义。

## **截图显示了app.xml文件中的这些属性**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **设置内置文档属性的ScaleCrop和LinksUpToDate属性**
以下示例代码设置了工作簿的[BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--)和[BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--)扩展的内置文档属性。请检查用此代码生成的[输出Excel文件](5115500.xlsx)，将其扩展名改为.zip并解压内容，查看app.xml，效果如上方屏幕截图所示。

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
