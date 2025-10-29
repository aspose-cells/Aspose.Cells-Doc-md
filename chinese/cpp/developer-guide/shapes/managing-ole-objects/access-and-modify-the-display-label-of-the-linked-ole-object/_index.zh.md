---
title: 使用 C++ 访问和修改关联 Ole 对象的显示标签
linktitle: 访问和修改链接的OLE对象的显示标签
type: docs
weight: 100
url: /zh/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: 学习如何使用 Aspose.Cells for C++ 访问和修改 Excel 文件中链接的 Ole 对象的显示标签。
---

## **可能的使用场景**

Microsoft Excel 允许您更改 Ole 对象的显示标签，如以下截图所示。您还可以使用 Aspose.Cells API 结合 [**GetLabel()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getlabel/) 和 [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/) 方法访问或修改 Ole 对象的显示标签。

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **访问和修改链接的OLE对象的显示标签**

请参见以下样本代码，它加载包含Ole对象的 [样本Excel文件](64716810.xlsx)。该代码访问Ole对象并将其标签从Sample APIs更改为Aspose APIs。请参见下面给出的控制台输出，以了解样本代码对样本Excel文件的效果。

## **示例代码**

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file
    U16String inputFilePath = u"sampleAccessAndModifyLabelOfOleObject.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    OleObject oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object
    std::cout << "Ole Object Label - Before: " << oleObject.GetLabel().ToUtf8() << std::endl;

    // Modify the Label of the Ole Object
    oleObject.SetLabel(u"Aspose APIs");

    // Save workbook to memory stream
    auto ms = wb.SaveToStream();

    // Set the workbook reference to null
    wb = Workbook();

    // Load workbook from memory stream
    wb = Workbook(ms);

    // Access first worksheet
    ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object that has been modified earlier
    std::cout << "Ole Object Label - After: " << oleObject.GetLabel().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **控制台输出**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
