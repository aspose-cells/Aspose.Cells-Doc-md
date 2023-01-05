---
title: 新しい行にデータを入力しながら、テーブルまたはリスト オブジェクトに数式を自動的に適用する
linktitle: テーブル式を設定します
type: docs
weight: 260
url: /ja/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---
## **考えられる使用シナリオ**
場合によっては、新しいデータを入力するときに、テーブル オブジェクトまたはリスト オブジェクトの式を新しい行に自動的に反映させたいことがあります。これは、Microsoft Excel の既定の動作です。 Aspose.Cells で同じことを達成するには、[ListColumn.Formula](https://reference.aspose.com/cells/net/aspose.cells.tables/listcolumn/properties/formula)財産。
## **新しい行にデータを入力しながら、テーブルまたはリスト オブジェクトに数式を自動的に適用する**
次のサンプル コードでは、新しいデータを入力すると、列 B の数式が新しい行に自動的に反映されるように、テーブル オブジェクトまたはリスト オブジェクトを作成します。を確認してください[出力エクセルファイル](5115469.xlsx)このコードで生成されます。セル A3 に数値を入力すると、セル B2 の数式がセル B3 に自動的に反映されます。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PropagateFormulaInTable-1.cs" >}}
