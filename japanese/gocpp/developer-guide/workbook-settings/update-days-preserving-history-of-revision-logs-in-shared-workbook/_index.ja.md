---
title: GolangをC++経由で使用して、共有ブックのリビジョン履歴の日数を更新する方法
linktitle: 共有ワークブックのリビジョンログの履歴を保持する日数を更新
type: docs
weight: 80
url: /ja/go-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Golangを使ったC++経由でAspose.Cellsで履歴保存期間の日数を更新する方法を学ぶ
---

## **可能な使用シナリオ**

ワークブックを共有する際、次のスクリーンショットに示されるように、***N 日間リビジョン履歴を保持*** というオプションが表示されます。Aspose.Cells を使用して保持する履歴の日数を更新できます。

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **共有ブックにおける修正履歴の歴史を保持したまま日数を更新する**

次のサンプルコードは空のワークブックを作成し、それを共有し、履歴を30日通常のところ7日に維持する日数で更新します。コードによって生成された[出力Excelファイル](60489773.xlsx)を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.go" >}}
