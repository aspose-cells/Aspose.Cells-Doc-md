---
title: Редактирование гиперссылок в рабочем листе с помощью C++
linktitle: Редактирование гиперссылок на листе
type: docs
weight: 330
url: /ru/cpp/editing-hyperlinks-of-worksheet/
description: Узнайте, как редактировать гиперссылки в рабочем листе через API Aspose.Cells for C++.
keywords: Редактировать гиперссылки, Редактировать гиперссылки листа, Редактировать гиперссылку клетки, Получить все гиперссылки листа
---

{{% alert color="primary" %}}

Aspose.Cells позволяет получить доступ ко всем гиперссылкам листа с помощью коллекции [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/). Вы можете получить доступ к каждой гиперссылке из этой коллекции по одной и отредактировать ее свойства.

{{% /alert %}}

Следующий пример кода получает все гиперссылки листа и изменяет их свойство [**GetAddress()**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getaddress/) на сайт Aspose.

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

    // Create workbook from input file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Iterate through all hyperlinks in the worksheet
    for (int32_t i = 0; i < worksheet.GetHyperlinks().GetCount(); i++)
    {
        Hyperlink hl = worksheet.GetHyperlinks().Get(i);
        hl.SetAddress(u"http://www.aspose.com");
    }

    // Save the modified workbook to the output file
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Hyperlinks updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
