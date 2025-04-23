---
title: Сохраняйте префикс одинарной кавычки значения ячейки или диапазона с помощью C++
linktitle: Сохранить одинарное кавычку перед значением ячейки или диапазоном
type: docs
weight: 310
url: /ru/cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Узнайте, как сохранять префикс одинарной кавычки значения ячейки или диапазона через API Aspose.Cells for C++.
keywords: Сохранить предшествующий одинарный знак кавычки значения ячейки или диапазона, Скрыть ведущий апостроф или одинарный знак кавычки, Показать ведущий апостроф или одинарный знак кавычки
---

## **Возможные сценарии использования**

Когда вы вставляете значение в ячейку с ведущей апострофом или одинарной кавычкой, Microsoft Excel скрывает её, но при выборе ячейки она отображается в строке формул, как показано на следующем скриншоте.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells также скрывает ведущую апостроф или одинарную кавычку, как в Microsoft Excel, но устанавливает [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) в значение **true** для этой ячейки. Если вы установите пустой стиль ячейки, то [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) снова станет **false**. Чтобы решить эту проблему, Aspose.Cells предоставляет свойство [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/), при установке которого в **false** [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) не обновляется вовсе, и сохраняется его старое значение. Это означает, что если старое значение свойства [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) было **true**, оно останется **true**, а если — **false**, то останется **false**.

## **Сохранить префикс одинарной кавычки значения ячейки или диапазона**

Следующий пример кода иллюстрирует использование свойства [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/), как было описано ранее. Обратите внимание на комментарии внутри кода и посмотрите вывод в консоли ниже для получения дополнительной информации.

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = ws.GetCells().Get(u"A1");

    // Put some text in cell, it does not have Single Quote at the beginning
    cell.PutValue(u"Text");

    // Access style of cell A1
    Style st = cell.GetStyle();

    // Print the value of Style.QuotePrefix of cell A1
    std::cout << "Quote Prefix of Cell A1: " << st.GetQuotePrefix() << std::endl;

    // Put some text in cell, it has Single Quote at the beginning
    cell.PutValue(u"'Text");

    // Access style of cell A1
    st = cell.GetStyle();

    // Print the value of Style.QuotePrefix of cell A1
    std::cout << "Quote Prefix of Cell A1: " << st.GetQuotePrefix() << std::endl;

    // Print information about StyleFlag.QuotePrefix property
    std::cout << std::endl;
    std::cout << "When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix." << std::endl;
    std::cout << "Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix." << std::endl;
    std::cout << std::endl;

    // Create an empty style
    st = wb.CreateStyle();

    // Create style flag - set StyleFlag.QuotePrefix as false
    // It means, we do not want to update the Style.QuotePrefix property of cell A1's style.
    StyleFlag flag;
    flag.SetQuotePrefix(false);

    // Create a range consisting of single cell A1
    Range rng = ws.GetCells().CreateRange(u"A1");

    // Apply the style to the range
    rng.ApplyStyle(st, flag);

    // Access the style of cell A1
    st = cell.GetStyle();

    // Print the value of Style.QuotePrefix of cell A1
    // It will print True, because we have not updated the Style.QuotePrefix property of cell A1's style.
    std::cout << "Quote Prefix of Cell A1: " << st.GetQuotePrefix() << std::endl;

    // Create an empty style
    st = wb.CreateStyle();

    // Create style flag - set StyleFlag.QuotePrefix as true
    // It means, we want to update the Style.QuotePrefix property of cell A1's style.
    flag.SetQuotePrefix(true);

    // Apply the style to the range
    rng.ApplyStyle(st, flag);

    // Access the style of cell A1
    st = cell.GetStyle();

    // Print the value of Style.QuotePrefix of cell A1
    // It will print False, because we have updated the Style.QuotePrefix property of cell A1's style.
    std::cout << "Quote Prefix of Cell A1: " << st.GetQuotePrefix() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Вывод в консоль**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
