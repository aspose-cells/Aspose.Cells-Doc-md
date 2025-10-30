---
title: C++ kullanarak Hücreye Uygulanan Doğrulamayı Alın
linktitle: Hücreye Uygulanan Doğrulamayı Al
type: docs
weight: 200
url: /tr/cpp/get-validation-applied-on-a-cell/
description: Bu makale, C++ ile hücreye doğrulama nasıl uygulanacağını gösterir.
keywords: excelde hücre doğrulaması uygulama, c++ ile excelde hücre doğrulaması yapma, c++ ile excelde doğrulama uygulama, c++ ile excelde hücre doğrulaması, c++ ile excelde hücre doğrulamasını uygula, c++ ile excelde hücreye doğrulama yap, c++ ile excelde hücre doğrulaması, c++ ile excelde hücre doğrulama
---

{{% alert color="primary" %}}

Aspose.Cells'i kullanarak bir hücreye uygulanan doğrulamayı alabilirsiniz. Aspose.Cells bu amaçla [**Cell::GetValidation()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) yöntemini sağlar. Eğer hücreye uygulanan doğrulama yoksa, null değerini döndürür.

Benzer şekilde, [**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/cpp/aspose.cells/validationcollection/getvalidationincell/) yöntemini kullanarak bir hücreye uygulanan doğrulamayı alabilirsiniz. Bu yöntem, satır ve sütun indislerini sağlayarak çalışmaktadır.

{{% /alert %}}

## C++ kodu ile bir hücreye uygulanan doğrulamayı alma

Aşağıdaki kod örneği, hücreye uygulanan doğrulamayı nasıl alacağınızı gösterir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate the workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access its first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Cell C1 has the Decimal Validation applied on it. It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Access the validation applied on this cell
    Validation validation = cell.GetValidation();

    // Read various properties of the validation
    std::cout << "Reading Properties of Validation" << std::endl;
    std::cout << "--------------------------------" << std::endl;
    std::cout << "Type: " << static_cast<int>(validation.GetType()) << std::endl;
    std::cout << "Operator: " << static_cast<int>(validation.GetOperator()) << std::endl;
    std::cout << "Formula1: " << validation.GetFormula1().ToUtf8() << std::endl;
    std::cout << "Formula2: " << validation.GetFormula2().ToUtf8() << std::endl;
    std::cout << "Ignore blank: " << validation.GetIgnoreBlank() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## İlgili Makaleler

- [Veri Doğrulama](/cells/tr/cpp/data-validation/)
{{< app/cells/assistant language="cpp" >}}
