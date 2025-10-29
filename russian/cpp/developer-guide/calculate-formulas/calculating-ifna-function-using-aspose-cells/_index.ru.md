---
title: Вычисление функции IFNA с помощью Aspose.Cells в C++
linktitle: Вычисление функции IFNA
description: Как вычислять функции IFNA с помощью библиотеки Aspose.Cells на C++. Загружая существующий файл Excel или создавая новый, мы можем использовать методы Aspose.Cells для вычисления функции IFNA и получения результата. В конце мы сохраняем изменённый файл Excel на диск.
keywords: Aspose.Cells, Excel, функции IFNA, вычисления, C++
type: docs
weight: 40
url: /ru/cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells поддерживает вычисление функции Excel IFNA. Функция IFNA возвращает указанное вами значение, если формула возвращает ошибку #N/A, в противном случае возвращает результат формулы.

{{% /alert %}} 

## **Вычисление функции IFNA с помощью Aspose.Cells**
В следующем образце кода показано вычисление функции IFNA с помощью Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create new workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add data for VLOOKUP
    worksheet.GetCells().Get(u"A1").PutValue(u"Apple");
    worksheet.GetCells().Get(u"A2").PutValue(u"Orange");
    worksheet.GetCells().Get(u"A3").PutValue(u"Banana");

    // Access cell A5 and A6
    Cell cellA5 = worksheet.GetCells().Get(u"A5");
    Cell cellA6 = worksheet.GetCells().Get(u"A6");

    // Assign IFNA formula to A5 and A6
    cellA5.SetFormula(u"=IFNA(VLOOKUP(\"Pear\",$A$1:$A$3,1,0),\"Not found\")");
    cellA6.SetFormula(u"=IFNA(VLOOKUP(\"Orange\",$A$1:$A$3,1,0),\"Not found\")");

    // Calculate the formula of workbook
    workbook.CalculateFormula();

    // Print the values of A5 and A6
    std::cout << cellA5.GetStringValue().ToUtf8() << std::endl;
    std::cout << cellA6.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Вывод в консоль**
Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

Not found

Orange

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
