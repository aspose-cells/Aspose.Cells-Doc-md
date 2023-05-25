---
title: 设置边距
type: docs
weight: 20
url: /zh/net/setting-margins/
description: 在本文中，您将学习如何使用示例代码设置 Excel 工作表的页边距。您还将学习如何使用 C# API 或 .NET 库以编程方式设置页面中心的边距、页面设置的页眉和页脚边距。
keywords: set excel worksheet margin to center c#, set worksheet header and footer margin c#
---
{{% alert color="primary" %}}

Aspose.Cells 完全支持 Microsoft Excel 的页面设置选项。开发人员可能需要为工作表配置页面设置以控制打印过程。本主题讨论如何使用 Aspose.Cells 配置页边距。

{{% /alert %}}

##  **设置边距**

 Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , 表示一个 Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。

这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)用于设置工作表页面设置选项的属性。这[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)属性是[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)使开发人员能够为打印的工作表设置不同页面布局选项的类。这[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)类提供用于设置页面设置选项的各种属性和方法。

###  **页边距**

使用设置页边距（左、右、上、下）[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)班级成员。下面列出了一些用于指定页边距的方法：

- [**左边距**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**右边距**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**顶边距**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**底边距**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

###  **页面居中**

可以在页面上水平和垂直居中某些内容。为此，有一些有用的成员[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)班级，[**水平居中**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally)和[**垂直居中**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

###  **页眉和页脚边距**

设置页眉和页脚边距[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)班级成员如[**页眉边距**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin)和[**页脚边距**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
