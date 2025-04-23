---
title: 共有ブックの改訂ログの履歴を保持する日数を C++ で更新する
linktitle: 共有ワークブックのリビジョンログの履歴を保持する日数を更新
type: docs
weight: 80
url: /ja/cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Aspose.Cells を使ってC++で共有ブックの履歴保存日数を更新する方法を学びます。
---

## **可能な使用シナリオ**

ワークブックを共有する際、次のスクリーンショットに示されるように、***N 日間リビジョン履歴を保持*** というオプションが表示されます。Aspose.Cells を使用して保持する履歴の日数を更新できます。

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **共有ブックにおける修正履歴の歴史を保持したまま日数を更新する**

次のサンプルコードは空のワークブックを作成し、それを共有し、履歴を30日通常のところ7日に維持する日数で更新します。コードによって生成された[出力Excelファイル](60489773.xlsx)を参照してください。

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Share the workbook
    wb.GetSettings().SetShared(true);

    // Update DaysPreservingHistory of RevisionLogs
    wb.GetWorksheets().GetRevisionLogs().SetDaysPreservingHistory(7);

    // Save the workbook
    wb.Save(u"outputShared_DaysPreservingHistory.xlsx");

    std::cout << "Workbook shared and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
