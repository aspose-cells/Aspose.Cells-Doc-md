--- 
title: C++を使ったExcelのFrozen状態の確認方法 
linktitle: 凍結状態 
type: docs 
weight: 190 
url: /ja/cpp/how-to-check-frozen-state-of-excel-worksheet 
description: この記事では、Aspose.Cells APIを使用し、C++でExcelワークシートの固定状態をプログラムで確認する方法について説明します。 
--- 

## **紹介** 

この記事では、Excelワークシートの固定状態をプログラムで確認する方法について学びます。MS Excelでは、シートが固定されているかどうか、または分割されているかどうかを簡単に調べることができます。しかし、C++で固定または分割されているかどうかを調べる方法はあるのでしょうか？これはAspose.Cells for C++を使って行えます。 

## **ウィンドウペインは凍っていますか** 
Aspose.Cells for C++を使えば、ウインドウが固定されているかどうかや、ロックされている行数や列数を確認できます。 

ウインドウのペインの状態やロックされている行列を取得するには、[**Worksheet::GetFreezedPanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getfreezedpanes/)メソッドとともに[**GetPaneState()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getpanestate/)プロパティを使用してください。 
1. ファイルを開くためのワークブックを作成します。 
2. ワークシートが凍結しているかどうかを確認します。 
3. ロックされている行と列を取得します。 

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create the workbook from the specified file
    Workbook workbook(u"Frozen.xlsx");

    // Get the first worksheet from the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Check whether the worksheet is frozen
    if (sheet.GetPaneState() == PaneStateType::Frozen || sheet.GetPaneState() == PaneStateType::FrozenSplit)
    {
        int32_t row = 0, column = 0;
        int32_t rows = 0, columns = 0;

        // Get the locked rows and columns
        sheet.GetFreezedPanes(row, column, rows, columns);

        // Output the details if needed (just for demonstration)
        std::cout << "Frozen panes at Row: " << row << ", Column: " << column << ", Total Frozen Rows: " 
                  << rows << ", Total Frozen Columns: " << columns << std::endl;
    }

    Aspose::Cells::Cleanup();
}
``` 

{{< app/cells/assistant language="cpp" >}}
