--- 
title: Text in einer Arbeitsmappe mit regulärem Ausdruck in C++ ersetzen
linktitle: Ersetzen von Text in einer Arbeitsmappe mittels regulären Ausdrücken
type: docs 
weight: 90 
url: /de/cpp/replace-text-in-a-workbook-using-regular-expression/ 
description: Text in einer Arbeitsmappe mit regulärem Ausdruck mit Aspose.Cells in C++ ersetzen. 
--- 

Aspose.Cells bietet die Funktion, Text in einer Arbeitsmappe mithilfe eines regulären Ausdrucks zu ersetzen. Dafür stellt die API die [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/)-Eigenschaft der [**ReplaceOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/)-Klasse bereit. Das Setzen von [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) auf **true** zeigt an, dass der gesuchte Schlüssel ein regulärer Ausdruck ist.

Das folgende Codebeispiel demonstriert die Verwendung der [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/)-Eigenschaft anhand der [Beispieldatei](101089318.xlsx). Die [Ausgabedatei](101089319.xlsx), die durch das folgende Codebeispiel generiert wurde, ist zur Referenz beigefügt.

## **Beispielcode** 

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
