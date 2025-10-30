---
title: Hücre veya Aralıkta Tek Tırnak Öneki Koruma, C++ ile
linktitle: Hücre Değerinin veya Aralığının Tek Tek Tırnak Önekini Koru
type: docs
weight: 310
url: /tr/cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Aspose.Cells for C++ API kullanarak Hücre veya Aralıkta Tek Tırnak Ön Ekini Nasıl Koruyacağınızı öğrenin.
keywords: Tek Tırnak Öneki ile Hücre Değeri veya Aralığının Saklanması, Önde Gelen tırnak işareti veya tek tırnak işareti gizle, İlk tek tırnak işareti veya tek tırnak işareti göster
---

## **Olası Kullanım Senaryoları**

Bir hücreye öngörülen apostrof veya tek tırnak işareti ile bazı değerler koyduğunuzda, Microsoft Excel bunları gizler, ancak hücreyi seçtiğinizde, formül çubuğunda önde gelen apostrof veya tek tırnak gösterilir. Aşağıdaki ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells, Microsoft Excel gibi önde gelen apostrof veya tek tırnak işaretini gizler, ancak bu hücre için [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) değerini **doğru** yapar. Eğer hücrenin boş bir stili ayarlanırsa, o zaman [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) tekrar **yanlış** olur. Bu sorunla başa çıkmak için Aspose.Cells, [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/) özelliği sağlar, bu ayar **yanlış** yapıldığında, [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) hiç güncellenmez ve eski değeri korunur. Bu, eğer [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) özelliğinin eski değeri **doğru** ise, **doğru** kalacaktır ve eğer eski değer **yanlış** ise, o da **yanlış** kalacaktır.

## **Hücre Değerinin veya Aralığın Ön Eklemesini Koruma**

Aşağıdaki örnek kod, yukarıda açıklanan [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/) özelliğinin kullanımını açıklar. Lütfen kod içindeki yorumları okuyun ve aşağıda verilen kodun konsol çıktılarını inceleyerek daha fazla yardım alın.

## **Örnek Kod**

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

## **Konsol Çıktısı**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
