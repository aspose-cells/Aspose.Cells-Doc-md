---  
title: إنشاء كائن نمط باستخدام فئة CellsFactory باستخدام C++  
description: مكتبة Aspose.Cells هي مكتبة C++ للعمل مع ملفات الجدول الإلكتروني وتوفر كائن نمط لتنسيق الخلايا. ستقدم هذه المقالة طريقة إنشاء كائن نمط خلية باستخدام فئة CellsFactory في مكتبة Aspose.Cells ليتمكن المستخدمون من تخصيص مظهر الخلايا حسب الحاجة.  
keywords: مكتبة Aspose.Cells، مكتبة C++، جدول إلكتروني، كائن نمط، نمط خلية، تخصيص  
type: docs  
weight: 70  
url: /ar/cpp/create-style-object-using-cellsfactory-class/  
---  

## **انشاء كائن نمط باستخدام فئة CellsFactory**  
يتم إنشاء كائن نمط [Style](https://reference.aspose.com/cells/cpp/aspose.cells/style) باستخدام فئة [CellsFactory](https://reference.aspose.com/cells/cpp/aspose.cells/cellsfactory) ثم ضبط النمط الافتراضي لمفكرة العمل. يرجى تحميل [ملف الإكسل الناتج](5115153.xlsx) لمعاينة نتائج هذا الكود للمرجع الخاص بك.  

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

    // Create a Style object using CellsFactory class
    CellsFactory cf;
    Style st = cf.CreateStyle();

    // Set the Style fill color to Yellow
    st.SetPattern(BackgroundType::Solid);
    st.SetForegroundColor(Color::Yellow());

    // Create a workbook and set its default style using the created Style object
    Workbook wb;
    wb.SetDefaultStyle(st);

    // Save the workbook
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
