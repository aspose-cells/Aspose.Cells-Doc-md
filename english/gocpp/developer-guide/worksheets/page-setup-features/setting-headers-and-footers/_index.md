---
title: Setting Headers and Footers with Golang via C++
linktitle: Setting Headers and Footers
type: docs
weight: 30
url: /go-cpp/setting-headers-and-footers/
description: This article explains how to programmatically insert an image in the header and footer of Excel worksheets by setting the header and footer with script commands using the Go API or Library.
keywords: insert image in excel header footer c++, set excel header footer script commands c++
---

{{% alert color="primary" %}}

Headers and footers are the lines of text displayed **above** the top margin or **below** the bottom margin, respectively. Headers and footers can also be added to worksheets. They can be used to display useful information such as page number, author name, topic name, or date and time. Headers and footers are managed using the page‑setup settings.

{{% /alert %}}

## **Setting Headers and Footers**

Aspose.Cells allows you to add headers and footers to worksheets at runtime, but we recommend setting headers and footers manually in a pre‑designed file for printing. You can use Microsoft Excel as a GUI tool to set headers and footers to save effort and development time. Aspose.Cells can import the file and preserve the settings.

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
|&&Text|Shows &Text. For example: &&WO will be displayed as &WO|
|&"\<FontName>"|Represents a font name. For example: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Represents font name with style. For example: &"Arial,Bold"|
|&\<FontSize>|Represents font size. For example: "&14abc". However, if this command is followed by a plain number to be printed in the header, the number should be separated from the font size with a space character. For example: "&14 123".|

### **Set Headers and Footers**

The [**PageSetup**](https://reference.aspose.com/cells/go-cpp/pagesetup/) class provides two methods, [**SetHeader**](https://reference.aspose.com/cells/go-cpp/pagesetup/setheader/) and [**SetFooter**](https://reference.aspose.com/cells/go-cpp/pagesetup/setfooter/), used to add a header and footer to a worksheet. These methods take only two parameters:

- **Section** – the section where the header or footer should be placed. There are three sections: left, center and right, represented by 0, 1 and 2 respectively.
- **Script** – the script to be used for the header or footer. This script contains script commands to format headers or footers.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingHeadersAndFooters.go" >}}

### **Insert an Image into a Header or Footer**

The [**PageSetup**](https://reference.aspose.com/cells/go-cpp/pagesetup/) class has two additional methods, [**SetHeaderPicture**](https://reference.aspose.com/cells/go-cpp/pagesetup/setheaderpicture/) and [**SetFooterPicture**](https://reference.aspose.com/cells/go-cpp/pagesetup/setfooterpicture/), used to add pictures into the header and footer. These methods take the following parameters:

- **Section** – the header or footer section where the picture will be placed. There are three sections, left, center and right, represented by the values 0, 1 and 2 respectively.
- **Byte array** – the graphical data (the binary data should be written into the buffer of a byte array).

After executing the code below and opening the file, check the header of the worksheet as follows:

1. On the **File** menu, select **Page Setup**. A dialog will be displayed.  
2. Select the **Header/Footer** tab.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingHeadersAndFooters-1.go" >}}
{{< app/cells/assistant language="go" >}}
