---
title: 使用C++显示和隐藏工作表及标签
linktitle: 显示和隐藏工作表和选项卡
type: docs
weight: 10
url: /zh/cpp/show-and-hide-worksheets-and-tabs/
description: 本文提供了使用C++ API或库以编程方式显示和隐藏Excel工作表的示例。此外，还介绍了如何显示和隐藏Excel工作簿的标签。
---

{{% alert color="primary" %}}

Aspose.Cells 允许用户显示和隐藏工作簿的元素，包括工作表和标签。

{{% /alert %}}

## **显示和隐藏工作表**

Excel文件可以包含一个或多个工作表。每当我们创建一个Excel文件时，都会向其中添加工作表。Excel文件中的每个工作表都是独立的，具有自己的数据和格式设置等。有时，开发人员可能需要将一些工作表隐藏，并使其他工作表对他们的兴趣可见。因此，**Aspose.Cells**允许开发人员控制其Excel文件中工作表的可见性。

Aspose.Cells 提供了一个类[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，代表一个Excel文件。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，可访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了丰富的属性和方法来管理工作表。要控制工作表的可见性，使用[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类的[**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/)属性。[**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/)是布尔值属性，只能存储**true**或**false**。

### **使工作表可见**

将工作表设为可见，设置{3}类的{2}属性为**true**。

### **隐藏工作表**

将工作表隐藏，设置{3}类的{2}属性为**false**。

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the first worksheet of the Excel file
    worksheet.SetIsVisible(false);

    // Save the modified Excel file in default (Excel 2003) format
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Worksheet hidden and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **显示和隐藏标签**

如果您仔细查看Microsoft Excel文件的底部，您会看到许多控件。其中包括:

- 工作表标签。
- 选项卡滚动按钮。

工作表标签代表Excel文件中的工作表。单击任何选项卡以切换到该工作表。工作簿中有更多的工作表，也会有更多的工作表标签。如果Excel文件有大量工作表，您需要按钮来进行导航。因此，Microsoft Excel提供了选项卡滚动按钮来滚动工作表标签。

使用Aspose.Cells，开发人员可以控制Excel文件中工作表标签和选项卡滚动按钮的可见性。

Aspose.Cells 提供了一个类[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，代表一个Excel文件。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类提供了丰富的属性和方法来管理Excel文件。开发者可以使用[**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)类的[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)属性来控制Excel文件中标签的显示。[**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)是布尔值属性，只能存储**true**或**false**。

### **使选项卡可见**

使用{0}类的{2}属性，将标签设为可见（**true**）。

### **隐藏选项卡**

将Excel文件中的标签隐藏，通过设置{0}类的{2}属性为**false**。

下面是一个完整的示例，打开一个Excel文件（book1.xls），隐藏其标签并将修改后的文件保存为output.xls。代码执行后，您将看到工作簿的标签被隐藏了。

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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Hiding the tabs of the Excel file
    settings.SetShowTabs(false);

    // Shows the tabs of the Excel file
    // settings.SetShowTabs(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **控制选项卡栏宽度**

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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Show tabs in the Excel file
    settings.SetShowTabs(true);

    // Adjust the sheet tab bar width
    settings.SetSheetTabBarWidth(800);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
