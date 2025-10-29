---
title: كيفية استخدام لوحة الألوان مع C++
linktitle: كيفية استخدام لوحة الألوان
type: docs
weight: 80
url: /ar/cpp/excel-color-palette/
description: كود C++ لإضافة ألوان مخصصة إلى اللوحة واستخدام لوحة ألوان إكسل مع واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: إضافة ألوان مخصصة إلى لوحة الألوان، برمجة باستخدام C++ لواجهة برمجة تطبيقات ألوان إكسل، كيفية استخدام لوحة الألوان في المصنف برمجياً، كيفية استخدام لوحة الألوان في إكسل باستخدام C++
---

## **الألوان واللوحة**

اللوحة هي عدد الألوان المتاحة للاستخدام في إنشاء صورة. يتيح استخدام لوحة معيارية في العرض للمستخدم إنشاء مظهر متسق. كل ملف من ملفات Microsoft Excel (97-2003) لديه لوحة تتكون من 56 لون يمكن تطبيقها على الخلايا، الخطوط، الخطوط الشبكية، الكائنات الرسومية، التعبئات والخطوط في الرسم البياني.

مع Aspose.Cells، يمكن للمستخدم استخدام الألوان الموجودة في اللوحة بالإضافة إلى الألوان المخصصة. قبل استخدام لون مخصص، قم بإضافته إلى اللوحة أولاً.

يناقش هذا الموضوع كيفية إضافة ألوان مخصصة إلى اللوحة.

## **إضافة ألوان مخصصة إلى اللوحة**

تدعم Aspose.Cells لوحة الألوان من Microsoft Excel التي تتكون من 56 لون. لاستخدام لون مخصص غير معرف في اللوحة، أضف اللون إلى اللوحة.

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)، التي تمثل ملف Microsoft Excel. تقدم فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) طريقة [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/) التي تأخذ المعلمات التالية لإضافة لون مخصص لتعديل اللوحة:

- لون مخصص، اللون المخصص الذي سيتم إضافته.
- الفهرس، فهرس اللون في اللوحة الذي سيحل محل اللون المخصص. يجب أن يكون بين 0-55.

المثال أدناه يضيف لون مخصص (Orchid) إلى اللوحة قبل تطبيقه على خط النص.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Check if Orchid color is in the palette
    std::cout << "Is Orchid in palette? " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add Orchid color to the palette at index 55
    workbook.ChangePalette(Color::Orchid(), 55);

    // Verify if Orchid is now in the palette
    std::cout << "Is Orchid in palette now? " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add a new worksheet
    int i = workbook.GetWorksheets().Add();

    // Get the reference to the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"Hello Aspose!");

    // Create a new style
    Style styleObject = workbook.CreateStyle();

    // Set the custom color (Orchid) to the font
    styleObject.GetFont().SetColor(workbook.GetColors()[55]);

    // Apply the style to the cell
    cell.SetStyle(styleObject);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

تحتوي اللوحة فقط على 56 لونًا. عندما تقوم بإضافة لون مخصص إلى اللوحة، يتم تغيير اللوحة ويتم تغيير أي عنصر في الملف المنسق باللون السابق. لذا، عند تغيير اللوحة، يرجى أن تكون حذرًا جدًا. علاوة على ذلك، هذه هي القيود في تنسيق ملف XLS (Excel 97 - 2003) فقط حيث لا يوجد مثل هذا القيد لتنسيق ملف XLSX أو لأنساق ملفات Microsoft Excel (2007/2010 أو 2013) المتقدمة.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
