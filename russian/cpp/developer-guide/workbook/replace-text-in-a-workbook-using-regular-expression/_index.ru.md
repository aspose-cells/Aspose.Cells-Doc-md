--- 
title: Заменить текст в рабочей книге с использованием регулярных выражений с помощью C++
linktitle: Замена текста в книге с использованием регулярных выражений
type: docs 
weight: 90 
url: /ru/cpp/replace-text-in-a-workbook-using-regular-expression/ 
description: Заменить текст в рабочей книге с использованием регулярных выражений и Aspose.Cells в C++. 
--- 

Aspose.Cells предоставляет функцию для замены текста в рабочей книге с использованием регулярного выражения. Для этого API предоставляет свойство [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) класса [**ReplaceOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/). Установка [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) в значение **true** указывает, что поиск будет осуществляться с помощью регулярного выражения.

Следующий фрагмент кода демонстрирует использование свойства [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) на примере [пример файла Excel](101089318.xlsx). [Выходной файл](101089319.xlsx), созданный этим кодом, прикреплен для ознакомления.

## **Образец кода** 

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
{{< app/cells/assistant language="cpp" >}}
