---
title: تحويل دفتر عمل Excel إلى Ods و Sxc و Fods (OpenOffice / LibreOffice calc) باستخدام C++
linktitle: Ods
type: docs
weight: 20
url: /ar/cpp/convert-excel-to-ods/
description: كيفية تحويل Excel إلى Ods (OpenOffice / LibreOffice Calc) أو تحويل Ods (OpenOffice / LibreOffice Calc) إلى Excel باستخدام Aspose.Cells مع C++.
---

## **حول OpenDocument**
[تنسيق OpenDocument (ODF)](https://en.wikipedia.org/wiki/OpenDocument) هو تنسيق ملف مجاني ومفتوح للوثائق المكتبية الإلكترونية الذي طوّره الأصل لـ OpenOffice suite. تنسيق الجدول الخلية OpenDocument (ODS) هو تنسيق الملفات لوثائق Excel. حاليًا يُعتبر OpenDocument معيارًا لـ OASIS و ISO.

## **تحويل Ods (OpenOffice / LibreOffice calc) إلى Excel**
يدعم Aspose.Cells تحميل ملفات Ods و Sxc و Fods المدعومة من قبل OpenOffice / LibreOffice Calc، وتحويل [Ods](book1.ods) و [Sxc](book1.sxc) و [Fods](book1.fods) إلى ملفات Excel.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source ods file
    U16String odsFilePath(u"book1.ods");
    std::shared_ptr<Workbook> workbook = std::make_shared<Workbook>(odsFilePath);

    // Save as xlsx file
    U16String xlsxOutputPath(u"ods_out.xlsx");
    workbook->Save(xlsxOutputPath);

    // Load your source sxc file
    U16String sxcFilePath(u"book1.sxc");
    workbook = std::make_shared<Workbook>(sxcFilePath);

    // Save as xls file
    U16String xlsOutputPath(u"sxc_out.xls");
    workbook->Save(xlsOutputPath);

    // Load your source fods file
    U16String fodsFilePath(u"book1.fods");
    workbook = std::make_shared<Workbook>(fodsFilePath);

    // Save as xlsb file
    U16String xlsbOutputPath(u"fods_out.xlsb");
    workbook->Save(xlsbOutputPath);

    std::cout << "Files converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تحويل Excel إلى Ods (OpenOffice / LibreOffice Calc)**
يدعم Aspose.Cells تحويل ملفات Excel إلى ملفات Ods و Sxc و Fods. يوضح المثال البرمجي أدناه كيفية تحويل [القالب](book1.xlsx) إلى ملفات Ods و Sxc و Fods.

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

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [حفظ ملف ODS بمواصفات ODF 1.1 و 1.2](/cells/ar/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [العمل مع الخلفية في ملفات ODS](/cells/ar/cpp/working-with-background-in-ods-files/)
{{< app/cells/assistant language="cpp" >}}
