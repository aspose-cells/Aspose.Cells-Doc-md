--- 
title: Sostituisci testo in un libro di lavoro usando espressioni regolari con C++
linktitle: Sostituire il testo in un libro di lavoro utilizzando le espressioni regolari
type: docs 
weight: 90 
url: /it/cpp/replace-text-in-a-workbook-using-regular-expression/ 
description: Sostituisci testo in un libro di lavoro usando espressioni regolari con Aspose.Cells in C++. 
--- 

 Aspose.Cells fornisce la funzione di sostituire testo in un libro di lavoro usando un'espressione regolare. Per questo, l'API fornisce la proprietà [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) della classe [**ReplaceOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/). Impostare [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) su **true** indica che la chiave cercata sarà un'espressione regolare.

 Il seguente frammento di codice dimostra l'uso della proprietà {0} usando il {2} esempio di file Excel. Il {3} generato dal frammento di codice di seguito è allegato come riferimento.

## **Codice di Esempio** 

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
