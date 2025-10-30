---
title: 行と列のコピー
type: docs
weight: 40
url: /ja/python-net/copying-rows-and-columns/
description: Aspose.Cells for Python via .NET API を介して行と列をコピーする方法について説明します。
keywords: Python Excel ライブラリ、Python で行と列をコピーする方法、Python で行をコピーする、Python で列をコピーする、Aspose.Cells for Python via .NET を使用して行と列を貼り付ける方法、Python で複数の行と列を貼り付ける方法。
---

## **紹介**

時には、ワークシート全体をコピーせずに行や列をコピーする必要があります。Aspose.Cellsを使用すると、ワークブック内またはワークブック間で行や列をコピーすることができます。
行（または列）をコピーすると、それに含まれるデータ（更新された参照を含む数式、値、コメント、書式設定、非表示セル、画像、その他の図形オブジェクトなど）がコピーされます。

## **Microsoft Excelで行や列をコピーする方法**

1. コピーしたい行または列を選択します。
1. 行または列をコピーする場合は、**標準**ツールバーの**コピー**をクリックするか、**CTRL**+**C**を押します。
1. コピーする選択範囲の下または右側に行または列を選択します。
1. 行または列をコピーする際に、**挿入**メニューで**コピーしたセル**をクリックします。

{{% alert color="primary" %}}

**標準**ツールバーの**貼り付け**をクリックするか、**Insert**メニューのコマンドをクリックする代わりに**CTRL**+**V**を押すと、宛先セルの内容が置き換えられます。

{{% /alert %}}

## **Microsoft Excelを使用した貼り付けオプションを使用した行や列の貼り付け方法**

1. コピーしたいデータやその他の属性を含むセルを選択します。
1. **コピー**をクリックしてHomeタブを選択します。
1. **貼り付け**したいエリア内で最初のセルをクリックします。
1. Homeタブで、**貼り付け**の横にある矢印をクリックし、**貼り付け**を選択します。
1. 希望する**オプション**を選択します。

## **Aspose.Cells for Python で行と列をコピーする方法 via .NET**

## **単一の行をコピーする方法**

Aspose.Cellsは、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) クラスの[**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) メソッドを提供します。このメソッドは、数式、値、コメント、セルの書式、非表示セル、画像など、すべての種類のデータをコピーします。

[**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int)メソッドは以下のパラメーターを取ります:

- ソースの[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)オブジェクト
- ソースの行インデックス、および
- 宛先の行インデックス。

このメソッドを使用すると、シート内または他のシートへの行のコピーが可能です。この[**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) メソッドはMicrosoft Excelと同様に動作します。つまり、例えば、宛先行の高さを明示的に設定する必要はありません。その値もコピーされます。

以下の例は、ワークシート内の行をコピーする方法を示しています。テンプレートのMicrosoft Excelファイルを使用し、2番目の行（データ、書式設定、コメント、画像などを含む）を12番目の行に貼り付けます。

[**Cells.get_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/get_row_height/#int) メソッドを使用してソース行の高さを取得し、[**Cells.set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) メソッドを使用して宛先行の高さを設定する手順は省略できます。なぜなら、[**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) メソッドが自動的に行の高さを処理するからです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingRows-1.py" >}}

{{% alert color="primary" %}}

行をコピーする際は、関連する画像、グラフ、またはその他の描画オブジェクトに注目することが重要です。これはMicrosoft Excelと同じです。

1. もしソース行インデックスが5であれば、画像、グラフなどはその3行に含まれている場合にコピーされます（開始行インデックスが4で終了行インデックスが6の場合）。
1. 宛先行にある既存の画像やグラフなどは削除されません。

{{% /alert %}}

## **複数の行をコピーする方法**

追加の整数型パラメーターを取るメソッド[**Cells.copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int)を使用して、新しい宛先に複数の行をコピーすることもできます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingMultipleRows-1.py" >}}


## **列をコピーする方法**

Aspose.Cellsは[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)クラスの[**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int)メソッドを提供しており、このメソッドは、ソース列から宛先列へ数式（更新された参照を含む）、値、コメント、セル形式、非表示セル、画像、および他の描画オブジェクトなどを含むあらゆるタイプのデータをコピーします。

[**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int)メソッドは以下のパラメーターを取ります:

- ソースの[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)オブジェクト
- ソースの列インデックス、および
- 宛先の列インデックス。

シート内または他のシートへの列のコピーには[**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int)メソッドを使用します。

この例では、ワークシートから列をコピーして別のブック内のワークシートに貼り付けます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingColumns-1.py" >}}

## **複数の列をコピーする方法**

[**Cells.copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int)メソッドと同様に、Aspose.CellsのAPIは新しい位置に複数のソース列をコピーするための[**Cells.copy_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_columns/)メソッドも提供しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingMultipleColumns-1.py" >}}


## **貼り付けオプションを使用して行と列を貼り付ける方法**

Aspose.Cellsは現在、関数[**copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int-aspose.cells.CopyOptions-aspose.cells.PasteOptions)および[**copy_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_columns/#aspose.cells.Cells-int-int-int-aspose.cells.PasteOptions)を使用して[**PasteOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pasteoptions)を提供しています。これにより、Excelと同様の適切な貼り付けオプションを設定することができます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
