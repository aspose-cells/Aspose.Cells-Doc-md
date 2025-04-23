--- 
title: استبدال النص داخل دفتر العمل باستخدام التعبيرات العادية باستخدام C++
linktitle: استبدال النص في دفتر العمل باستخدام التعبير العادي
type: docs 
weight: 90 
url: /ar/cpp/replace-text-in-a-workbook-using-regular-expression/ 
description: استبدال النص داخل دفتر العمل باستخدام التعبيرات العادية باستخدام Aspose.Cells في C++. 
--- 

توفر Aspose.Cells ميزة استبدال النص داخل دفتر العمل باستخدام التعبيرات العادية. لهذا، توفر واجهة برمجة التطبيقات الخاصية [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) من فئة [**ReplaceOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/). تعيين [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) إلى **true** يدل على أن المفتاح الذي سيتم البحث عنه سيكون تعبيرًا عاديًا.

يوضح مقتطف الكود التالي استخدام الخاصية [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) باستخدام ملف Excel النموذجي ([ملف Excel sample](101089318.xlsx)). المخرجات ([ملف الإخراج](101089319.xlsx)) التي تم إنشاؤها بواسطة المقتطف مرفقة للمرجعية.

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
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Create workbook from the input file
    Workbook workbook(sourceDir + u"SampleRegexReplace.xlsx");

    // Create replace options
    ReplaceOptions replace;
    replace.SetCaseSensitive(false);
    replace.SetMatchEntireCellContents(false);
    // Set to true to indicate that the searched key is regex
    replace.SetRegexKey(true);

    // Perform the regex replace operation
    workbook.Replace(u"\\bKIM\\b", u"^^^TIM^^^", replace);

    // Save the modified workbook
    workbook.Save(outputDir + u"RegexReplace_out.xlsx");

    std::cout << "Regex replace operation completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
