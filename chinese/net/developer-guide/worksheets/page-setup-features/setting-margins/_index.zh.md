---
title: 设置页边距
type: docs
weight: 20
url: /zh/net/setting-margins/
description: 在本文中，您将了解如何使用示例代码设置Excel工作表的页边距。您还将学习如何使用C# API或.NET库对页面设置的页中心、页眉和页脚页边距进行编程设置。
keywords: 设置Excel工作表页边距为中心C#，设置工作表页眉和页脚页边距C#
---

{{% alert color="primary" %}}

Aspose.Cells完全支持Microsoft Excel的页面设置选项。开发人员可能需要为工作表配置页面设置以控制打印过程。本主题讨论了如何使用Aspose.Cells配置页面边距。

{{% /alert %}}

## **设置页边距**

Aspose.Cells提供了一个表示Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)属性，用于为工作表设置页面设置选项。[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)属性是[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)类的对象，使开发人员能够为打印的工作表设置不同的页面布局选项。[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)类提供了用于设置页面设置选项的各种属性和方法。

### **页边距**

使用[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)类成员设置页面边距（左、右、上、下）。下面列出了一些用于指定页面边距的方法：

- [**LeftMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**RightMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**TopMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**BottomMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **居中打印**

可以在页面水平和垂直方向上居中对齐。为此，[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)类有一些有用的成员，[**CenterHorizontally**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally)和[**CenterVertically**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically)。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **页眉和页脚页边距**

使用[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)类成员如[**HeaderMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin)和[**FooterMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin)设置页眉和页脚页边距。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
