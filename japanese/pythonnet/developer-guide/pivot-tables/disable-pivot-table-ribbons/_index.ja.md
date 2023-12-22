---
title: ピボットテーブルのリボンを無効にする
type: docs
weight: 90
url: /ja/python-net/disable-pivot-table-ribbons/
description: Aspose.Cells for Python via .NET でピボット テーブル リボンを無効にする方法。
keywords: Disable Pivot Table Ribbons.
---
{{% alert color="primary" %}}

ピボット テーブル ベースのレポートは便利ですが、ターゲット ユーザーがこれらのレポートを構成するための Excel の詳細な知識を持っていない場合、エラーが発生しやすくなります。このような状況では、組織はユーザーがピボット テーブル ベースのレポートを変更できないように制限する必要があります。フィルター、スライサー、フィールドの追加、レポート内の特定の項目の順序の変更などの一般的なピボット テーブル機能は、ほとんどの場合、すべてのユーザーに推奨されません。一方、これらのユーザーはレポートを更新し、既存のフィルターまたはスライサーを使用することもできます。 Aspose.Cells for Python via .NET は、これらのレポートの作成中にユーザーがこれらのレポートを変更できないように制限するこの機能を開発者に提供しました。この目的のために、Excel はピボット テーブル リボンを無効にする機能を提供しており、同様の機能が Aspose.Cells for Python via .NET によって提供されています。つまり、開発者はこれらのレポートを変更するためのコントロールを含むリボンを無効にすることができます。

{{% /alert %}}

##  **PivotTable.EnableWizard を使用してピボット テーブル リボンを無効にする**

次のコードは、シートからピボット テーブルにアクセスして設定することにより、この機能を示しています。[**有効化ウィザード**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/enable_wizard/)*偽**に。ピボットテーブルのサンプルファイルはここからダウンロードできます[リンク](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-DisablePivotTableRibbon.py" >}}
