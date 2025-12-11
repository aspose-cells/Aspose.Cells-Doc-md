---
title: Setting Headers and Footers
type: docs
weight: 30
url: /net/setting-headers-and-footers/
description: This article explains how to programmatically insert an image in the header and footer of Excel worksheets by setting the header and footer with script commands using the C# API or .NET Library.
keywords: insert image in excel header footer c#, set excel header footer script commands c#
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Headers and footers are the lines of text displayed below the top margin or above the bottom margin, respectively. Headers and footers can also be added to worksheets. They can be used to display useful information like the page number, author name, topic name, or date and time. Headers and footers are managed using the page‑setup settings.

{{% /alert %}}

## **Setting Headers and Footers**

Aspose.Cells allows you to add headers and footers to worksheets at runtime, but we recommend setting them manually in a pre‑designed file for printing. You can use Microsoft Excel as a GUI tool to set headers and footers, saving effort and development time. Aspose.Cells can then import the file and retain the settings.

To add headers and footers at runtime, Aspose.Cells provides special API calls and script commands to format them.

### **Script Commands**

Script commands are special commands that allow you to set header and footer formatting.

| **Script Commands** | **Description** |
| :- | :- |
| &P | The current page number |
| &G | A picture |
| &N | The total number of pages |
| &D | The current date |
| &T | The current time |
| &A | The worksheet name |
| &F | The file name without its path |
| &&Text | Shows &Text. For example, &&WO will be displayed as &WO |
| &"<FontName>" | Represents a font name. For example: &"Arial" |
| &"<FontName>, <FontStyle>" | Represents a font name with style. For example: &"Arial,Bold" |
| &<FontSize> | Represents font size. For example: “&14abc”. But if this command is followed by a plain number to be printed in the header, it should be separated with a space character from the font size. For example: “&14 123”. |

### **Set Headers and Footers**

The [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) class provides two methods, [**SetHeader**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader) and [**SetFooter**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter), used to add a header and footer to a worksheet. These methods take only two parameters:

- **Section** – the section where the header or footer should be placed. There are three sections: left, center, and right, represented by 0, 1 and 2 respectively.
- **Script** – the script to be used for the header or footer. This script contains script commands to format headers or footers.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

### **Insert an Image into a Header or Footer**

The [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) class has two additional methods, [**SetHeaderPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture) and [**SetFooterPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture), used to add pictures into the header and footer. These methods take the parameters:

- **Section** – the header or footer section where the picture will be placed. There are three sections: left, center, and right, represented by the values 0, 1 and 2 respectively.
- **Byte array** – the graphical data (the binary data should be written into the buffer of a byte array).

After executing the code below and opening the file, check the header of the worksheet by:

1. On the **File** menu, select **Page Setup**. A dialog will be displayed.  
2. Select the **Header/Footer** tab.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
