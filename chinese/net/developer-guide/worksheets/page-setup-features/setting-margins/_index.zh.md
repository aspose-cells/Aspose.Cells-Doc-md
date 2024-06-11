---
title: 设置边距
type: docs
weight: 20
url: /zh/net/setting-margins/
description: 在本文中，您将学习如何使用示例代码设置 Excel 工作表的边距。您还将学习如何使用 C# API 或 .NET Library 对页面设置的页中、页眉和页脚边距进行程序化设置。
keywords: 将 Excel 工作表边距设置为居中 c#，设置工作表页眉和页脚边距 c#
---

{{% alert color="primary" %}}

Aspose.Cells 完全支持微软 Excel 的页面设置选项。开发人员可能需要为工作表配置页面设置以控制打印过程。本主题讨论如何使用 Aspose.Cells 配置页面边距。

{{% /alert %}}

## **设置页边距**

Aspose.Cells 提供一个名为 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 的类，它表示 Excel 文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含允许访问 Excel 文件中每个工作表的 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合。工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)属性，用于设置工作表的页面设置选项。[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)属性是[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)类的一个对象，使开发人员能够为打印的工作表设置不同的页面布局选项。[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)类提供了用于设置页面设置选项的各种属性和方法。

### **页面边距**

使用[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)类的成员设置页面边距（左、右、上、下）。下面列出了一些用于指定页面边距的方法：

- [**LeftMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**RightMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**TopMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**BottomMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **页面居中**

可以在页面上水平和垂直居中某物。为此，[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)类的一些有用的成员是[**CenterHorizontally**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally)和[**CenterVertically**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically)。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **页眉和页脚边距**

使用[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)类的成员（如[**HeaderMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin)和[**FooterMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin)）设置页眉和页脚边距。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
