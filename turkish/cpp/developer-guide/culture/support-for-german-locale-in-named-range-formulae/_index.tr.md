---
title: C++ ile Adlandırılmış Aralık Formüllerinde Almanca Bölge Desteği
linktitle: Adlandırılmış Aralık Formüllerinde Alman Locale Desteği
type: docs
weight: 60
url: /tr/cpp/support-for-german-locale-in-named-range-formulae/
description: Aspose.Cells ile C++ kullanarak Almanca bölge ayarlarında adlandırılmış aralık formülleri ile nasıl başa çıkılacağını öğrenin.
---

İngilizce formüller adlandırılmış bölgelere yazılır. Bu Excel dosyası, sistemin Almanca Bölge ayarına göre yapılandırıldığı bir ortamda açılabilir; ancak, İngilizce formül Almanca diline çevrilmelidir. Aşağıdaki örnek, bu özelliği gösterir, ancak Excel'in Almanca kurulu ve sistem bölgesinin de Almanca olması gerekir.

Bu özelliği test etmek için bir örnek dosya aşağıdaki bağlantıdan indirilebilir:

[sampleNamedRangeTest.xlsm](73990165.xlsm)

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

    // Define the name and formula for the named range
    const U16String name(u"HasFormula");
    const U16String value(u"=GET.CELL(48, INDIRECT(\"ZS\",FALSE))");

    // Load the source workbook
    Workbook wbSource(srcDir + u"sampleNamedRangeTest.xlsm");

    // Get the worksheet collection
    WorksheetCollection wsCol = wbSource.GetWorksheets();

    // Add a new named range and get its index
    int32_t nameIndex = wsCol.GetNames().Add(name);

    // Get the named range by index
    Name namedRange = wsCol.GetNames().Get(nameIndex);

    // Set the formula for the named range
    namedRange.SetRefersTo(value);

    // Save the workbook with the new named range
    wbSource.Save(outDir + u"sampleOutputNamedRangeTest.xlsm");

    std::cout << "Named range added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
