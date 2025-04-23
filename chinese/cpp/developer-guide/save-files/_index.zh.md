---
title: 用C++保存文件的不同方法
linktitle: 保存文件
type: docs
weight: 40
url: /zh/cpp/different-ways-to-save-files/
description: Aspose.Cells for C++可以将文件保存为不同格式。保存为PDF。保存为HTML。保存为DOCX。保存为PPTX。保存为JSON。保存为MHTML。
keywords: Aspose.Cells使用C++将Excel保存为PDF、HTML、JSON、CSV、TXT、XML、DOCX、PPTX、MHT、MHTML等格式，或将工作簿保存或转换为PDF、HTML、JSON、TXT、SQL。
---

{{% alert color="primary" %}}

Aspose.Cells 可以创建和保存文件。本文介绍了可保存文件的各种方式。

{{% /alert %}}

## **不同的文件保存方式**

Aspose.Cells提供了[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，代表Microsoft Excel文件，并提供必要的属性和方法来处理Excel文件。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类提供了用于保存Excel文件的[**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法。[**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法有许多重载，用于以不同的方式保存文件。

保存文件的文件格式由[**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)枚举决定

|**文件格式类型**|**描述**|
| :- | :- |
|CSV|表示 CSV 文件|
|Excel97To2003|表示Excel 97-2003文件
|Xlsx|表示Excel 2007 XLSX文件|
|Xlsm|表示Excel 2007 XLSM文件|
|Xltx|表示Excel 2007模板XLTX文件|
|Xltm|表示Excel 2007启用宏的XLTM文件|
|Xlsb|表示Excel 2007二进制XLSB文件|
|SpreadsheetML|表示一种Spreadsheet XML文件|
|TSV|表示制表符分隔数值文件|
|TabDelimited|代表分隔符文本文件|
|ODS|表示 ODS 文件|
|Html|表示HTML文件|
|MHtml|表示一个MHTML文件|
|Pdf|表示一个PDF文件|
|XPS|表示一个XPS文档|
|TIFF|表示Tagged Image File Format (TIFF)|

## **如何将文件保存为不同的格式**

要将文件保存到存储位置，请在调用[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)对象的[**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法时指定文件名（包括存储路径）和所需的文件格式（从[**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)枚举中）。

```cpp
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

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xls";

    // Load your source workbook
    Workbook workbook(filePath);

    // Save in Excel 97 to 2003 format
    workbook.Save(outDir + u".output.xls");
    // OR
    XlsSaveOptions xlsSaveOptions;
    workbook.Save(outDir + u".output.xls", xlsSaveOptions);

    // Save in Excel2007 xlsx format
    workbook.Save(outDir + u".output.xlsx", SaveFormat::Xlsx);

    // Save in Excel2007 xlsb format
    workbook.Save(outDir + u".output.xlsb", SaveFormat::Xlsb);

    // Save in ODS format
    workbook.Save(outDir + u".output.ods", SaveFormat::Ods);

    // Save in Pdf format
    workbook.Save(outDir + u".output.pdf", SaveFormat::Pdf);

    // Save in Html format
    workbook.Save(outDir + u".output.html", SaveFormat::Html);

    // Save in SpreadsheetML format
    workbook.Save(outDir + u".output.xml", SaveFormat::SpreadsheetML);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **如何将工作簿保存为PDF**
便携式文档格式（PDF）是Adobe于1990年代创建的一种文档类型。该文件格式的目的是引入一种标准，以在与应用软件、硬件和操作系统无关的格式中表示文档和其他参考材料。PDF文件格式具有完整的能力，可以包含文本、图像、超链接、表单字段、富媒体、数字签名、附件、元数据、地理空间特征和3D对象等信息，这些信息可以成为源文档的一部分。

以下代码显示了如何使用Aspose.Cells将工作簿保存为PDF文件：
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the Workbook object
    Workbook workbook;

    // Set value to Cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"Hello World!");

    // Save the workbook to PDF
    workbook.Save(u"pdf1.pdf");

    // Save as Pdf format compatible with PDFA-1a
    PdfSaveOptions saveOptions;
    saveOptions.SetCompliance(PdfCompliance::PdfA1a);

    workbook.Save(u"pdfa1a.pdf", saveOptions);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **如何将工作簿保存为文本或CSV格式**

有时，您希望将包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如TXT、TabDelim、CSV等），默认情况下，Microsoft Excel和Aspose.Cells都仅保存活动工作表的内容。

以下代码示例说明如何将整个工作簿保存为文本格式。加载源工作簿，可以是任何Microsoft Excel或OpenOffice电子表格文件（例如XLS、XLSX、XLSM、XLSB、ODS等），并且可以具有任意数量的工作表。

执行代码后，将会将工作簿中所有工作表的数据转换为TXT格式。

你可以修改相同的示例将文件保存为CSV格式。默认情况下，[**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) 是逗号，因此在保存为CSV格式时无需指定分隔符。请注意：如果您使用的是评估版，即使将 [**TxtSaveOptions.GetExportAllSheets()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getexportallsheets/) 属性设置为 true，程序仍将只导出一个工作表。

```cpp
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output text file
    U16String outputFilePath = outDir + u"out.txt";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook data saved to text file successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **如何使用自定义分隔符将文件保存为文本文件**

文本文件包含无格式的电子表格数据。该文件是一种纯文本文件，可以在其数据之间具有一些自定义分隔符。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';');

    // Save the file with the options
    wb.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **如何将文件保存到流中**

要将文件保存到流，请创建*MemoryStream*或*FileStream*对象，并通过调用[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)对象的[**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法将文件保存到该流对象。在调用[**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法时，使用[**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)枚举指定所需的文件格式。

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

## **如何将Excel文件保存为Html和Mht文件**
Aspose.Cells可以简单地保存一个Excel文件、JSON、CSV或其他可以被Aspose.Cells加载的文件为.html和.mht文件。
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"Book1.xlsx");
    Workbook workbook(inputFilePath);

    // Save file to MHTML format
    U16String outputFilePath(u"out.mht");
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully to MHTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **如何将Excel文件保存为OpenOffice（ODS，SXC，FODS，OTS）**
我们可以将文件保存为开放办公格式：ODS、SXC、FODS、OTS等。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file
    workbook.Save(u"Out.ods");

    // Save as sxc file
    workbook.Save(u"Out.sxc");

    // Save as fods file
    workbook.Save(u"Out.fods");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **如何将Excel文件保存为JSON或XML**

JSON（JavaScript对象表示）是一种用于存储和传输数据的开放标准文件格式，它使用人类可读的文本。JSON文件存储为.json扩展名。JSON需要更少的格式化，是XML的一个很好的替代品。JSON源自JavaScript，但是是一种与语言无关的数据格式。许多现代编程语言都支持JSON的生成和解析。application/json是用于JSON的媒体类型。

Aspose.Cells支持将文件保存为JSON或XML。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output json file
    U16String outputFilePath = outDir + u"book1.json";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **高级主题**
- [调整工作簿压缩级别](/cells/zh/cpp/adjust-workbook-compression-level/)
- [将工作簿保存为严格的 Open XML 电子表格格式](/cells/zh/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [将文件保存到响应对象](/cells/zh/cpp/saving-file-to-response-object/)
