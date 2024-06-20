---
title: 新しい行にデータを入力すると、表またはリストオブジェクトの式を自動的に伝播させます
type: docs
weight: 980
url: /ja/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **可能な使用シナリオ**
時々、新しいデータを入力する際に表やリストオブジェクトの式が自動的に新しい行に伝播することが必要です。これはMicrosoft Excelのデフォルトの動作です。Aspose.Cellsでも同じことを実現するには、[ListColumn.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formula) プロパティを使用してください。
## **新しい行にデータを入力する際に、表やリストオブジェクトの式を自動的に伝播させる**
次のサンプルコードは、新しいデータを入力すると列Bの式が自動的に新しい行に伝播するような表やリストオブジェクトを作成します。このコードで生成された[出力エクセルファイル](5472519.xlsx)を確認してください。セルA3に数値を入力すると、セルB2の式が自動的にセルB3に伝播することが確認できます。
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
