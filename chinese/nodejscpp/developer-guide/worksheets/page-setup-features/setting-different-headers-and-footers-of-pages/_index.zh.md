---
title: 用 Node.js 和 C++ 为不同页面设置不同的页眉和页脚
linktitle: 设置不同页的不同页眉和页脚
type: docs
weight: 35
url: /zh/nodejs-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: 本文提供示例代码，展示如何使用 Aspose.Cells for Node.js via C++ 程序设置 Excel 工作表页面设置的页眉和页脚，包括首页、奇数页和偶数页。
keywords: 用 Node.js 和 C++ 设置 Excel 页眉页脚——首页、奇数页和偶数页
---

{{% alert color="primary" %}}

自Excel 2007起，MS Excel支持为首页、奇数页和偶数页设置不同的页眉和页脚。
Aspose.Cells for Node.js via C++支持相同的功能。

{{% /alert %}}

## **在MS Excel中设置不同的页眉和页脚**

**![设置不同的页眉和页脚](difpage.png)**

1. 单击**页面布局 > 打印标题 > 页眉/页脚**。
1. 检查 **不同奇数和偶数页面** 或 **首页不同**。
1. 输入不同的页眉和页脚。

## **使用 Aspose.Cells for Node.js via C++ 设置不同的页眉和页脚**

Aspose.Cells与Excel的行为相同。
1. 设置标志 [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffOddEven--) 和 [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffFirst--) 
1. 输入不同的页眉和页脚。
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Gets the setting of page setup.
const pageSetup = wb.getWorksheets().get(0).getPageSetup();
// Sets different odd and even pages
pageSetup.setIsHFDiffOddEven(true);
pageSetup.setHeader(1, "I am the header of the Odd page.");
pageSetup.setEvenHeader(1, "I am the header of the Even page.");
// Sets different first page
pageSetup.setIsHFDiffFirst(true);
pageSetup.setFirstPageHeader(1, "I am the header of the First page.");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
