---
title: OpenXmlのSheet.SheetIdプロパティをC++で使用
linktitle: OpenXmlのSheet.SheetIdプロパティを使用
type: docs
weight: 200
url: /ja/cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: この記事では、Excel操作のC++ APIまたはライブラリを使ってOpenXmlのSheet.SheetIdプロパティをプログラムで利用する方法を示します。
keywords: openxmlのシートIDプロパティ（C++）、ExcelワークシートのシートID（C++）
---

## **可能な使用シナリオ**

*Sheet.SheetId* プロパティは、 *DocumentFormat.OpenXml.Spreadsheet* ネームスペース内にあり、OpenXmlの一部です。次のスクリーンショットに表示されているように、このプロパティとその値を *workbook.xml* 内で見ることができます。Aspose.Cellsは、このプロパティを[**Worksheet.GetTabId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettabid/)として提供します。

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Aspose.Cellsを使用したOpenXmlのSheet.SheetIdプロパティを利用する**

次のサンプルコードは、[サンプルExcelファイル](51740716.xlsx)をロードし、そのシートまたはタブIDを読み取り、それに新しいタブIDを割り当てて[出力Excelファイル](51740717.xlsx)として保存します。以下に示すコードのコンソール出力も参照してください。

## **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load source Excel file
    Workbook wb(u"sampleSheetId.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Print its Sheet or Tab Id on console
    std::cout << "Sheet or Tab Id: " << ws.GetTabId() << std::endl;

    // Change Sheet or Tab Id
    ws.SetTabId(358);

    // Save the workbook
    wb.Save(u"outputSheetId.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **コンソール出力**

{{< highlight java >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
