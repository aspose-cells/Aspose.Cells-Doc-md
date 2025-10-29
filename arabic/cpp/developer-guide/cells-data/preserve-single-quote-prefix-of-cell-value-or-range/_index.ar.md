---
title: الحفاظ على بادئة الاقتباس المفرد ل قيمة الخلية أو النطاق باستخدام ++C
linktitle: الحفاظ على بادئة الاقتباس الفردي لقيمة الخلية أو النطاق
type: docs
weight: 310
url: /ar/cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: تعلم كيفية الحفاظ على بادئة الاقتباس المفرد ل قيمة الخلية أو النطاق من خلال API Aspose.Cells for C++.
keywords: الحفاظ على بادئة علامة اقتباس واحدة لقيمة الخلية أو النطاق، إخفاء الرصاصة بادئة أو علامة اقتباس واحدة، إظهار الرصاصة بادئة أو علامة اقتباس واحدة
---

## **سيناريوهات الاستخدام المحتملة**

عندما تضع قيمة داخل الخلية وتحتوي على فاصلة بادئة أو علامة اقتباس مفردة، فإن مايكروسوفت إكسل يخفيها، ولكن عند تحديد الخلية، يعرض الفاصلة أو علامة الاقتباس المفردة في شريط الصيغة كما هو موضح في لقطة الشاشة التالية.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

كما يخفي Aspose.Cells الفاصلة أو علامة الاقتباس المفردة كما في مايكروسوفت إكسل، لكنه يضبط [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) على أنه **true** لتلك الخلية. إذا قمت بضبط نمط فارغ للخلية، يصبح [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) **false** مرة أخرى. للتعامل مع هذه المشكلة، يوفر Aspose.Cells الخاصية [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/)، عندما تتم ضبطها على **false**، فإن [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) لن يتم تحديثه على الإطلاق ويحتفظ بقيمته القديمة. هذا يعني أنه إذا كانت القيمة القديمة لخاصية [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) كانت **true**، فستظل **true**، وإذا كانت خاطئة، فستظل خاطئة.

## **الحفاظ على بادئة اقتباس واحدة لقيمة الخلية أو النطاق**

الشفرة النموذجية التالية تشرح كيفية استخدام الخاصية [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/) كما هو موضح سابقًا. يرجى قراءة التعليقات داخل الكود ومشاهدة خرج وحدة التحكم للرمز أدناه للمزيد من المساعدة.

## **الكود المثالي**

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

## **مخرجات الوحدة**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
