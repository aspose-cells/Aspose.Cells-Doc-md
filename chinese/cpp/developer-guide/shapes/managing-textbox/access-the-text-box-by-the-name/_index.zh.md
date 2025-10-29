---
title: 使用C++按名称访问文本框
linktitle: 按名称访问文本框
type: docs
weight: 230
url: /zh/cpp/access-the-text-box-by-the-name/
description: 了解如何使用Aspose.Cells for C++按名称访问文本框。
---

## 按名称访问文本框

早先，可以通过索引访问[**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/)集合中的文本框，但现在也可以通过名称访问此集合中的文本框。如果你已知其名称，这是一种方便快捷的访问方式。

以下示例代码首先创建一个文本框并赋予其一些文本和名称，然后通过名称访问该文本框并打印其文本。

### 使用C++按名称访问文本框的代码

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    int idx = sheet.GetTextBoxes().Add(10, 10, 10, 10);

    // Access newly created TextBox using its index & name it
    TextBox tb1 = sheet.GetTextBoxes().Get(idx);
    tb1.SetName(u"MyTextBox");

    // Set text for the TextBox
    tb1.SetText(u"This is MyTextBox");

    // Access the same TextBox via its name
    TextBox tb2 = sheet.GetTextBoxes().Get(u"MyTextBox");

    // Display the text of the TextBox accessed via name
    std::cout << tb2.GetText().ToUtf8() << std::endl;

    std::cout << "Press any key to continue..." << std::endl;
    std::cin.get();

    Aspose::Cells::Cleanup();
}
```

### 样本代码生成的控制台输出

这是上面示例代码的控制台输出。

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
