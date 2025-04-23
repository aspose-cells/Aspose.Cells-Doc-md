---
title: ピボット接続を解除する
type: docs
weight: 30
url: /ja/net/remove-pivot-connection/
description: Aspose.Cellsライブラリを使用してピボット接続を解除する方法を学ぶ
keywords: オフィス2013、オフィス2016、オフィス2019およびオフィス365なしでピボット接続を解除する
---

## **可能な使用シナリオ**

Microsoft Excelでスライサーとピボットテーブルを非連携にしたい場合は、スライサーを右クリックし、「レポートの接続...」アイテムを選択する必要があります。オプションリストでチェックボックスを操作できます。同様に、Aspose.Cells APIを使用してスライサーとピボットテーブルを非連携にしたい場合は、[**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/removepivotconnection/) メソッドを使用してください。これにより、スライサーとピボットテーブルが非連携になります。

## **スライサーとピボットテーブルの非連携**

次のサンプルコードは、既存のスライサーを含む [サンプルExcelファイル](remove-pivot-connection.xlsx) を読み込みます。それからスライサーにアクセスして非連携にします。最後に、ワークブックを[出力Excelファイル](remove-pivot-connection-out.xlsx)として保存します。 


## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-Removing-Pivot-Connection.cs" >}}
{{< app/cells/assistant language="csharp" >}}
