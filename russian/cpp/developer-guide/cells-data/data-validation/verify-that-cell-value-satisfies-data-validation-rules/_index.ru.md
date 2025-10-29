---
title: Проверка соответствия значения ячейки правилам проверки данных с помощью C++
linktitle: Проверка того, что значение ячейки удовлетворяет правилам валидации данных
type: docs
weight: 210
url: /ru/cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Узнайте, как проверить, соответствует ли значение ячейки правилам проверки данных, с помощью API Aspose.Cells for C++.
keywords: Получить значение проверки ячейки, Получить значение проверки ячейки, Проверить, удовлетворяет ли значение правилам валидации данных, примененным к ячейке
---

{{% alert color="primary" %}} 

Microsoft Excel позволяет пользователям добавлять правила проверки данных к ячейкам. Например, правило дескриминативной проверки определяет, что могут вводиться только числа между 10 и 20. Если пользователь вводит другое число, Excel показывает сообщение об ошибке и предлагает ввести число в правильном диапазоне. Если вы копируете и вставляете число, например 3, в ячейку, проверка не запускается и сообщение об ошибке не показывается.

Иногда необходимо программно проверить, удовлетворяет ли значение правилам валидации данных, примененным к ячейке. В приведенном выше случае, например, ввод должен завершиться неудачей.

{{% /alert %}} 

## **Введение**
Aspose.Cells предоставляет метод [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) для программной проверки значений ячеек. Если значение в ячейке не соответствует правилу проверки данных, примененному к этой ячейке, он возвращает **False**, иначе — **True**.

Следующий пример иллюстрирует, как работает метод [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/). Сначала в C1 вводится значение 3, что не удовлетворяет правилу проверки данных, и метод возвращает **False**. Затем в C1 вводится значение 15, которое удовлетворяет правилу проверки, и метод возвращает **True**. Аналогично, для значения 30 возвращает **False**.

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

### **Вывод**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
