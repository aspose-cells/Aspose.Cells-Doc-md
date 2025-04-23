--- 
title: Remplacer du texte dans un classeur en utilisant Expression Régulière avec C++
linktitle: Remplacer du texte dans un classeur en utilisant une expression régulière
type: docs 
weight: 90 
url: /fr/cpp/replace-text-in-a-workbook-using-regular-expression/ 
description: Remplacer du texte dans un classeur en utilisant Expression Régulière avec Aspose.Cells en C++. 
--- 

Aspose.Cells offre la fonctionnalité de remplacer du texte dans un classeur en utilisant une expression régulière. Pour cela, l'API fournit la propriété [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) de la classe [**ReplaceOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/). La mise en place de [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) à **true** indique que la clé recherchée sera une expression régulière.

Le code ci-dessous démontre l'utilisation de la propriété [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) en utilisant le [fichier Excel d'exemple](101089318.xlsx). Le [fichier de sortie](101089319.xlsx) généré par ce code est joint pour référence.

## **Code d'exemple** 

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
