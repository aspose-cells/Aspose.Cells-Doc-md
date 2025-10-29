---
title: الحصول على التحقق المطبق على خلية باستخدام C++
linktitle: الحصول على التحقق المطبق على خلية ما
type: docs
weight: 200
url: /ar/cpp/get-validation-applied-on-a-cell/
description: توضح هذه المقالة كيفية تطبيق التحقق على خلية باستخدام C++.
keywords: تطبيق التحقق على الخلية في إكسل باستخدام C++، تطبيق التحقق على خلية في إكسل باستخدام C++، تطبيق التحقق في إكسل باستخدام C++، التحقق من صحة الخلايا في إكسل باستخدام C++، تطبيق التحقق على خلية باستخدام C++ في إكسل، تطبيق التحقق على خلية في إكسل باستخدام C++، التحقق من صحة الخلية في إكسل باستخدام C++، التحقق من صحة الخلية في إكسل باستخدام C++
---

{{% alert color="primary" %}}

يمكنك استخدام Aspose.Cells للحصول على التحقق المطبق على خلية. توفر Aspose.Cells الأسلوب [**Cell::GetValidation()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) لهذا الغرض. إذا لم يتم تطبيق التحقق على الخلية، يعيد قيمة فارغة.

بالمثل، يمكنك استخدام الأسلوب [**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/cpp/aspose.cells/validationcollection/getvalidationincell/) للحصول على التحقق المطبق على خلية عن طريق توفير مؤشرات الصف والعمود الخاصة بها.

{{% /alert %}}

## رمز C++ للحصول على التحقق المطبق على خلية

يعرض لك رمز العينة التالي كيفية الحصول على التحقق المطبق على خلية.

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

## مقالات ذات صلة

- [التحقق من البيانات](/cells/ar/cpp/data-validation/)
{{< app/cells/assistant language="cpp" >}}
