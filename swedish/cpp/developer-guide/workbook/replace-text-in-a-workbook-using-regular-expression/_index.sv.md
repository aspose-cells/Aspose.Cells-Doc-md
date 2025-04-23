--- 
title: Byt ut text i en arbetsbok med reguljära uttryck med C++
linktitle: Byt ut text i en arbetsbok med hjälp av reguljärt uttryck
type: docs 
weight: 90 
url: /sv/cpp/replace-text-in-a-workbook-using-regular-expression/ 
description: Byt ut text i en arbetsbok med reguljära uttryck med Aspose.Cells i C++. 
--- 

Aspose.Cells erbjuder funktionen att ersätta text i en arbetsbok med hjälp av ett reguljärt uttryck. För detta tillhandahåller API:t egenskapen [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) av klassen [**ReplaceOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/). Att ställa in [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) till **true** innebär att den sökta nyckeln är ett reguljärt uttryck.

Följande kodexempel visar användningen av [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/)-egenskapen med hjälp av [provfilen](101089318.xlsx). Den genererade [utdatafilen](101089319.xlsx) från kodexemplet bifogas för referens.

## **Exempelkod** 

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
