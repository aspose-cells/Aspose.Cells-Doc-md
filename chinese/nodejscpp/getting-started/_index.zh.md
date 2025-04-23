---
title: 入门
type: docs
weight: 5
url: /zh/nodejs-cpp/getting-started/
keywords: "nodejs, excel, install"
description: "安装Aspose.Cells for Node.js via C++和安装指南。"
---

## **产品描述**
Aspose.Cells for Node.js via C++是一个功能强大且稳健的库，专为在Node.js应用中高性能操控和管理电子表格设计。它提供全面的功能集，允许开发者以编程方式创建、编辑、转换和渲染Excel文件。支持所有主要的Excel格式，包括XLS、XLSX、XLSM等，确保兼容性和灵活性。这使得Aspose.Cells for Node.js via C++成为一个多用途工具，适用于各种数据处理与管理任务，为开发者提供了整合丰富Excel功能的完整且高效的解决方案。

## **主要特性**
1. **文件创建与编辑：** 从头创建新电子表格或轻松编辑现有电子表格，包括添加或修改数据、格式化单元格、管理工作表等。
1. **数据处理：** 执行复杂的数据操作，如排序、筛选和验证。库还支持高级公式和函数，以便数据分析和计算。
1. **文件转换：** 将Excel文件转换为PDF、HTML、ODS及图片格式（如PNG和JPEG），方便分享和分发数据。
1. **图表与图形：** 创建和定制各种图表和图形以直观显示数据，支持条形图、折线图、饼图等以及设计和布局的定制选项。
1. **渲染与打印：** 将Excel工作表渲染为高品质图像和PDF，确保显示效果准确，支持打印布局和格式控制。
1. **高级保护与安全：** 用密码保护电子表格、加密文件、管理访问权限，确保数据安全和完整性。
1. **性能与可扩展性：** 设计用于高效处理大数据集和复杂电子表格，Aspose.Cells for Node.js via C++确保企业级应用的高性能和可扩展性。


## **从 NPM 安装**
你可以通过以下命令轻松使用[NPМ](https://www.npmjs.com/package/aspose.cells.node)中的Aspose.Cells for Node.js via C++。
{{< highlight java >}}

 $ npm install aspose.cells.node

{{< /highlight >}}

如果在安装过程中遇到任何问题，请参考 https://www.npmjs.com/package/package。


## **Hello World 示例**

{{< highlight cpp >}}

const AsposeCells = require("aspose.cells.node");

var workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World");
workbook.save("hello-world.xlsx");

{{< /highlight >}}
