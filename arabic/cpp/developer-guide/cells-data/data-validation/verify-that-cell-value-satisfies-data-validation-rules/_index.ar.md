---
title: التحقق من أن قيمة الخلية تفي بقواعد التحقق من البيانات باستخدام C++
linktitle: التحقق من أن قيمة الخلية تفي بقواعد التحقق من البيانات
type: docs
weight: 210
url: /ar/cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: تعلم كيفية التحقق من أن قيمة الخلية تفي بقواعد التحقق من البيانات من خلال واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: الحصول على قيمة التحقق للخلية، الحصول على قيمة التحقق للخلية، التأكد مما إذا كانت القيمة تلبي قواعد التحقق من البيانات المطبقة على الخلية
---

{{% alert color="primary" %}} 

يسمح Microsoft Excel للمستخدمين بإضافة قواعد التحقق من البيانات إلى الخلايا. على سبيل المثال، تحدد التحقق العشري أن يتم إدخال أرقام بين 10 و20 فقط. إذا أدخل المستخدم رقمًا مختلفًا، يظهر Excel رسالة خطأ ويطالب بإدخال رقم في النطاق الصحيح. إذا نسخ ولصق رقم، مثل 3، في الخلية، فإن Excel لا يجري فحص تحقق أو يعرض رسالة خطأ.

في بعض الأحيان، يكون من الضروري التحقق مما إذا كانت القيمة تلبي قواعد التحقق من البيانات المطبقة على الخلية بشكل برمجي. في المثال أعلاه، على سبيل المثال، يجب أن يفشل الإدخال.

{{% /alert %}} 

## **مقدمة**
يوفر Aspose.Cells طريقة [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) للتحقق من صحة قيم الخلايا برمجياً. إذا كانت قيمة خلية لا تفي بقواعد التحقق من البيانات المطبقة على تلك الخلية، فإنه يرجع **False**، وإلا يرجع **True**.

يبرز رمز العينة التالي كيفية عمل طريقة [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/). أولاً، يضع القيمة 3 في C1. نظرًا لأن هذه القيمة لا تفي بقواعد التحقق من البيانات، فإن طريقة [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) تُرجع **False**. ثم يُدخل القيمة 15 في C1. نظرًا لأن هذه القيمة تفي بقواعد التحقق من البيانات، فإن الطريقة تُرجع **True**. وبالمثل، ترجع **False** للقيمة 30.

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

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access Cell C1
    // Cell C1 has the Decimal Validation applied on it.
    // It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Enter 3 inside this cell
    // Since it is not between 10 and 20, it should fail the validation
    cell.PutValue(3);

    // Check if number 3 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 3 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 15 inside this cell
    // Since it is between 10 and 20, it should succeed the validation
    cell.PutValue(15);

    // Check if number 15 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 15 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 30 inside this cell
    // Since it is not between 10 and 20, it should fail the validation again
    cell.PutValue(30);

    // Check if number 30 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 30 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **الناتج**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
