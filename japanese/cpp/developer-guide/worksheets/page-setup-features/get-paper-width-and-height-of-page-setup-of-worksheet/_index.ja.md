---
title: C++を使用してワークシートのページ設定から用紙の幅と高さを取得する
linktitle: ページ設定の用紙の幅と高さを取得します
type: docs
weight: 50
url: /ja/cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Aspose.Cells for C++ APIを使用して、Excelのページ設定の用紙幅と用紙高さをプログラムによって取得する方法を学びます。
keywords: Excelページ設定の用紙の幅 C++、Excelページ設定の用紙の高さ C++
---

## **可能な使用シナリオ**

時々、ワークシートのページ設定に設定された用紙の幅と高さを知る必要があります。これには、[**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/)と[**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/)メソッドを使用してください。

## **ワークシートのページ設定の用紙の幅と高さを取得**

以下のサンプルコードは、[**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/)と[**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/)メソッドの使用例を示しています。最初に用紙サイズを*A2*に変更し、その後に用紙の幅と高さを調べ、次に*A3*、*A4*、*Letter*に変更して用紙の幅と高さを調べます。

### **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook class
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Set paper size to A2 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA2);
    cout << "PaperA2: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A3 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3);
    cout << "PaperA3: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A4 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);
    cout << "PaperA4: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to Letter and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperLetter);
    cout << "PaperLetter: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **コンソール出力**

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
