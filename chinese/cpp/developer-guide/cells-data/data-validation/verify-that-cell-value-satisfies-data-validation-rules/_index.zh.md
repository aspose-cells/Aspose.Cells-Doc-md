---
title: 验证单元格值是否满足数据验证规则（使用C++）
linktitle: 验证单元格值是否满足数据验证规则
type: docs
weight: 210
url: /zh/cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: 学习如何通过Aspose.Cells for C++ API验证单元格值是否符合数据验证规则。
keywords: 获取单元格验证值，获取单元格验证值，验证值是否满足应用于单元格的数据验证规则
---

{{% alert color="primary" %}} 

Microsoft Excel允许用户为单元格添加数据验证规则。例如，小数验证指定只能输入10到20之间的数字。如果用户输入不同的数字，Excel会显示错误信息并提示他们输入正确范围内的数字。如果复制粘贴一个数字，比如3，Excel不会进行验证检查或显示错误信息。

有时，有必要以编程方式验证一个值是否满足应用于该单元格的数据验证规则。例如，上面的情况下，输入应该是失败的。

{{% /alert %}} 

## **介绍**
Aspose.Cells提供 [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) 方法，可以编程验证单元格值。如果单元格中的值不满足所应用的验证规则，将返回 **False**，否则返回 **True**。

以下示例代码演示了 [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) 方法的工作方式。首先在C1中输入值3，由于不满足验证规则，返回 **False**。然后在C1中输入值15，满足验证规则，返回 **True**。类似地，值30也会返回 **False**。

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

### **输出**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
