--- 
title: Çalışma kitabındaki metni Regular Expression kullanarak C++ ile değiştirin
linktitle: Düzenli İfade Kullanarak Bir Çalışma Kitabındaki Metni Değiştirme
type: docs 
weight: 90 
url: /tr/cpp/replace-text-in-a-workbook-using-regular-expression/ 
description: Aspose.Cells kullanarak C++ ile Çalışma kitabındaki metni Regular Expression kullanarak değiştirin. 
--- 

Aspose.Cells, bir çalışma kitabındaki metni düzenli ifade kullanarak değiştirme özelliği sağlar. Bunun için API, [**ReplaceOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/) sınıfının [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) özelliğini sunar. [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) öğesini **true** olarak ayarlamak, aranacak anahtarın bir düzenli ifade olacağını gösterir.

Aşağıdaki kod parçacığı, [örnek Excel dosyası](101089318.xlsx) kullanılarak [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) özelliğinin kullanımını gösterir. Aşağıdaki kod parçası tarafından oluşturulan [çıktı dosyası](101089319.xlsx) referans olması için eklenmiştir.

## **Örnek Kod** 

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
