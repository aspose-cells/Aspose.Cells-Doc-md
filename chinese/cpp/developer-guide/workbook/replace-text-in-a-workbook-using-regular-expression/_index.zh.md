--- 
title: 使用C++的正则表达式替换工作簿内的文本
linktitle: 使用正则表达式在工作簿中替换文本
type: docs 
weight: 90 
url: /zh/cpp/replace-text-in-a-workbook-using-regular-expression/ 
description: 使用Aspose.Cells在C++中通过正则表达式替换工作簿内的文本。 
--- 

Aspose.Cells提供通过正则表达式在工作簿中替换文本的功能。API提供了[**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/)属性的[**ReplaceOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/)类。将[**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/)设置为**true**表示搜索的关键字将是正则表达式。

以下代码片段演示了如何使用[**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/)属性，配合[示例Excel文件](101089318.xlsx)。生成的[输出文件](101089319.xlsx)已附带供参考。

## **示例代码** 

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
