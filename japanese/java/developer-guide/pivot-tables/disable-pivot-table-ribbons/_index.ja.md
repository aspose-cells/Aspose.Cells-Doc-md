---
title: ピボット テーブル リボンを無効にする
type: docs
weight: 40
url: /ja/java/disable-pivot-table-ribbons/
---
{{% alert color="primary" %}}

ピボット テーブル ベースのレポートは便利ですが、ターゲット ユーザーがこれらのレポートを構成するための Excel の詳細な知識を持っていない場合、エラーが発生しやすくなります。このような状況では、組織はユーザーがピボット テーブル ベースのレポートを変更できないように制限する必要があります。追加のフィルター、スライサー、フィールドの追加、レポート内の特定の項目の順序の変更などの一般的なピボット テーブル機能は、ほとんどの場合、すべてのユーザーに推奨されるわけではありません。一方、これらのユーザーは、レポートを更新して、既存のフィルターまたはスライサーを使用することもできます。 Aspose.Cells は、これらのレポートの作成中にユーザーがこれらのレポートを変更することを制限するために、開発者にこの機能を提供しました。この目的のために、Excel はピボット テーブル リボンを無効にする機能を提供し、同じことが Aspose.Cells によって提供されます。つまり、開発者は、これらのレポートを変更するためのコントロールを含むリボンを無効にすることができます。

{{% /alert %}}

## **PivotTable.setEnableWizard を使用してピボット テーブル リボンを無効にする**

次のコードは、シートからピボット テーブルにアクセスしてから、[**setEnableWizard**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#EnableWizard)このフラグを設定するには**間違い**.サンプルのピボット テーブル ファイルは、ここからダウンロードできます。[リンク](71630876.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-DisablePivotTableRibbon-1.java" >}}
