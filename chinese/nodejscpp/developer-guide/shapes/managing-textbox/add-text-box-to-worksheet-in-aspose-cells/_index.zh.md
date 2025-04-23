---
title: 如何使用Node.js通过C++向工作表添加/插入文本框
linktitle: 在工作表中添加文本框
type: docs
weight: 10
url: /zh/nodejs-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: 了解如何在Aspose.Cells for Node.js via C++中添加/插入文本框到工作表中。
keywords: 在Aspose.Cells for Node.js via C++中添加/插入文本框到工作表，使用Node.js通过C++
---

在Excel中的工作表中添加文本框

在Excel（版本07及以上）中，有两个地方可以插入文本框。一个是在"插入-形状"中，另一个在“插入”选项的顶端菜单右侧。

### 方法一：

![1](1.png)

### 方法二：

![2](2.png)

## 如何创建

您可以创建水平或垂直文本框。

- 选择相应的选项（横向或纵向）
- 在页面上单击左键
- 按住左键并在页面上拖动一段距离
- 释放左键

现在您可以获得一个文本框。

## 在Aspose.Cells for Node.js via C++中向工作表添加文本框

当你需要批量插入文本框到工作表时，手动插入方法显然是一场灾难。如果这让你困扰，我认为这份文档会帮到你。[Aspose.Cells](https://products.aspose.com/cells/) 为你提供了一个API，便于在代码中实现批量插入。

以下示例代码创建一个文本框。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an object of the Workbook class
const workbook = new AsposeCells.Workbook();

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
sheet.getTextBoxes().add(6, 10, 100, 200);

// Save. You can check your text box in this way.
workbook.save("result.xlsx", AsposeCells.SaveFormat.Xlsx);
```

你将获得一个类似 [结果文件](result.xlsx) 的文件。在文件中，你会看到以下内容：

![](52449.png)

