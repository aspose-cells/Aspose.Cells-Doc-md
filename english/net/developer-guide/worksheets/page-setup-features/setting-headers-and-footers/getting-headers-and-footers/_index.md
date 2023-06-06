---
title: Getting Headers or Footers
type: docs
weight: 30
url: /net/get-headers-or-footers/
description: This article explains how to programmatically get header and footers from Excel or OpenOffice files using the C# API or .NET Library.
---

{{% alert color="primary" %}}

Headers and footers are displayed only in Page Layout view, Print Preview, and on printed pages. 

You can also use the Page Setup dialog box if you want to insert headers or footers for more than one worksheet at a time. 

For other sheet types, such as chart sheets, or charts, you can insert headers and footers only by using the Page Setup dialog box.

{{% /alert %}}

## **Getting Headers and Footers in MS Excel**
1. Click the worksheet where you want to view or change headers or footers.
2. On the Vie tab, in the Workbook Views group, click Page Layout.
  Excel displays the worksheet in Page Layout view.
3. To view or edit a header or footer, click the left, center, or right header or footer text box at the top or the bottom of the worksheet page (under Header, or above Footer).


## **Getting Headers and Footers using Aspose.Cells for .Net**
With [**Worksheet.GetHeader**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetHeader/) and [**Worksheet.GetFooter**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFooter/) methods, .Net developer can simply get headers or footers from the file.

1. Construct Workbook to open the file.
2. Gets the worksheet which contains headers or footer.
3. Gets header or footer with specific section id.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Gets-Header-Footer.cs" >}}