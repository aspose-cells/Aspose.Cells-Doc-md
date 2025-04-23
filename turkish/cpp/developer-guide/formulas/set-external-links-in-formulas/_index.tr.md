---
title: İşlevlerde Dış Bağlantıları C++ ile Ayarlama
linktitle: Formüllerde Dış Bağlantıları Ayarlama
type: docs
weight: 20
url: /tr/cpp/set-external-links-in-formulas/
description: Aspose.Cells kullanarak ve C++ ile formüllerde harici dosyalara bağlantı eklemeyi öğrenin.
---

{{% alert color="primary" %}} 

Bazı durumlarda, formüllerde dış dosyalara bağlantı eklemek gerekebilir, örneğin, bir hücre veya aralık değerini bunlarla karşılaştırmak için. Aspose.Cells bu özelliği sağlar, bu belge, bunu nasıl kullanacağınızı açıklar.

{{% /alert %}} 

Aşağıdaki örnek kod, formüllerde harici dosyaların nasıl dahil edileceğini gösterir.

```cpp
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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get first Worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get Cells collection
    Cells cells = sheet.GetCells();

    // Set formula with external links
    cells.Get(u"A1").SetFormula(U16String(u"=SUM('[") + srcDir + u"book1.xlsx]Sheet1'!A2, '[" + srcDir + u"book1.xlsx]Sheet1'!A4)");

    // Set formula with external links
    cells.Get(u"A2").SetFormula(U16String(u"='[") + srcDir + u"book1.xlsx]Sheet1'!A8");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully with external links!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
