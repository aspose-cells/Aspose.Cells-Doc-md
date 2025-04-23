---
title: C++ ile Sıralı Olmayan Aralıkları Uygulama
linktitle: Sıralı Olmayan Menzilleri Uygulama
type: docs
weight: 700
url: /tr/cpp/implementing-non-sequential-ranges/
description: Aspose.Cells kullanarak, ardışık olmayan hücrelerle adlandırılmış aralıklar nasıl oluşturulur öğrenin.
---

{{% alert color="primary" %}} 

Normalde, adlandırılmış aralıklar hücrelerin ardışık ve bitişik olduğu dikdörtgen şeklindedir. Ancak bazen, bitişik olmayan hücrelerin bulunduğu sırasız bir hücre aralığını kullanmanız gerekebilir. Aspose.Cells, bitişik olmayan hücrelerle adlandırılmış bir aralık oluşturmaya olanak tanır.

{{% /alert %}} 

Aşağıdaki kod örneği, Aspose.Cells for C++ kullanarak ardışık olmayan adlandırılmış bir aralık nasıl oluşturulacağını gösterir.

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

    // Create a new workbook
    Workbook workbook;

    // Adding a Name for non sequenced range
    int index = workbook.GetWorksheets().GetNames().Add(u"NonSequencedRange");

    // Get the added name
    Name name = workbook.GetWorksheets().GetNames().Get(index);

    // Creating a non sequence range of cells
    name.SetRefersTo(u"=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6");

    // Save the workbook
    workbook.Save(outDir + u"Output.out.xlsx");

    std::cout << "Workbook saved successfully with non-sequenced range!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
