---
title: C++でセル値がシングルクォートマークで始まるかどうかを調べる
linktitle: セルの値がシングルクォートマークで始まるかどうかを検索
type: docs
weight: 270
url: /ja/cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Aspose.Cells for C++ APIを通じてセル値がシングルクォートマークで始まるかどうかを調べる方法を学習します。
keywords: シングルクォーテーション記号で始まるセルの値を見つける、シングルクォーテーション記号で始まるセルの値を検索する
---

{{% alert color="primary" %}}

Aspose.Cellsは、セルの値がシングルクォーテーション記号で始まるかどうかを見つけるための[**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/)プロパティを提供します。このプロパティがなかった場合、sampleと 'sampleなどの文字列を区別する方法はありません。

{{% /alert %}}

以下のサンプルコードは、sampleと 'sampleのような文字列を[**Cell::GetStringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/)プロパティで区別できないことを説明します。そのため、それらを区別するには[**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/)プロパティを使用する必要があります。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Create worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Access cell A1 and A2
    Cell a1 = sheet.GetCells().Get(u"A1");
    Cell a2 = sheet.GetCells().Get(u"A2");

    // Add sample in A1 and sample with quote prefix in A2
    a1.PutValue(u"sample");
    a2.PutValue(u"'sample");

    // Print their string values, A1 and A2 both are same
    std::cout << "String value of A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "String value of A2: " << a2.GetStringValue().ToUtf8() << std::endl;

    // Access styles of A1 and A2
    Style s1 = a1.GetStyle();
    Style s2 = a2.GetStyle();

    std::cout << std::endl;

    // Check if A1 and A2 has a quote prefix
    std::cout << "A1 has a quote prefix: " << s1.GetQuotePrefix() << std::endl;
    std::cout << "A2 has a quote prefix: " << s2.GetQuotePrefix() << std::endl;

    Aspose::Cells::Cleanup();
}
```
