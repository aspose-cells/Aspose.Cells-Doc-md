---
title: رسم مقطع أثناء تصدير إكسل إلى PDF باستخدام C++
linktitle: رسم المنقي أثناء تحويل Excel إلى PDF
type: docs
weight: 60
url: /ar/cpp/draw-slicer-while-rendering-excel-to-pdf/
description: تصدير إكسل إلى PDF مع إعدادات المقطع باستخدام Aspose.Cells مع C++.
---

## **رسم المنقي أثناء تحويل Excel إلى PDF**
 إذا كان لديك ملف إكسل يحتوي على مقطع مطبق عليه وترغب في تصديره إلى PDF مع إعدادات المقطع، فإن Aspose.Cells يدعم ذلك الآن بشكل افتراضي. ببساطة قم بتصدير ملف إكسل مع المقطع إلى PDF، وسيظهر PDF الناتج المقطع المطبق.

الكود العيني

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **الكود المثالي**
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleSlicerChart.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"SampleSlicerChart.pdf";

    // Create workbook from the excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as a PDF file
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved as PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
