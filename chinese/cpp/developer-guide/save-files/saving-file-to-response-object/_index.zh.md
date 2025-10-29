---
title: 使用C++将文件保存到响应对象
linktitle: 将文件保存到响应对象
type: docs
weight: 50
url: /zh/cpp/saving-file-to-response-object/
description: 学习如何使用Aspose.Cells for C++动态保存文件并直接发送给客户端浏览器。
---

{{% alert color="primary" %}}

Aspose.Cells可以操作文件。本文解释了可以将文件保存到响应对象的各种方法。

{{% /alert %}}

## **将文件保存到响应对象**

还可以动态生成文件并直接发送到客户端浏览器。 为此，使用接受以下参数的 [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法的特殊重载版本：

- **HttpResponse** 对象。
- 文件名。
- [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/)，输出文件的 content-disposition 类型。
- [**SaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/saveoptions/)，文件格式类型。

[**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/) 枚举确定发送到浏览器的文件是否提供直接在浏览器中打开或在与 .xls/.xlsx 或其他扩展名相关联的应用程序中打开的选项。

该枚举包含以下预定义的保存类型：

|**类型**|**描述**|
| :- | :- |
|附件|将电子表格发送到浏览器，并作为与.xls/.xlsx或其他扩展名相关联的附件在应用程序中打开|
|内置|将文档发送到浏览器，并提供选项将电子表格保存到磁盘或在浏览器中打开|

### **XLS文件**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Save in Excel2003 XLS format
    U16String outputPath = outDir + u"output.xls";
    XlsSaveOptions saveOptions;
    workbook.Save(outputPath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **XLSX文件**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook;

    // Save in Xlsx format
    OoxmlSaveOptions saveOptions;
    workbook.Save(outputFilePath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **PDF文件**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of output PDF file
    U16String outputPdf = outDir + u"output.pdf";

    // Creating a Workbook object
    Workbook workbook;

    // Save in Pdf format
    PdfSaveOptions saveOptions;
    workbook.Save(outputPdf, saveOptions);

    Aspose::Cells::Cleanup();
}
```

### **注意**

由于未在.NET5和.Netstandard中包含"System.Web.HttpResponse"对象，
因此，在Aspose.Cells .NET5和.Netstandard版本中不存在此函数，您可以参考以下代码将文件保存到流中，然后对流进行操作。

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save workbook to memory stream with explicit FileFormatType
    Vector<uint8_t> data = workbook.SaveToStream();

    std::cout << "File size: " << data.GetLength() << std::endl;

    Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
