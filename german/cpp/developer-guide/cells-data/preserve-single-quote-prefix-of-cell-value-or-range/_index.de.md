---
title: Einzelnen Anführungszeichenpräfix eines Zellwerts oder Bereichs mit C++ bewahren
linktitle: Behalten Sie das einfache Anführungszeichenpräfix des Zellwerts oder bereichs bei
type: docs
weight: 310
url: /de/cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Lernen Sie, wie man das Einzelnen Anführungszeichenpräfix eines Zellwerts oder Bereichs mit der API Aspose.Cells for C++ bewahrt.
keywords: Präfix eines Zellenwerts oder Bereichs mit einfachem Anführungszeichen beibehalten, Anführende Apostrophe oder einfaches Anführungszeichen ausblenden, Anführende Apostrophe oder einfaches Anführungszeichen anzeigen
---

## **Mögliche Verwendungsszenarien**

Wenn Sie einen Wert in die Zelle eingeben, der ein führendes Apostroph oder einzelnes Anführungszeichen hat, blendet Microsoft Excel diese aus, aber wenn Sie die Zelle auswählen, wird das führende Apostroph oder einzelne Anführungszeichen in der Formelleiste angezeigt, wie im folgenden Screenshot.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells blendet das führende Apostroph oder einzelne Anführungszeichen genauso aus wie Microsoft Excel, setzt aber [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) für diese Zelle auf **true**. Wenn Sie einen leeren Stil der Zelle setzen, wird [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) wieder auf **false** gesetzt. Um dieses Problem zu lösen, bietet Aspose.Cells die Eigenschaft [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/) an, die bei Einstellung auf **false** bewirkt, dass [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) überhaupt nicht aktualisiert wird und sein alter Wert beibehalten wird. Das bedeutet, wenn der alte Wert der Eigenschaft [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) **true** war, bleibt er **true**, und wenn der alte Wert **false** war, bleibt er **false**.

## **Einzelnes Anführungszeichen-Prefix des Zellenwerts oder -bereichs beibehalten**

Der folgende Beispielcode erklärt die Verwendung der Eigenschaft [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/), wie zuvor beschrieben. Bitte lesen Sie die Kommentare im Code und sehen Sie sich die Konsolenausgabe an, die unten für weitere Hilfe gezeigt wird.

## **Beispielcode**

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

## **Konsolenausgabe**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
