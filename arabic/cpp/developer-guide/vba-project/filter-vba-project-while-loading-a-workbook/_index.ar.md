---
title: تصفية مشروع VBA عند تحميل مصنف باستخدام C++
linktitle: تصفية مشروع VBA أثناء تحميل جدول عمل
type: docs
weight: 140
url: /ar/cpp/filter-vba-project-while-loading-a-workbook/
description: تعلم كيفية تصفية مشاريع VBA عند تحميل مصنف إكسل باستخدام Aspose.Cells و C++.
---

## **تصفية مشروع VBA عند تحميل مصنف إكسل باستخدام C++**

 تحتوي بعض ملفات .xlsm/.xslb على كمية هائلة من الماكروز (أو ماكروز طويلة جدًا). ستقوم Aspose.Cells بتحميل هذه البيانات (البيانات الوصفية) بشكل غير مشروط عند فتح هذه المصنفات. قد تحتاج إلى السيطرة على ذلك من خلال [**LoadDataFilterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions) عندما تحتاج فقط إلى استخراج أسماء الأوراق لمجموعة كبيرة من المصنفات، وبالتالي تتجاوز المحتوى غير المطلوب. يتم توفير هذا الفلتر من خلال إدخال خيار جديد، [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions).

## **الكود المثالي**

يحمل الرمز العيني التالي عملاق العمل حتى يتم تصفية VBA فقط. يمكن تنزيل ملف عينة لاختبار هذه الميزة من الرابط التالي:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Set the load options, we do not want to load VBA
    LoadOptions loadOptions(LoadFormat::Auto);
    LoadFilter loadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::VBA);
    loadOptions.SetLoadFilter(&loadFilter);

    // Create workbook object from sample excel file using load options
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleMacroEnabledWorkbook.xlsm";
    Workbook book(inputFilePath, loadOptions);

    // Save the output in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    U16String outputFilePath = outputDir + u"OutputSampleMacroEnabledWorkbook.xlsm";
    book.Save(outputFilePath, SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
