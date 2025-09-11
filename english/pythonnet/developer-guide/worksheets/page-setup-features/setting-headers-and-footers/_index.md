---
title: Setting Headers and Footers
type: docs
weight: 30
url: /python-net/setting-headers-and-footers/
description: This article explains how to programmatically insert an image in the header and footer of Excel worksheets by setting the header and footer with script commands using the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python insert image in excel header footer, set excel header footer script commands using Python.
---

{{% alert color="primary" %}}

Headers and footers are the lines of text displayed below the top margin or above the bottom margin respectively. It's possible to add headers and footers to the worksheets also. Headers and footers can be used to display useful information like page number, author name, topic name, or date and time. Headers and footers are managed using the page setup settings.

{{% /alert %}}

## **Setting Headers and Footers**

Aspose.Cells for Python via .NET allows you to add headers and footers to worksheets at runtime but we recommend setting headers and footers manually in a pre-designed file for printing. You can use Microsoft Excel as a GUI tool to set headers and footers to save effort and development time. Aspose.Cells for Python via .NET can import the file and save the settings.

To add headers and footers at runtime, Aspose.Cells for Python via .NET provides special API calls and script commands to format headers and footers.

### **Script Commands**

Script commands are special commands that allow you to set header and footer formatting.

|**Script Commands**|**Description**|
| :- | :- |
|&P|The current page number|
|&G|A picture|
|&N|The total number of pages|
|&D|The current date|
|&T|The current time|
|&A|The worksheet name|
|&F|The file name without its path|
|&"\<FontName>"|Represents a font name. For example: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Represents font name with style. For example: &"Arial,Bold"|
|&\<FontSize>|Represents font size. For example: “&14abc”. But, if this command is followed by a plain number to be printed in the header, this should be separated with a space character from the font size. For example: “&14 123”.|

### **How to Set Headers and Footers**

The [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class provides two methods, [**set_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header/#int-str) and [**set_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer/#int-str), used to add a header and footer to a worksheet. These methods take only two parameters:

- **Section** – the section where the header or footer should be placed. There are three sections: left, center and right, represented by 0, 1 and 2 respectively.
- **Script** – the script to be used for the header or footer. This script contains script commands to format headers or footers.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.py" >}}

### **How to Insert an Image into a Header or Footer**

The [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class has two additional methods, [**set_header_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header_picture/#int-bytes) and [**set_footer_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer_picture/#int-bytes), used to add pictures into the header and footer. These methods take the parameters:

- **Section** – the header or footer section where the picture will be placed. There are three sections, left, center and right, represented by the values 0, 1 and 2 respectively.
- **Byte array** – the graphical data (the binary data should be written into the buffer of a byte array).

After executing the code below and opening the file, check the header of the worksheet by:

1. On the **File** menu, select **Page Setup**. A dialog will be displayed.
1. Select the **Header/Footer** tab.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.py" >}}
{{< app/cells/assistant language="python-net" >}}