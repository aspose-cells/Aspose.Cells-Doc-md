---
title: فواصل الأسطر والتفاف النصوص باستخدام C++
description: كيفية تنفيذ التفاف النص وتغليف الكلمات باستخدام مكتبة Aspose.Cells في C++. من خلال استخدام مكتبة Aspose.Cells، يمكنك إدراج النص بسهولة في الخلايا وتعيين طريقة التفاف النص، مثل التفاف الكلمات اليدوي، والتفاف الكلمات، وغيرها. يوضح هذا المستند كيفية تنفيذ هذه الميزات ويقدم رمزًا نموذجيًا لمرجعك.
keywords: Aspose.Cells، تقسيم الأسطر، تفصيل النص، تخطيط النص
type: docs
weight: 60
url: /ar/cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

لضمان قراءة النص في خلية معينة يمكن تطبيق كسرات الأسطر الصريحة وتضمين النص. يحول تضمين النص سطرًا واحدًا إلى عدة أسطر داخل خلية، بينما تضع كسرات الأسطر الصريحة فواصل تمامًا حيث تريدها.

{{% /alert %}}

## **لتضمين النص في خلية**

لتغليف النص في خلية، استخدم الخاصية [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/).

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

    // Create Workbook Object
    Workbook wb;

    // Open first Worksheet in the workbook
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Cells cell = ws.GetCells();

    // Increase the width of the first column
    cell.SetColumnWidth(0, 35);

    // Increase the height of the first row
    cell.SetRowHeight(0, 36);

    // Add text to the first cell
    cell.Get(0, 0).PutValue(u"I am using the latest version of Aspose.Cells to test this functionality");

    // Make the cell's text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    wb.Save(srcDir + u"WrappingText.out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **للاستخدام كسرات الأسطر الصريحة**

يمكنك استخدام ‘\n’ في C++ لإدراج فواصل أسطر صريحة داخل خلية.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create Workbook Object
    Workbook workbook;

    // Open first Worksheet in the workbook
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Aspose::Cells::Cells cell = ws.GetCells();

    // Increase the width of First Column Width
    cell.SetColumnWidth(0, 35);

    // Increase the height of first row
    cell.SetRowHeight(0, 65);

    // Add Text to the First Cell with Explicit Line Breaks
    cell.Get(0, 0).PutValue(u"I am using\nthe latest version of \nAspose.Cells to \ntest this functionality");

    // Make Cell's Text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    U16String outputFilePath = u"WrappingText.out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
