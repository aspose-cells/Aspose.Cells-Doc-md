---
title: Getting Headers or Footers
type: docs
weight: 30
url: /python-net/get-headers-or-footers/
description: This article explains how to programmatically get headers and footers from Excel or OpenOffice files using the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python get headers and footers, Parse Headers and Footers to Command List using Python.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Headers and footers are displayed only in Page Layout view, Print Preview, and on printed pages. 

You can also use the Page Setup dialog box if you want to view headers or footers for more than one worksheet at a time. 

For other sheet types, such as chart sheets, or charts, you can insert headers and footers only by using the Page Setup dialog box.

{{% /alert %}}

## **How to Get Headers and Footers in MS Excel**
1. Click the worksheet where you want to view or change headers or footers.
2. On the **View** tab, in the Workbook Views group, click **Page Layout**.  
   Excel displays the worksheet in Page Layout view.
3. To view or edit a header or footer, click the left, center, or right header or footer text box at the top or the bottom of the worksheet page (under Header or above Footer).


## **How to Get Headers and Footers using Aspose.Cells for Python Excel Library**
With [**Worksheet.page_setup.get_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_header/#int) and [**Worksheet.page_setup.get_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_footer/#int) methods, .NET developers can simply retrieve headers or footers from a workbook.

1. Construct a [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) to open the file.
2. Get the worksheet from which you want to retrieve the header or footer.
3. Get the header or footer using a specific section ID.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Gets-Header-Footer.py" >}}

## **How to Parse Headers and Footers to Command List**
The header or footer text can contain special commands, for example a placeholder for the page number, current date, or text‑formatting attributes.

Special commands are represented by a single letter with a leading ampersand ("&").

The header and footer strings are constructed using ABNF grammar. It’s not easy to understand without a viewer.

Aspose.Cells for Python via .NET provides the [**Worksheet.page_setup.get_commands**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_commands/#str) method to parse headers and footers into a command list.

The following code shows how to parse the header or footer into a command list and process the commands:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Parses-Header-Footer.py" >}}
{{< app/cells/assistant language="python-net" >}}
