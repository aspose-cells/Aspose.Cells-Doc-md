---
title: ピボット接続を解除する
type: docs
weight: 30
url: /ja/java/remove-pivot-connection/
description: Aspose.Cells Javaライブラリを使用してピボット接続を削除する方法を学ぶ。
keywords: オフィス2013、オフィス2016、オフィス2019およびオフィス365なしでピボット接続を解除する
---

## **可能な使用シナリオ**

Microsoft Excelでスライサーとピボットテーブルを非連携にしたい場合は、スライサーを右クリックし、「レポートの接続...」アイテムを選択する必要があります。オプションリストでチェックボックスを操作できます。同様に、Aspose.Cells APIを使用してスライサーとピボットテーブルを非連携にしたい場合は、[**Slicer.removePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#removePivotConnection-com.aspose.cells.PivotTable-) メソッドを使用してください。これにより、スライサーとピボットテーブルが非連携になります。

## **スライサーの削除**

次のサンプルコードは、既存のスライサーを含む [サンプルExcelファイル](remove-pivot-connection.xlsx) を読み込みます。それからスライサーにアクセスして非連携にします。最後に、ワークブックを[出力Excelファイル](remove-pivot-connection-out.xlsx)として保存します。 


## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Removing-Pivot-Connection.java" >}}
{{< app/cells/assistant language="java" >}}
