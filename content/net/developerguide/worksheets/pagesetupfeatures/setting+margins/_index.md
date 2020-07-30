---
title : "Setting Margins" 
description : "" 
weight : 16154 
toc : false
type: docs
url: /net/developerguide/worksheets/pagesetupfeatures/setting+margins/
---

# Aspose.Cells for .NET : Setting Margins


Aspose.Cells fully supports Microsoft Excel's page setup options. Developers may need to configure page setup settings for worksheets to control the printing process. This topic discusses how to use Aspose.Cells to configure page margins.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Setting Margins](#setting-margins)
    *   1.1 [Page Margins](#page-margins)
    *   1.2 [Center on Page](#center-on-page)
    *   1.3 [Header and Footer Margins](#header-and-footer-margins)
{{< /panel >}}
 

 

## Setting Margins

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook), that represents an Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains the [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class.

The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides the [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/pagesetup) property used to set the page setup options for a worksheet. The [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/pagesetup) attribute is an object of the [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class that enables developers to set different page layout options for a printed worksheet. The [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class provides various properties and methods used to set page setup options.

### Page Margins

Set page margins (left, right, top, bottom) using [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class members. A few of the methods are listed below which are used to specify page margins:

*   [LeftMargin](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/leftmargin)
*   [RightMargin](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/rightmargin)
*   [TopMargin](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/topmargin)
*   [BottomMargin](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/bottommargin)

### Center on Page

It is possible to center something on a page horizontally and vertically. For this, there are some useful members of the [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class, [CenterHorizontally](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/centerhorizontally) and [CenterVertically](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/centervertically).

### Header and Footer Margins

Set header and footer margins with the [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class members such as [HeaderMargin](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/headermargin) and [FooterMargin](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/footermargin).

