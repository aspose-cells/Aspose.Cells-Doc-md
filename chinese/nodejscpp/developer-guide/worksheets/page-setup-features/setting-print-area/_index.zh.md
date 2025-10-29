---
title: 如何通过Node.js使用C++设置打印区域
linktitle: 如何设置打印区域
type: docs
weight: 200
url: /zh/nodejs-cpp/how-to-set-print-area/
description: 本文显示了如何使用C++的Aspose.Cells库，通过Node.js设置打印区域的代码示例。
keywords: 限制打印范围、设置打印范围、清除打印范围、使用Node.js通过C++设置和清除打印范围、如何在Node.js通过C++设置打印区域、在Excel中设置和清除打印区域。
---

## **可能的使用场景**

 在文档（如 Excel 表格）中设置打印区域，有助于控制打印内容。设定打印区域的原因包括：

1. 聚焦特定数据：只打印最相关的部分，避免不必要的内容。
1. 改善布局：帮助整理和合理排放内容，避免拆分或不必要的分页。
1. 节省资源：通过限制打印区域，减少用纸和墨水。
1. 专业呈现：确保只打印整理好的最终版数据，特别适用于报告或演示。
1. 保持一致性：多次打印同一文档时，设定打印区域确保输出一致。

<br>
设置打印区域特别适合较大文档，只需部分内容用于打印或审查。

## ** 如何在 Excel 中设置打印区域**

 在 Excel 中设置打印区域的步骤：

 1. 选择单元格：点击并拖动以选择你希望设为打印区域的单元格区域。
 1. 打开页面布局标签：在 Excel 窗口顶部的功能区中点击“页面布局”标签。
 1. 设置打印区域：在“页面设置”组中点击“打印区域”。在下拉菜单中选择“设为打印区域”。
<br>
<img src="3.png" width=60% />

 1. 添加到打印区域：如果想添加更多单元格到现有打印区域，选择额外的单元格，转到“页面布局”中的“打印区域”，选择“添加到打印区域”。

<br>
此操作将选中的单元格定义为打印区域。当你打印工作表时，只有这个定义的区域会被打印。

## **如何在Excel中清除打印区域**

在Excel中清除打印区域，请按照以下步骤：

1. 打开页面布局选项卡：点击 Excel 窗口顶部功能区中的“页面布局”。
1. 清除打印区域：在“页面设置”组中，点击“打印区域”。在下拉菜单中选择“清除打印区域”。
<br>
<img src="4.png" width=60% />

<br>
此操作将删除任何先前设置的打印区域，使整个工作表都可以被打印。

## **清除打印区域后会发生什么**

在使用Aspose.Cells的电子表格程序中清除打印区域，将导致打印时包含整个工作表。如果已设置打印区域，则只会打印指定范围的单元格。通过清除打印区域，确保没有特定范围被定义，默认的打印行为——包括整个工作表——将生效。

1. 默认打印行为：整个工作表将被考虑进行打印。这意味着所有带有数据或格式的单元格都将被打印。
1. 无打印区域限制：之前定义的打印区域限制将被移除。如果曾经指定了特定的行和列用于打印，那些限制将不再生效。
1. 全内容打印：所有内容，包括标题、页脚和工作表内的其他数据，都将包含在打印任务中。

## ** 如何使用Aspose.Cells for Node.js via C++设置打印区域**

 要在指定工作表中设置打印区域：首先加载[示例文件](input.xlsx)，然后需要修改目标工作表的[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/)对象的[**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--)属性。将此属性设置为范围字符串将设置打印区域。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area - specify the range you want to print
worksheet.getPageSetup().setPrintArea("A1:D10");

// Save the workbook
workbook.save("set_print_area.pdf");
```

输出结果：
<br>
<img src="1.png" width=60% />

## ** 如何使用Aspose.Cells for Node.js via C++清除打印区域**

要在指定工作表中清除打印区域：首先加载[示例文件](input.xlsx)，然后需要修改目标工作表的[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/)对象的[**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--)属性。将该属性设置为空字符串，即可清除打印区域。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Clear the print area
worksheet.getPageSetup().setPrintArea("");

// Save the workbook
workbook.save("clear_print_area.pdf");
```

输出结果：
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="nodejs-cpp" >}}
