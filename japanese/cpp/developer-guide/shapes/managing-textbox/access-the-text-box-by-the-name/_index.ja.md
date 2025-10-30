---
title: C++を使用して名前でテキストボックスにアクセス
linktitle: 名前でテキストボックスにアクセス
type: docs
weight: 230
url: /ja/cpp/access-the-text-box-by-the-name/
description: Aspose.Cells for C++を使って名前でテキストボックスにアクセスする方法を学びます。
---

## 名前でテキストボックスにアクセスする

以前は、テキストボックスは[**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/)コレクションのインデックスでアクセスされていましたが、現在はこのコレクションから名前でアクセスすることもできます。これは、名前をすでに知っている場合に便利で迅速な方法です。

以下のサンプルコードは、最初にテキストボックスを作成し、いくつかのテキストと名前を割り当て、その後、同じ名前のテキストボックスにアクセスしてテキストを印刷します。

### C++で名前によるテキストボックスへのアクセス方法

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    int idx = sheet.GetTextBoxes().Add(10, 10, 10, 10);

    // Access newly created TextBox using its index & name it
    TextBox tb1 = sheet.GetTextBoxes().Get(idx);
    tb1.SetName(u"MyTextBox");

    // Set text for the TextBox
    tb1.SetText(u"This is MyTextBox");

    // Access the same TextBox via its name
    TextBox tb2 = sheet.GetTextBoxes().Get(u"MyTextBox");

    // Display the text of the TextBox accessed via name
    std::cout << tb2.GetText().ToUtf8() << std::endl;

    std::cout << "Press any key to continue..." << std::endl;
    std::cin.get();

    Aspose::Cells::Cleanup();
}
```

### サンプルコードによって生成されたコンソール出力

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
