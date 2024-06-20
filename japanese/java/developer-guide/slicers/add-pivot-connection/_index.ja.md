---
title: ピボット接続を追加する
type: docs
weight: 30
url: /ja/java/add-pivot-connection/
description: Aspose.Cells Javaライブラリを使用してピボット接続を追加する方法を学ぶ。
keywords: オフィス2013、オフィス2016、オフィス2019およびオフィス365なしでピボット接続を追加する
---

## **可能な使用シナリオ**

Excelでスライサーとピボットテーブルを関連付けたい場合は、スライサーを右クリックし、「レポート接続...」項目を選択する必要があります。オプションリストでチェックボックスで操作できます。Aspose.Cells Java APIを使用してスライサーとピボットテーブルをプログラムで関連付ける場合は、[**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#addPivotConnection(com.aspose.cells.PivotTable)/) メソッドを使用してください。

## **スライサーとピボットテーブルを関連付ける**

次のサンプルコードは、既存のスライサーが含まれる[sample Excelファイル](add-pivot-connection.xlsx)を読み込みます。次に、スライサーにアクセスしてスライサーとピボットテーブルを関連付けます。最後に、ワークブックを[output Excelファイル](add-pivot-connection-out.xlsx)として保存します。 


## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Adding-Pivot-Connection.java" >}}
