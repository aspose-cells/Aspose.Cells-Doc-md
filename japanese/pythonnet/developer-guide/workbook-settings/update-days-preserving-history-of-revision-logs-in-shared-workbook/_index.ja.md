---
title: 共有ワークブックのリビジョンログの履歴を保持する日数を更新
type: docs
weight: 80
url: /ja/python-net/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **可能な使用シナリオ**

ワークブックを共有するとき、***変更履歴をN日間保持***というオプションが次のスクリーンショットのように表示されます。履歴を保持する日数は、Aspose.Cells for Python via .NETの[**WorksheetCollection.revision_logs.days_preserving_history**](https://reference.aspose.com/cells/python-net/aspose.cells.revisions/revisionlogcollection/days_preserving_history)プロパティを使用して調整できます。

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **共有ブックにおける修正履歴の歴史を保持したまま日数を更新する**

次のサンプルコードは空のワークブックを作成し、それを共有し、履歴を30日通常のところ7日に維持する日数で更新します。コードによって生成された[出力Excelファイル](60489773.xlsx)を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.py" >}}

