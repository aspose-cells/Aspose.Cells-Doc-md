---
title: Open Different Microsoft Excel Versions Files with C++
linktitle: Open Different Microsoft Excel Versions Files
type: docs
weight: 20
url: /cpp/opening-different-microsoft-excel-versions-files/
description: This article explains how to open different Excel versions files using Aspose.Cells for C++ API.
keywords: C++ Open Different Microsoft Excel file, How do I open Encrypted Excel Files.
---

{{% alert color="primary" %}}

Aspose.Cells can open a range of different Microsoft Excel Versions Files, such as Microsoft Excel 95/97 - 2003, SpreadsheetML, Opening Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 XLSX or Encrypted Excel Files.

{{% /alert %}}

## **How to Open Files of Different Microsoft Excel Versions**

An application often has to be able to open Microsoft Excel files created in different versions, for example, Microsoft Excel 95,97, or Microsoft Excel 2007/2010/2013/2016/2019 and Office 365. You might need to load a file in any one of several formats, including XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited or TSV, CSV, ODS and so on. Use the constructor, or specify the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class' [**FileFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getfileformat/) type attribute that specifies the format using the [**FileFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/) enumeration.

The [**FileFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/) enumeration contains many pre-defined file formats some of which are given below.

|**File Format Types**|**Description**|
| :- | :- |
|Csv|Represents a CSV file|
|Excel97To2003|Represents an Excel 97 - 2003 file|
|Xlsx|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSX file|
|Xlsm|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSM file|
|Xltx|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 template XLTX file|
|Xltm|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 macro-enabled XLTM file|
|Xlsb|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 binary XLSB file|
|SpreadsheetML|Represents a SpreadsheetML file|
|Tsv|Represents a Tab-separated values file|
|TabDelimited|Represents a Tab Delimited text file|
|Ods|Represents an ODS file|
|Html|Represents an HTML file|
|Mhtml|Represents an MHTML file|

### **Open Microsoft Excel 95/5.0 Files**

To open a Microsoft Excel 95/5.0 file, use [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) and set the related attribute for the [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) class for the template file to be loaded. A sample file for testing this feature can be downloaded from the following link:

[Excel95 File](Excel95.xls)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Excel95_5.0.xls";

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions1(LoadFormat::Excel97To2003);

    // Create a Workbook object and open the file from the stream
    Workbook wbExcel95(inputFilePath, loadOptions1);

    std::cout << "Microsoft Excel 95/5.0 workbook opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Open Microsoft Excel 97 - 2003 Files**

To open a Microsoft Excel 97 - 2003 file, use [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) and set the related attribute for the [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) class for the template file to be loaded.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book_Excel97_2003.xls";

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions1(LoadFormat::Excel97To2003);

    // Create a Workbook object and open the file from the stream
    Workbook wbExcel97(inputFilePath, loadOptions1);

    std::cout << "Microsoft Excel 97 - 2003 workbook opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Open Microsoft Excel 2007/2010/2013/2016/2019 and Office 365  XLSX Files**

To open a Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 format, that is, XLSX or XLSB, specify the file path. You can also use [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) and set the related attribute/options of the [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) class for the template file to be loaded.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions2(LoadFormat::Xlsx);

    // Create a Workbook object and open the file from its path
    Workbook wbExcel2007(srcDir + u"Book_Excel2007.xlsx", loadOptions2);

    std::cout << "Microsoft Excel 2007 - Office365 workbook opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Open Encrypted Excel Files**

It's possible to create encrypted Excel files using Microsoft Excel. To open an encrypted file, use the [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) and set its attributes and options (for example, give a password) for the template file to be loaded.
A sample file for testing this feature can be downloaded from the following link:

[Encrypted Excel](EncryptedExcel.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate LoadOptions
    LoadOptions loadOptions6;

    // Specify the password
    loadOptions6.SetPassword(u"1234");

    // Create a Workbook object and open the file from its path
    Workbook wbEncrypted(srcDir + u"encryptedBook.xls", loadOptions6);

    std::cout << "Encrypted excel file opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Aspose.Cells also supports opening password-protected Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 files.