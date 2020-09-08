---
title: Setting Headers and Footers
type: docs
weight: 30
url: /net/setting-headers-and-footers/
---

{{% alert color="primary" %}}

Headers and footers are the lines of text displayed below the top margin or above the bottom margin respectively. It's possible to add headers and footers to the worksheets also. Headers and footers can be used to display useful information like page number, author name, topic name, or date and time. Headers and footers are managed using the page setup settings.

{{% /alert %}}

## **Setting Headers and Footers**

Aspose.Cells allows you to add headers and footers to worksheets at runtime but we recommend setting headers and footers manually in a pre-designed file for printing. You can use Microsoft Excel as a GUI tool to set headers and footers to save effort and development time. Aspose.Cells can import the file and save the settings.

To add headers and footers at runtime, Aspose.Cells provides special API calls and script commands to format headers and footers.

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

### **Set Headers and Footers**

The [**PageSetup**](https://apireference.aspose.com/cells/net/aspose.cells/pagesetup) class provides two methods, [**SetHeader**](https://apireference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader) and [**SetFooter**](https://apireference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter), used to add a header and footer to a worksheet. These methods take only two parameters:

- **Section** – the section where the header or footer should be placed. There are three sections: left, center and right, represented by 0, 1 and 2 respectively.
- **Script** – the script to be used for the header or footer. This script contains script commands to format headers or footers.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

### **Insert an Image into a Header or Footer**

The [**PageSetup**](https://apireference.aspose.com/cells/net/aspose.cells/pagesetup) class has two additional methods, [**SetHeaderPicture**](https://apireference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture) and [**SetFooterPicture**](https://apireference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture), used to add pictures into the header and footer. These methods take the parameters:

- **Section** – the header or footer section where the picture will be placed. There are three sections, left, center and right, represented by the values 0, 1 and 2 respectively.
- **Byte array** – the graphical data (the binary data should be written into the buffer of a byte array).

After executing the code below and opening the file, check the header of the worksheet by:

1. On the **File** menu, select **Page Setup**. A dialog will be displayed.
1. Select the **Header/Footer** tab.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
