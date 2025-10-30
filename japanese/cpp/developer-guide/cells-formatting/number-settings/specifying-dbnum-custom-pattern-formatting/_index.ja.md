---
title: C++でDBNumカスタムパターン書式設定を指定する
linktitle: DBNumのカスタムパターン書式を指定する
description: Aspose.Cellsは、カスタム書式パターンを使用して日付と数値の書式設定をサポートするC++用のスプレッドシート操作ライブラリです。この記事では、Aspose.Cellsライブラリを使用して「dbnum」のカスタム書式パターンを指定し、ユーザーが数値の表示方法をより細かく制御できるようにします。
keywords: Aspose.Cells、C++ライブラリ、電子スプレッドシート、カスタム書式パターン、書式設定、「dbnum」、表示制御
type: docs
weight: 110
url: /ja/cpp/specifying-dbnum-custom-pattern-formatting/
---

## **可能な使用シナリオ**

Aspose.Cellsは*DBNum*カスタムパターン書式設定をサポートしています。例：セルの値が123の場合、カスタム書式を[DBNum2][$-804]Generalと指定すると、「壹佰贰拾叁」と表示されます。セルのカスタム書式は[**Cell.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)メソッドと[**Style.Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/)プロパティを使用して指定できます。

## **サンプルコード**

以下のサンプルコードは、「*DBNum*」カスタムパターンの書式設定を指定する方法を示しています。[出力PDF](43352081.pdf)もご確認ください。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A1 and put value 123
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(123);

    // Access cell style
    Style st = cell.GetStyle();

    // Specifying DBNum custom pattern formatting
    st.SetCustom(u"[DBNum2][$-804]General", true);

    // Set the cell style
    cell.SetStyle(st);

    // Set the first column width
    ws.GetCells().SetColumnWidth(0, 30);

    // Save the workbook in output pdf format
    wb.Save(outDir + u"outputDBNumCustomFormatting.pdf", SaveFormat::Pdf);

    std::cout << "DBNum custom formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
