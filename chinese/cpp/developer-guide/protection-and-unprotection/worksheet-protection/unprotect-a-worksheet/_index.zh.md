---
title: 使用 C++ 取消保护工作表
linktitle: 取消保护工作表
type: docs
weight: 20
url: /zh/cpp/unprotect-a-worksheet/
description: 了解如何使用 Aspose.Cells for C++ 取消保护工作表。
---

{{% alert color="primary" %}}

 如果开发人员需要在运行时移除受保护的工作表的保护，以便对文件进行一些更改，可以轻松地使用 Aspose.Cells 实现。

{{% /alert %}}

## **取消保护工作表**

### **使用Microsoft Excel**

要取消工作表的保护：

 在**工具**菜单中，选择 **保护** 然后选择 **取消工作表保护**。除非工作表设置了密码，否则保护将被移除。如果设置了密码，将出现对话框提示输入密码。输入密码后，工作表将被取消保护。

### **使用Aspose.Cells取消简单保护的工作表**

 可以通过调用 [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类的 [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) 方法来取消保护工作表。未设置密码的简单受保护工作表可以通过调用不带参数的 [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) 方法来取消保护。

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create a Workbook object
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unprotect the worksheet without a password
    worksheet.Unprotect();

    // Save the Workbook in Excel97-2003 format
    workbook.Save(outputFilePath, SaveFormat::Excel97To2003);

    std::cout << "Worksheet unprotected and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **使用Aspose.Cells取消受密码保护的工作表**

 密码保护的工作表是用密码保护的工作表。可以通过调用 [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) 方法的重载版本（带密码参数）来取消保护此类工作表。

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unprotecting the worksheet with a password
    worksheet.Unprotect(u"");

    // Save Workbook
    workbook.Save(outputFilePath);

    std::cout << "Worksheet unprotected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
