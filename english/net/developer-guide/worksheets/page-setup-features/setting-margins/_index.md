---
title: Setting Margins
type: docs
weight: 20
url: /net/setting-margins/
description: In this article, you will learn how to set the margins of an Excel worksheet using sample code. You will also learn how to programmatically set the margins for the page centre, the header and footer margins of Page Setup using the C# API or .NET Library.
keywords: set excel worksheet margin to center c#, set worksheet header and footer margin c#
---

{{% alert color="primary" %}}

Aspose.Cells fully supports Microsoft Excel's page setup options. Developers may need to configure page setup settings for worksheets to control the printing process. This topic discusses how to use Aspose.Cells to configure page margins.

{{% /alert %}}

## **Setting Margins**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains the [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class.

The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides the [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) property used to set the page setup options for a worksheet. The [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) attribute is an object of the [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) class that enables developers to set different page layout options for a printed worksheet. The [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) class provides various properties and methods used to set page setup options.

### **Page Margins**

Set page margins (left, right, top, bottom) using [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) class members. A few of the methods are listed below which are used to specify page margins:

- [**LeftMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**RightMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**TopMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**BottomMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **Center on Page**

It is possible to center something on a page horizontally and vertically. For this, there are some useful members of the [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) class, [**CenterHorizontally**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) and [**CenterVertically**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **Header and Footer Margins**

Set header and footer margins with the [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) class members such as [**HeaderMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) and [**FooterMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
{{< app/cells/assistant language="csharp" >}}