---
title: تطبيق تأثيرات فوق السطر وتحت السطر على الخطوط باستخدام C++
linktitle: تطبيق تأثيرات فوق السطر وتحت السطر على الخطوط
type: docs
weight: 80
url: /ar/cpp/apply-superscript-and-subscript-effects-on-fonts/
description: كود C++ لتطبيق تأثير السطور فوق وتحت على النص في Excel باستخدام API Aspose.Cells for C++.
keywords: Excel فوق السطر، Excel تحت السطر، Excel فوق وتحت السطر، إدراج تحت وتحت السطر في Excel، إضافة تحت وتحت السطر في Excel، إضافة فوق وتحت السطر في Excel، إضافة فوق وتحت السطر في Excel، إضافة تحت وتحت السطر في Excel
---

{{% alert color="primary" %}}

توفر Aspose.Cells الوظيفة لتطبيق تأثيرات فوق السطر (نص فوق الخط الأساسي) وتحت السطر (نص تحت الخط الأساسي) على النص.

{{% /alert %}}

## **العمل مع تأثير فوق السطر وتحت السطر**

تطبيق تأثير الحرف الفوقي عن طريق ضبط [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) خاصية الكائن [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) إلى **صحيح**. لتطبيق التحتي، قم بتعيين خاصية [**IsSubscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) للكائن [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) إلى **صحيح**.

تظهر أمثلة الشيفرة التالية كيفية تطبيق حالة فوقية وتحتية على النص.

### كود C++ لتطبيق تأثير السطر العلوى على النص

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Hello");

    // Setting the font Superscript
    Style style = cell.GetStyle();
    style.GetFont().SetIsSuperscript(true);
    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"Superscript_out.xls", SaveFormat::Auto);

    std::cout << "Excel file saved successfully with superscript text!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### كود C++ لتطبيق تأثير السطر السفلي على النص

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello");

    // Set the font Subscript
    Style style = cell.GetStyle();
    style.GetFont().SetIsSubscript(true);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"Subscript_out.xls", SaveFormat::Auto);

    std::cout << "File saved successfully with subscript text!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
