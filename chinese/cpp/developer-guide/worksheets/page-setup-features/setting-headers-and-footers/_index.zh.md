---
title: 用C++设置页眉页脚
linktitle: 设置页眉和页脚
type: docs
weight: 30
url: /zh/cpp/setting-headers-and-footers/
description: 本文介绍如何通过使用C++ API或库中的脚本命令，编程方式在Excel工作表的页眉和页脚中插入图片。
keywords: 在Excel头脚中插入图片，设置头脚脚本命令（C++）
---

{{% alert color="primary" %}}

页眉和页脚是显示在顶部边距下方或底部边距上方的文本行。还可以将页眉和页脚添加到工作表中。页眉和页脚可用于显示有用的信息，如页码、作者姓名、主题名称或日期和时间。通过页面设置设置页眉和页脚。

{{% /alert %}}

## **设置页眉和页脚**

Aspose.Cells允许您在运行时向工作表添加页眉和页脚，但我们建议在预先设计的文件中手动设置页眉和页脚以便打印。您可以使用Microsoft Excel作为GUI工具来设置页眉和页脚以节省工作量和开发时间。Aspose.Cells可以导入文件并保存设置。

要在运行时添加页眉和页脚，Aspose.Cells提供了特殊的API调用和脚本命令来格式化页眉和页脚。

### **脚本命令**

脚本命令是特殊命令，允许您设置页眉和页脚的格式。

|**脚本命令**|**描述**|
| :- | :- |
当前页号||&P|
图片||&G|
总页数||&N|
|&D|当前日期|
|&T|当前时间|
|&A|工作表名称|
|&F|文件名（不含路径）|
|&&文本|显示 &文本。例如：&&WO 将显示为 &WO|
|&"\<FontName>"|表示字体名称。例如：&"Arial"|
|&"\<FontName>, \<FontStyle>"|表示带有样式的字体名称。例如：&"Arial,Bold"|
|&\<FontSize>|代表字体大小。例如：“&14abc”。但如果此命令后跟一个要在页眉中打印的普通数字，则应与字体大小用空格分隔。例如：“&14 123”。

### **设置页眉和页脚**

[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) 类提供两种方法，[**SetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheader/) 和 [**SetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooter/)，用于向工作表添加页眉和页脚。这些方法只有两个参数：

- **Section** – 应放置页眉或页脚的部分。有三个部分：左、中、右，分别由0、1和2表示。
- **Script** – 用于页眉或页脚的脚本。此脚本包含对页眉或页脚进行格式化的脚本命令。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook excel;

    // Get the first worksheet's PageSetup
    PageSetup pageSetup = excel.GetWorksheets().Get(0).GetPageSetup();

    // Set worksheet name at the left section of the header
    pageSetup.SetHeader(0, u"&A");

    // Set current date and time at the central section of the header with custom font
    pageSetup.SetHeader(1, u"&\"Times New Roman,Bold\"&D-&T");

    // Set current file name at the right section of the header with custom font
    pageSetup.SetHeader(2, u"&\"Times New Roman,Bold\"&12&F");

    // Set a string at the left section of the footer with custom font for part of the string
    pageSetup.SetFooter(0, u"Hello World! &\"Courier New\"&14 123");

    // Set the current page number at the central section of the footer
    pageSetup.SetFooter(1, u"&P");

    // Set page count at the right section of the footer
    pageSetup.SetFooter(2, u"&N");

    // Save the workbook
    excel.Save(u"SetHeadersAndFooters_out.xls");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **将图像插入页眉或页脚**

[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) 类还有两个额外的方法，[**SetHeaderPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheaderpicture/) 和 [**SetFooterPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooterpicture/)，用于在页眉和页脚中添加图片。这些方法需要以下参数：

- **Section** – 图片将放置的页眉或页脚部分。有三个部分：左、中、右，分别由值0、1和2表示。
- **字节数组** – 图形数据（二进制数据应写入字节数组的缓冲区）。

执行以下代码并打开文件后，请通过以下方式检查工作表的页眉：

1. 在 **文件** 菜单上，选择 **页面设置**。将显示一个对话框。
1. 选择 **页眉/页脚** 选项卡。

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Creating a Workbook object
    Workbook workbook;

    // Creating a string variable to store the url of the logo/picture
    U16String logo_url = srcDir + u"aspose-logo.jpg";

    // Declaring a FileStream object
    ifstream inFile;

    // Declaring a byte array
    vector<uint8_t> binaryData;

    // Opening the logo/picture in the stream
    inFile.open(logo_url.ToUtf8(), ios::binary);

    if (inFile.is_open())
    {
        // Get the size of the file
        inFile.seekg(0, ios::end);
        size_t fileSize = inFile.tellg();
        inFile.seekg(0, ios::beg);

        // Resize the byte array to the size of the file
        binaryData.resize(fileSize);

        // Read the file into the byte array
        inFile.read(reinterpret_cast<char*>(binaryData.data()), fileSize);

        // Creating a PageSetup object to get the page settings of the first worksheet of the workbook
        PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

        // Convert std::vector to Aspose::Cells::Vector
        Aspose::Cells::Vector<uint8_t> asposeBinaryData(binaryData.data(), static_cast<int32_t>(binaryData.size()));

        // Setting the logo/picture in the central section of the page header
        pageSetup.SetHeaderPicture(1, asposeBinaryData);

        // Setting the script for the logo/picture
        pageSetup.SetHeader(1, u"&G");

        // Setting the Sheet's name in the right section of the page header with the script
        pageSetup.SetHeader(2, u"&A");

        // Saving the workbook
        workbook.Save(outDir + u"InsertImageInHeaderFooter_out.xls");

        // Closing the FileStream object
        inFile.close();
    }
    else
    {
        cerr << "Failed to open the image file." << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
