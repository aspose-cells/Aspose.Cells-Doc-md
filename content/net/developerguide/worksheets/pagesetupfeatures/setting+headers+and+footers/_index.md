---
title : "Setting Headers and Footers" 
description : "" 
weight : 16155 
toc : false
type: docs
url: /net/developerguide/worksheets/pagesetupfeatures/setting+headers+and+footers/
---

# Aspose.Cells for .NET : Setting Headers and Footers


Headers and footers are the lines of text displayed below the top margin or above the bottom margin respectively. It's possible to add headers and footers to the worksheets also. Headers and footers can be used to display useful information like page number, author name, topic name, or date and time. Headers and footers are managed using the page setup settings.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Setting Headers and Footers](#setting-headers-and-footers)
    *   1.1 [Script Commands](#script-commands)
    *   1.2 [Set Headers and Footers](#set-headers-and-footers)
    *   1.3 [Insert an Image into a Header or Footer](#insert-an-image-into-a-header-or-footer)
{{< /panel >}}
 

 

## Setting Headers and Footers

Aspose.Cells allows you to add headers and footers to worksheets at runtime but we recommend setting headers and footers manually in a pre-designed file for printing. You can use Microsoft Excel as a GUI tool to set headers and footers to save effort and development time. Aspose.Cells can import the file and save the settings.

To add headers and footers at runtime, Aspose.Cells provides special API calls and script commands to format headers and footers.

### Script Commands

Script commands are special commands that allow you to set header and footer formatting.

{{< table style="table-striped" >}}
|Script Commands|Description|
|:----|:----|
|&P|The current page number|
|&G|A picture|
|&N|The total number of pages|
|&D|The current date|
|&T|The current time|
|&A|The worksheet name|
|&F|The file name without its path|
|&"<FontName>"|Represents a font name. For example: &"Arial"|
|&"<FontName>, <FontStyle>"|Represents font name with style. For example: &"Arial,Bold"|
|&<FontSize>|Represents font size. For example: “&14abc”. But, if this command is followed by a plain number to be printed in the header, this should be separated with a space character from the font size. For example: “&14 123”.|
{{< /table >}}

### Set Headers and Footers

The [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class provides two methods, [SetHeader](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/methods/setheader) and [SetFooter](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/methods/setfooter), used to add a header and footer to a worksheet. These methods take only two parameters:

*   **Section** – the section where the header or footer should be placed. There are three sections: left, center and right, represented by 0, 1 and 2 respectively.
*   **Script** – the script to be used for the header or footer. This script contains script commands to format headers or footers.

### Insert an Image into a Header or Footer

The [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class has two additional methods, [SetHeaderPicture](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/methods/setheaderpicture) and [SetFooterPicture](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/methods/setfooterpicture), used to add pictures into the header and footer. These methods take the parameters:

*   **Section** – the header or footer section where the picture will be placed. There are three sections, left, center and right, represented by the values 0, 1 and 2 respectively.
*   **Byte array** – the graphical data (the binary data should be written into the buffer of a byte array).

After executing the code below and opening the file, check the header of the worksheet by:

1.  On the **File** menu, select **Page Setup**. A dialog will be displayed.
2.  Select the **Header/Footer** tab.

