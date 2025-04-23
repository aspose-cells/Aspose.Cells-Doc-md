---
title: 新しい行にデータを入力すると、表またはリストオブジェクトの式を自動的に伝播させます
linktitle: テーブルの数式を設定する
type: docs
weight: 260
url: /ja/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **可能な使用シナリオ**
テーブルまたはリストオブジェクトの数式が、新しい行に自動的に伝播するようにしたいことがあります。これは、Microsoft Excelのデフォルトの動作です。Aspose.Cellsでも同じことを実現するには、[ListColumn.Formula](https://reference.aspose.com/cells/net/aspose.cells.tables/listcolumn/properties/formula)プロパティを使用してください。
## **新しい行にデータを入力する際に、表やリストオブジェクトの式を自動的に伝播させる**
次のサンプルコードは、列Bの数式が新しいデータを入力すると新しい行に自動的に伝播するように、テーブルまたはリストオブジェクトを作成します。このコードで生成される[出力Excelファイル](5115469.xlsx)をご確認ください。セルA3に数値を入力すると、セルB2の数式が自動的にセルB3に伝播することがわかります。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PropagateFormulaInTable-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
