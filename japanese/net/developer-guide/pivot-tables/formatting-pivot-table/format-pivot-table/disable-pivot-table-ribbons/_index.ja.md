---
title: ピボットテーブルリボンの無効化
type: docs
weight: 90
url: /ja/net/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

ピボットテーブルベースのレポートは便利ですが、対象ユーザーがこれらのレポートを詳細に設定するための知識を持っていない場合、エラーの原因となることがあります。これらの状況では、組織はユーザーがピボットテーブルベースのレポートを変更できないように制限したいと考えることがあります。レポートのフィルターの追加やスライサー、フィールドの追加、あるいはレポート内の特定の項目の順序の変更など、一般的なピボットテーブルの機能は、ほとんどのユーザーには推奨されません。一方で、これらのユーザーはレポートを更新したり、既存のフィルターやスライサーを使用したりすることはできるようになる必要があります。Aspose.Cellsでは、これらのレポートを作成する際にユーザーがこれらを変更できないようにする機能が提供されます。この目的のために、Excelではピボットテーブルリボンを無効にする機能が提供されており、Aspose.Cellsでも同様の機能が提供されています。つまり、開発者はこれらのレポートを変更できないようにリボンを無効にすることができます。

{{% /alert %}}

## **PivotTable.EnableWizardを使用してピボットテーブルリボンを無効にする**

次のコードは、シートからピボットテーブルを取得し、[**EnableWizard**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/enablewizard)を**false**に設定することでこの機能を示しています。サンプルのピボットテーブルファイルは、この[リンク](pivot_table_test.xlsx)からダウンロードできます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-DisablePivotTableRibbon.cs" >}}
{{< app/cells/assistant language="csharp" >}}
