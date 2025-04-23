---
title: ダイナミックチャートの作成
type: docs
weight: 200
url: /ja/java/create-dynamic-charts/
---

{{% alert color="primary" %}}

ダイナミック（またはインタラクティブ）チャートは、データのスコープを変更すると変化する能力を持ちます。つまり、データソースが変更されると、動的なチャートは自動的にその変更を反映します。データソースの変更をトリガーするために、Excelテーブルのフィルタリングオプションを使用するか、ComboBoxやDropdownリストなどのコントロールを使用できます。

本記事では、上記のアプローチの両方を使用してAspose.Cells for Java APIを使用して動的なチャートを作成する方法を示しています。

{{% /alert %}}

## **Excelテーブルの使用**

{{% alert color="primary" %}}

Aspose.Cellsの観点ではExcelテーブルはListObjectsと呼ばれ、明快さのために「テーブル」の代わりに「ListObject」という用語を使用します。Aspose.Cells for .NET APIを使用して[リストオブジェクトの作成](/cells/ja/java/creating-a-list-object/)について詳細をお読みください。

{{% /alert %}}

ListObjectsは、ユーザーの操作に応じてデータをソートおよびフィルタリングする組み込みの機能を提供します。ソートおよびフィルタリングオプションは、ListObjectのヘッダー行に自動的に追加されるドロップダウンリスト経由で提供されます。これらの機能（ソートおよびフィルタリング）により、ListObjectは、ソートやフィルタリングが変更されると、チャートのデータの表現も変わり、ListObjectの現在の状態を反映するかのように見えます。

デモンストレーションを理解しやすくするために、以下に概説されているように始め、Workbookを作成し、段階的に進めます。

1. 空のワークブックを作成します。
1. ワークブック内の最初のワークシートのセルにアクセスします。
1. セルにデータを挿入します。
1. 挿入したデータに基づいてListObjectを作成します。
1. ListObjectのデータ範囲に基づいてチャートを作成します。
1. 結果をディスクに保存します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **動的な数式の使用**

ListObjectsを動的なチャートのデータソースとして使用したくない場合、別のオプションとしてExcel関数（または式）を使用してデータの動的な範囲を作成し、データの変更をトリガーするコントロール（たとえば、ComboBoxなど）を使用することができます。このシナリオでは、ComboBoxの選択に基づいて適切な値を取得するためにVLOOKUP関数を使用します。選択が変更されると、VLOOKUP関数はセルの値を更新します。複数のセルの範囲がVLOOKUP関数を使用している場合、ユーザーの操作により全体の範囲を更新できるため、動的なチャートのデータソースとして使用できます。

デモンストレーションを理解しやすくするために、以下に概説されているように始め、Workbookを作成し、段階的に進めます。

1. 空のワークブックを作成します。
1. ワークブック内の最初のワークシートのセルにアクセスします。
1. 名前付き範囲を作成して、セルにいくつかのデータを挿入します。このデータは、動的なチャートの系列として機能します。
1. 前のステップで作成した名前付き範囲に基づいてComboBoxを作成します。
1. VLOOKUP関数のソースとして機能するために、セルにさらにいくつかのデータを挿入します。
1. 適切なパラメータを使用して、セルの範囲にVLOOKUP関数を挿入します。この範囲は、動的なチャートのデータソースとして機能します。
1. 以前のステップで作成した範囲に基づいてチャートを作成します。
1. 結果をディスクに保存します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
{{< app/cells/assistant language="java" >}}
