---
title: C++ ile Birleşim Aralığı Oluşturma
linktitle: Birleşik Aralık Oluştur
type: docs
weight: 360
url: /tr/cpp/create-union-range/
description: Aspose.Cells kullanarak C++ ile Excel dosyalarında Birleşim Aralığı oluşturun.
---

## **Birleşik Aralık Oluştur**
Aspose.Cells, [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/) metodunu kullanarak Birleşim Aralığı oluşturma imkanı sağlar. [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/) yöntemi, birleşim aralığı oluşturmak için adres ve çalışma sayfası indeksini parametre olarak alır. Bu metod, bir [UnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/unionrange/) nesnesi döner.

Aşağıdaki kod parçası, [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/) metodunu kullanarak bir Birleşim Aralığı oluşturmayı gösterir. Çalıştırılan kodun sonucu olan dosya referans amaçlı eklenmiştir.

- [Çıktı Dosyası](106364952.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Create union range
    UnionRange unionRange = workbook.GetWorksheets().CreateUnionRange(u"sheet1!A1:A10,sheet1!C1:C10", 0);

    // Put value "ABCD" in the range
    unionRange.SetValue(u"ABCD");

    // Save the output workbook
    workbook.Save(u"CreateUnionRange_out.xlsx");

    std::cout << "Union range created and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
