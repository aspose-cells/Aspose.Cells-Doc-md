---
title: 将日期转换为日本日期（C++）
linktitle: 将日期转换为日本日期
type: docs
weight: 350
url: /zh/cpp/convert-dates-to-japanese-dates/
description: 学习如何使用 Aspose.Cells for C++ 将公历日期转换为日本日期。
---

{{% alert color="primary" %}}

在日本日历中，新的时代随着新皇帝的即位而开始。2019年5月1日，一位新皇帝即位，平成时代结束，令和时代开始。

{{% /alert %}}

Aspose.Cells 提供一种将公历日期转换为日本日期的方法。在此转换过程中，也考虑了时代的变化。下面的代码片段将包含公历日期的[源Excel](90112015.xlsx)文件转换为带有日本日期的[输出PDF](90112016.pdf)，如下图所示。

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)

```c++
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

    // Create load options for XLSX format
    LoadOptions options(LoadFormat::Xlsx);

    // Set culture info to Japanese
    options.SetLanguageCode(CountryCode::Japan);

    // Load the workbook with Japanese dates
    Workbook workbook(srcDir + u"JapaneseDates.xlsx", options);

    // Save the workbook as PDF
    workbook.Save(outDir + u"JapaneseDates.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF with Japanese dates!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
