---
title: C++を使用してセル値や範囲のシングルクオートプレフィックスを保持する
linktitle: セル値または範囲の接頭辞を保存します
type: docs
weight: 310
url: /ja/cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Aspose.Cells for C++ APIを通じてセル値や範囲のシングルクオートプレフィックスを保持する方法を学習します。
keywords: セル値または範囲の先頭アポストロフィを保持し、先頭のアポストロフィまたはシングルクォートマークを非表示にする、先頭のアポストロフィまたはシングルクォートマークを表示する
---

## **可能な使用シナリオ**

先頭のアポストロフィまたはシングルクオート記号を持つセルに値を入力すると、Microsoft Excelはそれを隠しますが、セルを選択すると、数式バーに先頭のアポストロフィまたはシングルクオートが表示される例です。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.CellsはMicrosoft Excelと同様に先頭のアポストロフィまたはシングルクオートを隠しますが、そのセルには[**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/)を**true**に設定します。セルのスタイルを空に設定すると、[**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/)は再び**false**になります。この問題に対処するために、Aspose.Cellsは[**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/)プロパティを提供しており、設定されているときは**false**にされると[**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/)は全く更新されず、古い値が保持されます。これは、[**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/)プロパティの古い値が**true**であった場合は**true**のまま、**false**だった場合はそのままです。

## **セル値または範囲の先頭にシングルクォートのプレフィックスを保存**

以下のサンプルコードは、前述の[**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/)プロパティの使用例を説明しています。コード内のコメントを読んで、以下のコードのコンソール出力も確認してください。

## **サンプルコード**

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

## **コンソール出力**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
