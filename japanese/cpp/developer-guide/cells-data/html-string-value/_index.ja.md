---
title: C++を使ったセル内にHTMLリッチテキストを追加
linktitle: HTML文字列値
type: docs
weight: 50
url: /ja/cpp/adding-html-rich-text-inside-the-cell/
description: Aspose.Cells for C++ APIを使用して、セル内にHTMLリッチテキストを追加する方法を学びます。
keywords: セル内にHTMLリッチテキストを追加する、セル内にHTMLリッチテキストを設定する、セル内にHTMLリッチテキストを追加する
---

{{% alert color="primary" %}}

Aspose.Cellsは、Microsoft Excel指向のHTMLをXLS/XLSX形式に変換する機能をサポートしています。つまり、Microsoft Excelによって生成されたHTMLは、Aspose.Cellsを使用してXLS/XLSX形式に変換できます。

同様に、簡単なHTMLがある場合、Aspose.CellsはそれをHTMLリッチテキストに変換できます。Aspose.Cellsは、[**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) メソッドを提供しており、そのようなシンプルなHTMLを取り込み、フォーマットされたセルテキストに変換します。

{{% /alert %}}

以下のコードサンプルは、セル内に HTML リッチテキストを追加する方法を示しています。出力 Excel ファイルのスクリーンショットを参照してください。

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set HTML formatted text in the cell
    cell.SetHtmlString(u"<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "HTML formatted text added to cell A1 successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## 関連記事

- [HTMLを設定して箇条書きを表示](/cells/ja/cpp/display-bullets-by-setting-cell-value-using/)
- [セルからHTML5文字列を取得](/cells/ja/cpp/get-html5-string-from-cell/)
{{< app/cells/assistant language="cpp" >}}
