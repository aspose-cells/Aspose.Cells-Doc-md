---
title: ピボットテーブルリボンの無効化
type: docs
weight: 90
url: /ja/nodejs-cpp/disable-pivot-table-ribbons/
description: Aspose.Cells for Node.js via C++を使ったピボットテーブルリボンの無効化方法
keywords: Aspose.Cells for Node.js Excel、Excel Node.jsライブラリ、Aspose.Cells for Node.js via C++を使ったピボットテーブルリボンの無効化
---

{{% alert color="primary" %}}

ピボットテーブルに基づくレポートは有用ですが、ターゲットユーザーがExcelの詳細な知識を持っていない場合はエラーが発生しやすいです。こうした場合、組織はピボットテーブルベースのレポートを変更できないよう制限したいと考えます。追加のフィルターやスライサー、フィールドの追加、またはレポート内の特定の順序変更などの一般的なピボットテーブル機能は、すべてのユーザーに推奨されません。一方で、これらのユーザーはレポートの更新や既存のフィルターやスライサーの使用は可能です。Aspose.Cells for Node.js via C++は、これらのレポートの変更を制限するための機能を開発者に提供しています。これにより、Excelはリボンの無効化機能を提供しており、Aspose.Cells for Node.js via C++も同じ機能を提供します。つまり、開発者はこれらのレポートを修正するコントロールを含むリボンを無効にできます。

{{% /alert %}}

## **Aspose.Cells for Node.js via C++を使ったピボットテーブルリボン無効化方法**

次のコードは、シートからピボットテーブルを取得し、[**setEnableWizard**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setEnableWizard-boolean-)を**false**に設定することでこの機能を示しています。サンプルのピボットテーブルファイルは、この[リンク](pivot_table_test.xlsx)からダウンロードできます。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-DisablePivotTableRibbon.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
