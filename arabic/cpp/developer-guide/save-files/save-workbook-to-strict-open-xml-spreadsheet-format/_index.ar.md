---
title: حفظ ملف العمل بتنسيق Open XML الصارم باستخدام C++
linktitle: حفظ الدفتر إلى تنسيق جدول بيانات إكس الإكس إم الصارم
type: docs
weight: 150
url: /ar/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: تعلم كيفية حفظ ملف العمل بتنسيق Open XML الصارم باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

 يسمح لك Aspose.Cells بحفظ ملف العمل بتنسيق *Open XML الصارم*. لهذا الغرض، يوفر الخاصية [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcompliance/). إذا قمت بضبط قيمتها على [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/)، فسيتم حفظ ملف Excel الناتج بتنسيق *Open XML الصارم*.

## **حفظ الدفتر إلى تنسيق جدول بيانات إكس الإكس إم الصارم**

 ينشئ رمز العينة التالي ملف عمل ويضبط قيمة الخاصية [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcompliance/) إلى [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/) ويحفظه كـ [ملف Excel المخرج](67338272.xlsx). إذا فتحت ملف Excel المخرج في Microsoft Excel وفتحت مربع الحوار Save As...، سترى تنسيقه كـ *Open XML الصارم* كما هو موضح في هذه الصورة.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Specify - Strict Open XML Spreadsheet - Format
    wb.GetSettings().SetCompliance(OoxmlCompliance::Iso29500_2008_Strict);

    // Add message in cell B4 of first worksheet
    Cell b4 = wb.GetWorksheets().Get(0).GetCells().Get(u"B4");
    b4.PutValue(u"This Excel file has Strict Open XML Spreadsheet format.");

    // Save to output Excel file
    wb.Save(u"outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully with Strict Open XML Spreadsheet format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
