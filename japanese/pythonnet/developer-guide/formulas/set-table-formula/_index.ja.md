---
title: 新しい行にデータを入力すると、表またはリストオブジェクトの式を自動的に伝播させます
linktitle: テーブルの数式を設定する
type: docs
weight: 260
url: /ja/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **可能な使用シナリオ**
時には、表やリストオブジェクトに入力した新しいデータに対して、式が自動的に新しい行に反映されてほしいことがあります。これはMicrosoft Excelの既定の動作です。Aspose.Cells for Python via .NETで同じ動作を実現するには、[**ListColumn.formula**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listcolumn/formula)プロパティを使用してください。

## **新しい行にデータを入力する際に、表やリストオブジェクトの式を自動的に伝播させる**
次のサンプルコードは、列Bの数式が新しいデータを入力すると新しい行に自動的に伝播するように、テーブルまたはリストオブジェクトを作成します。このコードで生成される[出力Excelファイル](5115469.xlsx)をご確認ください。セルA3に数値を入力すると、セルB2の数式が自動的にセルB3に伝播することがわかります。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-PropagateFormulaInTable-1.py" >}}

