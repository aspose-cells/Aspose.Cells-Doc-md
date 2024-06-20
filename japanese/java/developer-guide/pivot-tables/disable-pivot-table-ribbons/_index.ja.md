---
title: ピボットテーブルリボンの無効化
type: docs
weight: 40
url: /ja/java/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

ピボットテーブルベースのレポートは便利ですが、対象ユーザーがこれらのレポートを詳細に設定するための知識を持っていない場合、エラーの原因となることがあります。これらの状況では、組織はユーザーがピボットテーブルベースのレポートを変更できないように制限したいと考えることがあります。レポートのフィルターの追加やスライサー、フィールドの追加、あるいはレポート内の特定の項目の順序の変更など、一般的なピボットテーブルの機能は、ほとんどのユーザーには推奨されません。一方で、これらのユーザーはレポートを更新したり、既存のフィルターやスライサーを使用したりすることはできるようになる必要があります。Aspose.Cellsでは、これらのレポートを作成する際にユーザーがこれらを変更できないようにする機能が提供されます。この目的のために、Excelではピボットテーブルリボンを無効にする機能が提供されており、Aspose.Cellsでも同様の機能が提供されています。つまり、開発者はこれらのレポートを変更できないようにリボンを無効にすることができます。

{{% /alert %}}

## **PivotTable.setEnableWizardを使用したピボットテーブルリボンの無効化**

次のコードは、シートからピボットテーブルを取得し、そのフラグを**false**に設定する[**setEnableWizard**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#EnableWizard)を呼び出すことで、この機能を示しています。サンプルピボットテーブルファイルは、この[リンク](71630876.xlsx)からダウンロードできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-DisablePivotTableRibbon-1.java" >}}
