---
title: Golangを使ったピボットコネクションの追加（C++経由）
linktitle: ピボット接続を追加する
type: docs
weight: 30
url: /ja/go-cpp/add-pivot-connection/
description: Aspose.Cellsライブラリを使用したC++でのピボットコネクションの追加方法を学びます。
keywords: オフィス2013、オフィス2016、オフィス2019およびオフィス365なしでピボット接続を追加する
---

## **可能な使用シナリオ**

Excelでスライサーとピボットテーブルを関連付けたい場合は、スライサーを右クリックして「レポートの接続...」項目を選択する必要があります。オプションリストでチェックボックスで操作できます。同様に、Aspose.Cells APIを使用してプログラムでスライサーとピボットテーブルを関連付けたい場合は、[**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/go-cpp/slicer/addpivotconnection/) メソッドを使用してください。これはスライサーとピボットテーブルを関連付けます。

## **スライサーとピボットテーブルを関連付ける**

次のサンプルコードは、既存のスライサーが含まれる[sample Excelファイル](add-pivot-connection.xlsx)を読み込みます。次に、スライサーにアクセスしてスライサーとピボットテーブルを関連付けます。最後に、ワークブックを[output Excelファイル](add-pivot-connection-out.xlsx)として保存します。 

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPivotConnection.go" >}}
